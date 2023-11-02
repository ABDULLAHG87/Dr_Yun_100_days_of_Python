alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrpyt, type 'decode' to decrypt: ")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))

#Don't change the code above
#TODO=1: Create a funcion called 'encrpt' that takes the 'text' and shifts as inputs
  #TODO -2: inside the 'encrypt' function, shift each letter of 'text' forward in the alphabet by the shift amount and primpt encrypted tex

def encrypt(msg, shift_amount):
  encrypt_msg = ""
  for letter in msg:
    encrypt_msg += alphabet[(alphabet.index(letter) + shift) % 26]
  print(f"The encode text is {encrypt_msg}")

def decrypt(msg, shift_amount):
  decrypt_msg = ""
  for letter in msg:
    decrypt_msg += alphabet[(alphabet.index(letter) - shift) % 26]
  print(decrypt_msg)

encrypt(msg = text, shift_amount = shift)    