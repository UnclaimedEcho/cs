import taichi as ti

ti.init(arch=ti.cpu)
window = ti.ui.Window('Pool Table', (800, 800))
canvas = window.get_canvas()
scene = window.get_scene()
camera = ti.ui.Camera()
camera.position(6, 7, 14)
camera.lookat(5.6, 6.5, 13.2)

n = 10
 
table_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
table_indices = ti.field(int, shape = n*n*6)

bumper1_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper1_indices = ti.field(int, shape = n*n*6)

bumper2_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper2_indices = ti.field(int, shape = n*n*6)

@ti.kernel
def init_table_vertices():
    tick=0
    x=0
    z=0
    while z<=n:
        while x<=n:
            table_vertices[tick] = (44*x/1000*n,1,88*z/1000*n)
            tick+=1
            x+=1
        x=0
        z+=1

@ti.kernel
def init_bumper1_vertices():
    tick=0
    x=0
    y=0
    while y<=n:
        while x<=n:
            bumper1_vertices[tick] = (4.4*x/n,0.2*y/n+1,0)
            tick+=1
            x+=1
        x=0
        y+=1
        
@ti.kernel
def init_bumper2_vertices():
    tick=0
    x=0
    y=0
    while y<=n:
        while x<=n:
            bumper2_vertices[tick] = (4.4*x/n,0.2*y/n+1,8.8)
            tick+=1
            x+=1
        x=0
        y+=1

@ti.kernel
def init_indices(indices:ti.template()): # type: ignore
    tick = 0
    for z in range(0,n):
        for x in range(0,n):
            indices[tick]=x+z*(n+1)
            indices[tick+1]=x+z*(n+1)+1
            indices[tick+2]=x+z*(n+1)+n+2
            
            indices[tick+3]=x+z*(n+1)
            indices[tick+4]=x+z*(n+1)+n+1
            indices[tick+5]=x+z*(n+1)+n+2
            tick+=6

init_table_vertices()
init_indices(table_indices)

init_bumper1_vertices()
init_indices(bumper1_indices)

init_bumper2_vertices()
init_indices(bumper2_indices)

while window.running:
    scene.set_camera(camera)
    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.LMB)
    scene.ambient_light((0.9, 0.9, 0.9))
    scene.mesh(vertices=table_vertices, indices=table_indices, color=(21/255,88/255,67/255), show_wireframe=False)
    scene.mesh(vertices=bumper1_vertices, indices=bumper1_indices, color=(1,0,1), show_wireframe=False)
    scene.mesh(vertices=bumper2_vertices, indices=bumper2_indices, color=(1,0,1), show_wireframe=False)
    canvas.scene(scene)
    window.show()