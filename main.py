import pyxel as px
WIDTH = 512
HEIGHT = 256
px.init(WIDTH, HEIGHT, title="Beyond Reality")

def update():
    pass

def draw():
    px.cls(0)

px.run(update, draw)

