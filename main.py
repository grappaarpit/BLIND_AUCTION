from replit import clear
import art

#HINT: You can call clear() to clear the output in the console.
data = {}
winner = ""
winning_price = 0
def add_data(data,name_bid,bid_price):
  data[name_bid]=bid_price
answer = "Y"
print(art.logo)
while(answer=="Y"):
  name_bid = input("Whats your name bidder:  ")
  bid_price = float(input("Whats your price:  "))

  add_data(data,name_bid,bid_price)
  answer = input ("Are there more bidders Y/N :  ")
  if answer =="Y":
    clear()

for name_bid in data:
  if data[name_bid] > winning_price:
     winner = name_bid
     winning_price=data[name_bid]

print(f"The winner is {winner}, with {winning_price} as the bid") 
