import taichi as ti
arch = ti.vulkan if ti._lib.core.with_vulkan() else ti.cpu
ti.init(arch=arch)
n = 128
quad_size = 1.0 / n
dt = 4e-2 / n
substepsmain = int(1 / 60 // dt)
gravity = ti.Vector([0, -9.8, 0])
spring_Y = 3e4
dashpot_damping = 1e4
drag_damping = 1
tempvertleft = ti.Vector.field(3, dtype=float, shape=(n, n))
tempvectleft = ti.Vector.field(3, dtype=float, shape=(n, n))
tempvertright = ti.Vector.field(3, dtype=float, shape=(n, n))
tempvectright = ti.Vector.field(3, dtype=float, shape=(n, n))
indicesleft = ti.field(int, shape=(n - 1) * (n - 1) * 6)
verticesleft = ti.Vector.field(3, dtype=float, shape=n * n)
indicesright = ti.field(int, shape=(n - 1) * (n - 1) * 6)
verticesright = ti.Vector.field(3, dtype=float, shape=n * n)
colors = ti.Vector.field(3, dtype=float, shape=n * n)
bending_springs = False
window = ti.ui.Window("The Theater", (768, 768), vsync=True)
canvas = window.get_canvas()
scene = window.get_scene()
camera = ti.ui.Camera()
current_t = 0.0000



#region init_curtains
@ti.kernel
def initialize_mass_points():
    for i, j in tempvertleft:
        tempvertleft[i, j] = [i * quad_size - 0.9, j * quad_size - 0.5, ti.sin(float(i))*0.001]
        tempvertright[i, j] = [i * quad_size-0, j * quad_size - 0.5, ti.sin(float(i))*0.001]
        tempvectleft[i, j] = [0, 0, 0]
        tempvectright[i, j] = [0, 0, 0]

@ti.kernel
def initialize_mesh_indices():
    for i, j in ti.ndrange(n - 1, n - 1):
        quad_id = (i * (n - 1)) + j
        # 1st triangle of the square
        indicesleft[quad_id * 6 + 0] = i * n + j
        indicesleft[quad_id * 6 + 1] = (i + 1) * n + j
        indicesleft[quad_id * 6 + 2] = i * n + (j + 1)
        # 2nd triangle of the square
        indicesleft[quad_id * 6 + 3] = (i + 1) * n + j + 1
        indicesleft[quad_id * 6 + 4] = i * n + (j + 1)
        indicesleft[quad_id * 6 + 5] = (i + 1) * n + j
        # 1st triangle of the square
        indicesright[quad_id * 6 + 0] = i * n + j
        indicesright[quad_id * 6 + 1] = (i + 1) * n + j
        indicesright[quad_id * 6 + 2] = i * n + (j + 1)
        # 2nd triangle of the square
        indicesright[quad_id * 6 + 3] = (i + 1) * n + j + 1
        indicesright[quad_id * 6 + 4] = i * n + (j + 1)
        indicesright[quad_id * 6 + 5] = (i + 1) * n + j
    for i, j in ti.ndrange(n, n):
            colors[i * n + j] = (125/255, 29/255, 29/255)

spring_offsets_left = []
spring_offsets_right = []
def initialize_spring_offsets():
    if bending_springs:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i, j) != (0, 0):
                    spring_offsets_left.append(ti.Vector([i, j]))
                    spring_offsets_right.append(ti.Vector([i, j]))
    else:
        for i in range(-2, 3):
            for j in range(-2, 3):
                if (i, j) != (0, 0) and abs(i) + abs(j) <= 2:
                    spring_offsets_left.append(ti.Vector([i, j]))
                    spring_offsets_right.append(ti.Vector([i, j]))
  

#endregion init_curtains
  







#region steps
                                                         
