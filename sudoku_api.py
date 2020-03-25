import requests
import sudoku_solver


def print_grid(grid):
	for i in range(9):
		print(grid[i])

url="http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9"
response=requests.get(url)

data=response.json()
grid=[[0 for i in range(9)] for j in range(9)]
# for i in range(9):
# 	for j in range(9):
# 		grid[i][j]=0
if data["response"]:
	values=data["squares"]
	for one in values:
		r=one["x"]
		c=one["y"]
		grid[r][c]=one["value"]

if sudoku_solver.solver(grid):
	print_grid(grid)

else:
	print("No Soln")