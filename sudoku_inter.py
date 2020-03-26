from tkinter import *
from sudoku_api import get_grid,solve
from sudoku_solver import solver,if_poss


root=Tk()

canvas=Canvas(root,height=500,width=450)
canvas.pack()
board=[[0 for i in range(9)] for j in range(9)]
def get(event):
	return (event.widget.get())
# entry1=Entry(root)
# mylabel = canvas.create_text((25,25),text="1")
# my_entry=canvas.create_window((75,75),height=50,width=50,window=entry1)
# entry1.bind('<Return>',get)
def create_board(grid):
	global canvas
	global root
	global board
	board=grid
	entries=user_inps=[[0 for i in range(9)] for j in range(9)]
	user_inps=[[0 for i in range(9)] for j in range(9)]
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
	solve_button=Button(canvas,text="SOLVE!!!",font="Times 20 bold")
	canvas.create_window((225,475),height=50,width=450,window=solve_button)
	solve_button.bind("<Button-1>",get_solved)
	
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




# num=Label(canvas,text="1")
# num.pack()





# for i in range(1,9):
# 	canvas.create_line(0,i*50,450,i*50)

# for i in range(1,9):
# 	canvas.create_line(i*50,0,i*50,450)

# entry1=Entry(root)
# mylabel = canvas.create_text((25,25),text="1")
# my_entry=canvas.create_window((75,75),height=50,width=50,window=entry1)
# entry1.bind('<Return>',get)









# frame=Frame(root,width=200,height=200)
# frame.pack()
# diff_label=Label(frame,text="Select Difficulty")
# diff_label.pack()

# easy_button.pack()
# med_button.pack()
# hard_button.pack()

root.mainloop()