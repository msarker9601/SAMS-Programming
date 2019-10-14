### SAMS Senior CS-Track Hw4
### Due Date: Friday 07/26 8:30pm
### Name: Muhaimin Sarker
### andrewID: msarker

# Write code in each of the functions below such that they fulfill the
# instructions. You can run the file to test your code against the test cases
# at the bottom.

# Starting this week, you will need to write some test cases yourself to
# check your code! You can add them to the test functions at the bottom.

# Submit your work on Autolab. Autolab may contain additional test cases,
# so don't hard-code your solutions. We will manually grade any code that
# does not have tests, or does not pass the test cases on Autolab.

### Problem 1: Console Interaction ###

"""
Write an interactive function, averageRainfall(), which takes no parameters and
calculates the average rainfall based on entries made by the user. The program
should repeatedly ask the user to input a rainfall amount, and collect the
user's answers. When the user enters the number -999, that is a signal that the
entry is done, and the program should stop collecting numbers. At that point,
the program should average all the valid rainfall entries and print out the
result. An entry is only valid if it is a non-negative number.
"""
def averageRainfall():
    averageRain= int(input("Input rain fall: "))
    if (averageRain==-999):
        print("Average rainfall: 0")
        return
    term= 1
    while (True):
        try:
            userInput = int(input("Input rain fall: "))
            if (userInput<0):
                if (userInput==-999):
                    averageRain/=term
                    break
                print("STOP PUTTING NEGATIVE NUMBERS")
                term-=1
            else: 
                averageRain+=userInput
            term+=1 
        except:
            print("ENTER A NUMBER!!!!")
    print("Average rainfall: " + str(averageRain))
    return
        
        


### Problem 2: Interactive Graphics ###

"""
Program an interactive Sudoku game using Tkinter graphics. If you have never
played Sudoku before, try it out here: http://www.logicgamesonline.com/sudoku/

This problem comes in three parts. We strongly recommend you complete them in 
order, to make your life easier!

For additional clarification, you may wish to view an online writeup of the 
problem here: http://www.krivers.net/15112-f18/notes/hw5.html

STEP 1
Build an interactive Sudoku board using the framework below the # GRAPHICS CODE 
line. You can design your game as you wish, but it should meet the following 
requirements:

 - The game must start by displaying the full 9x9 grid (in the format of a 
   standard Sudoku board) and filling in the numbers already included in the 
   starter board. We include two starter boards below for testing. Note that
   in our starter boards, a 0 represents a blank space.
   
board1 = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]

board2 = [
  [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [ 5, 0, 8, 1, 3, 9, 6, 2, 4],
  [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
  [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
  [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
  [ 3, 8, 7, 5, 6, 4, 0, 9, 1],
  [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
  [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
  [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
]

 - At all times, a single cell on the board is highlighted (using either a 
   different color or different outline than the rest of the cells). The player 
   can change the highlighted cell by clicking on a new cell, or by moving from 
   the current cell with the up, down, left, and right arrows.

 - To make a move, the player can press a single digit key to insert a number 
   into an empty square. The player can also clear the number from the 
   highlighted square by pressing the backspace key.
   
 - Initial numbers (squares that were filled in before game play began) should 
   be a different color than numbers added by a player. In addition, the player 
   cannot modify initial numbers.


STEP 2
Fill in the five functions listed below (areLegalValues, isLegalRow, isLegalCol,
isLegalBlock, and isLegalSudoku) to test whether a given Sudoku board is legal.
Each function has its own set of requirements listed above the function.

Hint: you should use areLegalValues in isLegalRow/isLegalCol/isLegalBlock,
and you should use those three isLegals in isLegalSudoku!


STEP 3
Update your interactive graphics code to use your Sudoku legality checking code,
which will make the game playable. You'll need to add the following features:

 - The user should only be allowed to enter a number if it will still result in 
   a valid board, as determined by isLegalSudoku.

 - If, after a move, the player has properly filled in the entire board and won 
   the game, a message should be displayed congratulating the player. After 
   this, all further keypresses and mouse presses should be ignored.

Get creative, and have fun!
"""


