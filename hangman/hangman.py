import random
# create the splash screen loading

def hangman():
  word_bank = ["mouse", "Aadvark", "present"]
  select = random.choice(word_bank)
  for _ in range(len(select)):
    print("_", end = "")
  print()



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
    

  
