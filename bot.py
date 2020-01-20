import random
import numpy
from IMotion import IMotion
from MotionFromMap import MotionFromMap


class Bot:

    def scan(self):
        m1 = IMotion()
        mfp = MotionFromMap(m1)
        # position initiale
        position = [0, 0]
        # matrice contenant la carte
        mapresult = [[1]]
        while numpy.shape(mapresult) != (66, 66):
            # initialisation rotate
            rotate = 0
            # essaye de bouger en ligne droite vers la droite
            position[0] = position + 1
            # appel de la récursive
            mapresult, position = self.rec(m1, position, rotate, mapresult)

    def rec(self, m1, position, rotate, mapresult):
        # effectue la rotation, si premier appel, pas de rotation
        m1.rotate(rotate)
        # tente  le mouvement
        boolMove = m1.move(1)
        # Si mouvement valide
        if boolMove:
            # renseigne le résultat de la map à positif
            mapresult[position[0]][position[1]] = 1
            # renvoit les résultats et la nouvelle position
            return mapresult, position
        # Sinon, mouvement invalide
        else:
            # initie une valeur pour une rotation
            rotate = random.randint(0, 3)
            # renseigne le résultat de la map à positif
            mapresult[position[0]][position[1]] = 0
            # prépare la position pour le prochain appel en fonction de la rotation
            if rotate == 0:
                position[0] = position[0] + 1
            elif rotate == 1:
                position[1] = position[1] + 1
            elif rotate == 2:
                position[0] = position[0] - 1
            else:
                position[1] = position[1] - 1
            # appel de la récurvise pour retenter le mouvement avec les nouvelles valeurs
            self.rec(m1, position, rotate, mapresult)