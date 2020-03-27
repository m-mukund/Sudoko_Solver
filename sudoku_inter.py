from tkinter import *
from sudoku_api import get_grid,solve
from sudoku_solver import solver,if_poss
import tkinter.messagebox

root=Tk()
entries=user_inps=[[0 for i in range(9)] for j in range(9)]
canvas=Canvas(root,height=500,width=450)
canvas.pack()
board=[[0 for i in range(9)] for j in range(9)]
def get(event):
	return (event.widget.get())

#Create GUI

def create_board(grid):
	global canvas
	global root
	global board
	board=grid
	global entries
	canvas.delete("all")
	for i in range(9):
		canvas.create_line(0,i*50,450,i*50)
		canvas.create_line(i*50,0,i*50,450)
	for i in range(9):
		for j in range(9):
			if grid[i][j]==0:
				entry=Entry(root)
				entries[i][j]=entry
				canvas.create_window(((25+50*j),(25+50*i)),height=50,width=50,window=entry)
			else:
				canvas.create_text(((25+50*j),(25+50*i)),text=str(grid[i][j]))
	check_button=Button(canvas,text="CHECK!!!",font="Times 20 bold")
	solve_button=Button(canvas,text="SOLVE!!!",font="Times 20 bold")
	canvas.create_window((122,475),height=50,width=225,window=solve_button)
	canvas.create_window((347,475),height=50,width=225,window=check_button)
	solve_button.bind("<Button-1>",get_solved)
	check_button.bind("<Button-1>",check_correct)

def check_correct(event):
	global board
	global entries
	global canvas
	for i in range(9):
		for j in range(9):
			if board[i][j]==0:
				if entries[i][j].get():
					board[i][j]=int(entries[i][j].get())
				else:
					board[i][j]=0
	if is_correct(board):
		tkinter.messagebox.showinfo("Congratulations!!!!","You have completed the sudoku!!!")
		canvas.delete("all")
		for i in range(9):
			canvas.create_line(0,i*50,450,i*50)
			canvas.create_line(i*50,0,i*50,450)
		for i in range(9):
			for j in range(9):
				canvas.create_text(((25+50*j),(25+50*i)),text=str(board[i][j]))
		check_button=Button(canvas,text="CHECK!!!",font="Times 20 bold")
		solve_button=Button(canvas,text="SOLVE!!!",font="Times 20 bold")
		canvas.create_window((122,475),height=50,width=225,window=solve_button)
		canvas.create_window((347,475),height=50,width=225,window=check_button)
	else:
		tkinter.messagebox.showinfo("SORRY!!!!","That is not correct!!!")

def is_correct(grid):
	for i in range(9):
		for j in range(9):
			if grid[i][j]==0:
				return False
			if not if_poss(grid,i,j,grid[i][j]):
				return False
	return True
	
def get_solved(event):
	global board
	global canvas
	solver(board)
	canvas.delete("all")
	for i in range(9):
		canvas.create_line(0,i*50,450,i*50)
		canvas.create_line(i*50,0,i*50,450)
	for i in range(9):
		for j in range(9):
			canvas.create_text(((25+50*j),(25+50*i)),text=str(board[i][j]))



def easy(event):
	grid=get_grid(1)
	create_board(grid)

def medium(event):
	grid=get_grid(2)
	create_board(grid)

def hard(event):
	grid=get_grid(3)
	create_board(grid)

#Select Difficult

canvas.create_text((220,75),text="Select Difficulty",font="Times 20 bold")

easy_button=Button(canvas,text="Easy",font="Times 20 bold")
med_button=Button(canvas,text="Medium",font="Times 20 bold")
hard_button=Button(canvas,text="Hard",font="Times 20 bold")

canvas.create_window((220,125),height=40,width=200,window=easy_button)
canvas.create_window((220,205),height=40,width=200,window=med_button)
canvas.create_window((220,285),height=40,width=200,window=hard_button)

easy_button.bind("<Button-1>",easy)
med_button.bind("<Button-1>",medium)
hard_button.bind("<Button-1>",hard)



root.mainloop()