"""
This function takes a 1D list of values. These values may be extracted from any 
given row, column, or block in a Sudoku board. The function returns True if the 
values are legal: that is, if every value is an integer between 0 and 9, 
inclusive, and if each integer from 1 to 9 occurs at most once in the given 
list (0 may be repeated, of course).
"""
def areLegalValues(values):
    for i in range(len(values)):
        if (values[i]>=10 or values[i]<0):
            return False
        if (type(values[i])!=int):
            return False
    for k in range(1,10):
        if (values.count(k)>1):
            return False
    return True
"""
This function takes a Sudoku board and a row number. The function returns True 
if the given row in the given board is legal (where row 0 is the top row and 
row 8 is the bottom row), and False otherwise.
"""
def isLegalRow(board, row):
    return areLegalValues(board[row])

"""
This function takes a Sudoku board and a column number. The function returns 
True if the given column in the given board is legal (where col 0 is the left 
column and col 8 is the right column), and False otherwise.
"""
def isLegalCol(board, col):
    coldata= []
    for i in range(len(board)):
        coldata.append(board[i][col])
    return areLegalValues(coldata)

"""
This function works just like isLegalRow and isLegalCol, only for blocks. In a
Sudoku board, we'll label the blocks as follows, where each block is a 3x3 grid:

0 1 2
3 4 5
6 7 8

So Block 0 is the top-left block, and block numbers proceed across, then down.
For additional clarification, see this writeup:
http://www.krivers.net/15112-f18/notes/hw5.html

Hint: use div and mod to find the starting row and col for each block!
"""
def isLegalBlock(board, block):
    startRow= (block//3)*3
    startCol= (block%3)*3
    blockdata= []
    for k in range(startRow, startRow+3):
        for i in range(startCol, startCol+3):
            blockdata.append(board[k][i])
    return areLegalValues(blockdata)

"""
This function takes a Sudoku board (which you may assume is a 9x9 2D list of 
integers), and returns True if the board is legal. A Sudoku board is legal if
every row, column, and block in the board is legal.
"""
def isLegalSudoku(board):
    for i in range(9):
        if (isLegalBlock(board,i)==True and isLegalCol(board,i)==True and isLegalRow(board,i)==True):
            return True
        else:
            return False
    
        

######################################################################
# GRAPHICS CODE
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *

def init(data):
    data.grid= [
            [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
           ]
    data.colors= [
            [ "red", "red", "red", "green", "green", "green", "blue", "blue", "blue" ],
            [ "red", "red", "red", "green", "green", "green", "blue", "blue", "blue" ],
            [ "red", "red", "red", "green", "green", "green", "blue", "blue", "blue" ],
            [ "yellow", "yellow", "yellow", "purple", "purple", "purple", "orange", "orange", "orange" ],
            [ "yellow", "yellow", "yellow", "purple", "purple", "purple", "orange", "orange", "orange" ],
            [ "yellow", "yellow", "yellow", "purple", "purple", "purple", "orange", "orange", "orange" ],
            [ "white", "white", "white", "gray", "gray", "gray", "brown", "brown", "brown" ],
            [ "white", "white", "white", "gray", "gray", "gray", "brown", "brown", "brown" ],
            [ "white", "white", "white", "gray", "gray", "gray", "brown", "brown", "brown" ]
           ]
    
    data.buttonX, data.buttonY = data.width/9, data.height/9
    data.buttonClicked = False
    data.buttonSize= 81
    data.prevColor=''
    
def mousePressed(event, data):
    for row in range(9):
        for col in range(9):
            if data.colors[row][col]=="aqua":
                data.colors[row][col]=data.prevColor
    col= event.x//(data.width//9)
    row= event.y//(data.height//9)
    data.prevColor= data.colors[row][col]
    data.colors[row][col]= "aqua"
    
    
def keyPressed(event, data):
    pass
def redrawAll(canvas, data):
    fillNumber=0
    for row in range(9):
        for col in range(9):
            fillNumber+=1
            newHeight = row*(data.width/9) #Takes the value of the row and multiplies it
            newWidth = col*(data.width/9) #Takes the value of the column and multiples it
            canvas.create_rectangle(newWidth, newHeight, newWidth + (data.width/9), newHeight + (data.width/9), fill= data.colors[row][col])
            if (data.grid[row][col]!=0):
                canvas.create_text(((2*newWidth+(data.width/9))/2), ((2*newHeight+(data.height/9))/2), text=data.grid[row][col], font="Arial 20 bold")
def runSudoku(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)    
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        redrawAllWrapper(canvas, data)
        mousePressed(event, data)
        

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed


######################################################################
# TEST CODE
######################################################################

def testAverageRainfall():
    print("Testing averageRainfall()...", end="")
    averageRainfall()
    print("Done with these calculations")
def getBasicBoard():
    return [
            [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
           ]
def getNewBoard():
    return [
            [ 1, 1, 1, 0, 0, 9, 4, 0, 0 ],
            [ 1, 1, 1, 20, 10, 9, 4, 0, 0 ],
            [ -5, 6, 7, -20, 10, 9, 4, 6, 0],
            [ 5, 90, 5, '', 10, 9, 4, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
           ]

def testAreLegalValues():
    print("Testing areLegalValues()...", end="")
    for i in range(len(getBasicBoard())):
        print(i)
        assert(areLegalValues(getBasicBoard()[i]) == True)
    print("Done testing basic board")
    for i in range(4):
        print(i)
        assert(areLegalValues(getNewBoard()[i]) == False)
    print("WROTE THEM CASES for areLegalValues!")
    print()
    

def testIsLegalRow():
    print("Testing isLegalRow()...", end="")
    for i in range(len(getBasicBoard())):
        print(i)
        assert(isLegalRow(getBasicBoard(), i) == True)
    print("Done testing basic board")
    for i in range(4):
        print(i)
        assert(isLegalRow(getNewBoard(), i) == False)
    print("HAHA TESTED EVERYTHING!!!! for those ROWS")
    print()

def testIsLegalCol():
    print("Testing isLegalCol()...", end="")
    for i in range(len(getBasicBoard())):
        print(i)
        assert(isLegalCol(getBasicBoard(), i) == True)
    print("Done testing basic board")
    for i in range(6):
        print(i)
        assert(isLegalCol(getNewBoard(), i) == False)
    print("COLUMNS ARE NO PROBLEM SINCE I PASSED ALL THEM TESTS")
    print()

def testIsLegalBlock():
    print("Testing isLegalBlock()...", end="")
    for i in range(len(getBasicBoard())):
        print(i)
        assert(isLegalBlock(getBasicBoard(), i) == True)
    print("Done testing basic board")
    for i in range(3):
        print(i)
        assert(isLegalBlock(getNewBoard(), i) == False)
    print("Passed the block tests. Sudoku tests are incoming")
    print()

def testIsLegalSudoku():
    print("Testing isLegalSudoku()...", end="")
    assert(isLegalSudoku(getBasicBoard()) == True)
    assert(isLegalSudoku(getNewBoard())==False)
    print("Sudoku  tests were passed. It was a joint effort from helper functions")
def testSudokuAnimation():
    print("Running Sudoku Animation...", end="")
    # Feel free to change the width and height!
    width = 540
    height = 540
    runSudoku(width, height)
    print("Done.")

def testAll():
    # 1
    testAverageRainfall()
    # 2
    testSudokuAnimation()
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testIsLegalBlock()
    testIsLegalSudoku()

testAll()