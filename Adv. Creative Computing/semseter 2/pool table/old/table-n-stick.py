import taichi as ti
import math
ti.init(arch=ti.cpu)
window = ti.ui.Window('Pool Table', (800, 800))
canvas = window.get_canvas()
scene = window.get_scene()
camera = ti.ui.Camera()
camera.position(6, 7, 14)
camera.lookat(5.6, 6.5, 13.2)

n = 10
 
 
ydist = 1
rad = 1

stick_vertices = ti.Vector.field(3, dtype=ti.f32, shape=50)
stick_indices = ti.field(int, shape = 144)


@ti.kernel
def init_stick_vertices(rad1: float, rad2: float, height1: float, height2: float, angle: float):
    tick=0
    rad = 0.0
    for tick2 in range(2):
        print(tick2)
        y=0.0
        if tick2 == 0:
            y=height1
            rad=rad1
        else:
            y=height2
            rad=rad2
        print(rad)
        w=0.0
        while w<(2*math.pi):
            x=ti.sin(w)
            z=ti.cos(w)
            stick_vertices[tick] = (x*rad,y,z*rad)
            tick+=1
            w+=ti.math.pi/12       
        
        
@ti.kernel
def init_stick_indices():
    tick=0
    for x in range(24):
        stick_indices[tick] = x
        stick_indices[tick+1] = x + 1
        stick_indices[tick+2] = x + 25

        stick_indices[tick+3] = x + 1
        stick_indices[tick+4] = x + 25
        stick_indices[tick+5] = x + 26
        tick+=6


init_stick_vertices(0.1,0.35, -1, 3, 0)
#print(stick_vertices)
init_stick_indices()
#print(stick_indices)

while window.running:
    scene.set_camera(camera)
    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.LMB)
    scene.ambient_light((0.9, 0.9, 0.9))
    #scene.particles(centers=stick_vertices, radius = 0.1, color = (1,1,1))
    scene.mesh(vertices=stick_vertices, indices=stick_indices, color=(21/255,88/255,67/255), show_wireframe=False)
    canvas.scene(scene)
    window.show()