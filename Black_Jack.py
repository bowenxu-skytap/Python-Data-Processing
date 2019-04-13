#!/usr/bin/env python
import random

# Hearts, Diamonds,Clubs,Spades
suits = (u"\u2660", u"\u2665", u"\u2666", u"\u2663")

# Possible card ranks
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Point values dict (Note: Aces can also be 11, check self.ace for details)
card_val = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
            'K': 10}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self):
        print (self.suit + self.rank)


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        deck_show = ""
        for card in self.deck:
            deck_show += card.__str__() + " "

        return deck_show


class Player:
    def __init__(self, total=0):
        self.total = total
        self.cards = []
        self.value = 0
        self.bet = 0

    def make_bet(self):
        chance = True
        bet_tmp = 0
        while self.bet == 0 or chance:
            try:
                bet_tmp = int(raw_input("What amount of chips would you like to bet? (Enter whole integer please): "))
            except ValueError:
                print("Sorry, the amount you entered is not allowed. ")
                continue
            if 0 <= bet_tmp <= self.total - self.bet:
                self.bet += bet_tmp
                chance = False
            else:
                print "Invalid bet, you only have", self.total - self.bet, "remaining"
        return bet_tmp

    def __str__(self):
        player_show = ""
        for card in self.cards:
            player_show += card.__str__() + " "

        return player_show

    def card_add(self, card):
        self.cards.append(card)
        self.value += card_val[card.rank]
        if self.value > 21 and card.rank == 'A':
            self.value -= 10

    def draw(self, hidden):
        if hidden:
            starting_card = 1
            print Card('X', 'X')
        else:
            starting_card = 0
        for i in range(starting_card, len(self.cards)):
            self.cards[i].draw()


def deal_cards(deck, player, dealer):
    print "Player get total", player.total, "money!!"
    chip_pool = 0
    playing = True
    chip_pool += player.make_bet() * 2
    print "Chip pool now has", chip_pool, "dollars"
    player.card_add(deck.deal())
    player.card_add(deck.deal())
    dealer.card_add(deck.deal())
    dealer.card_add(deck.deal())
    while playing:
        print '***************'
        # Display Player Hand
        print('Player Hand is: ')
        player.draw(False)
        print 'Player Hand value is:', player.value, '\n'
        # Display Dealer Hand
        print('Dealer Hand is: \n'),
        dealer.draw(hidden=True)
        print ""
        action = raw_input("Hit or Stand? Press either h or s: ")
        if action == 'h':
            chip_pool, playing = hit(chip_pool, dealer, deck, player, playing)
        elif action == 's':
            playing = stand(chip_pool, dealer, deck, player, playing)
    again = raw_input("Would you like to play again? Press either y or n: ")
    if again.startswith('y'):
        reset_player(player)
        return True
    else:
        return False


def hit(chip_pool, dealer, deck, player, playing):
    chip_pool += player.make_bet() * 2
    print "Chip pool now has", chip_pool, "dollars"
    player.card_add(deck.deal())
    if player.value > 21:
        print 'Busted! Player Hand is: '
        player.draw(False)
        print 'Player Hand value is:', player.value, '\n'
        player.total -= chip_pool
        playing = False
        print "Player now has total", player.total, "money!!"
    else:
        dealer.card_add(deck.deal())
    return chip_pool, playing


def stand(chip_pool, dealer, deck, player, playing):
    while dealer.value < 17:
        dealer.card_add(deck.deal())
    print '***************'
    # Display Player Hand
    print('Player Hand is: ')
    player.draw(False)
    print 'Player Hand value is:', player.value, '\n'
    # Display Dealer Hand
    print('Dealer Hand is: \n'),
    dealer.draw(False)
    print 'Dealer Hand value is:', dealer.value, '\n'
    if dealer.value > 21:
        print"Dealer busts! You win!"
        player.total += chip_pool
    elif player.value > dealer.value:
        print"You beat the dealer, you win!"
        player.total += chip_pool
    elif player.value < dealer.value:
        print "Dealer Wins!"
        player.total -= chip_pool
    else:
        print "Tied up, push!"
        player.total += chip_pool / 2
    playing = False
    print "Player now has total", player.total, "money!!"
    return playing


def reset_player(player):
    player.cards = []
    player.value = 0
    player.bet = 0


def intro():
    statement = "Welcome to BlackJack! Get as close to 21 as you can without going over! \n \
Dealer hits until she reaches 17. Aces count as 1 or 11. \n"
    print statement


def start_game():
    again = True
    deck = Deck()
    player = Player(100)
    while again:
        deck.shuffle()
        dealer = Player()
        intro()
        again = deal_cards(deck, player, dealer)
    print("See you next time. Bye")
    exit()


start_game()
