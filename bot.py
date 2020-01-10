import random
import numpy

class Bot:

    def scan(self):
        m1 = motion()
        position = [0, 0]
        mapResult = [[1]]
        while numpy.shape(mapResult) != (66, 66):
            rotate = 1
            mapResult, position = self.rec(m1, position, rotate, mapResult)

    def rec(self, m1, position, rotate, mapResult):
        m1.rotate(rotate)
        boolMove = m1.move(1)
        if boolMove:
            # Ligne du dessous pas ouf ?
            mapResult[position[1]].append(1)
            position[0] = position[0] + 1
            return mapResult, position
        else:
            rotate = random.randint(1, 4)
            if rotate == 1:
                position[0] = position[0] + 1
            elif rotate == 2:
                position[1] = position[1] + 1
            elif rotate == 3:
                position[0] = position[0] - 1
            else:
                position[1] = position[1] - 1

        # manque un truc dans ce putain de if/else, ou alors des opérations pas faites au bon endroit ?...

            self.rec(m1, position, rotate, mapResult)