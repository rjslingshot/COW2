##------
## These are the methods used in the game
##
##------

import objects
import random
import display

#--  Clear the output window  --
def clearScreen():
  print("\033c")

def symbol(suit):
  ##------
  ## define symbol for printing cards to screen
  ##------
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
  ##------
  ## define text color for printing cards to screen
  ##------
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
  ##------
  ## provides spacing for printing cards to screen
  ##------
  if len(value) > 1:
    fill = value + '   '
  else:
    fill = value + '    '
  return fill

def shuffle():
  ##------
  ## Creates a list of cards and shuffles them
  ##------
  suits=['H','D','C','S']
  values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']

  # add the main cards with a hyphen delimiter
  for x in suits:
    for a in values:
      objects.deck.append(a+"-"+x)

  # add the jokers
  objects.deck.append("JK-R")
  objects.deck.append("JK-B")

  # shuffle the cards
  random.shuffle(objects.deck)

def displayCards(cards):
  ##------
  ## prints out a graphical representation 
  ##  for a list of cards
  ##------
  row1 = ""
  row2 = ""
  row3 = ""
  row4 = ""
  row5 = ""
  row6 = ""
  row7 = ""

  # build the cards line by line
  for x in cards:
    value = x.split("-")[0]
    suit = x.split("-")[1]
  
    row1 = row1 + color(suit) + "  ┌────────┐  "
    row2 = row2 + color(suit) + "  | "+symbol(suit)+"      |  "
    row3 = row3 + color(suit) + "  |        |  "
    row4 = row4 + color(suit) + "  |   "+fill(value)+"|  "
    row5 = row5 + color(suit) + "  |        |  "
    row6 = row6 + color(suit) + "  |      "+symbol(suit)+" |  "
    row7 = row7 + color(suit) + "  └────────┘  " 

  # put it all together
  printedCards = row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7

  return printedCards

def drawCard(source,destination,start,stop):
  ##------
  ## draws card from list and adds to destination
  ##------
  i = 0
  while i < stop:
    destination.append(source[0])
    source.pop(start)
    i += 1

def discardCard(card, source, destination):
  # move card to destination
  destination.insert(0,card)
  # find index number for card in source
  i = source.index(card)
  # remove card from source
  source.pop(i)

def defineMenu():
  options = "What would you like to do? \n <Cyan>Draw<Reset>, <Red>Discard<Reset> or <Magenta>Quit<Reset>\n"
  
  return options

#--  Display main menu  --
def displaymenu(playerIndex):
  #display main menu
  action = input(display.output(defineMenu())).lower()
  #continue menu display until player choses to go forward
  while action != "g":
    validateMenu(action,playerIndex)
    action = input(display.output(defineMenu())).lower()

#--  Validate selection options for main menu  --
def validateMenu(choice, playerIndex):
  if choice == "q":
    raise SystemExit
  elif choice == "h":
    clearScreen()
    print("ok whatever...")