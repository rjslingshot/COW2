# Design Documentation

I would like to design the program using more formal Python development methodologies.

I will break it down in the following way:

## Classes/Objects
  + ### Attributes
  + ### Methods
*** 
### Cards
  + Attributes
    + Suit --_{hearts, spades, etc..}_
    + Color --_{red or black}_
    + Value --_{3, 9, K, A, etc..}_
    + Attack --_{current attack value}_
    + Defense --_{current defense value}_
    + Ability --_{pointer to ability rule}_
    + Trait --_{pointer to trait rule}_
    + Facing --_{up or down}_
    + Location --_{pointer to collection}_
    + Owner --_{pointer to player}_
  + Methods
    + ModifyValue (value, how, amount)
    + Flip (collection, card)
    + SetOwner (player)

### Collections
  + Attributes
    + Name --_{Deck, Barrows, Hand, Front Ranks, etc..}_
    + Cards --_{list of cards}_
    + Owner --_{pointer to player}_
    + SizeLimit --_{maximum number of card for collection}_
  + Methods
    + Draw (card, destination)
    + Discard (card, destination)
    + Deploy (card, destination)
    + GetRandom ()
    + GetNext ()
    + AddCard (card)

### Players 
  + Attributes
    + Name --_{player name}_
    + Number --_{player number}_
    + Health --_{player health}_
    + Current --_{yes or no}_
  + Methods
    + ModifyHealth (how, amount)

***
The card's special abilities and house traits will be difficult to manage. I'm listing these here for future consideration.
### Abilities 
  + Attributes
    + --_{}_
  + Methods
    + 

### Traits 
  + Attributes
    + --_{}_
  + Methods
    + 

***
###NOTES:
1. I am considering that the game itself will need to be a "player". For example the game (player 0) needs to have ownership of the Deck, Barrows, etc..
2. The Draw methos would default to pulling the top card. However if a player is able to draw a specific card, then the card param must be passed
3. 
