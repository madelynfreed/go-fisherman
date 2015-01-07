from sys import argv
from sys import exit
import random
from random import shuffle

script, player1, player2 = argv

deck = range(0,52)
shuffle(deck)

whose_turn_is_it = 1

def draw_first_hand(player, deck):
	length_of_deck = len(deck)

	hand = []


	for i in range(0,7):
		hand.append(deck[i])
		deck.pop(i)
	
	return deck, hand



def check_hand_for_pairs(playerhand):

	#print "check hand for pairs, ", playerhand
	checkhand = list(playerhand)	

	for i in range(0, len(checkhand)):
		module = checkhand[i] % 13
		checkhand[i] = [checkhand[i]]
		checkhand[i].append(module)

	match = []
	position = []
	
	guess_list = range(0,13)
	shuffle(guess_list)

	for i in guess_list:
		#print i, " outer"
		for x in range(0, len(checkhand)):
			
			if i == checkhand[x][1]:
				match.append(checkhand[x])
				position.append(x)
				#print position
				print "for check hand, the match so far is ", match
		if len(match) == 4:
			print "COMPLETECOMPLETE COMPLETECOMPLETE", checkhand[position[0]], checkhand[position[1]], checkhand[position[2]], checkhand[position[3]]
			print "position[0] ", position[0]
			#print playerhand
			#print "match ", match[0]
			playerhand.remove(match[0][0])
			#print "hand without match0 ", playerhand
			playerhand.remove(match[1][0])
			#print "hand without match1 ", playerhand
			playerhand.remove(match[2][0])
			#print "hand without match2 ", playerhand
			playerhand.remove(match[3][0])
			#print "hand without match3 ", playerhand
			
			return 1, playerhand
			
		else:
			
			return 0, playerhand
		match = []
		position = []

def ask_for_cards(playerAskerhand, playerReceiverhand, deck):

	player_request = best_guess(playerAskerhand)
	#player_request = int(raw_input("%s, what card would you like? > " % playerAsker))
	#player_request = random.randint(0,52)

	if len(playerReceiverhand) == 0:
		#print "the receiver has no cards left.  "

		die()
	elif player_request in playerReceiverhand:
		playerAskerhand.append(player_request)
		playerReceiverhand.remove(player_request)
		#ask_for_cards(playerAskerhand, playerReceiverhand, deck)
		
	else:
		go_fish(playerAskerhand, deck)
	
	return playerAskerhand, playerReceiverhand, deck
		
def go_fish(playerhand, deck):
	if len(deck) == 0:
		print "looping"

	else:
		playerhand.append(deck[0])
		deck.pop(0)


def play_back_and_forth(player1, player2, player1hand, player2hand, deck):
	
	whose_turn_is_it = 0
	score_player1 = 0
	score_player2 = 0
	print "what is going on? whose turn is it: ", whose_turn_is_it

	while True:
		if whose_turn_is_it%2 == 0:
			
			playerasker, playeraskerhand = player1, player1hand
			playerreceiver, playerreceiverhand = player2, player2hand

			print "whose turn is it, ", whose_turn_is_it
			print "%r's hand is %r" % (playerasker, playeraskerhand)
			print "XXXXXXXXXXplayer asker is %r and player receiver is %r " % (player1, player2)
			#print "play back and forth on %r's turn" % player1, player1hand
			
			playeraskerhand, playerreceiverhand, deck = ask_for_cards(playeraskerhand, playerreceiverhand, deck)
			x, playeraskerhand = check_hand_for_pairs(playeraskerhand)
			#why doesn't check hand for pairs work as well as best guess? 
			
			if x == 1:
				score_player1 += 1
				print "%r's score is %r" % (player1, score_player1)
			elif x == 0:
				print "check hand for pairs didn't result in any score"
			y, playerreceiverhand = check_hand_for_pairs(playerreceiverhand)
			if y == 1:
				score_player2 += 1
				print "%r's score is %r" % (player2, score_player2)
			elif x == 0:
				print "check hand for pairs didn't result in any score"
			
			print "After asking for cards, %r's score is %r, %r's score is %r" % (player1, score_player1, player2, score_player2)
			whose_turn_is_it += 1
			
			

		elif whose_turn_is_it%2 != 0:
			print "YYYYYYYYplayer asker is %r and player receiver is %r " % (player2, player1)
			playerasker, playeraskerhand = player2, player2hand
			
			playerreceiver, playerreceiverhand = player1, player1hand
			#print player2hand
			playeraskerhand, playerreceiverhand, deck = ask_for_cards(playeraskerhand, playerreceiverhand, deck)
			
			x, playeraskerhand = check_hand_for_pairs(playeraskerhand)
			if x == 1:
				score_player2 += 1
				print "%r's score is %r" % (player2, score_player2)
			elif x == 0:
				print "check hand for pairs didn't result in any score"
			y, playerreceiverhand = check_hand_for_pairs(playerreceiverhand)
			if y == 1:
				score_player1 += 1
				print "%r's score is %r" % (player1, score_player1)
			elif x == 0:
				print "check hand for pairs didn't result in any score"
			

			print "After asking for cards, %r's score is %r, %r's score is %r" % (player1, score_player1, player2, score_player2)
			whose_turn_is_it +=1

		else:
			die()
	
	return score_player1, score_player2

