import pyxel as px
WIDTH = 256
HEIGHT = 128
px.init(WIDTH, HEIGHT)
px.mouse(True)
px.load("res.pyxres")
state = "main_menu"
l = locals()
perso = {"pied":0, "corps":0, "tete":0}
test = {"entier":0}
from frames import *

#Les lettres ont 6 hauteur et 3 largeur
#son  ton:Pulse,Triangle,Square,Noise  efx:F; la note s'arrête instant, S;relie les notes, Vibrato, Normal

px.playm(0, loop=True)
class Player:
    def __init__(self, name, pv, pa, pos = [0, 0]):
        self.name = name
        self.pv = pv
        self.pa = pa
        self.pos = pos

def drawEntitie(entitie, x, y, name):
    for i in entitie.items():
        sprite = frames[name][i[0]][int(i[1])] #va prendre les dimensions du sprite [nom de l'entité];[nom de la partie du corps];[frame de cette partie]
        px.blt(x + frames[name][i[0]][0][0] - frames[name]["defaut"][0] + (sprite[4] if len(sprite)>=5 else 0), y + frames[name][i[0]][0][1] - frames[name]["defaut"][1] + (sprite[5] if len(sprite)>=6 else 0), frames[name]["image"], sprite[0], sprite[1], sprite[2]-sprite[0]+1, sprite[3]-sprite[1]+1, colkey=frames[name]["transparence"])

def update():
    global test,perso
    test["entier"] += 0.24
    if test["entier"] > 6:
        test["entier"] = 0

def draw():
    px.cls(0)
    if state == "main_menu":
        px.bltm(0,0,0,832,0,256,128)
        px.blt(int(WIDTH/2)-72, 0, 0, 8, 0, 145, 24, colkey=0)
        px.text(91,75,"press space to play",1)
        drawEntitie(test, 120, 56, "cristal")
        drawEntitie(perso, 78, 56, "perso")

px.run(update, draw)