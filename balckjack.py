import random

# Set up the deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# Shuffle the deck
random.shuffle(deck)

# Deal the initial two cards to the player and the dealer
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# Calculate the initial scores for the player and the dealer
player_score = sum(player_hand)
dealer_score = sum(dealer_hand)

# Print the initial hands and scores
print(f'Player hand: {player_hand} ({player_score})')
print(f'Dealer hand: {dealer_hand} ({dealer_score})')

# The player goes first
while True:
  # Check if the player has bust (gone over 21)
  if player_score > 21:
    print('You bust!')
    break

  # Prompt the player to hit or stand
  choice = input('Would you like to hit or stand? (h/s) ')
  if choice == 'h':
    # Deal the player another card
    player_hand.append(deck.pop())

    # Recalculate the player's score
    player_score = sum(player_hand)

    # Print the new hand and score
    print(f'Player hand: {player_hand} ({player_score})')
  elif choice == 's':
    # The player stands, so it's the dealer's turn
    break
  else:
    # Invalid input, so ask again
    print('Invalid input. Please try again.')

# The dealer goes second
while True:
  # Check if the dealer has bust (gone over 21) or has a score higher than the player's
  if dealer_score > 21 or dealer_score >= player_score:
    print('Dealer stands.')
    break

  # Deal the dealer another card
  dealer_hand.append(deck.pop())

  # Recalculate the dealer's score
  dealer_score = sum(dealer_hand)

  # Print the new hand and score
  print(f'Dealer hand: {dealer_hand} ({dealer_score})')

# Determine the winner
if player_score > 21:
  print('Dealer wins!')
elif dealer_score > 21:
  print('Player wins!')
elif dealer_score > player_score:
  print('Dealer wins!')
elif player_score > dealer_score:
  print('Player wins!')
else:
  print('It\'s a tie!')