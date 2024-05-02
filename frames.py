
"""
Pour chaque partie du corps on a les coordonnées du point haut gauche, celle du coin bas droit et celle du décalage (0,0 si rien)
transparence: indique la couleur de transparence
defaut: emplacement du sprite entier par défaut (dans les parties du corps élements 0 = par défaut)
"""
frames = {
        "perso": 
        {
            "transparence":7,
            "image":0,
            "defaut":[0,40,15,55],
            "pied":[[6,53,10,55],[17,48,22,50,-1],[24,48,30,50,-2],[17,52,21,54],[23,52,26,54,1],[28,52,32,54]],
            "corps":[[4,47,12,52],[17,41,25,46],[27,41,35,46]],
            "tete":[[5,41,11,46]]
        },
        "cristal":
        {
            "transparence":0,
            "image":1,
            "defaut":[0,0,15,15],
            "entier":[[0,0,15,15],[16,0,31,15],[32,0,47,15],[48,0,63,15],[64,0,79,15],[80,0,95,15],[0,0,15,15,0,2],[0,0,15,15,0,1],[0,0,15,15,0,-1],[0,0,15,15,0,-2]]
        },
        "scientifique":
        {
            "transparence":1,
            "image":0,
            "defaut":[0,56,15,71],
            "pied":[[6,69,10,71],[27,64,31,66]],
            "corps":[[4,63,12,68],[17,65,25,70]],
            "tete":[[5,57,11,62],[17,57,23,63,-1,-1],[25,57,31,62],[33,57,39,62]],
            "oeil":[[6,60,10,60],[33,64,37,64],[33,66,37,66],[33,68,37,68],[33,70,37,70]]
        }
    }

maps = {
        "labo_-5":[576,256,1336,632]
    }