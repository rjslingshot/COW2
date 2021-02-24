##------
## Here is the main code for the game
##
##------

# -- reference other files --
import display
import methods
import objects
import testing

# -- greet the player --
print(display.output(objects.greeting))

testing.doStuff()


#print(methods.displayCards(objects.testHand))



# ---------------------- TO DO ----------------------
'''
Here are some notes on the features to work on...

1) lists for deck, graveyard and player hands {DONE}
2) display of player's hand {DONE}
3) display of cards (ASCII ??) {DONE}
4) JSON for card attributes 
5) method for tracking player health
6) turn order actions, tracking and display
7) simple AI

'''