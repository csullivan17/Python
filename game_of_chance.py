import random
import time

money = 100
invalid_guess = "That was not a valid guess."
game_lost = "Sorry, you lost the game and what money ou wagered."
game_won = "Congratulations! You won $%s!"

#Games of Chance:
#Coin Flipping (Guessing either heads or tails)
def coin_flip(guess, bet):
    flip = random.randint(1, 2)
    if flip == 1 and (guess == "HEADS" or guess == "TAILS"):
        print(game_won % bet)
        money += bet
        return wallet
    elif guess != "HEADS" and guess != "TAILS":
        return invalid_guess
    else:
        print(game_lost)
        money -= bet

#Cho Han (Guessing the outcome of a 2d6 roll)
def cho_han(guess, bet):
    roll = random.randint(1, 6) + random.randint(1, 6)
    try:
        guess = int(guess)
    except:
        print(invalid_guess)
    else:
        guess = int(guess)
    time.sleep(1)
    if guess == roll:
        print(game_won % bet)
        money += bet
    elif guess > 12 or guess < 2:
        print(invalid_guess)
    else:
        print(game_lost + " The roll was %s." % roll)
        money -= bet

#Card Drawing (Hoping for a better draw than the dealer)
def card_draw(bet):
    draw_to_beat = random.randint(1, 13)
    player_draw = random.randint(1, 13)
    card_values = {1 : "ace", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9", 10 : "10", 11 : "Jack", 12 : "Queen", 13 : "King"}
    if draw_to_beat > 1:
        print("The draw to beat is %s." % card_values[draw_to_beat])
    else:
        print("Ace! The best that can happen is a tie.")
    print("You drew a %s." % card_values[player_draw])
    time.sleep(1)
    if player_draw > draw_to_beat:
        print(game_won % bet)
        money += bet
    elif player_draw < draw_to_beat:
        print(game_lost % bet)
        money -= bet
    else:
        print("It's a tie!")

#Game Hall:
#Navigating the different games
def game_hall():
    choice = ""
    while choice != "X":
        print("Welcome to Cole's Game Hall!")
        choice = input("What would you like to play?\n  [F]: Coin Flip  [H]: Cho Han  [D]: Card Draw [X]: Quit\n")
        if choice == "F":
            print("You have chosen Coin Flip!")
            coin_flip((input("Head or Tails? ")).upper(), (input("How much would you like to wager? ")))
        elif choice == "H":
            print("You have chosen Cho Han!")
            cho_han((input("What will the dice roll? ")).upper(), (input("How much would you like to wager? ")))
        elif choice == "D":
            print("You have chosen Card Draw!")
            card_draw(input("How much would you like to wager? "))
        elif choice == "X":
            return "Thanks for playing! You finished with %s." % (money)
            break


game_hall()
