art = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      '------'                           |__/
'''

import random

def end_game_msg(hand: list, computer: list) -> None:
    print(f"    Your final hand: {hand}, final score: {sum(hand)}")
    print(f"    Computer's final hand: {computer}, final score: {sum(computer)}")

def game():
    your_hand = random.choices(game_cards, k=2)
    computers_hand = [random.choice(game_cards)]
    
    if sum(your_hand) == 21:
        end_game_msg(your_hand, computers_hand)
        print("Win with a Blackjack 😎")
        return
    elif sum(your_hand) == 22:
        your_hand[1] = 1
    
    while True:
        print(f"Your cards: {your_hand}, current score: {sum(your_hand)}")
        print(f"Computer's first card: {sum(computers_hand)}")
        if sum(your_hand) > 21:
            end_game_msg(your_hand, computers_hand)
            print("You went over. You lose 😭")
            return
        keep_dealing = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if keep_dealing == 'n':
            break
        your_hand.append(random.choice(game_cards))
        
    while True:
        computers_hand.append(random.choice(game_cards))
        if sum(computers_hand) == 22 and len(computers_hand) == 2:
            computers_hand[1] = 1
        if sum(computers_hand) == 21 and len(computers_hand) == 2:
            end_game_msg(your_hand, computers_hand)
            print("Lose, opponent has Blackjack 😱")
            return
        if sum(computers_hand) > 21:
            end_game_msg(your_hand, computers_hand)
            print("Opponent went over. You win 😁")
            return
        if sum(computers_hand) >= 17 and sum(computers_hand)>sum(your_hand):
            end_game_msg(your_hand, computers_hand)
            print("You lose 😤")
            return
        if sum(computers_hand) >= 17 and sum(computers_hand)<sum(your_hand):
            end_game_msg(your_hand, computers_hand)
            print("You win 😃")
            return
            
    
game_on = True
game_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while game_on:
    print("\n" * 100)
    print(art)
    game()
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n':
        game_on = False
        print("GoodBye.")