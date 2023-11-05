from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("Welcome to the secret auction program.")
condition=True
auction={}
while condition:
  name=input("What is your name?: ")
  bid=int(input("whats your bid?: $"))
  auction[name]=bid
  choice=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if choice=='no':
    condition=False
  clear()
maxi=0
winner=''
for name in auction:
  if auction[name]>maxi:
    maxi=auction[name]
    winner=name
print(f"The winner is {winner} with a bid of ${maxi}.")
    

    
  