def best_guess(playerhand):
	checkhand = list(playerhand)
	ask_for = 0	

	for i in range(0, len(checkhand)):
		module = checkhand[i] % 13
		checkhand[i] = [checkhand[i]]
		checkhand[i].append(module)

	match = []
	position = []

	guess_list = range(0,13)
	shuffle(guess_list)

	for i in guess_list:
		#print i, " outer"
		for x in range(0,len(checkhand)):
			
			if i == checkhand[x][1]:
				match.append(checkhand[x])
				position.append(x)
				#print position
				print "the match so far is ", match
		if len(match) == 4:
			print "I caught a match here"

		if len(match) == 3:
			matchsum = match[0][0] + match[1][0] + match[2][0]
			difference = 3 * match[0][1]
			print "the matchsum is ", matchsum
			print "the difference is ", difference
			if matchsum - difference == 78:
				ask_for = match[0][1]
			elif matchsum - difference == 65:
				ask_for = 13 + match[0][1]
			elif matchsum - difference == 52:
				ask_for = 26 + match[0][1]
			elif matchsum - difference == 39:
				ask_for = 39 + match[0][1]
			#return True
			return ask_for
		elif len(match) == 2:
			matchsum = match[0][0] + match[1][0]
			difference = 2 * match[0][1]
			random_choice = random.randint(0,1)

			"""print "the matchsum is ", matchsum
			print "the difference is ", difference
			print "the random choice is", random_choice"""

			if matchsum - difference == 65:
				if random_choice == 0:
					ask_for = 13 + match[0][1]
				else:
					ask_for = match[0][1]
			elif matchsum - difference == 52:
				if random_choice == 0:
					ask_for = 26 + match[0][1]
				else:
					ask_for = match[0][1]
			elif matchsum - difference == 39:
				ask_for = choose_random_outside_your_hand(playerhand)	
			elif matchsum - difference == 26:
				if random_choice == 0:
					ask_for = 13 + match[0][1]
				else:
					ask_for = 39 + match[0][1]
			elif matchsum - difference == 13:
				if random_choice == 0:
					ask_for = 13 + match[0][1]
				else:
					ask_for = 39 + match[0][1]
			return ask_for
		else:
			ask_for = choose_random_outside_your_hand(playerhand)
			return ask_for

		match = []
		position = []
			#return False

def choose_random_outside_your_hand(playerhand):
	full_deck = range(0,52)
	for i in playerhand:
		full_deck.remove(i)
	random_choice = random.randint(0, len(full_deck)-1)
	ask_for = full_deck[random_choice]
	return ask_for

def die():
	print "The game is done!"
	exit(0)


#whose_turn_is_first()
deck, player1hand = draw_first_hand(player1, deck)
print deck, player1hand
deck, player2hand = draw_first_hand(player2, deck)
print deck, player2hand

scoreplayer1, scoreplayer2 = play_back_and_forth(player1, player2, player1hand, player2hand, deck)
if scoreplayer1>scoreplayer2:
	print "%r won!" % player1
elif scoreplayer2>score_player1:
	print "%r won!" % player2
else:
	print "It was a tie, apparently. Play again to see who's dominant."