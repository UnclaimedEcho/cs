import taichi as ti
ti.init(arch=ti.cpu)
n = 128
n2 = 4
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
indices = ti.field(int, shape=(n - 1) * (n - 1) * 6)
verticesleft = ti.Vector.field(3, dtype=float, shape=n * n)
indicesright = ti.field(int, shape=(n - 1) * (n - 1) * 6)
verticesright = ti.Vector.field(3, dtype=float, shape=n * n)
bending_springs = False
window = ti.ui.Window("The Theater", (768, 768), vsync=True)
canvas = window.get_canvas()
scene = window.get_scene()
camera = ti.ui.Camera()
current_t = 0.0000

stage_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
stage_indices = ti.field(int, shape = n*n*6)

back_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
back_indices = ti.field(int, shape = n*n*6)

left_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
left_indices = ti.field(int, shape = n*n*6)

right_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
right_indices = ti.field(int, shape = n*n*6)

lights = ti.Vector.field(3, dtype=float, shape=2)

lights[0]=(0.6, 0.5, 0.5)
lights[1]=(-0.4, 0.5, 0.5)
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
        # 1st triangle
        indices[quad_id * 6 + 0] = i * n + j
        indices[quad_id * 6 + 1] = (i + 1) * n + j
        indices[quad_id * 6 + 2] = i * n + (j + 1)
        # 2nd triangle
        indices[quad_id * 6 + 3] = (i + 1) * n + j + 1
        indices[quad_id * 6 + 4] = i * n + (j + 1)
        indices[quad_id * 6 + 5] = (i + 1) * n + j

spring_offsets_left = []
spring_offsets_right = []
def initialize_spring_offsets():
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (i, j) != (0, 0) and abs(i) + abs(j) <= 2:
                spring_offsets_left.append(ti.Vector([i, j]))
                spring_offsets_right.append(ti.Vector([i, j]))

#endregion init_curtains
  
def init_vertices(vertices, a,b,c):
    tick=0
    x=0
    z=0
    while z<=n2:
        while x<=n2:
            vertices[tick] = (eval(a),eval(b),eval(c))
            # vertices[tick] = ((2*x/n2)-0.9,-0.5,(z/n2)-1.1)
            tick+=1
            x+=1
        x=0
        z+=1

@ti.kernel
def init_indices(indices:ti.template()): # type: ignore
    tick = 0
    for z in range(0,n2):
        for x in range(0,n2):
            indices[tick]=x+z*(n2+1)
            indices[tick+1]=x+z*(n2+1)+1
            indices[tick+2]=x+z*(n2+1)+n2+2
            
            indices[tick+3]=x+z*(n2+1)
            indices[tick+4]=x+z*(n2+1)+n2+1
            indices[tick+5]=x+z*(n2+1)+n2+2
            tick+=6

def make_cube(c1: list,c2: list, name: str):
    
    eval(name)[0] = (c1[0],c1[1],c1[2])
    eval(name)[1] = (c2[0],c1[1],c1[2])
    eval(name)[2] = (c1[0],c2[1],c1[2])
    eval(name)[3] = (c2[0],c2[1],c1[2])
    eval(name)[4] = (c1[0],c1[1],c2[2])
    eval(name)[5] = (c2[0],c1[1],c2[2])
    eval(name)[6] = (c1[0],c2[1],c2[2])
    eval(name)[7] = (c2[0],c2[1],c2[2])
    
    eval(name+"_indices")[0] = 0
    eval(name+"_indices")[1] = 1
    eval(name+"_indices")[2] = 2
    eval(name+"_indices")[3] = 2
    eval(name+"_indices")[4] = 1
    eval(name+"_indices")[5] = 3
    
    eval(name+"_indices")[6] = 2
    eval(name+"_indices")[7] = 3
    eval(name+"_indices")[8] = 6
    eval(name+"_indices")[9] = 3
    eval(name+"_indices")[10] = 6
    eval(name+"_indices")[11] = 7
    
    eval(name+"_indices")[12] = 0
    eval(name+"_indices")[13] = 4
    eval(name+"_indices")[14] = 2
    eval(name+"_indices")[15] = 6
    eval(name+"_indices")[16] = 4
    eval(name+"_indices")[17] = 2
    
    eval(name+"_indices")[18] = 0
    eval(name+"_indices")[19] = 1
    eval(name+"_indices")[20] = 4
    eval(name+"_indices")[21] = 1
    eval(name+"_indices")[22] = 4
    eval(name+"_indices")[23] = 5

    eval(name+"_indices")[24] = 1
    eval(name+"_indices")[25] = 5
    eval(name+"_indices")[26] = 3
    eval(name+"_indices")[27] = 7
    eval(name+"_indices")[28] = 5
    eval(name+"_indices")[29] = 3

    eval(name+"_indices")[30] = 4
    eval(name+"_indices")[31] = 5
    eval(name+"_indices")[32] = 6
    eval(name+"_indices")[33] = 5
    eval(name+"_indices")[34] = 6
    eval(name+"_indices")[35] = 7



