# program: dog_brain
# purpose: explore how a dog's brain works through a series of yes or no questions
# pseudocode/layout:
# begin
#   ask "is it an object"
#       |(Y) ask "can you eat it
#       |    |(Y) eat it
#       |    |    ask "was it good"
#       |    |        (Y) wag your tail
#       |    |        (N) puke it out
#       |    |            re-eat it
#       |    |(N) ask "is it a tennis ball"
#       |         (Y) pick it up
#       |             return to owner
#       |         (N) bark at it
#       |(N) ask "is it a sound"
#             (Y) bark at it
#             (N) ignore it
# end
####################################################

def dog_brain():
    answer = input("Is it an object? [y/n] ")           #ask for input
    if answer == "y":                                   #yes it's an object
        answer = input("Can you eat it? [y/n] ")
        if answer == "y":                               #yes it's edible
            print("Eat it")
            answer = input("Was it good? [y/n] ")
            if answer == "y":                           #yes it was good
                print("Wag your tail")

            else:                                       #no it was bad
                print("Puke it out")
                print("Re-eat it")

        else:                                           #no it's not edible
            answer = input("Is it a tennis ball? [y/n] ")
            if answer == "y":                           #yes it's a ball
                print("Pick it up")
                print("Return to owner")

            else:                                       #no it's not a ball
                print("Bark at it")

    else:                                               #no it's not an object
        answer = input("Is it a sound? [y/n] ")
        if answer == "y":                               #yes it's a sound
            print("Bark at it")

        else:                                           #no it's not a sound
            print("Ignore it")

    return""                                            #finished


print(dog_brain())                                      #actually run it
