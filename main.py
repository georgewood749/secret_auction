import gavelASCII

bids = {}
print(gavelASCII.logo)
continuing = True

while continuing:
    name = input("\nPlease enter your name.\n")
    bid = int(input("\nHow much are you willing to bid?\n£"))
    another_bid = input("\nWould anyone else like to place a bid? Y or N\n").lower()

    bids[name] = bid
    highest_bid = 0
    highest_bidder = ""

    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            highest_bidder = name

    if another_bid == "n":
        continuing = False

print(f"\nHighest bid was {highest_bid}, made by {highest_bidder}.")