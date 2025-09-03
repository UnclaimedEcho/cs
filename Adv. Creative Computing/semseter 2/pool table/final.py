#region init

import taichi as ti
ti.init(arch=ti.cpu)
window = ti.ui.Window('Pool Simulation', (800, 800))
canvas = window.get_canvas()
scene = window.get_scene()
camera = ti.ui.Camera()
camera.position(6, 7, 14)
camera.lookat(5.6, 6.5, 13.2)
n = 10
 
surface = (21/255,88/255,67/255) 
tablecolor = (66/255,40/255,14/255)
resistance = 1
bool = False
switch = True
stickval=0.01

#endregion init

#region table
table_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
table_indices = ti.field(int, shape = n*n*6)

bumper1_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper1_indices = ti.field(int, shape = n*n*6)

bumper1top_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper1top_indices = ti.field(int, shape = n*n*6)

bumper2_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper2_indices = ti.field(int, shape = n*n*6)

bumper2top_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper2top_indices = ti.field(int, shape = n*n*6)

bumper3_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper3_indices = ti.field(int, shape = n*n*6)

bumper3top_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper3top_indices = ti.field(int, shape = n*n*6)

bumper4_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper4_indices = ti.field(int, shape = n*n*6)

bumper4top_vertices = ti.Vector.field(3, dtype=float, shape=(n+1)*(n+1))
bumper4top_indices = ti.field(int, shape = n*n*6)

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
def init_bumper1top_vertices():
    tick=0
    x=0
    y=0
    while y<=n:
        while x<=n:
            bumper1top_vertices[tick] = (4.6*x/n,1.2,0.2*y/n-0.2)
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
def init_bumper2top_vertices():
    tick=0
    x=0
    y=0
    while y<=n:
        while x<=n:
            bumper2top_vertices[tick] = (4.6*x/n,1.2,0.2*y/n+8.8)
            tick+=1
            x+=1
        x=0
        y+=1 
    
@ti.kernel
def init_bumper3_vertices():
    tick=0
    x=0
    y=0
    while y<=n:
        while x<=n:
            bumper3_vertices[tick] = (0,0.2*y/n+1,8.8*x/n)
            tick+=1
            x+=1
        x=0
        y+=1

@ti.kernel
def init_bumper3top_vertices():
    tick=0
    x=0
    y=0
    while y<=n:
        while x<=n:
            bumper3top_vertices[tick] = (0.2*y/n-0.2,1.2,9.2*x/n-0.2)
            tick+=1
            x+=1
        x=0
        y+=1
        
@ti.kernel
def init_bumper4_vertices():
    tick=0
    x=0
    y=0
    while y<=n:
        while x<=n:
            bumper4_vertices[tick] = (4.4,0.2*y/n+1,8.8*x/n)
            tick+=1
            x+=1
        x=0
        y+=1
        
@ti.kernel
def init_bumper4top_vertices():
    tick=0
    x=0
    y=0
    while y<=n:
        while x<=n:
            bumper4top_vertices[tick] = (0.2*y/n+4.4,1.2,8.8*x/n)
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

init_bumper1top_vertices()
init_indices(bumper1top_indices)

init_bumper2_vertices()
init_indices(bumper2_indices)

init_bumper2top_vertices()
init_indices(bumper2top_indices)

init_bumper3_vertices()
init_indices(bumper3_indices)

init_bumper3top_vertices()
init_indices(bumper3top_indices)

init_bumper4_vertices()
init_indices(bumper4_indices)

init_bumper4top_vertices()
init_indices(bumper4top_indices)

#endregion table

#region stick
stick_vertices = ti.Vector.field(3, dtype=ti.f32, shape=50)
stick_indices = ti.field(int, shape = 144)

@ti.kernel
def init_stick_vertices(rad1: float, rad2: float, height1: float, height2: float, offsetx: float, offsety: float, offsetz: float, angle: float):
    tick=0
    rad = 0.0
    for tick2 in range(2):
        y=0.0
        if tick2 == 0:
            y=height1
            rad=rad1
        else:
            y=height2
            rad=rad2
        w=0.0
        while w<(2*ti.math.pi):
            x=ti.sin(w)
            z=ti.cos(w)
            #add angle stick_vertices[tick] = (x*rad + offsetx ,z*rad+offsety, x*rad+y+offsetz)
            stick_vertices[tick] = (x*rad + offsetx ,z*rad+offsety, y+offsetz)
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

init_stick_indices()

#endregion stick

