import objects

def symbol(suit):
  ## Determine symbol
  if suit == "H":
    symbol = '♥'
  elif suit =="D":
    symbol = '♦'
  elif suit =="C":
    symbol = '♣'
  elif suit =="S":
    symbol = '♠'
  else:
    symbol = ' '
  return symbol

def color(suit):
  ## Set text color
  if suit == 'D' or suit == 'H' or suit == 'R':
    # red
    color = '\033[31m'  
  elif suit == 'C' or suit == 'S' or suit == 'B':
    # blue
    color = '\033[34m'
  else:
    # no color
    color = '\033[0m'

  return color

def fill(value):
  ## Filler spaces for value row
  if len(value) > 1:
    fill = value + '   '
  else:
    fill = value + '    '
  return fill

## ----------------------------------------
##            USING DICTIONARIES
## ----------------------------------------

def displayCards(cards):
  row1 = ""
  row2 = ""
  row3 = ""
  row4 = ""
  row5 = ""
  row6 = ""
  row7 = ""

  # build the cards line by line
  for x in cards:
    value = (cards[x]["value"])
    suit = (cards[x]["suit"])
  
    row1 = row1 + color(suit) + "  ┌────────┐  "
    row2 = row2 + color(suit) + "  | "+symbol(suit)+"      |  "
    row3 = row3 + color(suit) + "  |        |  "
    row4 = row4 + color(suit) + "  |   "+fill(value)+"|  "
    row5 = row5 + color(suit) + "  |        |  "
    row6 = row6 + color(suit) + "  |      "+symbol(suit)+" |  "
    row7 = row7 + color(suit) + "  └────────┘  " 

  # put it all together
  rank = row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7

  return rank
  

def shuffle():
  suits=['H','D','C','S']
  values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  n = 1

  for x in suits:
    for a in values:
      objects.deck[n] = {"value": a, "suit":x}
      n=n+1
      #{'name': 'Cara', 'age': 25}
      #objects.deck.update({"value": a},{"suit":x}) 
      #print(a + x)

## ----------------------------------------
##                USING LISTS
## ----------------------------------------
def shuffle2():
  suits=['H','D','C','S']
  values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']

  # add the main cards with a hyphen delimiter
  for x in suits:
    for a in values:
      objects.deck2.append(a+"-"+x)

  # add the jokers
  objects.deck2.append("JK-R")
  objects.deck2.append("JK-B")

# -- DISPLAY CARD(s)
def displayCards2(cards):
  row1 = ""
  row2 = ""
  row3 = ""
  row4 = ""
  row5 = ""
  row6 = ""
  row7 = ""

  # build the cards line by line
  for x in cards:
    value = (cards[x]["value"])
    suit = (cards[x]["suit"])
  
    row1 = row1 + color(suit) + "  ┌────────┐  "
    row2 = row2 + color(suit) + "  | "+symbol(suit)+"      |  "
    row3 = row3 + color(suit) + "  |        |  "
    row4 = row4 + color(suit) + "  |   "+fill(value)+"|  "
    row5 = row5 + color(suit) + "  |        |  "
    row6 = row6 + color(suit) + "  |      "+symbol(suit)+" |  "
    row7 = row7 + color(suit) + "  └────────┘  " 

  # put it all together
  rank = row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7

  return rank


#---------------
def test():
  print(objects.deck2)
  #shuffle()