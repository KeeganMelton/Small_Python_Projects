import random

# adds deck of cards to a list
deck = ["A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥",
        "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
        "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣",
        "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠"]


# point system for cards in hand
def score(cards):
    score = 0
    for card in cards:
        if card.__contains__("2"):
            score += 2
        if card.__contains__("3"):
            score += 3
        if card.__contains__("4"):
            score += 4
        if card.__contains__("5"):
            score += 5
        if card.__contains__("6"):
            score += 6
        if card.__contains__("7"):
            score += 7
        if card.__contains__("8"):
            score += 8
        if card.__contains__("9"):
            score += 9
        if card.__contains__("10"):
            score += 10
        if card.__contains__("J"):
            score += 10
        if card.__contains__("Q"):
            score += 10
        if card.__contains__("K"):
            score += 10
        if card.__contains__("A"):
            if score + 11 > 21:
                score += 1
            if score + 11 <= 21:
                score += 11
    return score


# adds cards to the player and dealers hand
def draw_card(player_hand, player_hand_total, show_player_hand,
              dealer_hand, dealer_hand_total, show_dealer_hand,
              cards_dealt):
    print("\nYour Hand:")
    player_hand.append(deck[cards_dealt])
    player_hand_total = score(player_hand)
    cards_dealt += 1
    card = player_hand[-1] + " "
    show_player_hand += card
    print(f"{show_player_hand}\n")

    # adds a card to the dealers had if score is 17 or lower
    if dealer_hand_total <= 17:
        dealer_hand.append(deck[cards_dealt])
        dealer_hand_total = score(dealer_hand)
        cards_dealt += 1
        card = "[] "
        show_dealer_hand += card
    print("Dealer's Hand")
    print(f"{show_dealer_hand} \n")

    return player_hand_total, player_hand, show_player_hand, \
        dealer_hand_total, dealer_hand, show_dealer_hand, cards_dealt


# plays blackjack
# contains exit conditions based on the score of either hand
# asks user for another game once complete

def play_blackjack():
    random.shuffle(deck)
    player_hand = []
    show_player_hand = ""

    dealer_hand = []
    show_dealer_hand = ""

    cards_dealt = 0

    player_hand_total = 0
    dealer_hand_total = 0
    while cards_dealt < 4:
        if cards_dealt < 2:
            player_hand.append(deck[cards_dealt])
            cards_dealt += 1
        else:
            dealer_hand.append(deck[cards_dealt])
            cards_dealt += 1
    print("\nYour Hand:")
    for i in range(0, len(player_hand)):
        card = player_hand[i] + " "
        show_player_hand += card
        player_hand_total = score(player_hand)
    print(f"{show_player_hand}  \n")

    print("Dealer's Hand:")
    for i in range(0, len(dealer_hand)):
        if i == 1:
            card = "[] "
        else:
            card = dealer_hand[i] + " "
        show_dealer_hand += card
        dealer_hand_total = score(dealer_hand)
    print(f"{show_dealer_hand} \n")

    if player_hand_total == 21 and dealer_hand_total != 21:
        print("You Win!")
    if player_hand_total == 21 and dealer_hand_total == 21:
        print("It's a Draw!")

    while player_hand_total < 21:
        if input(f"\nYour score is: {player_hand_total} do you want another card? (y\\n)?: ").lower() == 'y':
            player_hand_total, player_hand, show_player_hand, dealer_hand_total, dealer_hand, show_dealer_hand, \
                cards_dealt = draw_card(player_hand, player_hand_total, show_player_hand,
                                        dealer_hand, dealer_hand_total, show_dealer_hand,
                                        cards_dealt)

            if player_hand_total > 21:
                print(f"Your Score is {player_hand_total}\n")
                print("You Lose!")
                if input("Do you want to play another game of Blackjack? (y\\n): ").lower() == 'y':
                    play_blackjack()
                else:
                    print("Thanks for Playing")
                    break

            if player_hand_total == dealer_hand_total and player_hand_total == 21:
                show_dealer_hand = ""
                for i in range(0, len(dealer_hand)):
                    card = dealer_hand[i] + " "
                    show_dealer_hand += card
                    dealer_hand_total = score(dealer_hand)
                print("It's a Draw!")
                if input("Do you want to play another game of Blackjack? (y\\n): ").lower() == 'y':
                    play_blackjack()
                else:
                    print("Thanks for Playing")
                    break

        else:
            show_dealer_hand = ""
            for i in range(0, len(dealer_hand)):
                card = dealer_hand[i] + " "
                show_dealer_hand += card
                dealer_hand_total = score(dealer_hand)

            print(show_player_hand)
            print(f"Your Score is {player_hand_total}\n")
            print(show_dealer_hand)
            print(f"The Dealer's Score is {dealer_hand_total}")

            if dealer_hand_total < player_hand_total <= 21 or player_hand_total <= 21 < dealer_hand_total:
                print("\nYou Win!")

            if player_hand_total < dealer_hand_total <= 21 or dealer_hand_total <= 21 < player_hand_total:
                print("\nYou Lose!")

            if player_hand_total > 21:
                print("\nYou Lose!")

            if player_hand_total == dealer_hand_total:
                print("\nIt's a Draw!")

            if player_hand_total <= 21 < dealer_hand_total:
                show_dealer_hand = ""
                for i in range(0, len(dealer_hand)):
                    card = dealer_hand[i] + " "
                    show_dealer_hand += card
                    dealer_hand_total = score(dealer_hand)
                print("\nThe Dealer went over 21")
                print(show_dealer_hand)
                if input("\nDo you want to play another game of Blackjack? (y\\n): ").lower() == 'y':
                    play_blackjack()
                else:
                    print("Thanks for Playing")
                    break

            if input("Do you want to play another game of Blackjack? (y\\n): ").lower() == 'y':
                play_blackjack()
            else:
                print("Thanks for Playing")
                break
    if player_hand_total == 21 and dealer_hand_total != 21:
        show_dealer_hand = ""
        for i in range(0, len(dealer_hand)):
            card = dealer_hand[i] + " "
            show_dealer_hand += card
            dealer_hand_total = score(dealer_hand)
        print(show_player_hand)
        print(f"Your Score is {player_hand_total}\n")
        print(show_dealer_hand)
        print(f"The Dealer's Score is {dealer_hand_total}")
        print("You Win!")
        if input("Do you want to play another game of Blackjack? (y\\n): ").lower() == 'y':
            play_blackjack()
        else:
            print("Thanks for Playing")


if input("Do you want to play a game of Blackjack? (y\\n): ").lower() == 'y':
    play_blackjack()
else:
    print("Another time then")
