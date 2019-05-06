import random

#create a list of possible words for the game
wordlist = ["frazzled", "grogginess", "crypt", "ostracize", "oxygen", \
            "rhythmic", "pajama", "jinx", "yacht", "banjo", "awkward", \
            "zigzag", "twelfth", "unzip", "mystify", "jukebox"]

return random.choice(wordlist).lower()
# #randomize the list
# random.shuffle(wordlist)

# #select the first word from the list and create a list of that item
# #word = ['p','a','j','a','m','a']
# word = list(wordlist[0])

#print word
word = get_word()
#empty list called display that will show user spaces of selected word
display = []

#empty list contains used letters
used = []

#adds the word to display
#display = ['p','a','j','a','m','a']
display.extend(word)

#adds guessed letter to used list
used.extend(display)

#iterate through display and replace it with '__'
#display = ['__', '__', '__', '__','__','__','__']
for i in range(len(display)):
    display[i] = '_'

#'prettify' what the user sees
#removes spaces from display by converting list into string
#__ __ __ __ __ __
print (' '.join(display))
print ()

def main():
    #create counter that stops when all letters have been guessed
    counter = 0 

    #limit the number of incorrect guesses allowed
    incorrect = 5

    #keep asking user until all guesses have been used
    while counter < len(word) and incorrect > 0:
        guess = input("Please select a letter: ")
        guess = guess.lower()
        #shows correct guesses taken
        print ("Number of correct guesses: {}".format(counter))

        #iterates through letter in word
        for i in range(len(word)):
            #if letter guessed matches letter in word
            if word[i] == guess and guess in used:
                #display matched letter in its corresponding space
                display[i] = guess
                #increment counter
                counter = counter + 1

                #print item uses 
                used.remove(guess)

        #wrong guess
        if guess not in display:
            incorrect = incorrect - 1
            print ("Sorry, that's incorrect. You have", incorrect, "chances remaining.")

        #prints string with matched letters
        print (' '.join(display))
        print ()

    if counter == len(word):
        print ("Great job! You found the word.")
    else:
        print ("Game over. You ran out of attempts.")
main()


