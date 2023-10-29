#write you code below
def prime_checker(number):
  is_prime = True
  for n in range(2, number):
    if number % n == 0:
      is_prime = False
  
  if is_prime:
    print("It is a prime Number")
  else:
    print("It is not a prime number")

#write your code above
#Do not touch the code below
n = int(input())
prime_checker(number = n)