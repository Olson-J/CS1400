import random
import time

die = random.randint(1, 6)
myScore = 0
devilScore = 0
myTurn = True
myPts = myScore
devilPts = devilScore
pts = 100
start = 0
done = False

def printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start):
    # die - 'rolls' to get int value 1-6
    # myScore - player saved score, int 0-100
    # devilScore - devil saved score, int 0-100
    # myTurn - Boolean value, True = player turn
    # myPts - human saved score + points from that round, int 0-100
    # devilPts - devil saved score + points for that round, int 0-100
    # pts - int value, used to print the scoreboard in increments of 5
    # start - int value, prevents a die value from being printed before game starts

# print top of board
    print("\t\t\tDevil's Dice")
    if (myTurn):
        print("\t ***you***\t\t\t   devil")                         # shows who's turn it is
    else:
        print("\t   you   \t\t    ***devil***")
    print(" turn  \t     score \t turn   \t score")

# prints number part of board
    while(pts >= 0):
        if (myPts <= (pts + 4) and (myPts >= pts)):                  # checks if myPts markers are needed
            if (myPts == 100):
                print(str(myPts) + "=> ", end=" ")
            elif ((myPts <= (0 + 4))):
                print("  " + str(myPts) + "=> ", end=" ")
            elif ((myPts <= (5 + 4)) and (myPts >= 5)):
                print("  " + str(myPts) + "=> ", end=" ")
            else:
                print(" " + str(myPts) + "=> ", end=" ")
        else:
            print("\t  ", end=" ")                                 # if no point marker needed, leaves blank

        if (pts == 70):                                              # formatting for lines with the die display
            print(str(pts), end=" ")
            if (myScore <= (pts + 4) and (myScore >= pts)):
                print(" <= " + str(myScore) + " die ", end=" ")
                if (devilPts <= (pts +4) and (devilPts >= pts)):            # checks if devilPts markers needed
                    print(str(devilPts) + " => " + str(pts), end=" ")
                    if (devilScore <= (pts + 4) and (devilScore >= pts)):   #checks if devilScore marker is needed
                        print(" <= " + str(devilScore))
                    else:
                        print("\t\t\t\n")
                else:
                    if (devilScore <= (pts + 4) and (devilScore >= pts)):   #checks if devilScore marker is needed
                        print(" <= " + str(devilScore))
                    else:
                        print("\t\t" + str(pts) + "\t")
            else:
                print("\t\t  die", end=" ")
                if (devilPts <= (pts + 4) and (devilPts >= pts)):
                    print(str(devilPts) + " => " + str(pts), end=" ")
                    if (devilScore <= (pts + 4) and (devilScore >= pts)):
                        print(" <= " + str(devilScore))
                    else:
                        print("\t\t\t")
                else:
                    print("\t\t" + str(pts) + "\t")
        elif (pts == 65):                                                       #formatting for line with dice result
            print(str(pts), end = " ")
            if (start == 0):
                print("\t\t  \t\t\t" + str(pts) + "\t")
            else:
                if (myScore <= (pts + 4) and (myScore >= pts)):
                    print(" <= " + str(myScore) + "  " + str(die) + "  ", end=" ")
                    if (devilPts <= (pts + 4) and (devilPts >= pts)):
                        print(str(devilPts) + " => " + str(pts), end=" ")
                        if (devilScore <= (pts + 4) and (devilScore >= pts)):
                            print(" <= " + str(devilScore))
                        else:
                            print("\t")
                    else:
                        print("\t\t" + str(pts), end=" ")
                        if (devilScore <= (pts + 4) and (devilScore >= pts)):
                            print(" <= " + str(devilScore))
                        else:
                            print("\t")
                else:
                    print("\t\t   " + str(die), end=" ")
                    if (devilPts <= (pts + 4) and (devilPts >= pts)):
                        print(" " + str(devilPts) + " => " + str(pts), end=" ")
                        if (devilScore <= (pts + 4) and (devilScore >= pts)):
                            print(" <= " + str(devilScore))
                        else:
                            print("\t")
                    else:
                        print("\t\t" + str(pts), end=" ")
                        if (devilScore <= (pts + 4) and (devilScore >= pts)):
                            print(" <= " + str(devilScore))
                        else:
                            print("\t")
        elif (pts == 5):                                             # formatting for single digit point values
            print(str(pts), end="  ")
            if (myScore <= (pts + 4) and (myScore >= pts)):
                print(" <= " + str(myScore) + "\t", end=" ")
                if (devilPts <= (pts +4) and (devilPts >= pts)):
                    print(str(devilPts) + " => " + str(pts))
                else:
                    print("\t\t" + str(pts) + "\t")
            else:
                print("\t\t\t", end=" ")
                if (devilPts <= (pts +4) and (devilPts >= pts)):
                    print("  " + str(devilPts) + " => " + str(pts))
                else:
                    print("\t\t" + str(pts))
        elif (pts == 100):                                                          # formatting for three digit number
            print(str(pts), end=" ")
            if (myScore <= (pts + 4) and (myScore >= pts)):
                print(" <= " + str(myScore) + "  ", end=" ")
                if (devilPts <= (pts + 4) and (devilPts >= pts)):
                    print(str(devilPts) + " => " + str(pts), end=" ")
                    if (devilScore <= (pts + 4) and (devilScore >= pts)):
                        print(" <= " + str(devilScore))
                else:
                    print("\t\t" + str(pts) + "\t")
            else:
                print("\t\t   ", end=" ")
                if (devilPts <= (pts + 4) and (devilPts >= pts)):
                    print(" " + str(devilPts) + " => " + str(pts), end=" ")
                    if (devilScore <= (pts + 4) and (devilScore >= pts)):
                        print(" <= " + str(devilScore))
                    else:
                        print("\t")
                else:
                    print("\t\t" + str(pts) + "\t")
        else:                                                        # default formatting
            print(str(pts), end= " ")
            if (myScore <= (pts + 4) and (myScore >= pts)):
                print(" <= " + str(myScore), end=" ")
                if (pts == 0):
                    if (devilPts <= (pts +4) and (devilPts >= pts)):
                        print("\t\t\t" + str(devilPts) + "=> " + str(pts), end=" ")
                        if (devilScore <= (pts + 4) and (devilScore >= pts)):
                            print(" <= " + str(devilScore))
                        else:
                            print("\t")
                    else:
                        print("\t\t\t\t" + str(pts), end=" ")
                        if (devilScore <= (pts + 4) and (devilScore >= pts)):
                            print(" <= " + str(devilScore))
                        else:
                            print("\t")
                else:
                    if (devilPts <= (pts +4) and (devilPts >= pts)):
                        print("\t  " + str(devilPts) + "=> " + str(pts), end=" ")
                        if (devilScore <= (pts + 4) and (devilScore >= pts)):
                            print(" <= " + str(devilScore))
                        else:
                            print("\t")
                    else:
                        print("\t\t\t" + str(pts), end=" ")
                        if (devilScore <= (pts + 4) and (devilScore >= pts)):
                            print(" <= " + str(devilScore))
                        else:
                            print("\t")
            else:
                print("\t\t\t", end=" ")
                if(pts == 0):
                    print(" ",end=" ")
                if (devilPts <= (pts +4) and (devilPts >= pts)):
                    print(" " + str(devilPts) + " => " + str(pts), end=" ")
                    if (devilScore <= (pts + 4) and (devilScore >= pts)):
                        print(" <= " + str(devilScore))
                    else:
                        print("\t")
                else:
                    print("\t\t" + str(pts), end=" ")
                    if (devilScore <= (pts + 4) and (devilScore >= pts)):
                        print(" <= " + str(devilScore))
                    else:
                        print("\t")

        pts -= 5                                                                        # point board decreases in increments of 5
    print("\n")


