# Clase para la nave.
class Ship:
    def __init__(self, size, vertices, indices, speed, pipeline) -> None:
        self.color = np.zeros(3, dtype=np.float32)
        self.position = np.zeros(3, dtype=np.float32)
        self.scale = np.ones(3, dtype=np.float32)
        self.rotation = np.zeros(3, dtype=np.float32)
        self.yaw = 0
        self.pitch = 0
        self.speed = speed
        self._buffer = pipeline.vertex_list_indexed(size, GL_TRIANGLES, indices)
        self._buffer.position = vertices

    def place(self):
        translation = Mat4.from_translation(Vec3(*self.position))
        rotation = Mat4.from_rotation(self.rotation[0]+self.pitch, Vec3(1, 0, 0)).rotate(self.rotation[1]+self.yaw, Vec3(0, 1, 0)).rotate(
            self.rotation[2] , Vec3(0, 0, 1))
        scale = Mat4.from_scale(Vec3(*self.scale))
        return translation @ rotation @ scale

    def draw(self):
        self._buffer.draw(GL_TRIANGLES)

