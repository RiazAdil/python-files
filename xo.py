

a=['1','2','3','4','5','6','7','8','9']
def printBoard ():
	print( a[0]+'|'+a[1]+'|'+a[2])
	print("--------------------------")
	print( a[3]+'|'+a[4]+'|'+a[5])
	print("--------------------------")
	print( a[6]+'|'+a[7]+'|'+a[8])


playeroneturn=True
for i in range(9):
	printBoard()

#Player 1 plays 
	if playeroneturn:
		p=input("Player 1,Choose your place :")
		if p in a:
			a[int(p)-1]='X'
			playeroneturn = not playeroneturn

	else:
		p=input("player 2,Choose your place :")
		if p in a:
			a[int(p)-1]='O'
			playeroneturn= not playeroneturn

#check for winning combinations
	if ((a[0]==a[1] and a[0]==a[2]) or (a[0]==a[3] and a[0]==a[6]) or (a[3]==a[4] and a[3]==a[5]) or (a[6]==a[7]and a[6]==a[8]) or (a[1]==a[4] and a[1]==a[7]) or (a[2]==a[5]and a[2]==a[8]) or (a[0]==a[4] and a[0]==a[8]) or (a[2]==a[4] and a[2]==a[6])):
				print("game over")
