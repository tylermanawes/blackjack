def play_blackjack():
    print('-----------------------------------------')
    print('-----     Welcome to BlackJack!     -----')
    print('-----------------------------------------')
    print('-----       Choose an option        -----')
    print('-----------------------------------------')
    print('1.      Play        |2.       Quit       ')
    print('-----------------------------------------')

def payout(target):
    target.purse += target.bet * 2

def push(target):
    target.purse += target.bet

def calculate_score(target):
    for cards in target.hand:
        target.score += cards

def determine_winner(player, dealer):
    if player.score > dealer.score and player.score <= 21:
        print("{} wins the hand!".format(player.name))
        payout(player)
    elif player.score == dealer.score:
        print("The hand is pushed.")
        push(player)
    elif dealer.score > player.score and dealer.score <= 21:
        print("{} wins the hand!".format(dealer.name))