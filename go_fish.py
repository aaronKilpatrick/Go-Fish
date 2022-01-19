import cards as c

game_start = True

    
if game_start == True:
    print("*****************************")
    print("           Go Fish           ")
    print("*****************************\n")

    # Deal hand
    score = [0, 0]

    deck = c.shuffle_deck(c.build_deck())
    hands = c.deal_hands(deck, 2, 7)

    game_start = False

print(hands[0])
c.pairs_in_hand(hands[0])
print(hands[0])
print(hands[1])
c.pairs_in_hand(hands[1])
print(hands[1])

    