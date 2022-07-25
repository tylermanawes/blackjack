import random
from game_functions import play_blackjack, determine_winner, payout

class Deck:
    def __init__(self):
        self.stack = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    
    def shuffle(self):
        random.shuffle(self.stack)

    def show(self):
        print(self.stack)

    def deal(self, target):
        card = self.stack.pop()
        target.hand.append(card)

class Dealer:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def dealer_hit(self):
        if self.score < 17:
            deck.deal(self)
            print(self.hand)
        else:
            pass

    def calcuate_score(self):
        self.score = sum(self.hand)

    def dealer_playout(self):
        print("{} shows his second card.".format(self.name))
        self.calcuate_score()
        print("{} is now holding {}".format(self.name, self.score))
        if 17 <= self.score <= 21:
            print("\n{} will stay.".format(self.name))
            return 0 
        if self.score < 17:
            while True:
                print("\n{} hits.".format(dealer.name))
                self.dealer_hit()
                self.calcuate_score()
                print("\n{} is now showing {}".format(dealer.name, dealer.score))
                if 17 <= self.score <= 21:
                    print("\n{} will stay.".format(self.name))
                    return 1
                if self.score > 21:
                    print("\n{} busts!".format(self.name))
                    print("\n{} wins the hand!".format(tyler.name))
                    payout(tyler)
                    return 2

    def end_hand(self):
        while True:
            return_card = self.hand.pop()
            deck.stack.append(return_card)
            if self.hand == []:
                break





class Player(Dealer):
    def __init__(self, name):
        super().__init__(name)
        self.purse = 100
        self.bet = 0

    def place_bet(self):
        self.bet = int(input('Place your bet: '))
        if self.bet > self.purse or self.bet < 5:
            print('\nInvalid bet. Refer to the table minimum, and check your current purse amount.')
            return 0
        else:
            self.purse -= self.bet
            return 1

    def hit_or_stay(self):
        while True:
            hit_choice = int(input('1. Hit or 2. Stay? '))
            if hit_choice == 1:
                deck.deal(self)
                print(self.hand)
                self.calcuate_score()
                if self.score > 21:
                    print("\n{} busts!".format(self.name))
                    print("\n{} wins the hand.".format(dealer.name))
                    break
                print("\n{} is currently holding {}".format(tyler.name, tyler.score))
            if hit_choice == 2:
                print('\n{} stays.'.format(self.name))
                self.calcuate_score()
                print(self.hand)
                print("\n{} is currently holding {}".format(tyler.name, tyler.score))
                break

    def player_playout(self):
        self.calcuate_score()
        if self.score > 21:
            print("{} busts!".format(self.name))
        if self.score < 21:
            self.hit_or_stay()


#GAME SCRIPT BEGINS HERE

deck = Deck()
dealer = Dealer('Dealer')
tyler = Player('Tyler')
while True:
    tyler.purse = 100
    play_blackjack()
    user_choice = int(input('Choose an option: '))
    if user_choice == 1:
        while True:
            deck.shuffle()
            print('\nPlease place a bet to play.')
            if tyler.place_bet() == 0:
                continue
            deck.deal(tyler)
            deck.deal(dealer)
            deck.deal(tyler)
            deck.deal(dealer)
            print("\n{}'s hand contains a {} and a {}".format(tyler.name, tyler.hand[0], tyler.hand[1]))
            print("\n{} is showing a {}".format(dealer.name, dealer.hand[0]))
            dealer.calcuate_score()
            tyler.calcuate_score()
            print("\n{} is currently holding {}".format(tyler.name, tyler.score))
            if dealer.score == 21:
                determine_winner(tyler, dealer)
            if dealer.score != 21:
                tyler.hit_or_stay()
                dealer.dealer_playout()
                determine_winner(tyler, dealer)
                dealer.end_hand()
                tyler.end_hand()
                print("\n{}'s purse is now {}".format(tyler.name, tyler.purse))
            if tyler.purse < 5:
                print("\nYou are all out of money...Better luck next time!")
                break
    elif user_choice == 2:
        print('\nGoodbye!')
        break
    else:
        print('\nEnter the corresponding number for the choice you would like to choose.')