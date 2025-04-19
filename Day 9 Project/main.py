import art

bids = {}
continue_bidding = True

while continue_bidding:
    print(art.logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))

    bids[name] = bid

    more_bidders = input("Are there any more bidders? Type 'y' or 'n': ")
    if more_bidders == 'n':
        continue_bidding = False

    print("\n" * 25)
winner = ""
winning_bid = 0

for bidder in bids:
    if bids[bidder] > winning_bid:
        winner = bidder
        winning_bid = bids[bidder]

print(f"The winner is {winner} with a bid of ${winning_bid}!")
