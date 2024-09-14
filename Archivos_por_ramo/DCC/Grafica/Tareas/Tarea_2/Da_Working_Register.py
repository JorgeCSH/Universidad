# Clase para la nave.
class Ship:
    def __init__(self, size, vertices, indices, speed, pipeline) -> None:
        self.color = np.zeros(3, dtype=np.float32)
        self.position = np.zeros(3, dtype=np.float32)
        self.scale = np.ones(3, dtype=np.float32)
        self.rotation = np.zeros(3, dtype=np.float32)

        self.sensitivity = 0.01
        self.yaw = 0
        self.pitch = 0

        self.speed = speed
        self.direction = np.zeros(2)
        self.front = np.array([0, 0, -1], dtype=np.float32)
        self.up = np.array([0, 1, 0], dtype=np.float32)

        self._buffer = pipeline.vertex_list_indexed(size, GL_TRIANGLES, indices)
        self._buffer.position = vertices

    def update(self, dt):
        self.front[0] = np.cos(self.yaw) * np.cos(self.pitch)
        self.front[1] = np.sin(self.pitch)
        self.front[2] = np.sin(self.yaw) * np.cos(self.pitch)
        self.front /= np.linalg.norm(self.front)

        dir = self.direction[0]*self.front + self.direction[1]*np.cross(self.up, self.front)
        dir_norm = np.linalg.norm(dir)
        if dir_norm:
            dir /= dir_norm

        self.position += dir*self.speed*dt

    def model(self):
        translation = Mat4.from_translation(Vec3(*self.position))
        rotation = Mat4.from_rotation(self.rotation[0] + self.pitch, Vec3(1, 0, 0)).rotate(self.rotation[1] + self.yaw, Vec3(0, 1, 0)).rotate(self.rotation[2], Vec3(0, 0, 1))
        scale = Mat4.from_scale(Vec3(*self.scale))
        return translation @ rotation @ scale

    def draw(self):
        self._buffer.draw(GL_TRIANGLES)





def file_to_vertexlist(self, path, pipeline):
    mesh = tm.load(path)
    # aplicamos un scale y una traslación para asegurarnos
    # que el modelo cabe en la pantalla y que está al centro
    mesh.apply_transform(tr.uniformScale(2.0 / mesh.scale) @ tr.translate(*-mesh.centroid))

    vertex_list = tm.rendering.mesh_to_vertexlist(mesh)

    # en la posicion [0] esta la cantidad de vertices
    # en [3] estan los indices
    buffer = pipeline.vertex_list_indexed(vertex_list[0], GL_TRIANGLES, vertex_list[3])

    # en [4][1] estan los vertices
    buffer.position = vertex_list[4][1]
    return buffer






Ship("objects/Extremely basic space shuttle (2).obj", speed = 1)

# Para no borrarlo por accidente:
provitional_ship = models_from_file("objects/Extremely basic space shuttle (2).obj", pipeline)[0]
provitional_ship.color = real_rgb(150, 140, 150)
provitional_ship.scale = [.5] * 3
provitional_ship.position = [2, 1, 1]
