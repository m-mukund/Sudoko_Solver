import requests
import sudoku_solver

	
def solve(grid):
	if sudoku_solver.solver(grid):
		print_grid(grid)

	else:
		print("No Soln")

def print_grid(grid):
	for i in range(9):
		print(grid[i])

def get_grid(difficulty):

	heads={"size":9, "level":difficulty}
	url="http://www.cs.utep.edu/cheon/ws/sudoku/new/"
	response=requests.get(url,params=heads)
	data=response.json()
	grid=[[0 for i in range(9)] for j in range(9)]


	if data["response"]:
		values=data["squares"]
		for one in values:
			r=one["x"]
			c=one["y"]
			grid[r][c]=one["value"]

	return grid

# string=""
# for i in range(9):
# 	for j in grid[i]:
# 		if j==0:
# 			string+="| |"
# 		else:
# 			string+="|"
# 			string+=str(j)
# 			string+="|"
# 	string+="\n"

# print(string)
# print("Press enter to solve")
# input()
# solve(grid)