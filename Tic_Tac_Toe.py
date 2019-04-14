#!/usr/bin/env python
import random

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
	marker = ''
	while not (marker == 'X' or marker == 'O'):
		marker = input("Player 1: Do you want to be X or O? ").upper()

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

def player_choice(board, role):
	position = ''
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
		position = input(role + " Choose your next position: (1-9) ")
	return int(position)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
	if random.randint(0, 1) == 0:
		return 'Player 1'
	else:
		return 'Player 2'

def space_check(board, position):
	return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]

def replay():
	return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')


print('Welcome to Tic Tac Toe!')
while True:
	board = [' ']*10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + " will go first.")
	game_on = True

	while game_on:
		if turn == "Player 1":
			display_board(board)
			place_marker(board, player1_marker, player_choice(board, turn))
			if win_check(board,player1_marker):
				display_board(board)
				print("Player 1 Win!")
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print("Tie")
					game_on = False
				else:
					turn = "Player 2"
		else:
			display_board(board)
			place_marker(board, player2_marker, player_choice(board, turn))
			if win_check(board,player2_marker):
				display_board(board)
				print("Player 2 Win!")
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print("Tie")
					game_on = False
				else:
					turn = "Player 1"

	if not replay():
		break
