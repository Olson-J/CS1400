import random
import time

#Julie Olson - MW2 XL
# write all your code below this line
class Card:
    def __init__(self, num=1, suit="S"):
        self.__num = num
        self.__suit = suit
    # each card has a number value between 1 and 13 (inclusive)
    # each card has a suit: "C", "D", "H", and "S"

    def __lt__(self, other):
        if self.__suit != other.__suit:
            return self.__suit < other.__suit
        return self.__num < other.__num

    # define which cards are less than others for sorting
    # first decide by card suit, in alphabetical order
    # then decide by card number

    def print(self):
        if self.__suit == "C":
            if self.__num == 10:
                print(str(self.__num) + '\u2663', end=" ")
            elif self.__num == 1:
                print(" A" + '\u2663', end=" ")
            elif self.__num == 11:
                print(" J" + '\u2663', end=" ")
            elif self.__num == 12:
                print(" Q" + '\u2663', end=" ")
            elif self.__num == 13:
                print(" K" + '\u2663', end=" ")
            else:
                print(" " + str(self.__num) + '\u2663', end=" ")
        elif self.__suit == "D":
            if self.__num == 10:
                print(str(self.__num) + '\u2662', end=" ")
            elif self.__num == 1:
                print(" A" + '\u2662', end=" ")
            elif self.__num == 11:
                print(" J" + '\u2662', end=" ")
            elif self.__num == 12:
                print(" Q" + '\u2662', end=" ")
            elif self.__num == 13:
                print(" K" + '\u2662', end=" ")
            else:
                print(" " + str(self.__num) + '\u2662', end=" ")
        elif self.__suit == "H":
            if self.__num == 10:
                print(str(self.__num) + '\u2661', end=" ")
            elif self.__num == 1:
                print(" A" + '\u2661', end=" ")
            elif self.__num == 11:
                print(" J" + '\u2661', end=" ")
            elif self.__num == 12:
                print(" Q" + '\u2661', end=" ")
            elif self.__num == 13:
                print(" K" + '\u2661', end=" ")
            else:
                print(" " + str(self.__num) + '\u2661', end=" ")
        elif self.__suit == "S":
            if self.__num == 10:
                print(str(self.__num) + '\u2660', end=" ")
            elif self.__num == 1:
                print(" A" + '\u2660', end=" ")
            elif self.__num == 11:
                print(" J" + '\u2660', end=" ")
            elif self.__num == 12:
                print(" Q" + '\u2660', end=" ")
            elif self.__num == 13:
                print(" K" + '\u2660', end=" ")
            else:
                print(" " + str(self.__num) + '\u2660', end=" ")

    # print out a card (see example output for details)

    def blackJackValue(self):
        if self.__num == 1:
            return 11
        elif self.__num >= 10:
            return 10
        else:
            return self.__num

    # return the value of a card.
    # face cards are worth 10
    # aces are worth 11 always here


class Deck:
    def __init__(self):
        # create a deck of 52 cards in order
        self.deck = []
        for i in range(1, 14):
            self.deck.append(Card(i, "S"))
            self.deck.append(Card(i, "C"))
            self.deck.append(Card(i, "H"))
            self.deck.append(Card(i, "D"))
        self.deck.sort()


    def print(self):
        for c in self.deck:
            c.print()

            print()

    # print all the cards in the deck, one per line

    def shuffle(self):
        random.shuffle(self.deck)

    # randomly shuffle all the cards in the deck

    def arrange(self):
        self.deck.sort()

    # put all the cards currently in the deck back in order

    def restore(self):
        self.deck = []
        suits = ['C', 'D', 'H', 'S']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for i in suits:
            for j in values:
                self.deck.append(Card(j, i))

    # restore all the missing cards from the deck and arrange them

    def deal(self):
        c = self.deck.pop(len(self.deck)-1)
        return c

    # remove a card from the top of the deck and return it to the client

    def numCards(self):
        return len(self.deck)
    # return the number of cards currently in the deck


class Hand:
    def __init__(self):
        self.hand = []

    # create an empty list of cards

    def addCard(self, card):
        self.hand.append(card)
    # add a card to the hand (for example, from the deck)

    def numCards(self):
        return len(self.hand)

    # return the number of cards currently in the hand

    def print(self):
        for c in self.hand:
            c.print()

    # print the cards currently in the hand, without newlines
    # see example output for details

    def printBlackJackDealer(self):
        print(" ??", end=" ")
        for i in range(1, (len(self.hand))):
            self.hand[i].print()

    # print the cards currently in the hand, without newlines
    # replace the first card with "??" to hide it
    # see example output for details

    def blackJackValue(self):
        total = 0
        aces = 0
        for i in range(0, (len(self.hand))):
            total += self.hand[i].blackJackValue()
            if self.hand[i].blackJackValue() == 11:
                aces += 1

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    # return the blackjack value of this hand
    # aces are worth 11 unless that causes a bust.
    # then the minimum number of aces are counted as 1s
    # so that no bust occurs. ("bust" == any value over 21)


# write all your code above this line


