import art
print(art.logo)
def finding_winner(bidding_dict):
    highest_bit=0
    winner=''
    for bidder in bidding_dict:
        bid_amount=bidding_dict[bidder]
        if bid_amount>highest_bit:
            highest_bit=bid_amount
            winner=bidder
    print(f"the winner is {winner} with the bid amount of {highest_bit}")


bids={}
continue_bidding=True
while continue_bidding:
    name = input("what is your name?: ")
    price = int(input("What is your bid?: $"))
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    bids[name] = price
    if should_continue=='no':
        continue_bidding=False
        finding_winner(bids)
    elif should_continue=='yes':
        print("\n"*50)






