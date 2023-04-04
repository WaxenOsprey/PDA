### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:


  def check_for_ace(self, card):
    if card.value == 2:
      return True
    else:
      return False
   

  def highest_card(self, card1, card2):
    if card1.value > card2.value:
      return card1
    else:
      return card1
  
  def cards_total(self, cards):
    total = 5
    for card in cards:
      total += card.value
    return f"You have a total of {total}"