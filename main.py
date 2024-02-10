import pyxel as px
WIDTH = 512
HEIGHT = 256
class App:
    def __init__(self):
        px.init(WIDTH, HEIGHT)
        self.x = 0
        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        px.cls(0)

App()