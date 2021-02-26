##------
## This is used for building testing cenarios
##
##------
import methods
import objects


def doStuff():
  # -- test case draws and discards cards --
  print ('\n-- shuffling cards and displaying deck--\n')
  methods.shuffle()
  ##print (objects.deck)

  print ('\n-- draw 5 cards into hand and show new deck--\n')
  methods.drawCard(objects.deck, objects.testHand, 0, 5)
  ##print (objects.deck)

  print ('\n-- display contents of hand --\n')
  ##print (objects.testHand)

  print ('\n-- discard 4th card in hand, and display barrows --\n')
  methods.discardCard(objects.testHand[3], objects.testHand, objects.barrows)
  ##print (objects.barrows)

  print ('\n-- display contents of hand --\n')
  print (objects.testHand)
  print ('\n-- display contents of barrows --\n')
  print (objects.barrows)
