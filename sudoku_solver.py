def if_poss(board,r,c,num):
	for i in range(9):
		if board[i][c]==num and i!=r:
			return False
		if board[r][i]==num and i!=c:
			return False
	row=r-r%3
	col=c-c%3
	for i in range(3):
		for j in range(3):
			if board[i+row][j+col]==num and (i+row)!=r and (j+col)!=c:
				return False
	return True

def is_empty(board,lis):
	for i in range(9):
		for j in range(9):
			if board[i][j]==0:
				lis[0]=i
				lis[1]=j
				return True
	return False

def solver(board):
	lis=[0,0]
	if not is_empty(board,lis):
		return True
	r=lis[0]
	c=lis[1]
	for num in range(1,10):
		if if_poss(board,r,c,num):
			board[r][c]=num
			if solver(board):
				return True
			else:
				board[r][c]=0
	return False

