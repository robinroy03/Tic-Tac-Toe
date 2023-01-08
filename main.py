# tic tac toe

import tkinter

root = tkinter.Tk()

x_or_y = 'X'    # starting with X
draw = 0        # if 9 then game is draw

def win():
    x = ['X','X','X']
    o = ['O','O','O']

    # 'X' linearly
    
    if [b1['text'],b2['text'],b3['text']] == x:
        tkinter.Message(root, text = "X Won", bg="green").grid()
    elif [b4['text'],b5['text'],b6['text']] == x:
        tkinter.Message(root, text = "X Won", bg="green").grid()
    elif [b7['text'],b8['text'],b9['text']] == x:
        tkinter.Message(root, text = "X Won", bg="green").grid()
    
    #'O' linearly
    
    elif [b1['text'],b2['text'],b3['text']] == o:
        tkinter.Message(root, text = "O Won", bg="green").grid()
    elif [b4['text'],b5['text'],b6['text']] == o:
        tkinter.Message(root, text = "O Won", bg="green").grid()
    elif [b7['text'],b8['text'],b9['text']] == o:
        tkinter.Message(root, text = "O Won", bg="green").grid()
    
    # 'X' vertically
    
    elif [b1['text'],b4['text'],b7['text']] == x:
        tkinter.Message(root, text = "X Won", bg="green").grid()
    elif [b2['text'],b5['text'],b8['text']] == x:
        tkinter.Message(root, text = "X Won", bg="green").grid()
    elif [b3['text'],b6['text'],b9['text']] == x:
        tkinter.Message(root, text = "X Won", bg="green").grid()
    
    # 'O' vertically
    
    elif [b1['text'],b4['text'],b7['text']] == o:
        tkinter.Message(root, text = "O Won", bg="green").grid()
    elif [b2['text'],b5['text'],b8['text']] == o:
        tkinter.Message(root, text = "O Won", bg="green").grid()
    elif [b3['text'],b6['text'],b9['text']] == o:
        tkinter.Message(root, text = "O Won", bg="green").grid()

    # 'X' diagonally

    elif [b1['text'],b5['text'],b9['text']] == x:
        tkinter.Message(root, text = "X Won", bg="green").grid()
    elif [b3['text'],b5['text'],b7['text']] == x:
        tkinter.Message(root, text = "X Won", bg="green").grid()

    # 'O' diagonally

    elif [b1['text'],b5['text'],b9['text']] == o:
        tkinter.Message(root, text = "O Won", bg="green").grid()
    elif [b3['text'],b5['text'],b7['text']] == o:
        tkinter.Message(root, text = "O Won", bg="green").grid()

    elif draw == 9:
        tkinter.Message(root, text = "Game is a draw :(", bg="blue").grid(columnspan=3)

def click(b):   
    global x_or_y, draw

    b['text'] = x_or_y
    if x_or_y == "X":
        x_or_y = "O"
    else:
        x_or_y = "X"
    
    b["state"] = "disabled"
    
    draw += 1
    win()

# buttons

b1 = tkinter.Button(root, text = " ", height = 3, width = 6, command = lambda: click(b1))
b2 = tkinter.Button(root, text = " ", height = 3, width = 6, command = lambda: click(b2))
b3 = tkinter.Button(root, text = " ", height = 3, width = 6, command = lambda: click(b3))

b4 = tkinter.Button(root, text = " ", height = 3, width = 6, command = lambda: click(b4))
b5 = tkinter.Button(root, text = " ", height = 3, width = 6, command = lambda: click(b5))
b6 = tkinter.Button(root, text = " ", height = 3, width = 6, command = lambda: click(b6))

b7 = tkinter.Button(root, text = " ", height = 3, width = 6, command = lambda: click(b7))
b8 = tkinter.Button(root, text = " ", height = 3, width = 6, command = lambda: click(b8))
b9 = tkinter.Button(root, text = " ", height = 3, width = 6, command = lambda: click(b9))

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)

b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)

b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)

root.mainloop()