import random

# the chess piece super class
class ChessPiece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__x = x
        self.__y = y

    def color(self):
        return self.__color

    def location(self):
        return (self.__x, self.__y)

    def x(self):
        return self.__x

    def y(self):
        return self.__y


# TODO: write all your code below this line
# Julie Olson - MW2 XL
class Pawn(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def pic(self):
        if super().color() == "w":
            return "\u2659"
        else:
            return "\u265f"

    def validMove(self, i, j):
        x, y = super().location()
        c = super().color()
        # makes sure pawns can only move in the correct direction based on their color
        if c == "w" and i == x and j == y + 1: return True
        if c == "b" and i == x and j == y - 1: return True
        return False

class Queen(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def pic(self):
        if super().color() == "w":
            return "\u2655"
        else:
            return "\u265B"

    def validMove(self, i, j):
        x, y = super().location()
        # can move diagonally
        if abs(x-i) == abs(y-j): return True
        # can move in straight lines
        if i == x or j == y: return True
        return False



class King(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def pic(self):
        if super().color() == "w":
            return "\u2654"
        else:
            return "\u265A"

    def validMove(self, i, j):
        x, y = super().location()
        # can move one space in any direction
        if i == x and j == y + 1: return True
        if i == x and j == y - 1: return True
        if i == x - 1 and j == y: return True
        if i == x + 1 and j == y: return True
        if i == x - 1 and j == y - 1: return True
        if i == x - 1 and j == y + 1: return True
        if i == x + 1 and j == y - 1: return True
        if i == x + 1 and j == y + 1: return True
        return False


class Rook(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def pic(self):
        if super().color() == "w":
            return "\u2656"
        else:
            return "\u265C"

    def validMove(self, i, j):
        x, y = super().location()
        # can only move in straight lines
        if i == x or j == y: return True
        return False


class Knight(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def pic(self):
        if super().color() == "w":
            return "\u2658"
        else:
            return "\u265E"

    def validMove(self, i, j):
        x, y = super().location()
        # can only move 2 forward and 1 over, but can do so in any direction
        if i == x + 2 and j == y - 1: return True
        if i == x - 2 and j == y - 1: return True
        if i == x + 2 and j == y + 1: return True
        if i == x - 2 and j == y + 1: return True
        if i == x + 1 and j == y - 2: return True
        if i == x - 1 and j == y - 2: return True
        if i == x + 1 and j == y + 2: return True
        if i == x - 1 and j == y + 2: return True
        return False

class Bishop(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def pic(self):
        if super().color() == "w":
            return "\u2657"
        else:
            return "\u265D"

    def validMove(self, i, j):
        x, y = super().location()
        # can only move diagonally
        if abs(x-i) == abs(y-j): return True
        return False


# TODO: write all your code above this line
# print a nice picture of the valid moves 
# white pawns only move "up" one space
# black pawns only move "down" one space
# other chess pieces move normally
def printValidMoves(cp):
    print("\t  ", cp.pic(), "at", cp.location())
    for i in range(7, -1, -1):
        print("\t" + str(i) + " ", end="")
        for j in range(0, 8):
            if cp.x() == j and cp.y() == i:
                print(cp.pic() + " ", end="")
            elif cp.validMove(j, i):
                print("* ", end="")
            else:
                print(". ", end="")
        print()
    print("\t  ", end="")
    for i in range(0, 8):
        print(str(i) + " ", end="")
    print()
    print()


# returns a random chess piece at a random location
# each of these types must inherit from ChessPiece
def randomChessPiece():
    if random.randint(0, 1) == 0:
        c = "w"
    else:
        c = "b"
    t = random.randint(1, 6)
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if t == 1: return Pawn(c, x, y)
    if t == 2: return Queen(c, x, y)
    if t == 3: return King(c, x, y)
    if t == 4: return Rook(c, x, y)
    if t == 5:
        return Knight(c, x, y)
    else:
        return Bishop(c, x, y)


def main():
    clist = []
    # make a list of random chess pieces
    for i in range(0, 10):
        clist.append(randomChessPiece())
    # display thier valid moves
    for i in range(0, len(clist)):
        # behold! polymorphism works!
        printValidMoves(clist[i])


main()