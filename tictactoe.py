# Tic Tac Toe game
# This game uses functions to build and update the board
done = False
def tictactoe():
	board = [1,2,3,4,5,6,7,8,9]
	WIN_COMBO = [
	(0,1,2),
	(3,4,5),
	(6,7,8),
	(0,3,6),
	(1,4,7),
	(2,5,8),
	(0,4,8),
	(2,4,6)
	]

	def displayBoard():
		print "\n"
		print "|",board[6],"|",board[7],"|",board[8],"|"
		print "-------------"
		print "|",board[3],"|",board[4],"|",board[5],"|"
		print "-------------"
		print "|",board[0],"|",board[1],"|",board[2],"|" 
		print "\n"

	def pickPlayer():
		print "Choose which player goes first (X or O) : ",
		pchoice = raw_input()
		playerChoice(pchoice)

	def playerChoice(choice_str):
		try:
			if choice_str == 'X' or choice_str == 'x':
				playGame(choice_str.upper())
			elif choice_str == 'O' or choice_str == 'o':
				playGame(choice_str.upper())
		except ValueError:
			print "Oops, wrong entry, try again"
			pickPlayer()

	def checkWin(board,playerPiece):
		for a,b,c in WIN_COMBO:
			if board[a] == board[b] == board[c] == playerPiece:
				print "Player {0} has won".format(playerPiece)
				done = True
			else:
				switchPlayer(playerPiece)

	def switchPlayer(player):
		if player == 'X':
			player = 'O'
			playGame(player)
		elif player == 'O':
			player = 'X'
			playGame(player)

	def playGame(player):
		displayBoard()
		print "Player {0}, make your move (1-9) : ".format(player),
		try:
			choice_int = int(input())
			if choice_int in board:
				board[int(choice_int)-1] = player
				displayBoard()
				print "Player {0} moved to {1}".format(player,choice_int)
				checkWin(board,player)
			else:
				print "Invalid move, try again"
				playGame(player)
		except ValueError:
			print "That's not a number, please try again"
			playGame(player)

	pickPlayer()

print "TIC TAC TOE V 1.0"
while done != True:
	tictactoe()