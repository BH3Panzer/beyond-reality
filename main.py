import pyxel as px
WIDTH = 512
HEIGHT = 256
class App:
    def __init__(self):
        px.init(WIDTH, HEIGHT)
        px.mouse(True)
        px.run(self.update, self.draw)
        self.state = "main_menu"

    def update(self):
        pass

    def draw(self):
        px.cls(0)

App()