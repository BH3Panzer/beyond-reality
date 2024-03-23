import pyxel as px
WIDTH = 512
HEIGHT = 256
px.init(WIDTH, HEIGHT)
px.mouse(True)
px.load("res.pyxres")
state = "main_menu"

px.playm(0, loop=True)
class Player:
    def __init__(self, name, pv, pa, pos = [0, 0]):
        self.name = name
        self.pv = pv
        self.pa = pa
        self.pos = pos


def update():
    pass

def draw():
    px.cls(0)
    if state == "main_menu":
        px.blt(int(WIDTH/8)*3, 0, 0, 8, 0, 145, 23, colkey=0)

px.run(update, draw)