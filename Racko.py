import random

#David Han and Alex Perez

import random
# shuffle the deck to start the game. Also shuffle the discard pile if
#we ever run out of cards and need to ‘restart’ the game. This function does not return
#anything. You can import the random module and just use random.shuffle.
def shuffle(cardstack):
  random.shuffle(cardstack)
  return cardstack


#given a rack (this will be either the user’s or the computer’s)
#determine if Racko has been achieved. Remember that Racko means that the cards
#are in ascending order. This function returns a boolean value.
def check_racko(rack):
  for card in range (len(rack) - 1):
    if rack[card + 1] <= rack[card]:
      return False
  return True
    
  # get the top card from any stack of cards. Used at the
#start of game play for dealing cards. This same function will also be used during each
#player’s turn to take the top card from either the discard pile or from the deck.
#This function must return an integer.
def get_top_card(card_stack):
  topcard = card_stack[0]
  card_stack.pop(0)
  return topcard

#deal initial hands(deck) - start the game off by dealing two hands of 10 cards each. This function returns two lists - one representing the user’s hand and the other representing the computer’s hand. Make sure that you follow normal card game conventions of dealing. So programatically you have to deal one card to the computer, one to the user, one to the computer, one to the user and so on. The computer is always the first person that gets dealt to. The user always plays first. Remember that the rules of our version of Racko will be that you have to place your cards in the order of top most slot of the rack first, then the next slot and so on. In the example above, this would mean that someone was dealt the cards 3, 17, 11, 30, 33, . . . in that order. 
def deal_initial_hands(deck):
  comp_deck = []
  user_deck = []
  for x in range (20):
    if x % 2 == 0:
      comp_deck.append(deck[0])
      deck.pop(0)
    else:
      user_deck.append(deck[0])
      deck.pop(0)

      
  return (comp_deck, user_deck)

#given a rack(represented as a list) print it out from top to bottom in a manner that looks more akin to the game (more stack like than list like). See the example above for the exact specification. Please stick to that specification in terms of the representation of the rack.
def print_top_to_bottom(rack):
  for card in rack:
    print(card)

def comp_find_and_replace(new_card, card_to_be_replaced, hand, discard):
  index_of_replace_card = hand.index(card_to_be_replaced)
  discard.insert(0, card_to_be_replaced) #add replaced card to discard
  hand[index_of_replace_card] = new_card #replace hand card with new card

def computer_play(hand, deck, discard_pile):

    #strategy for our program:
    #For our strategy, the computer is 
    card_replaced = False
    discard_card = discard_pile[0]
    deck_card = deck[0]
    #print("discard card: ", discard_card)
    #print("deck card:", deck_card)
    for card in range (len(hand) - 2): 
      #print("next card", hand[card + 1], "curr card", hand[card], "deck card", deck_card, "discard", discard_card)
      if(hand[card] < deck_card < hand[card + 2]):
        comp_find_and_replace(deck_card, hand[card + 1], hand, discard_pile)
        card_replaced = True
        break;
      elif(hand[card] < discard_card < hand[card + 2]):
        comp_find_and_replace(discard_card, hand[card + 1], hand, discard_pile)
        card_replaced = True
        break;
      elif (hand[card + 1] < hand[card] and deck_card > hand[card] and discard_card > hand[card]):
        comp_find_and_replace(min(deck_card, discard_card), hand[card + 1], hand, discard_pile)
      #  print("first cond")
        card_replaced = True
        break;
      elif(hand[card + 1] < hand[card] and deck_card > hand[card] and discard_card < hand[card]):
       comp_find_and_replace(deck_card, hand[card + 1], hand, discard_pile)
      # print("second cond")
       card_replaced = True
       break;
      elif(hand[card + 1] < hand[card] and deck_card < hand[card] and discard_card > hand[card]):
        comp_find_and_replace(discard_card, hand[card + 1], hand, discard_pile)
        #print("third cond")
        card_replaced = True
        break;
     
    if not card_replaced:
      comp_find_and_replace(min(discard_card, deck_card), hand[0], hand, discard_pile)
      #print("fourth cond")
        

#find the card to be replaced (represented by a number) in the hand and replace it with newCard. The replaced card then gets put on top of the discard. Check and make sure that the cardToBeReplaced is truly a card in the hand. If the user accidentally typed a card number incorrectly, just politely remind them to try again and leave the hand unchanged.
def find_and_replace(new_card, card_to_be_replaced, hand, discard):
  
  while(card_to_be_replaced not in hand):
    print("Invalid")
    card_to_be_replaced = int(input("Which Card Would You like to Replace?"))
  index_of_replace_card = hand.index(card_to_be_replaced)
  discard.insert(0, card_to_be_replaced) #add replaced card to discard
  hand[index_of_replace_card] = new_card #replace hand card with new card
    
    
#add the card(represented as just an integer) to the top of the discard pile.
def add_card_to_discard(card, discard):
  discard.insert(0, discard)


      


    

    

    
# put's function together
def main():
  cardstack = [(x + 1) for x in range (60)]
  cardstack = shuffle(cardstack)
  racks = deal_initial_hands(cardstack)
  comp_rack = racks[0]
  user_rack = racks[1]
  discard = []
  discard.append(get_top_card(cardstack))
  cardstack.pop(0)
  while not(check_racko(user_rack)) and not(check_racko(comp_rack)):
    #print("Computers Deck:")
    #print_top_to_bottom(comp_rack)
    print("Your Deck:")
    print_top_to_bottom(user_rack)
    print("Top Card in Discard:", discard[0])
    card_choice = str(input("Would you like to take a card from the discard pile or the deck? [di] or [de]"))
    if card_choice == "di":
      new_card = get_top_card(discard)
      card_to_be_replaced = int(input("Which Card Would You like to Replace?"))
      find_and_replace(new_card, card_to_be_replaced, user_rack, discard)
    else:
      new_card = get_top_card(cardstack)
      print("The Top Card in the deck is", new_card)
      replace_with_deck = str(input("Would you like to replace a card in your deck with this card? (y / n)"))
      if replace_with_deck == "y":
        cardstack.pop(0)
        card_to_be_replaced = int(input("Which Card Would You like to Replace?"))
        find_and_replace(new_card, card_to_be_replaced, user_rack, discard)
    computer_play(comp_rack, cardstack, discard)
  if (check_racko(user_rack)):
    print("Your Final Deck:")
    print_top_to_bottom(user_rack)
    print("You Win!")
  else:
    print("ok bro")
    
    
    
  
if __name__ == '__main__':
  main()
