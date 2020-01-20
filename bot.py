import random
import numpy
import sys
from MotionFromMap import MotionFromMap
from Generatemap import generatemap


class Bot:
    def scan(self):
        mfp = MotionFromMap("maps/map1")
        # mapresult = generatemap()
        # numpy.set_printoptions(threshold=sys.maxsize)
        # print(mapresult)
        # position initiale
        position = [1, 1]
        # matrice contenant la carte (premiere case de première ligne à positif)

        x, y = 66, 66
        mapresult = [[0 for x in range(x)] for y in range(y)]
        mapresult[position[0]][position[1]] = 1


        # Tant que la map n'est pas rempli
        # while numpy.shape(mapresult) != (66, 66):
        while True:
            # initialisation rotate
            rotate = 1
            print(rotate)
            print(position)

            # affichage de la matrice
            s = [[str(e) for e in row] for row in mapresult]
            lens = [max(map(len, col)) for col in zip(*s)]
            fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
            table = [fmt.format(*row) for row in s]
            print('\n'.join(table))

            print(mfp)
            # appel de la récursive
            mapresult, position = self.rec(mfp, position, rotate, mapresult)

    def rec(self, mfp, position, rotate, mapresult):
        # effectue la rotation, si premier appel, pas de rotation
        print("position dans recursive : " + str(position))
        mfp.rotate(rotate)
        # tente  le mouvement
        boolMove = mfp.move(1)
        # Si mouvement valide et sans rotation
        print("boolmove :" + str(boolMove))
        if boolMove and rotate == 0:
            # renseigne le résultat de la map à positif après avoir mis à jour la position
            position[1] += 1
            mapresult[position[0]][position[1]] = 1
            # renvoit les résultats et la nouvelle position
            return mapresult, position
        # Si mouvement valide et avec rotation (effectué avant dans rec)
        elif boolMove and rotate != 0:
            # renseigne le résultat de la map à positif
            mapresult[position[0]][position[1]] = 1
            # renvoit les résultats et la nouvelle position
            return mapresult, position
        # Sinon, mouvement invalide
        else:
             print("C'est faux")
            # initie une valeur pour une rotation
            rotate = random.randint(1, 4)
            print("rotation dans c'est faux :  " + str(rotate))
            # renseigne le résultat de la map à positif
            mapresult[position[0]][position[1]] = 0
            # prépare la position pour le prochain appel en fonction de la rotation
            if rotate == 2:
                position[0] += 1
            elif rotate == 3:
                position[1] -= 1
            elif rotate == 4:
                position[0] -= 1
            # appel de la récurvise pour retenter le mouvement avec les nouvelles valeurs
            self.rec(mfp, position, rotate, mapresult)

