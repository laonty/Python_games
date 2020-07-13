# -*- coding: utf-8 -*-
import random

# 4 decks for a game
values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4 * 4

def new_game():

	#карты игрока
	player_hand = []
	#карты диллера
	dealer_hand = []

	print ('+'*30)
	print ('\nNEW GAME \n')

	#shuffle the decks
	random.shuffle(values)
	#number of cards in decks
	deck_lenght = len(values)-1

	#one card for dealer
	dealer_hand = (get_card(deck_lenght))
	deck_lenght -= 1
	print ('\nDealer hand: %s  and dealer score: %s' %(str(dealer_hand), get_value(dealer_hand)))
	
	#two cards for player
	player_hand = get_card(deck_lenght)
	deck_lenght -= 1
	player_hand += get_card(deck_lenght)
	deck_lenght -= 1
	print ('\nPlayer hand: %s  and player score: %s'%(str(player_hand), str(get_value(player_hand))))

	#if its 0 the game over
	game = 1

	#if less 21 you can hit more cards one by one
	while get_value(player_hand) < 21:
		choice = input('\nPress any key to hit or press [N] to stand >')
		if choice.lower() =='n':
			break
		else:
			player_hand += get_card(deck_lenght)
			deck_lenght -= 1
			print ('Player hand: %s  and player score: %s'%(str(player_hand), str(get_value(player_hand))))

		#if you got more 21 you lose
		if get_value(player_hand) > 21:
			print ('*'*20)
			print ('\nPLAYER LOOSE\n')
			print ('Player hand: %s  and player score: %s'%(str(player_hand), str(get_value(player_hand))))
			print ('Dealer hand: %s  and dealer score: %s' %(str(dealer_hand), get_value(dealer_hand)))
			game = 0

	if game:
		#dealer have to hit cards if his sore less 17
		while get_value(dealer_hand) < 17:
			dealer_hand += get_card(deck_lenght)
			deck_lenght -= 1
			print ('\nDealer hand: %s  and dealer score: %s' %(str(dealer_hand), get_value(dealer_hand)))
			#if dealer got more 21 than dealer loose
			if get_value(dealer_hand) > 21:
				print ('*'*20)
				print ('\nDEALER LOOSE\n')
				print ('Dealer hand: %s  and dealer score: %s' % (str(dealer_hand), get_value(dealer_hand)))
				print ('Player hand: %s  and player score: %s'%(str(player_hand), str(get_value(player_hand))))
				game = 0
	if game:
		#if both got less 21 than the winner will be the biggest score
		if get_value(player_hand) > get_value(dealer_hand):
			print ('*'*20)
			print ('\nDEALER LOOSE\n')
			print ('Dealer hand: %s  and dealer score: %s' % (str(dealer_hand), get_value(dealer_hand)))
			print ('Player hand: %s  and player score: %s'%(str(player_hand), str(get_value(player_hand))))
		else:
			print ('*'*20)
			print ('\nPLAYER LOOSE\n')
			print ('Dealer hand: %s  and dealer score: %s' % (str(dealer_hand), get_value(dealer_hand)))
			print ('Player hand: %s  and player score: %s'%(str(player_hand), str(get_value(player_hand))))

#get a card from desk
def get_card(lenght):
	new_card = []
	new_card.append(values.pop(lenght))
	return new_card

#get value of card
def card_value(card):
	if str(card) in 'JQK':
		return 10
	elif card == 'A':
		return 11
	else:
		return card
#get score of all cards in hand
def get_value(card):
	#score
	result = 0
	#aces
	aces = 0

	#looking for aces
	for each in card:
		result += card_value(each)
		if each == 'A':
			aces += 1
	#if sum of cards with aces more than 21 than acex count as 1
	if result + (aces*11) > 21:
		result += aces
	else:
		result += aces*11
	return result

#loop of a game
while input('\nPress any key to play '):
	new_game()