body = ti.Vector.field(3, dtype=float, shape=8)
body_indices = ti.field(int, shape = 36)

left_arm = ti.Vector.field(3, dtype=float, shape=8)
left_arm_indices = ti.field(int, shape = 36)

right_arm = ti.Vector.field(3, dtype=float, shape=8)
right_arm_indices = ti.field(int, shape = 36)

left_leg = ti.Vector.field(3, dtype=float, shape=8)
left_leg_indices = ti.field(int, shape = 36)

right_leg = ti.Vector.field(3, dtype=float, shape=8)
right_leg_indices = ti.field(int, shape = 36)

head = ti.Vector.field(3, dtype=float, shape=8)
head_indices = ti.field(int, shape = 36)

make_cube([0,-0.4,-0.5],[0.2,-0.2,-0.7],"body")
make_cube([0.3,-0.4,-0.55],[0.2,-0.2,-0.65],"left_arm")
make_cube([-0.1,-0.4,-0.55],[0,-0.2,-0.65],"right_arm")
make_cube([0,-0.4,-0.55],[0.08,-0.5,-0.65],"left_leg")
make_cube([0.12,-0.4,-0.55],[0.2,-0.5,-0.65],"right_leg")
make_cube([0.05,-0.1,-0.575],[0.15,-0.2,-0.625],"head")

init_vertices(stage_vertices,"(2*x/n2)-0.9","-0.5","(z/n2)-1.1")
init_indices(stage_indices)

init_vertices(back_vertices,"(2*x/n2)-0.9","z/n2-0.5","-1.1")
init_indices(back_indices)

init_vertices(left_vertices,"-0.9","x/n2-0.5","z/n2-1.1")
init_indices(left_indices)

init_vertices(right_vertices,"1.1","x/n2-0.5","z/n2-1.1")
init_indices(right_indices)

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

@ti.kernel
def updateArms(current_t: float):
    for i in range(8):
            left_arm[i][1] += gravity * dt
            right_arm[i][2] += gravity * dt
#endregion steps

camera.position(0.1, 0.0, 3)
camera.lookat(0.1, 0.0, 0)

initialize_mesh_indices()
initialize_spring_offsets()
initialize_mass_points()

while window.running:
    if current_t<=3:
        for i in range(substepsmain):
            substepleft(current_t)
            substepright(current_t)
            current_t = current_t + dt
        update_vertices()
    else:
        for i in range(substepsmain):
            updateArms(current_t)
            current_t = current_t + dt

        
    scene.set_camera(camera)
    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.LMB)
    # scene.point_light(pos=lights[0], color=(1, 1, 1))
    scene.point_light(pos=lights[1], color=(1, 1, 1))
    # scene.particles(radius=0.1,color=(1,1,1),centers=lights)
    scene.ambient_light(color=(0.6, 0.6, 0.6))
    scene.mesh(verticesleft, indices=indices, color=(125/255, 29/255, 29/255), two_sided=True)
    scene.mesh(verticesright, indices=indices, color=(125/255, 29/255, 29/255), two_sided=True)
    scene.mesh(vertices=stage_vertices, indices=stage_indices, color=(0.588,0.294,0), show_wireframe=False,two_sided=False)
    scene.mesh(vertices=back_vertices, indices=back_indices, color=(0.588,0.294,0), show_wireframe=False,two_sided=False)
    scene.mesh(vertices=left_vertices, indices=left_indices, color=(0.588,0.294,0), show_wireframe=False,two_sided=False)
    scene.mesh(vertices=right_vertices, indices=right_indices, color=(0.588,0.294,0), show_wireframe=False,two_sided=False)

    scene.mesh(body, indices=body_indices, color=(1,1,0), two_sided=False)
    scene.mesh(left_arm, indices=left_arm_indices, color=(1,1,0), two_sided=False)
    scene.mesh(right_arm, indices=right_arm_indices, color=(1,1,0), two_sided=False)
    scene.mesh(left_leg, indices=left_leg_indices, color=(1,1,0), two_sided=False)
    scene.mesh(right_leg, indices=right_leg_indices, color=(1,1,0), two_sided=False)
    scene.mesh(head, indices=head_indices, color=(1,1,0), two_sided=False)
    
    canvas.scene(scene)
    window.show()
# TODO: include self-collision handling