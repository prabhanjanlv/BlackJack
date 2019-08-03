import itertools
import random


def getsum(cards_list):
    card_sum = 0
    numberas = 0  #Number of A's in the Throw
    for i in range(len(cards_list)):
        if cards_list[i].split(' ')[0] in ('J', 'Q', 'K'): card_sum = card_sum + 10
        elif cards_list[i].split(' ')[0] == 'A': numberas = numberas + 1
        else: card_sum = card_sum + int(cards_list[i].split(' ')[0])
    #Add either 11 or 1 for A's based on other cards
    if numberas == 1 and ((card_sum + 11) < 22): card_sum = card_sum + 11
    elif numberas == 1 and ((card_sum + 11) > 21): card_sum = card_sum + 1
    if numberas > 1:
        if(card_sum + (numberas - 1)) < 11: card_sum = card_sum + 11 + (numberas - 1)
        if(card_sum + (numberas - 1)) > 10: card_sum = card_sum + numberas
    return card_sum

List_Cards = ['A Club', 'A Spade', 'A Diamond', 'A Heart', '2 Club', '2 Spade', '2 Diamond', '2 Heart', '3 Club', '3 Spade', '3 Diamond', '3 Heart', '4 Club', '4 Spade', '4 Diamond', '4 Heart', '5 Club', '5 Spade', '5 Diamond', '5 Heart', '6 Club', '6 Spade', '6 Diamond', '6 Heart', '7 Club', '7 Spade', '7 Diamond', '7 Heart', '8 Club', '8 Spade', '8 Diamond', '8 Heart', '9 Club', '9 Spade', '9 Diamond', '9 Heart', '10 Club', '10 Spade', '10 Diamond', '10 Heart', 'J Club', 'J Spade', 'J Diamond', 'J Heart', 'Q Club', 'Q Spade', 'Q Diamond', 'Q Heart', 'K Club', 'K Spade', 'K Diamond', 'K Heart']
Complete_Deck = list(itertools.chain.from_iterable(itertools.repeat(x, 8) for x in List_Cards))
random.shuffle(Complete_Deck)

#Get the User Name
UserName = input("Enter your Name: ")
print("Hello " + UserName + "! Welcome to BlackJack.")

DealCommand = 'D'

while Complete_Deck:
    while DealCommand == 'D':
        #Instruct to Deal
        DealCommand = input("Press D to Deal or Q to Quit: ")

        if DealCommand == 'D':

            player_cards = []
            dealer_cards = []
            player_sum = 0
            dealer_sum = 0

            #Draw Random Cards
            #player_cards.append(random.choice(Complete_Deck))
            #player_cards.append(random.choice(Complete_Deck))
            #dealer_cards.append(random.choice(Complete_Deck))
            #dealer_cards.append(random.choice(Complete_Deck))
            player_cards.append(Complete_Deck.pop())
            player_cards.append(Complete_Deck.pop())
            dealer_cards.append(Complete_Deck.pop())
            dealer_cards.append(Complete_Deck.pop())

            print("Player Cards:")
            print(player_cards)
            player_sum = getsum(player_cards)
            print("Player Sum:")
            print(player_sum)
            print("Dealer Cards:")
            print(dealer_cards[0])

            hit_flag = 1
            while hit_flag == 1:
                PlayCommand = input("H - Hit, S - Stand, Q - Quit: ")

                if PlayCommand == 'H':
                    #player_cards.append(random.choice(Complete_Deck))
                    player_cards.append(Complete_Deck.pop())
                    print("Player Cards:")
                    print(player_cards)
                    player_sum = getsum(player_cards)
                    print("Player Sum:")
                    print(player_sum)
                    if player_sum > 21:
                        print("Player Busted!")
                        break
                if PlayCommand == 'S':
                    hit_flag = 0
                    dealer_sum = getsum(dealer_cards)
                    while dealer_sum < 17:
                        #dealer_cards.append(random.choice(Complete_Deck))
                        dealer_cards.append(Complete_Deck.pop())
                        dealer_sum = getsum(dealer_cards)
                    print("Dealer Cards:")
                    print(dealer_cards)
                    print("Dealer Sum:")
                    print(dealer_sum)

                    #Winner Validations
                    if dealer_sum > 21:
                        print("Player Wins!")
                        break
                    if player_sum == 21 and len(player_cards) == 2 and dealer_sum == 21 and len(dealer_cards) == 2:
                        print("Push")
                        break
                    if player_sum == 21 and len(player_cards) == 2:
                        print("Player Wins!")
                        break
                    if player_sum == 21 and dealer_sum == 21:
                        print("Push")
                        break
                    if dealer_sum < player_sum < 22:
                        print("Player Wins!")
                        break
                    if player_sum < dealer_sum < 22:
                        print("Dealer Wins!")
                        break
                    if player_sum == dealer_sum:
                        print("Push")
                        break

                if(PlayCommand == 'Q'): exit(0)

        if DealCommand == 'Q': exit(0)

print("Game Over!! Restart to play another game")


