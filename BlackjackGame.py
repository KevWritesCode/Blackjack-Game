import random

def draw_card():
    return random.randint(1, 11)

def total_points(hand):
    points = sum(hand)
    for i in hand:
        if i == 1 and points <= 11:
            points += 10
    return points

def play_again():
    answer = input("Do you want to play again? (yes or no) ")
    return answer.lower() == "yes"

def play_blackjack():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    print("Dealer shows one card:", dealer_hand[0])
    print("Your hand is:", player_hand, "=", total_points(player_hand))

    while total_points(player_hand) < 21:
        action = input("Do you want to hit or stand? ")
        if action.lower() == "hit":
            player_hand.append(draw_card())
            print("Your hand is:", player_hand, "=", total_points(player_hand))
        elif action.lower() == "stand":
            break
        else:
            print("Invalid input. Please enter hit or stand.")
            continue

    if total_points(player_hand) > 21:
        print("You bust.")
    else:
        while total_points(dealer_hand) < 17:
            dealer_hand.append(draw_card())

        if total_points(dealer_hand) > 21:
            print("Dealer busts.")
        else:
            if total_points(player_hand) > total_points(dealer_hand):
                print("You win.")
            elif total_points(player_hand) < total_points(dealer_hand):
                print("Dealer wins.")
            else:
                print("It's a tie.")

    if play_again():
        play_blackjack()

play_blackjack()
