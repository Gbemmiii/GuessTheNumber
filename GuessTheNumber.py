import random

while True:

    def level_difficulty():
        level = input("Pick a level; easy, medium, hard: ")
        return level
    level = level_difficulty()

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

    if level == "easy":
        number = random.randint(1, 10)

    if level == "medium":
        number = random.randint(1, 20)

    if level == "hard":
        number = random.randint(1, 50)    
    

    def guesses():
        while True: 
            try:
                guess = int(input("Take a guess:"))
            except:
                print("You can only enter a number \n Guess the number")  
            return guess    
    guess = guesses()

    def number_guesses():
        guessesTaken = 0
        while guessesTaken < total_guess:  
            guessesTaken += 1
        return guessesTaken
    guessesTaken = str(number_guesses())
    print("You have " + guessesTaken + " guesses left." )     

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



        