#region balls
balls = ti.Vector.field(3, dtype=ti.f32, shape=16)
colors = ti.Vector.field(3, dtype=ti.f32, shape = 16)
ballsvectors = ti.Vector.field(3, dtype=ti.f32, shape=16)

for i in range(15):
    x=0
    y=1.1
    z=0
    if i == 0:
        x=2.2
        z=2
        colors[0] = (255/255,255/255,0/255)
    elif i in [1,2]:
        if i == 1:
            x=2.2-0.1
            colors[1] = (0/255,0/255,255/255)
        else:
            x=2.2+0.1
            colors[2] = (255/255,0/255,0/255)
        z=2-0.0866*2
    elif i in [3,4,5]:
        if i == 3:
            x=2.2-0.2
            colors[3] = (255/255,0/255,255/255)
        elif i == 4:
            x=2.2
            colors[4] = (255/255,165/255,0/255)
        else:
            x=2.2+0.2
            colors[5] = (0/255,255/255,0/255)
        z=2-0.0866*4
    elif i in [6,7,8,9]:
        if i == 6:
            x=2.2-0.3
            colors[6] = (255/255,0/255,0/255)
        elif i == 7:
            x=2.2-0.1
            colors[7] = (0/255,0/255,0/255)
        elif i == 8:
            x=2.2+0.1
            colors[8] = (255/255,255/255,0/255)
        else:
            x=2.2+0.3
            colors[9] = (0/255,0/255,255/255)
        
        z=2-0.0866*6
    elif i in [10,11,12,13,14]:
        if i == 10:
            x=2.2-0.4
            colors[10] = (255/255,0/255,0/255)
        elif i == 11:
            x=2.2-0.2
            colors[11] = (255/255,0/255,255/255)
        elif i == 12:
            x=2.2+0
            colors[12] = (255/255,165/255,0/255)
        elif i == 13:
            x=2.2+0.2
            colors[13] = (0/255,255/255,0/255)
        else:
            x=2.2+0.4
            colors[14] = (255/255,0/255,0/255)
        
        
        
        z=2-0.0866*8
    balls[i] = (x,y,z)
    
balls[15] = (2.2,1.1,5.8)
colors[15] = (1,1,1)

