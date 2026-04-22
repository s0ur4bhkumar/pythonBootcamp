def clear_output():
    print("\n" * 20)


def highest_bidder(bids):
    highest_bidderder = ""
    highest_bidder = 0
    for key in bids:
        if bids[key]["bid"] > highest_bidder:
            highest_bidder = bids[key]["bid"]
            highest_bidderder = key
    print(f"The highest bidder is {highest_bidderder} with {highest_bidder} dollars")


bids = {}
while True:
    name = input("what is your name: ")
    bid = int(input("Enter your bid: "))
    continue_bid = input("Are there others who need to bid? ")
    bids[f"{name}"] = {"bid": bid}
    if continue_bid == "yes":
        clear_output()
    else:
        highest_bidder(bids)
        break