@ti.kernel
def substepleft(current_t: float):
    for i in ti.grouped(tempvertleft):
            tempvectleft[i] += gravity * dt
    for i in ti.grouped(tempvertleft):
        force = ti.Vector([0.0, 0.0, 0.0])
        for spring_offset in ti.static(spring_offsets_left):
            j = i + spring_offset
            if 0 <= j[0] < n and 0 <= j[1] < n:
                x_ij = tempvertleft[i] - tempvertleft[j]
                v_ij = tempvectleft[i] - tempvectleft[j]
                d = x_ij.normalized()
                current_dist = x_ij.norm()
                original_dist = quad_size * float(i - j).norm()  # pylint: disable=no-member
                # Spring force
                force += -spring_Y * d * (current_dist / original_dist - 1)
                # Dashpot damping
                force += -v_ij.dot(d) * d * dashpot_damping * quad_size
        tempvectleft[i] += force * dt
    for tempvertleft in range(n):
        if (tempvertleft+1)%32 == 0 or tempvertleft==0:
            tempvectleft[(tempvertleft,n-1)] = (tempvectleft[(tempvertleft,n-1)][0],0.0,0)
    if current_t<=0.7:
        tempvectleft[(0,n-1)] -= (4,0,0)
        tempvectleft[(31,n-1)] -= (4,0,0)
        tempvectleft[(63,n-1)] -= (4,0,0)
        tempvectleft[(97,n-1)] -= (4,0,0)
    else:
        tempvectleft[(0,n-1)] = (0.0,0,0)
        tempvectleft[(31,n-1)] = (0.0,0,0)
        tempvectleft[(63,n-1)] = (0.0,0,0)       
        tempvectleft[(97,n-1)] = (0.0,0,0)       
        tempvectleft[(127,n-1)] = (0.0,0,0)
    for i in ti.grouped(tempvertleft):
        tempvectleft[i] *= ti.exp(-drag_damping * dt)
        tempvertleft[i] += dt * tempvectleft[i]

@ti.kernel
def substepright(current_t: float):
    for i in ti.grouped(tempvertright):
            tempvectright[i] += gravity * dt
    for i in ti.grouped(tempvertright):
        force = ti.Vector([0.0, 0.0, 0.0])
        for spring_offset in ti.static(spring_offsets_right):
            j = i + spring_offset
            if 0 <= j[0] < n and 0 <= j[1] < n:
                x_ij = tempvertright[i] - tempvertright[j]
                v_ij = tempvectright[i] - tempvectright[j]
                d = x_ij.normalized()
                current_dist = x_ij.norm()
                original_dist = quad_size * float(i - j).norm()  # pylint: disable=no-member
                # Spring force
                force += -spring_Y * d * (current_dist / original_dist - 1)
                # Dashpot damping
                force += -v_ij.dot(d) * d * dashpot_damping * quad_size
        tempvectright[i] += force * dt
    for tempvertright in range(n):
        if (tempvertright+1)%32 == 0 or tempvertright==0:
            tempvectright[(tempvertright,n-1)] = (tempvectright[(tempvertright,n-1)][0],0.0,0)
    if current_t<=0.7:
        tempvectright[(127,n-1)] += (4,0,0)
        tempvectright[(97,n-1)] += (4,0,0)
        tempvectright[(63,n-1)] += (4,0,0)
        tempvectright[(31,n-1)] += (4,0,0)
    else:
        tempvectright[(0,n-1)] = (0.0,0,0)
        tempvectright[(31,n-1)] = (0.0,0,0)
        tempvectright[(63,n-1)] = (0.0,0,0)       
        tempvectright[(97,n-1)] = (0.0,0,0)       
        tempvectright[(127,n-1)] = (0.0,0,0)
    for i in ti.grouped(tempvertright):
        tempvectright[i] *= ti.exp(-drag_damping * dt)
        tempvertright[i] += dt * tempvectright[i]

@ti.kernel
def update_vertices():
    for i, j in ti.ndrange(n, n):
        verticesleft[i * n + j] = tempvertleft[i, j]
        verticesright[i * n + j] = tempvertright[i, j]


#endregion steps

camera.position(0.0, 0.0, 3)
camera.lookat(0.0, 0.0, 0)

initialize_mesh_indices()
initialize_spring_offsets()
initialize_mass_points()

while window.running:
    if current_t<=5:
        for i in range(substepsmain):
            substepleft(current_t)
            substepright(current_t)
            current_t = current_t + dt
        update_vertices()
        
    scene.set_camera(camera)
    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.LMB)
    scene.point_light(pos=(0.2, -0.6, 2.5), color=(1, 1, 1))
    scene.mesh(verticesleft, indices=indicesleft, per_vertex_color=colors, two_sided=True)
    scene.mesh(verticesright, indices=indicesright, per_vertex_color=colors, two_sided=True)
    canvas.scene(scene)
    window.show()
# TODO: include self-collision handling