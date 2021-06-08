def secret_auction():
    from turtle import clear
    from bidding_art import logo
    print(logo)
    bids = {}
    bidding_finished = False

    def highest_bidder(bidding_record):
        highest_bid = 0
        winner = ""
        for bidder in bidding_record:
            bid_amt = bidding_record[bidder]
            if bid_amt > highest_bid:
                highest_bid = bid_amt
                winner = bidder
        print(f"the winner is{winner} with highest bid is {highest_bid}\n")

    while not bidding_finished:
        name = input("enter ur name: ")
        price = int(input("enter the amount: $"))
        bids[name] = price
        should_bid = input("should continue to bid? enter yes or no\n")
        if should_bid == "no":
            bidding_finished = True
            highest_bidder(bids)
        elif should_bid == "yes":
            clear()
