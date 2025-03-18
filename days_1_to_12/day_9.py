art ='''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-`''---------'' '-'
                          )"""""""(
                         /________\\
                       .-------------.
                      /_______________\\
'''
print(art)
have_bidders = True
bids = {}

while(have_bidders):
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    if input("Are there any other bidders? Type 'yes or 'no'") == 'no':
        have_bidders = False
    else:
        print("\n" * 100)

max_bid = 0
max_bidder = ''
for keys in bids:
    if bids[keys] > max_bid:
        max_bid, max_bidder = bids[keys], keys
    
print(f"\nThe winner is {max_bidder} with a bid of ${max_bid}")