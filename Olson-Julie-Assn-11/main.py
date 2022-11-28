import random
import time

# Julie Olson - MW2 XL
class life:
    def __init__(self):
        self.__genA = []
        self.__genB = []
        self.__gens = 0
        # make the lists
        for i in range(0, 22):
            self.__genA.append([])
            self.__genB.append([])
            for j in range(0, 22):
                self.__genA[i].append(" ")
                self.__genB[i].append(" ")

    def chance(self):
        # each cell gets a 1 in 3 chance of life
        for i in range(1, 21):
            for j in range(1, 21):
                chance = random.randint(1, 3)
                if chance == 1:
                    chance = "x"
                else:
                    chance = " "
                self.__genA[i][j] = chance

    def print(self):
        # prints the lists
        for i in range(0, 22):
            for j in range(0, 22):
                print(self.__genA[i][j], end=" ")
            print()

    def grow(self):
        # does not include border
        for i in range(1, 21):
            for j in range(1, 21):
                # if a cell has less than 2 live neighbors it dies
                if self.buddies(i, j) < 2:
                    self.__genB[i][j] = ' '
                # if it has 2 live neighbors it lives
                if self.buddies(i, j) == 2:
                    self.__genB[i][j] = self.__genA[i][j]
                # if it has 3 live neighbors it lives
                if self.buddies == 3:
                    self.__genB[i][j] = self.__genA[i][j]
                # if it has more than 3 live neighbors it dies
                if self.buddies(i, j) > 3:
                    self.__genB[i][j] = ' '
                # if a dead cell has 3 live neighbors it gains life
                elif self.deadBuddies(i, j) == 3:
                    self.__genB[i][j] = 'x'

        # after the cells are arranged in the future generation
        # the future gen becomes the current gen
        for i in range(1, 21):
            for j in range(1, 21):
                self.__genA[i][j] = self.__genB[i][j]
        # keeps track of the number of gens that have occurred
        self.__gens += 1

    def buddies(self, i, j):
        num = 0
        # checks cells neighbors
        if self.__genA[i][j] == 'x':
            # cell itself does not count as a neighbor
            num -= 1
        for p in range(i-1, i+1):
            for q in range(j-1, j+1):
                if self.__genA[p][q] == 'x':
                    num += 1
        return num

    def deadBuddies(self, i, j):
        num = 0
        # checks neighbors of dead cells
        if self.__genA[i][j] == ' ':
            num -= 1
        for p in range(i-1, i+1):
            for q in range(j-1, j+1):
                if self.__genA[p][q] == ' ':
                    num += 1
        return num

    def gens(self):
        return self.__gens


def main():
    l = life()
    l.chance()
    while l.gens() < 50:
        l.print()
        l.grow()
        print("Number of generations: ", end='')
        print(l.gens())
        time.sleep(0.3)

    print()
main()