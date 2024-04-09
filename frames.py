
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
            "entier":[[0,0,15,15],[16,0,31,15],[32,0,47,15],[48,0,63,15],[64,0,79,15],[80,0,95,15]]
        }
    }