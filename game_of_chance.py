import random
import time

money = 100
invalid_guess = "That was not a valid guess."
game_lost = "Sorry, you lost."
game_won = "Congratulations! You won $%s!"

#Write your game of chance functions here
def coin_flip(guess, bet):
    flip = random.randint(1, 2)
    if flip == 1 and (guess == "HEADS" or guess == "TAILS"):
        return game_won % bet
        money += bet
    elif guess != "HEADS" and guess != "TAILS":
        return invalid_guess
    else:
        return game_lost
        money -= bet

def cho_han(guess, bet):
    roll = random.randint(1, 6) + random.randint(1, 6)
    try:
        guess = int(guess)
    except:
        return invalid_guess
    else:
        guess = int(guess)
    time.sleep(1)
    if guess == roll:
        return game_won % bet
        money += bet
    elif guess > 12 or guess < 2:
        return invalid_guess
    else:
        return game_lost + " The roll was %s." % roll
        money -= bet

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
        return game_won % bet
        money += bet
    elif player_draw < draw_to_beat:
        return game_lost % bet
        money -= bet
    else:
        return "It's a tie!"

#Call your game of chance functions here
#print(coin_flip(input("Heads or Tails? ").upper(), str(input("And how much would you like to wager? "))))
#print(cho_han(input("What are the dice going to roll? "), str(input("And how much would you like to wager? "))))
#print(card_draw(str(input("And how much would you like to wager? "))))
