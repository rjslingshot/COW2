import display
import methods
import player
import objects
import random

# -- Greeting --
greet = "<LightGreen>-- Cards of War --<Reset>\n"
print(display.output(greet))

# -- TO DO --
'''
Here are some notes on the functions required

1) arrays for deck, graveyard and player hands
2) display of player's hand 
3) display of battlefield (ASCII ??)  DONE methods.displayCards
4) JSON for card attributes
5) method for tracking player health
6) turn order actions, tracking and display
7) simple AI

'''


## ----------------------------------------
##                USING LISTS
## ----------------------------------------


methods.shuffle2()

example = [["10-C"],["4-D"]]
print (example)
print (objects.deck2)
for x in example:
  #print(x[0].split("-")[0])
  s=x[0]
  t=str(s).split("-")
  print(t[1])
  
  #print (x[0])
  #print(str(s).split("-"))


'''for x in objects.deck2:
  if x == "7-C":
    print ("found it---> " + str(x.split("-")))
    break
  else:
    print ("no luck..." + x)'''

#methods.test()


## ----------------------------------------
##            USING DICTIONARIES
## ----------------------------------------

'''methods.shuffle()
num = random.randint(1,42)

objects.test = {
  1 : {
    "value":objects.deck[num]["value"],
    "suit":objects.deck[num]["suit"]
  }}


#print (objects.deck[31]["value"])
    #suit = list(cards.values())[31]["suit"]

#print (objects.deck)
print (methods.displayCards(objects.test))
'''