#print blank board, both pts at 0, then start loop
printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start)
start = 1
while (not done):                                                                    # main game loop
    while (myTurn):
        if (myPts >= 100):                                                           # did you win?
            print("You win!")
            done = True
            break
        i = input("[r]oll or [p]ass: ")                                               # choose to roll or pass
        if (i == "r"):                                                                # roll
            print("You roll\n")
            die = random.randint(1, 6)
            myPts += die
            if (die == 1):
                print("You rolled a 1, Devil's turn.\n")
                time.sleep(2)
                myPts = myScore
                printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start)
                myTurn = False
            printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start)
        elif (i == "p"):                                                                    # pass
            print("You pass\n")
            time.sleep(2)
            myScore = myPts
            printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start)
            myTurn = False
        elif (i == "quit"):                                                                 # quit
            print("Devil wins!")
            done = True
        else:                                                                               # other input
            print("huh?\n")

    while (not myTurn):                                                                     # devils turn
        if (devilPts >= 100):
            print("Devil wins!")
            done = True
            break
        if (devilScore >= myScore):
            if (devilPts < (myScore + 21)):
                print("The Devil rolls\n")
                time.sleep(2)
                die = random.randint(1, 6)
                devilPts += die
                if (die == 1):
                    print("The Devil rolled a 1, your turn.\n")
                    time.sleep(1)
                    devilPts = devilScore
                    myTurn = True
                printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start)
            elif (devilPts >= (myScore + 21)):
                print("The Devil passes\n")
                devilScore = devilPts
                printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start)
                myTurn = True
        elif (devilScore < myScore):
            if (devilPts < (devilScore + 30)):
                print("The Devil rolls\n")
                time.sleep(2)
                die = random.randint(1, 6)
                devilPts += die
                if (die == 1):
                    print("The Devil rolled a 1, your turn.\n")
                    devilPts = devilScore
                    printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start)
                    myTurn = True
                printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start)
            elif (devilPts >= (devilScore + 30)):
                print("The Devil passes\n")
                devilScore = devilPts
                printBoard(die, myScore, devilScore, myTurn, myPts, devilPts, pts, start)
                myTurn = True
