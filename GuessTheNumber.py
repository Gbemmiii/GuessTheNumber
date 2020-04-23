import random


play = True

while play:

    level = (input("Pick a level 1(easy), 2(medium), 3(hard): "))

    # Level of difficulty arrangement
    if level == "easy":

        top = 10
        total_guess = 6
        print ("You have choosen easy. You have 6 guesses")
        print("Try to guess the number! Its between 1 and 10.")

    elif level == "medium":
        max_number = 20
        total_guess = 4
        print ("You have choosen medium. You have 4 guesses.")    
        print("Try to guess the number! Its between 1 and 20.")

    elif level == "hard": 
        max_number = 50
        total_guess = 3
        print ("You have choosen hard. You have 3 guesses.") 
        print("Try to guess the number! Its between 1 and 50.")

    number = random.randint(1, 100)

    guessesTaken = 0
    while guessesTaken <= total_guess:
        try:
            guess = int(input("Take a guess:"))
        except:
            print("You can only enter a number \n Guess the number")    
        guessesTaken += 1
        if guess < number:
            print("Your guess is too low")     
        if guess > number:
            print("Your guess is too high.")
        if guess == number:
            break

    # End statements depending on whether user guessed correct number or not.    
    if guess == number:
        guessesTaken = str(guessesTaken)
        print("You guessed the number in " + guessesTaken + " guesses!")

    if guess != number:
        number = str(number)
        print("Nope. The number was " + number)

    # Play again loop that attaches to original statement that allows you to quit or play again.
    count=1
    again=(input("Do you want to play again, type yes or no "))
    if again == "no":
        play = False   


    print(guess)
        


    