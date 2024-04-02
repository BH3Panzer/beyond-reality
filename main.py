import pyxel as px
WIDTH = 256
HEIGHT = 128
px.init(WIDTH, HEIGHT)
px.mouse(True)
px.load("res.pyxres")
state = "main_menu"

#son  ton:Pulse,Triangle,Square,Noise  efx:F; la note s'arrête instant, S;relie les notes, Vibrato, Normal

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
        px.blt(int(WIDTH/2)-72, 0, 0, 8, 0, 145, 24, colkey=0)
        px.text(int(WIDTH/2),int(HEIGHT/2),"abcdefghijklmno pqrstuvwxyz",1) #6 hauteur, 3 largeur

px.run(update, draw)