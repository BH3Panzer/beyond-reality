import pyxel as px
WIDTH = 512
HEIGHT = 256
px.init(WIDTH, HEIGHT)
px.mouse(True)
px.load("res.pyxres")
state = "main_menu"

def update():
    pass

def draw():
    px.cls(0)
    if state == "main_menu":
        px.blt(int(WIDTH/8)*3, 0, 0, 8, 0, 39, 24, colkey=0)

px.run(update, draw)