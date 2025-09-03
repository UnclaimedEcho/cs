import taichi as ti
ti.init(arch=ti.cpu)

window = ti.ui.Window('Test triangle', (800, 800))
canvas = window.get_canvas()
scene = ti.ui.Scene()
camera = ti.ui.Camera()

camera.position(3, 3, 1)
camera.lookat(2, 1, 1)
scene.set_camera(camera)

num_triangles = 1
mesh_indices = ti.field(int, shape = num_triangles * 3)
vertices = ti.Vector.field(3, dtype=float, shape = num_triangles * 3)
colors = ti.Vector.field(3, dtype=float, shape = num_triangles * 3)

colors[0] = (1,0,0)
colors[1] = (0,1,0)
colors[2] = (0,0,1)

@ti.kernel
def init_mesh_pos(points: ti.template()):
  points[0] = (2,0,0)
  points[1] = (4,0,0)
  points[2] = (3,-2,0)

@ti.kernel
def init_mesh_indices(indices: ti.template()):
  indices[0] = 0
  indices[1] = 1
  indices[2] = 2

init_mesh_pos(vertices)
init_mesh_indices(mesh_indices)

while window.running:
  camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.SPACE)
  scene.set_camera(camera)
  scene.ambient_light((0.9, 0.9, 0.9))
  scene.point_light(pos=(3,3,1), color=(1,0.9,0.5))
  scene.point_light(pos=(-3,3,1), color=(1,0.9,0.5))
  scene.mesh(vertices, indices=mesh_indices, per_vertex_color=colors, two_sided=True, vertex_count=3, show_wireframe=False)
  canvas.scene(scene)
  window.show()