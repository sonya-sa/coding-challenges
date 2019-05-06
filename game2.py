#hangman game
import random

#create a function that randomly selects a word
def get_word():
    wordlist = ['unzip']
    return random.choice(wordlist).lower()

#create function that checks word and guess
#function has 3 paramaters: word selected, guess letter, list of guesses taken
def check(word, guesses, guess):
    status = ''
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '-'
        if letter == guess:
            matches += 1
    if matches > 1:
        print('Yes! The word contains', matches, '"' +guess + "'" + 's')
    elif matches == 1:
        print ('Yes! The word contains the letter: ' + guess + "'")
    else:
        print ('Sorry. The word does not contain the letter "' + guess + '".')

    return status

#main function that runs game
def main():
    #call get_word function and assign to word variable
    word = get_word()
    #print(word)
    guesses = []
    guessed = False

    while not guessed:
        text = 'Please enter one letter or a {}-letter word: '.format(len(word))
        guess = input(text).lower()
        if guess in guesses:
            print('You already guessed:' + guess + ". Try again.")
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print ('Sorry! That is incorrect.')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses,guess)
            if result == word:
                guessed = True
            else:
                print(result)
        else:
            print('Invalid entry.')

    print ('Yes, the word is', word + '. It took you', len(guesses), 'tries.')

main()