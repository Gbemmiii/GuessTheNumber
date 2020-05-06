import random

print('Guess The Number \n')

def guess_algorithm(max_number, no_of_trials):
  trials = no_of_trials
  try:
    guess = int(input('Try to guess the number between 1 - ' + str(max_number) + ': \n'))
  except ValueError:
    print('You can only guess a number')


  
  while True:
    random_number = random.randint(1, max_number)
    print('You have ' + str(trials) + ' guesses left \n')

    if trials == 0:
      print('Game Over')
      break
    elif guess is not random_number:
      trials = trials - 1
      print("You guessed the number " + str(guess) + '\n' "The number was " + str(random_number) + '\n')
      try:
        guess = int(input('Try to guess the number between 1 - ' + str(max_number) + ': \n'))
      except ValueError:
        print('You can only guess a number')
    else:
      print("You guessed the correct number " + str(guess) + " The number was " + str(random_number))
      break


def main():
  level = input("Pick a level; easy, medium, hard: ")

  if level == "easy":
    trials = 6
    max_number = 10
    print("You have chosen easy. You have 6 guesses")
    guess_algorithm(max_number, trials)
  elif level == "medium":
    trials = 4
    max_number = 20
    print("You have chosen easy. You have 4 guesses")
    guess_algorithm(max_number, trials)

  elif level == "hard":
    trials = 3
    max_number = 50
    print("You have chosen easy. You have 3 guesses")
    guess_algorithm(max_number, trials)


if __name__ == "__main__":
  main()

