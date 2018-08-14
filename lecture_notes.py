#palindrome 

import random

for word in ["racecar", "radar", "house"]:
    palindrome = True
    start = 0
    end = len(word) - 1

    while start < end:
        if word[start] != word[end]:
            print ("Not a palindrome: {}".format(word))
            palindrome = False
            break
        start = start + 1
        end = end - 1

    if palindrome:
        print("palindrome: {}".format(word))

def play_game():

    secret_number = random.randint(1, 100)
    guess = None
    too_low = 0
    too_high = 101
    
    print("Shh... the secret number is {}".format(secret_number))
    
    while secret_number != guess:
        guess = int((too_high - too_low) / 2) + too_low
        print("Too High = {}, Too Low = {}, Guess = {}".format(
            too_high, too_low, guess))
    
        if guess > secret_number:
            too_high = guess
        if guess < secret_number:
            too_low = guess

play_game()