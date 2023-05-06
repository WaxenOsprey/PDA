### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  # this function has two errors. 
  # 1. The if statement should read if card.value == 1 to check for equality not too assign. 
  # 2. The else line is missing a colon.

  def check_for_ace(self, card):
    # if card.value == 1:
    if card.value = 1:
      return True
    # else:
    else
      return False

  # The errors in the following function are: 
  # 1. def is misspelled
  # 2. there is no comma seperating the two card arguments passed in.
  # 3. card is not a value to be returned, it should read card1.

   
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2

# 1. This code does not initialise total to 0 meaning it might cause a name error when it is used later
# the return statement should be outside the for loop.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
