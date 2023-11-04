#import Libraries
from random import choice 
from time import sleep
import os
from art import logo, vs
from data import data

def format_data_display(account):
  """format the display of account comparism."""
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_descr}, from {account_country}"

def main():

  #TODO-2: Declaration of Dataset for Questioning user
  #account_a = choice(data)
  account_b = choice(data)
  score = 0
  final_score = 0
  game_lose = False
  while not game_lose:
    #TODO-1 printing the Higher and lower splash screen
    print(logo)
    account_a = account_b
    account_b = choice(data)
    while account_a == account_b:
      account_b = choice(data)
    print(f"Compare A: {format_data_display(account_a)} ")
    print(vs)
    print(f"Against B: {format_data_display(account_b)}")
    
    guess = input('Who has more followers? Type "A" or "B": ').lower()
    os.system('clear')
    print(logo)
    if guess == 'a' and account_a['follower_count'] > account_b['follower_count']:
      account_b = account_a
      score += 1
      print(f"You are right! Current score: {score}")
    elif guess == 'b' and account_b['follower_count'] > account_a['follower_count']:
      score += 1
      print(f"You are right! Current score: {score}")
    else:
      final_score = score
      print(logo)
      print(F"Sorry, that's wrong!, final score: {final_score}")
      game_lose = True
      
main()