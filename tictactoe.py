from prettytable import PrettyTable

def table(t):
	x = PrettyTable()
	x.field_names = ["", "1", "2", "3"]
	x.add_row(['A'] + t[0])
	x.add_row(['B'] + t[1])
	x.add_row(['C'] + t[2])
	print(x)

def win(t):
	if t[0][0] != '':
		if t[0][0] == t[0][1] and t[0][0] == t[0][2]:
			return True
		if t[0][0] == t[1][0] and t[1][0] == t[2][0]:
			return True
		if t[0][0] == t[1][1] and t[0][0] == t[2][2]:
			return True
	if t[1][0] != '':
		if t[1][0] == t[1][1] and t[1][2] == t[1][1]:
			return True
	if t[2][0] != '':
		if t[2][0] == t[2][1] and t[2][2] == t[2][0]:
			return True
		if t[2][0] == t[1][1] and t[1][1] == t[0][2]:
			return True
	if t[0][1] != '':
		if t[0][1] == t[1][1] and t[2][1] == t[1][1]:
			return True	
	if t[0][2] != '':
		if t[0][2] == t[1][2] and t[2][2] == t[1][2]:
			return True		
	return False

def tie(t):
	for row in t:
		for square in row:
			if square == '':
				return False
	return True
def run():
	t = [['','',''],['','',''],['','','']]
	table(t)
	current_player = 'O'
	while win(t)!=True and tie(t) != True:
		if current_player == 'X':
			current_player = 'O'
		else:
			current_player = 'X'
		turn = input('Player '+current_player+' choose a square(ex A2): ')
		row = ord(turn[0])-ord('A')
		col = int(turn[1])-1
		t[row][col] = current_player
		print(row, col)
		table(t)
	if win(t) == True:
		print("Winner is ", current_player)
	else:
		print("Tie")