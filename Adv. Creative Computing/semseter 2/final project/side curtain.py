import taichi as ti
arch = ti.vulkan if ti._lib.core.with_vulkan() else ti.cuda
ti.init(arch=ti.cpu)
n = 128
quad_size = 1.0 / n
dt = 4e-2 / n
substeps = int(1 / 60 // dt)
gravity = ti.Vector([0, -9.8, 0])
spring_Y = 3e4
dashpot_damping = 1e4
drag_damping = 1
x = ti.Vector.field(3, dtype=float, shape=(n, n))
v = ti.Vector.field(3, dtype=float, shape=(n, n))

num_triangles = (n - 1) * (n - 1) * 2
indices = ti.field(int, shape=num_triangles * 3)
vertices = ti.Vector.field(3, dtype=float, shape=n * n)
colors = ti.Vector.field(3, dtype=float, shape=n * n)
bending_springs = False

window = ti.ui.Window("The Theater", (768, 768), vsync=True)
canvas = window.get_canvas()

scene = window.get_scene()
camera = ti.ui.Camera()
current_t = 0.0


dtt = 0.000
@ti.kernel
def initialize_mass_points():
    for i, j in x:
        x[i, j] = [
            i * quad_size - 0.5,
            j * quad_size - 0.5,
            ti.sin(float(i))*0.001
        ]
        v[i, j] = [0, 0, 0]
@ti.kernel

def initialize_mesh_indices():
    for i, j in ti.ndrange(n - 1, n - 1):
        quad_id = (i * (n - 1)) + j
        # 1st triangle of the square
        indices[quad_id * 6 + 0] = i * n + j
        indices[quad_id * 6 + 1] = (i + 1) * n + j
        indices[quad_id * 6 + 2] = i * n + (j + 1)
        # 2nd triangle of the square
        indices[quad_id * 6 + 3] = (i + 1) * n + j + 1
        indices[quad_id * 6 + 4] = i * n + (j + 1)
        indices[quad_id * 6 + 5] = (i + 1) * n + j
    for i, j in ti.ndrange(n, n):
            colors[i * n + j] = (125/255, 29/255, 29/255)
            
            



spring_offsets = []
def initialize_spring_offsets():
    if bending_springs:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i, j) != (0, 0):
                    spring_offsets.append(ti.Vector([i, j]))
    else:
        for i in range(-2, 3):
            for j in range(-2, 3):
                if (i, j) != (0, 0) and abs(i) + abs(j) <= 2:
                    spring_offsets.append(ti.Vector([i, j]))
                                       
@ti.kernel
def substep():
    for i in ti.grouped(x):
            v[i] += gravity * dt
    for i in ti.grouped(x):
        force = ti.Vector([0.0, 0.0, 0.0])
        for spring_offset in ti.static(spring_offsets):
            j = i + spring_offset
            if 0 <= j[0] < n and 0 <= j[1] < n:
                x_ij = x[i] - x[j]
                v_ij = v[i] - v[j]
                d = x_ij.normalized()
                current_dist = x_ij.norm()
                original_dist = quad_size * float(i - j).norm()  # pylint: disable=no-member
                # Spring force
                force += -spring_Y * d * (current_dist / original_dist - 1)
                # Dashpot damping
                force += -v_ij.dot(d) * d * dashpot_damping * quad_size
        v[i] += force * dt
    for x in range(n):
        if (x+1)%32 == 0 or x==0:
            v[(x,n-1)] = (v[(x,n-1)][0],0.0,0)
    if dtt<=0.24:
        v[(0,n-1)] -= (0.0004,0,0)
        # v[(16,n-1)] -= (0.001,0,0)
        v[(31,n-1)] -= (0.0004,0,0)
        # v[(48,n-1)] -= (0.001,0,0)
        v[(63,n-1)] -= (0.0004,0,0)
        
        v[(97,n-1)] -= (0.0004,0,0)
    else:
        print("asdf")
        v[(0,n-1)] = (0.0,0,0)
        # v[(16,n-1)] -= (0.001,0,0)
        v[(31,n-1)] = (0.0,0,0)
        # v[(48,n-1)] -= (0.001,0,0)
        v[(63,n-1)] = (0.0,0,0)
        
        v[(97,n-1)] = (0.0,0,0)
    for i in ti.grouped(x):

        
        #v[(n-2,n-2)] -= (0.001,0,0)
        v[i] *= ti.exp(-drag_damping * dt)
        x[i] += dt * v[i]
  

@ti.kernel
def update_vertices():
    for i, j in ti.ndrange(n, n):
        vertices[i * n + j] = x[i, j]


camera.position(0.0, 0.0, 3)
camera.lookat(0.0, 0.0, 0)

initialize_mesh_indices()
initialize_spring_offsets()
initialize_mass_points()
while window.running:
    for i in range(substeps):
        substep()
        current_t += dt
        dtt+=dt
        # print(dtt)
    update_vertices()

    scene.set_camera(camera)
    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.LMB)
    scene.point_light(pos=(0.2, -0.6, 2.5), color=(1, 1, 1))
    # scene.ambient_light((0.5, 0.5, 0.5))
    scene.mesh(vertices, indices=indices, per_vertex_color=colors, two_sided=True)
    canvas.scene(scene)
    window.show()
# TODO: include self-collision handling