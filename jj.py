import random
play_again = True

hangman = (
"""
 -----
|    |
|
|
|
|
|
|
|
 --------
 """,
 """
 -----
|    |
|    0
|
|
|
|
|
|
 --------
 """,
 """
 -----
|    |
|    0
|    |
|
|
|
|
|
 --------
 """,
 """
 -----
|    |
|    0
|   /|
|
|
|
|
|
 --------
 """,
 """
 -----
|    |
|    0
|   /|\\
|
|
|
|
|
 --------
 """,
 """
 -----
|    |
|    0
|   /|\\
|   /
|
|
|
|
 --------
 """,
 """
 -----
|    |
|    0
|   /|\\
|   / \\
|
|
|
|
 --------
 """
 )
blank_word = []
attempts = 6
guess_letters = []
#n = 2
#while n >= 2:
while play_again:

#    n-=1
    #blank_word = []
    with open("practice30.txt") as d:
        words_list = d.read()
        chosen_word = random.choice(words_list).lower()
    #print(chosen_word)
    #guess_letters = []
    #blank_word = []
    for letter in chosen_word:
        blank_word.append("_")
#print(blank_word)
#print(attempts)
    attempts = 6
    while attempts > 0:



        if(attempts != 0 and "_" in blank_word):
            print("You have {} attempts remaining".format(attempts))

        guess = str(input("Enter any word between A-Z")).lower()


        if not guess.isalpha():
            print("This is not a letter")
            continue

        elif not len(guess) == 1:
            print("The guess is more or less than 1. Please select a valid input")
            continue

        elif guess in guess_letters:
            print("You have already used this letter")
            continue
        else:
            pass

        guess_letters.append(guess)

        if guess not in chosen_word:
            attempts -= 1
            #print(attempts)
            print(hangman[len(hangman)-1-attempts])
        else:
            search_More = True
            start_Search_Index = 0
            while search_More:
                try:
                    found_At_Index = chosen_word.index(guess,start_Search_Index)
                    blank_word[found_At_Index] = guess
                    start_Search_Index = found_At_Index+1
                except:
                    search_More = False

        print("".join(blank_word))

        if attempts == 0:
            print("Sorry! The game is over")
            print("The word was ",chosen_word)
            print("Would you like to play again?")
            response = input("?").lower()
            if response not in("y","yes"):
                print("Thank You for playing hangman game")
                play_again = False
            break


        if "_" not in blank_word:
            print("Congratulatios! You won")
            print("You easily detected the word ",chosen_word)
            print("You get nothing. Sorry! thats how mean programmers work")
            print("Would you like o play again?")
            response = input("?").lower()
            if response not in("y","yes"):
                print("Thank you for playing HANGMAN")
                play_again = False
            break
