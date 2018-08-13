#palindrome 

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