class BlackJackGame:
    def __init__(self):
        self.__d = Deck()
        self.__d.shuffle()

    def displayLine(self, who, hand):
        # print a "hand" line of the output
        print(who + ": ", end="")
        print(" (" + str(hand.blackJackValue()) + ")\t", end="")
        hand.print()
        if hand.numCards() <= 5: print("\t", end="")
        if hand.numCards() <= 3: print("\t", end="")

    def pickWinner(self, n, dn, b, db, pf, df):
        # print out the winner of the hand
        print()
        if n and not dn:
            print("\t\tyou win!")
        elif n and dn:
            print("\t\t(push)")
        elif not n and dn:
            print("\t\tdealer wins.")
        elif b and not db:
            print("\t\tdealer wins.")
        elif not b and db:
            print("\t\tyou win!")
        elif pf == df:
            print("\t\t(push)")
        elif pf > df:
            print("\t\tyou win!")
        else:
            print("\t\tdealer wins.")
        print()

    def play(self):
        print()
        print("        Welcome to Simple BlackJack")
        print()
        # the main event loop
        while True:
            # dealer reshuffles cards when 75% dealt
            if self.__d.numCards() < 14:
                print("\t\t\t\t\tDealer shuffles the deck")
                self.__d.restore()
                self.__d.shuffle()
            # dealer and player each have a hand
            dealer = Hand()
            player = Hand()
            # flags used to determine the eventual winner
            natural = False
            dnatural = False
            busted = False
            dbusted = False
            playerfinal = 0
            dealerfinal = 0

            # dealer gets a hand
            dealer.addCard(self.__d.deal())
            dealer.addCard(self.__d.deal())

            # dealer hand displayed with one card hidden
            print("dealer" + ": ", end="")
            print(" (??)\t", end="")
            dealer.printBlackJackDealer()
            print()

            # player gets a hand
            player.addCard(self.__d.deal())
            player.addCard(self.__d.deal())

            # check for player natural
            if player.blackJackValue() == 21:
                self.displayLine("player", player)
                print("natural blackjack!")
                natural = True

            # player get more cards if desired
            while player.blackJackValue() < 21:
                self.displayLine("player", player)
                response = input("hit? [y/n] ")
                if response == "n": break
                player.addCard(self.__d.deal())

            # find final player status for hand
            self.displayLine("player", player)
            playerfinal = player.blackJackValue()
            if playerfinal == 21 and not natural:
                print("blackjack!")
            elif playerfinal > 21:
                print("you busted.")
                busted = True
            else:
                print("you hold.")
            time.sleep(1)

            # now it is the dealers turn
            if dealer.blackJackValue() == 21:
                self.displayLine("dealer", dealer)
                print("dealer blackjack!")
                dnatural = True
            # if player busted, dealer does nothing
            if busted:
                self.displayLine("dealer", dealer)
                print()
            # dealer gets to add cards if no naturals
            if not natural and not busted:
                while dealer.blackJackValue() <= 15 and not busted:
                    self.displayLine("dealer", dealer)
                    print("dealer hits.")
                    time.sleep(1)

                    dealer.addCard(self.__d.deal())

                # find final dealer status for hand
                self.displayLine("dealer", dealer)
                dealerfinal = dealer.blackJackValue()
                if dealerfinal == 21 and not dnatural:
                    print("dealer blackjack!")
                elif dealerfinal > 21:
                    print("dealer busted.")
                    dbusted = True
                else:
                    print("dealer holds.")
            time.sleep(1)

            # find the winner for this hand
            self.pickWinner(natural, dnatural, busted, dbusted, playerfinal, dealerfinal)
            response = input("\t\t\t\t\tplay again? [y/n] ")
            if response == "n": break
        print("\t\t\t\t\tso long!")
        print()


def cardTest():
    print()
    print("Card Test")
    print()
    c1 = Card()
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    c4 = Card(3, "D")
    c1.print()
    c2.print()
    c3.print()
    c4.print()
    print()
    print(format(c1.blackJackValue(), "3.0f"), end=" ")
    print(format(c2.blackJackValue(), "3.0f"), end=" ")
    print(format(c3.blackJackValue(), "3.0f"), end=" ")
    print(format(c4.blackJackValue(), "3.0f"), end=" ")
    print()
    print()
    c0 = Card(13, "C")
    c1 = Card(1, "D")
    c2 = Card(2, "D")
    c3 = Card(3, "D")
    c4 = Card(10, "D")
    c5 = Card(11, "D")
    c6 = Card(12, "D")
    c7 = Card(13, "D")
    c8 = Card(1, "H")
    c9 = Card(1, "S")
    c0.print()
    c1.print()
    c2.print()
    c3.print()
    c4.print()
    c5.print()
    c6.print()
    c7.print()
    c8.print()
    c9.print()
    print()
    print(c0 < c1)
    print(c1 < c2)
    print(c2 < c3)
    print(c3 < c4)
    print(c4 < c5)
    print(c5 < c6)
    print(c6 < c7)
    print(c7 < c8)
    print(c8 < c9)
    print(c9 < c0)


def deckTest():
    print()
    print("Deck Test")
    print()
    d = Deck()
    d.print()
    print()
    d.shuffle()
    d.print()
    print()
    d.arrange()
    d.print()
    print()
    c0 = d.deal()
    c1 = d.deal()
    c0.print()
    c1.print()
    print()
    print()
    d.print()
    print()
    print(d.numCards())
    d.restore()
    print(d.numCards())
    print()
    d.print()
    print()


def handTest():
    print()
    print("Hand Test")
    print()
    c1 = Card(1, "S")
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    h = Hand()
    h.addCard(c1)
    h.addCard(c2)
    h.print()
    print()
    print(h.numCards())
    h.addCard(c3)
    h.print()
    print()
    print(h.numCards())
    print()
    h2 = Hand()
    h2.addCard(c1)
    h2.addCard(c2)
    h2.printBlackJackDealer()
    print()
    h2.print()
    print("=", h2.blackJackValue())
    print()
    h2.addCard(c3)
    h2.print()
    print("=", h2.blackJackValue())
    print()


def test():
    cardTest()
    deckTest()
    handTest()


def main():
    game = BlackJackGame()
    game.play()
    #test()


main()