# Clase para la nave.
class Ship:
    def __init__(self, size, vertices, indices, speed, pipeline) -> None:
        self.color = np.zeros(3, dtype=np.float32)
        self.position = np.zeros(3, dtype=np.float32)
        self.scale = np.ones(3, dtype=np.float32)
        self.rotation = np.zeros(3, dtype=np.float32)

        self.yaw = 0
        self.pitch = 0
        self.direction = np.zeros(2)
        self.speed = speed
'''        
        self.ship = models_from_file(path, self.pipeline)[0]
        self.indices = models_from_file(path, self.pipeline)[3]
        self.size = len(models_from_file(path, self.pipeline)[4][1]) // 3
        self._buffer = pipeline.vertex_list_indexed(self.size, GL_TRIANGLES, self.indices)
        self._buffer.position = models_from_file(path, self.pipeline)[4][1]
'''
    def place(self):
        translation = Mat4.from_translation(Vec3(*self.position))
        rotation = Mat4.from_rotation(self.rotation[0] + self.pitch, Vec3(1, 0, 0)).rotate(self.rotation[1] + self.yaw,
                                                                                           Vec3(0, 1, 0)).rotate(
            self.rotation[2], Vec3(0, 0, 1))
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
