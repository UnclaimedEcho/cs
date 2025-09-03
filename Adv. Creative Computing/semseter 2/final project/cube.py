import taichi as ti
ti.init(arch=ti.cpu)

window = ti.ui.Window("The Theater", (768, 768), vsync=True)
canvas = window.get_canvas()
scene = window.get_scene()
camera = ti.ui.Camera()

cube = ti.Vector.field(3, dtype=float, shape=8)
cube_indices = ti.field(int, shape = 36)

lights = ti.Vector.field(3, dtype=float, shape=2)

lights[0]=(0.6, 0.5, 0.5)
lights[1]=(-0.4, 0.5, 0.5)

        
        
def make_cube(c1,c2, name):
    
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


make_cube([0,0,0],[1,1,1],"cube")


camera.position(5, 5, 5)
camera.lookat(.5, 0.5, 0.5)

while window.running:

        
    scene.set_camera(camera)
    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.LMB)
    scene.point_light(pos=lights[0], color=(2, 2, 2))
    scene.point_light(pos=lights[1], color=(-1, -1, -1))
    # scene.particles(radius=0.1,color=(1,1,1),centers=lights)
    scene.ambient_light(color=(0.7, 0.7, 0.7))
    scene.mesh(cube, indices=cube_indices, color=(1,1,1), two_sided=False)
    # scene.particles(radius=0.1,color=(1,1,1),centers=cube)
    canvas.scene(scene)
    window.show()
# TODO: include self-collision handling