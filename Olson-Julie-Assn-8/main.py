#Julie Olson - MW2 XL

class PiggyBank:
    #set defaults
    def __init__(self, name="p0", money=0, broken=False):
        self.name = name
        self.money = money
        self.broken = broken

    # add money to the piggybank
    def deposit(self, change):
        if self.broken:
            # if it's broken, can't hold money
            self.money = 0
        else:
            # if not broken the money gets added to the bank
            self.money += change

    # breaks the piggybank
    def smash(self):
        broken = True
        self.broken = broken
        # once broken the bank loses all money
        self.money = 0

# prints the status of the piggybank specified when called
def printStatus(x,p1):
    print(x + " has $ " + str(format(p1.money, ".2f")) + " and is", end=" ")
    if p1.broken:
        print("broken.")
    else:
        print("not broken.")


def main():
    p1 = PiggyBank()
    p2 = PiggyBank()
    printStatus("p1",p1)
    p1.deposit(1.25)
    printStatus("p1",p1)
    p1.deposit(6.55)
    printStatus("p1",p1)
    p1.smash()
    printStatus("p1",p1)
    p1.deposit(2.15)
    printStatus("p1",p1)
    p1.__balance=100.0
    p1.__broken=False
    printStatus("p1",p1)

main()