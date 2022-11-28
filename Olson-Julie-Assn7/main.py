class Artomat:
    def __init__(self, text1="Adams", text2="Arbus", text3="Dali", text4="Lange", money=0.00, hopper=0.00, bin1=10, bin2=10, bin3=10, bin4=10):
        # set all = to the default values
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4
        self.money = money / 4  # divide by 4 because it's a dollar amount in quarters
        self.hopper = hopper / 4
        self.bin1 = bin1
        self.bin2 = bin2
        self.bin3 = bin3
        self.bin4 = bin4


    def printStatus(self):
        # prints how many packs there are in each bin, and what kind they are
        print("\n1: " + str(self.bin1) + " packs of " + self.text1)
        print("2: " + str(self.bin2) + " packs of " + self.text2)
        print("3: " + str(self.bin3) + " packs of " + self.text3)
        print("4: " + str(self.bin4) + " packs of " + self.text4)
        # prints the amount of money in the machine and in the hopper
        print("There is $ " + str(format(self.money, ".2f")) + " in the machine.")
        print("There is $ " + str(format(self.hopper, ".2f")) + " in the hopper.")
        print("\n")

    def dropQuarter(self):
        # adds 25 cents to both the hopper and total money count
        print("ching")
        self.hopper += .25
        self.money += .25
        return self.money, self.hopper

    def pullKnob(self, number):
        # specifies which knob was pulled
        if number == 1:
            # if there is at least 75 cents in the hopper the machine gives you a pack
            if self.hopper >= .75:
                print("A pack of " + self.text1 + " slides into view")
                # hopper empties
                self.hopper = 0
                # one less pack in the machine
                self.bin1 -= 1
                return self.hopper, self.bin1
            else:
                # if there is less than 75 cents in the hopper the machine will not give you a pack
                print("/(nothing happens/)")
        elif number == 2:
            if self.hopper >= .75:
                print("A pack of " + self.text2 + " slides into view")
                self.hopper = 0
                self.bin2 -= 1
                return self.hopper, self.bin2
            else:
                print("/(nothing happens/)")
        elif number == 3:
            if self.hopper >= .75:
                print("A pack of " + self.text3 + " slides into view")
                self.hopper = 0
                self.bin2 -= 1
                return self.hopper, self.bin3
            else:
                print("/(nothing happens/)")
        elif number == 4:
            if self.hopper >= .75:
                print("A pack of " + self.text4 + " slides into view")
                self.hopper = 0
                self.bin2 -= 1
                return self.hopper, self.bin4
            else:
                print("/(nothing happens/)")

    def restock(self):
        print("A grouchy-looking attendant shows up, opens the back, fiddles around a bit, closes it, and leaves.")
        # all bins are refilled to 10, all money is taken out of machine
        self.bin1 = 10
        self.bin2 = 10
        self.bin3 = 10
        self.bin4 = 10
        self.hopper = 0
        self.money = 0
        return self.bin1, self.bin2, self.bin3, self.bin4, self.hopper, self.money


# write your class definition above this line
# make no changes below this line

def main():
    photoMachine = Artomat(text1="Adams",text2="Arbus",text3="Dali",text4="Lange")
    portraitMachine = Artomat(money=212,hopper=2,bin1=1,bin2=0,bin3=8,bin4=10,text1="Picasso",text2="Rembrandt",text3="Van Gogh",text4="Monet")

    photoMachine.printStatus()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(1)
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.printStatus()
    photoMachine.restock()
    photoMachine.printStatus()
    print("----")
    portraitMachine.printStatus()
    portraitMachine.dropQuarter()
    portraitMachine.pullKnob(1)
    portraitMachine.printStatus()


main()
