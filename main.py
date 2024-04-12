import pyxel as px
WIDTH = 256
HEIGHT = 128
fps = 30
quit_key = px.KEY_ESCAPE
title = "beyond reality"
px.init(WIDTH, HEIGHT, title, fps, quit_key)
px.mouse(True)
px.load("res.pyxres")
state = "title_menu"
l = locals()
perso = {"pied":0, "corps":0, "tete":0}
cristal = {"entier":0}
cristalTick = [0,0]
cristalClock = [[0,3],[8,5],[9,16],[8,5],[0,3],[7,5],[6,16],[7,5]]
allEntities = []
title = 0

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

class Entities:
    def __init__(self, sId, name, skin, pos, reverse):
        self.sId = sId
        self.name = name
        self.skin = skin
        self.x = pos[0]
        self.y = pos[1]
        self.reverse = reverse
    
    def sDraw(self):
        drawEntitie(self.skin, self.x, self.y, self.name, self.reverse)

def newEntitie(name, skin, pos, reverse = False):
    global allEntities
    i = 0
    while i in allEntities:
        i += 1
    allEntities.append(i)
    l["Entitie"+str(i)] = Entities(i, name, skin, pos ,reverse)

def supprEntitie(i):
    del l["Entitie"+str(i)]
    allEntities.remove(i)

def drawEntitie(skin, x, y, name, reverse = False):
    for i in skin.items():
        sprite = frames[name][i[0]][int(i[1])] #va prendre les dimensions du sprite [nom de l'entité];[nom de la partie du corps];[frame de cette partie]
        px.blt(x + frames[name][i[0]][0][0] - frames[name]["defaut"][0] + ((sprite[4] * (-1 if reverse else 1)) if len(sprite)>=5 else 0), y + frames[name][i[0]][0][1] - frames[name]["defaut"][1] + (sprite[5] if len(sprite)>=6 else 0)
            , frames[name]["image"], sprite[0], sprite[1], (sprite[2]-sprite[0]+1) * (-1 if reverse else 1), sprite[3]-sprite[1]+1, colkey=frames[name]["transparence"])

def update():
    global cristal,cristalTick,title,state
    if state == "title_menu":
        cristalTick[1] += 1
        if cristalTick[1] == cristalClock[cristalTick[0]][1]:
            cristalTick[0] += 1
            if cristalTick[0] == len(cristalClock):
                cristalTick[0] = 0
            cristal["entier"] = cristalClock[cristalTick[0]][0]
            cristalTick[1] = 0
        if title == 0:
            if px.btn(px.KEY_SPACE):
                title += 1
        else:
            title += 1
            if title == 15:
                state = "main_menu"

def draw():
    px.cls(0)
    if state == "title_menu":
        px.bltm(0,0,0,832,0,256,128)
        px.blt(int(WIDTH/2)-72, 0, 0, 8, 0, 145, 24, colkey=0)
        if int(str(title)[-1])%3 == 0:
            px.text(91,75,"press space to play",1)
        drawEntitie(cristal, 120, 56, "cristal")
        for i in allEntities:
            l["Entitie"+str(i)].sDraw()
    elif state == "main_menu":
        px.bltm(0,0,0,832,0,256,128)
        px.blt(int(WIDTH/2)-72, 0, 0, 8, 0, 145, 24, colkey=0)

newEntitie("scientifique", {"pied":0,"corps":0,"tete":0,"oeil":0}, [81,56], False)
newEntitie("scientifique", {"pied":0,"corps":0,"tete":1,"oeil":4}, [159,56], True)
newEntitie("scientifique", {"pied":1,"corps":1,"tete":2,"oeil":1}, [57,29], False)
newEntitie("scientifique", {"pied":1,"corps":1,"tete":0,"oeil":3}, [182,29], True)
newEntitie("scientifique", {"pied":1,"corps":1,"tete":2,"oeil":0}, [57,82], False)
newEntitie("scientifique", {"pied":1,"corps":1,"tete":3,"oeil":2}, [182,82], True)
px.run(update, draw)