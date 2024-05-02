import pyxel as px
from os import listdir
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
tick = 0 #timer pour des animations trop stylé 
mapA = None #nom de la map actuel
listSaves = listdir("saves/") #liste les fichiers de sauvegardes
cursor = 0 #utiliser pour indiquer la position dans un menu déroulant
saveLoad = None #nom du fichier de sauvegarde actuellement utiliser

from frames import *

#Les lettres ont 6 hauteur et 3 largeur
#son  ton:Pulse,Triangle,Square,Noise  efx:F; la note s'arrête instant, S;relie les notes, Vibrato, Normal

px.playm(0, loop=True)

# class for players
class Player:
    def __init__(self, name, pv, pa, pos = [0, 0]):
        self.name = name
        self.pv = pv
        self.pa = pa
        self.pos = pos

# class for entities
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

#create an entitie
def newEntitie(name, skin, pos, reverse = False):
    global allEntities
    i = 0
    while i in allEntities:
        i += 1
    allEntities.append(i)
    l["Entitie"+str(i)] = Entities(i, name, skin, pos ,reverse)

# delete an entitie
def supprEntitie(i):
    del l["Entitie"+str(i)]
    allEntities.remove(i)

def drawEntitie(skin, x, y, name, reverse = False):
    for i in skin.items():
        sprite = frames[name][i[0]][int(i[1])] #va prendre les dimensions du sprite [nom de l'entité];[nom de la partie du corps];[frame de cette partie]
        px.blt(x + frames[name][i[0]][0][0] - frames[name]["defaut"][0] + ((sprite[4] * (-1 if reverse else 1)) if len(sprite)>=5 else 0), y + frames[name][i[0]][0][1] - frames[name]["defaut"][1] + (sprite[5] if len(sprite)>=6 else 0)
            , frames[name]["image"], sprite[0], sprite[1], (sprite[2]-sprite[0]+1) * (-1 if reverse else 1), sprite[3]-sprite[1]+1, colkey=frames[name]["transparence"])

def drawFichier(x,y,name):
    px.rect(x,y,236,25,1)
    px.text(x+5,y+5,name[0:-4],9)

def readSaves(saves):
    pass

def animStyle(col = 1): #anim trop stylée avec des tit' rectangles
    if tick > 0:
        for x in range(int(tick)):
            for y in range(13):
                i = x - y
                tickA = tick - y
                if i >= 0:
                    if 4-(tickA-i) >= 0:
                        temp = 4-(tickA-i)
                    else:
                        temp = 0
                    px.rect(i*10+temp,y*10+temp,(tickA-i+1)*2 if tickA-i<4 else 10,(tickA-i+1)*2 if tickA-i<4 else 10,col)

#détecte si un point est dans un rectangle
def collidpoint(point, rect):
    if point[0] >= rect[0] and point[0] <= rect[2] and point[1] >= rect[1] and point[1] <= rect[3]:
        return True
    else:
        return False

# update game
def update():
    global cristal,cristalTick,tick,state,cursor
    if state == "title_menu": #menu avec uniquement le titre
        cristalTick[1] += 1
        if cristalTick[1] == cristalClock[cristalTick[0]][1]:
            cristalTick[0] += 1
            if cristalTick[0] == len(cristalClock):
                cristalTick[0] = 0
            cristal["entier"] = cristalClock[cristalTick[0]][0]
            cristalTick[1] = 0
        if tick == 0:
            if px.btn(px.KEY_SPACE):
                tick += 1
        else:
            tick += 1
            if tick == 15:
                state = "main_menu"
                tick = 0
    elif state == "main_menu": #menu principal
        if px.btnp(px.MOUSE_BUTTON_LEFT):
            if collidpoint([px.mouse_x, px.mouse_y], [3,3,18,18]):
                px.quit()
            elif collidpoint([px.mouse_x, px.mouse_y], [112,56,144,72]):
                state = "selFichier"
    elif state == "selFichier": #menu de séléction de fichier de sauvegarde
        if tick != 0:
            tick += 0.7
            if tick > 42:
                state = "ingame"
                tick = 0
        else:
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                if collidpoint([px.mouse_x, px.mouse_y], [3,3,18,18]):
                    state = "main_menu"
                else:
                    for i in range(len(listSaves) if len(listSaves)<=3 else 3):
                        if collidpoint([px.mouse_x, px.mouse_y], [10,30+i*34,236,55+i*34]):
                            saveLoad = listSaves[i+cursor]
                            tick += 1
            if px.btnp(px.KEY_S, 30, 10) or px.btnp(px.KEY_DOWN, 30, 10):
                cursor += 1
            if (px.btnp(px.KEY_Z, 30, 10) or px.btnp(px.KEY_UP, 30, 10)) and cursor != 0:
                cursor -= 1

# draw game
def draw():
    px.cls(0)
    if state == "title_menu":
        px.bltm(0,0,0,832,384,256,128)
        px.blt(int(WIDTH/2)-72, 0, 0, 8, 0, 144, 24, colkey=0)
        if int(str(tick)[-1])%3 == 0:
            px.text(91,75,"press space to play",1)
        drawEntitie(cristal, 120, 56, "cristal")
        for i in allEntities:
            l["Entitie"+str(i)].sDraw()
    elif state == "main_menu":
        px.bltm(0,0,0,832,384,256,128)
        px.blt(int(WIDTH/2)-72, 0, 0, 8, 0, 144, 24, colkey=0)
        px.blt(3,3,0,152,0,16,16,colkey=0) #bouton quitter
        px.blt(237,3,0,168,0,16,16,colkey=0) #bouton option
        px.blt(112,56,0,184,0,32,16,colkey=0) #bouton play
        px.text(3,119,"created by BH3Panzer and Fraii",1)
    elif state == "selFichier":
        px.bltm(0,0,0,832,384,256,128)
        px.blt(int(WIDTH/2)-72, 0, 0, 8, 0, 144, 24, colkey=0)
        px.blt(3,3,0,152,0,16,16,colkey=0) #bouton quitter
        for i in range(len(listSaves) if len(listSaves)<=3 else 3):
            drawFichier(10,30+i*34,listSaves[i+cursor])
            if collidpoint([px.mouse_x, px.mouse_y], [10,30+i*34,236,55+i*34]):
                px.rectb(9,29+i*34,238,27,10)
        animStyle(9)

# created some entities for title menu
newEntitie("scientifique", {"pied":0,"corps":0,"tete":0,"oeil":0}, [81,56], False)
newEntitie("scientifique", {"pied":0,"corps":0,"tete":1,"oeil":4}, [159,56], True)
newEntitie("scientifique", {"pied":1,"corps":1,"tete":2,"oeil":1}, [57,29], False)
newEntitie("scientifique", {"pied":1,"corps":1,"tete":0,"oeil":3}, [182,29], True)
newEntitie("scientifique", {"pied":1,"corps":1,"tete":2,"oeil":0}, [57,82], False)
newEntitie("scientifique", {"pied":1,"corps":1,"tete":3,"oeil":2}, [182,82], True)
px.run(update, draw)