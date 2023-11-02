import os
from load_logo import load_logo

def get_max_auction(auction_dict):
  max_bid = 0
  max_bidder = None
  for name in auction_dict:
    if auction_dict[name] > max_bid:
      max_bid = auction_dict[name]
      max_bidder = name
  print(f"The Winner is {max_bidder} with a bid of ${max_bid}")

load_logo()
auction = {}
while True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  #bid_int = int(bid[1:])
  auction[name] = bid
  #print(auction)
  print("Are there any other bidder? Type 'yes' or 'no'")
  another_bidder = input().lower()
  
  if another_bidder == 'yes':
    os.system('clear')
  else:
    #METHOD 1
    #max_bidder = max(auction, key=auction.get)
    #max_bid = auction[max_bidder]
    get_max_auction(auction)
    break
    
  
