#Creating a pyPassword Generator
random = __import__("random")

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to pypassword Generator")
nr_letters = eval(input("Enter number of letters:"))
nr_numbers = eval(input("Enter number of numbers:"))
nr_symbols = eval(input("Enter number of symbols:"))
#create an empty password list
password = []

# randomly select letter password from the list of letters, numbers and symbols
for letter in range(nr_letters):
  password += random.choice(alphabet)
for number in range(nr_numbers):
  password += random.choice(numbers)
for symbol in range(nr_symbols):
  password += random.choice(symbols)
#shuffle list of  letters in the password 
random.shuffle(password)
# join the strings together using the join command
passgen = "".join(password)
# print out result 
print("Generated Password:", passgen)