@ti.kernel
def updateballs():
    for i in range(16):
        for j in range(i+1,16):
            distance = ti.math.sqrt((balls[i][0] - balls[j][0]) ** 2 + (balls[i][2] - balls[j][2]) ** 2)
            posdif = balls[j] - balls[i]
            vectdif = ballsvectors[j] - ballsvectors[i]
            normal = posdif.normalized() # make a unit vector direction
            change = vectdif.dot(normal) * normal #find the change by multipling amplitude by unit vector direction (like sin cos)
            if distance<=0.2: #check hit
                ballsvectors[i] += change #effect
                ballsvectors[j] -= change #effect
                

    #region old
                # phi = ti.atan2(balls[i][2]-balls[j][2],balls[i][0]-balls[j][0])
                
                # itheta = ti.atan2(balls[i][2],balls[i][0])
                # jtheta = ti.atan2(balls[j][2],balls[j][0])
                
                # ib4speed=ti.math.sqrt(balls[i][0]**2 + balls[i][2]**2)
                # jb4speed=ti.math.sqrt(balls[j][0]**2 + balls[j][2]**2)
                
                # imass = 1
                # jmass = 1
                
            
                # ballsvectors[i][0] = ((ib4speed * ti.cos(itheta-phi) * (imass-jmass) + 2 * jmass * jb4speed * ti.cos(jtheta-phi))/(imass+jmass)) * ti.cos(phi) + ib4speed * ti.sin(itheta-phi) * ti.sin(phi)
                # ballsvectors[i][2] = ((ib4speed * ti.cos(itheta-phi) * (imass-jmass) + 2 * jmass * jb4speed * ti.cos(jtheta-phi))/(imass+jmass)) * ti.sin(phi) + ib4speed * ti.sin(itheta-phi) * ti.cos(phi)
                
                # ballsvectors[j][0] = ((jb4speed * ti.cos(jtheta-phi) * (jmass-imass) + 2 * imass * ib4speed * ti.cos(itheta-phi))/(jmass+imass)) * ti.cos(phi) + jb4speed * ti.sin(jtheta-phi) * ti.sin(phi)
                # ballsvectors[j][2] = ((jb4speed * ti.cos(jtheta-phi) * (jmass-imass) + 2 * imass * ib4speed * ti.cos(itheta-phi))/(jmass+imass)) * ti.sin(phi) + jb4speed * ti.sin(jtheta-phi) * ti.cos(phi)
                
                # ballsvectors[i][0] = (2 * jmass * jb4speed * ti.cos(jtheta-phi))/(imass+jmass) * ti.cos(phi) + ib4speed * ti.sin(itheta-phi) * ti.sin(phi)
                # ballsvectors[i][2] = ((2 * jmass * jb4speed * ti.cos(jtheta-phi))/(imass+jmass)) * ti.sin(phi) + ib4speed * ti.sin(itheta-phi) * ti.cos(phi)
                
                # ballsvectors[j][0] = ((2 * imass * ib4speed * ti.cos(itheta-phi))/(jmass+imass)) * ti.cos(phi) + jb4speed * ti.sin(jtheta-phi) * ti.sin(phi)
                # ballsvectors[j][2] = ((2 * imass * ib4speed * ti.cos(itheta-phi))/(jmass+imass)) * ti.sin(phi) + jb4speed * ti.sin(jtheta-phi) * ti.cos(phi)
                
                
                #print(angle)
                #incorporate force from b4
                
                #this is creating momentum. both should not speed up
                
                # ballsvectors[i][0] = ti.cos(angle) * speed * resistance
                # ballsvectors[i][2] = ti.sin(angle) * speed * resistance
                
                # ballsvectors[j][0] = ti.cos(angle) * speed * resistance
                # ballsvectors[j][2] = ti.sin(angle) * speed * resistance
                
                # ballsvectors[i][0] = ti.cos(angle) * ti.sin(angle)**2 * speed * resistance
                # ballsvectors[i][2] = ti.sin(angle)**3 * speed * resistance
                
                # ballsvectors[j][0] = ti.cos(angle)**3 * speed * resistance
                # ballsvectors[j][2] = ti.sin(angle) * ti.cos(angle)**2 * speed * resistance
                

                # speed2 = ti.math.sqrt((ballsvectors[i][0] - ballsvectors[j][0]) ** 2 + (ballsvectors[i][2] - ballsvectors[j][2]) ** 2)
                
    #endregion         
                    
    #region barriers
    for i in range(16):
        # print(balls[i])
        if balls[i][2]>8.7:
            #flip only that bit
            ballsvectors[i][2] = -abs(ballsvectors[i][2]) * resistance
            
            
        if  balls[i][2]<0.1:
            ballsvectors[i][2] = abs(ballsvectors[i][2]) * resistance
            
            
        if balls[i][0]>4.3:
            #flip only that bit
            ballsvectors[i][0] = -abs(ballsvectors[i][0]) * resistance
            
        if balls[i][0]<0.1:
            ballsvectors[i][0] = abs(ballsvectors[i][0]) * resistance
    #endregion

    for i in range(16):
        ballsvectors[i] *= 0.993
        balls[i] = balls[i] + ballsvectors[i]

#endregion

while window.running:
    init_stick_vertices(0.05,0.1, -1, 3, 2.2, 1.5, 10-stickval, 0)
    scene.set_camera(camera)
    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.LMB)
    scene.ambient_light((0.9, 0.9, 0.9))
    
    #region table
    scene.mesh(vertices=table_vertices, indices=table_indices, color=surface, show_wireframe=False)
    scene.mesh(vertices=bumper1_vertices, indices=bumper1_indices, color=surface, show_wireframe=False)
    scene.mesh(vertices=bumper2_vertices, indices=bumper2_indices, color=surface, show_wireframe=False)
    scene.mesh(vertices=bumper3_vertices, indices=bumper3_indices, color=surface, show_wireframe=False)
    scene.mesh(vertices=bumper4_vertices, indices=bumper4_indices, color=surface, show_wireframe=False)
    scene.mesh(vertices=bumper1top_vertices, indices=bumper1top_indices, color=tablecolor, show_wireframe=False)
    scene.mesh(vertices=bumper2top_vertices, indices=bumper2top_indices, color=tablecolor, show_wireframe=False)
    scene.mesh(vertices=bumper3top_vertices, indices=bumper3top_indices, color=tablecolor, show_wireframe=False)
    scene.mesh(vertices=bumper4top_vertices, indices=bumper4top_indices, color=tablecolor, show_wireframe=False)
    #endregion
    
    scene.mesh(vertices=stick_vertices, indices=stick_indices, color=(177/255,85/255,34/255), show_wireframe=False)
    scene.particles(centers=balls, radius = 0.1, per_vertex_color=colors)
    
    canvas.scene(scene)
    window.show()
    if stickval<=2:
        stickval+=stickval/4
    elif switch == True:
        bool=True
        
    if bool==True:
        bool=False
        switch= False
        ballsvectors[15] = (0,0,-0.5)
        
    updateballs()  