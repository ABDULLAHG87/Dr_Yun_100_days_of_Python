import random

def hangman():
    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
    word_bank = ["mouse", "aadvark", "present", "premise"]
    select_word = random.choice(word_bank)
    list_word = []
    wrong_count = 0
    right_guess = 0
    for letter in select_word:
        list_word += "_"

    while True:
        print(list_word)
    #Guessing Letters
        guess = input("Guess a letter: ")
        for n,letter in enumerate(select_word):
            if guess == letter:
                list_word[n] = letter
                found = True
                right_guess += 1
        if right_guess == len(select_word):
            print("Correct Guess: ", select_word)
            print("You Win. Congratulations")
            break

        if guess not in select_word:
            print(HANGMANPICS[wrong_count])
            wrong_count += 1
        if wrong_count == len(HANGMANPICS):
            print("Game Over. You Lose")
            break


welcome_msg ="""Welcome to 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       
                   """
welcome_msg = welcome_msg.center(80)
print(welcome_msg)

print("Choose an Option for the Game")
print("""
1. Single Player with Timing
2. Single Player without Timing """)
while True:
  try:
    choice = int(input("Enter your choice:"))
  except ValueError:
    print("Please enter a valid Number")
  else:
    if choice == 1:
      print("single player with timing mode")
      hangman()
      break
    elif choice == 2:
      print("single player without timing mode")
      break
    else:
      print("Invalid choice")




