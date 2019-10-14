### SAMS Senior CS-Track Hw5
### Due Date: Monday 08/05 8:30pm
### Name:
### andrewID:

# Use the guidelines at the following website to implement the game Tetris.
# http://krivers.net/15112-s19/notes/notes-tetris/index.html

# If you finish before the deadline, consider adding bonus features for
# additional points! If you choose to do this, please submit the core Tetris
# implementation on Autolab under hw5, then submit the bonus implementation
# under hw5-bonus.

### Problem 1: Tetris ###

"""
Follow the instructions here:
http://krivers.net/15112-s19/notes/notes-tetris/index.html

Note that we already set up the starter code and wrote gameDimensions() for you.
"""

from tkinter import *
import random

def playTetris():
    run(300,350)
    #15*20 + 25*2 = 350
    #10*20 + 25*2= 300
def gameDimensions():
    # rows, cols, cellSize, margin
    return [15, 10, 20, 25]

def init(data):
    data.score=0
    data.sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]
    data.iPiece = [
        [  True,  True,  True,  True ]
    ]
    data.jPiece = [
            [  True, False, False ],
            [  True,  True,  True ]
        ]
    data.lPiece = [
            [ False, False,  True ],
            [  True,  True,  True ]
        ]
    data.oPiece = [
            [  True,  True ],
            [  True,  True ]
        ]
    data.tPiece = [
            [ False,  True, False ],
            [  True,  True,  True ]
        ]
    data.zPiece = [
            [  True,  True, False ],
            [ False,  True,  True ]
        ]
    tetrisPieces = [ data.iPiece, data.jPiece, data.lPiece, data.oPiece, data.sPiece, data.tPiece, data.zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]
    data.tetrisPieces = tetrisPieces
    data.tetrisPieceColors = tetrisPieceColors
    gameDimensions();
    data.emptyColor= "blue";
    # pre-load a few cells with known colors for testing purposes
    data.board= []
    data.gameOver= False
    data.rows=gameDimensions()[0]
    data.cols=gameDimensions()[1]
    data.cellSize=gameDimensions()[2]
    data.margin= gameDimensions()[3]
    temp= []
    for row in range(data.rows):
        colorCol= [data.emptyColor]*data.cols
        temp.append(colorCol)
    data.board= temp
    newFallingPiece(data)
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if data.gameOver==False:
        if event.keysym=="Left":
            moveFallingPiece(data,0,-1)
        if event.keysym=="Up":
            rotateFallingPiece(data)
        elif event.keysym=="Down":
            moveFallingPiece(data,1,0)
        elif event.keysym=="Right":
            moveFallingPiece(data,0,1)
    if event.keysym=="r":
        init(data)
def timerFired(data):
    if data.gameOver==False:
        if moveFallingPiece(data,1,0)==False:
            placeFallingPiece(data)
            newFallingPiece(data)
            if (fallingPieceisLegal(data)==False):
                data.gameOver=True

def redrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height, fill= "orange")
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    drawScore(canvas,data)
    if data.gameOver==True:
        canvas.create_rectangle(data.margin,data.margin,data.width-data.margin,data.height-data.margin,fill="white",width=0)
        canvas.create_text(data.width/2, data.height/2, font= "Times 33 italic bold", text= "Lost at Tetris!")
def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col, data.board[row][col])
def drawCell(canvas, data, row, col, color):
    newWidth= data.width-(2*data.margin)
    newHeight= data.height-(2*data.margin)
    canvas.create_rectangle(data.margin+((newWidth/data.cols)*col), data.margin+((newHeight/data.rows)*row), data.margin+((newWidth/data.cols)*(col+1)), data.margin+((newHeight/data.rows)*(row+1)), fill= color, width= 2.5)
def newFallingPiece(data):
    import random
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    data.fallingPiece= data.tetrisPieces[randomIndex]
    data.fallingPieceColor= data.tetrisPieceColors[randomIndex]
    data.fallingPieceRow=0
    data.fallingPieceCol= int(data.cols/2-(len(data.fallingPiece[0])/2))
def drawFallingPiece(canvas, data):
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            if (data.fallingPiece[row][col]):
                drawCell(canvas, data, data.fallingPieceRow + row, data.fallingPieceCol + col, data.fallingPieceColor)
def moveFallingPiece(data, drow, dcol):
    data.fallingPieceRow+=drow
    data.fallingPieceCol+=dcol
    if (fallingPieceisLegal(data)):
        return  True
    else:
        data.fallingPieceRow-=drow
        data.fallingPieceCol-=dcol
        return False

def fallingPieceisLegal(data):
    for newrow in range(len(data.fallingPiece)):
        for newcol in range(len(data.fallingPiece[0])):
            #Trying to check if each fallingPiece is at a legal place (aka in the board)
            if (data.fallingPiece[newrow][newcol]==True):
                if (data.fallingPieceRow+newrow<0 or data.fallingPieceCol+newcol<0 or data.fallingPieceRow+newrow>data.rows-1 or data.fallingPieceCol+newcol>data.cols-1 or data.board[data.fallingPieceRow+newrow][data.fallingPieceCol+newcol]!=data.emptyColor):
                        return False
    return True
def rotateFallingPiece(data):
    oldPiece= data.fallingPiece
    oldRow= len(data.fallingPiece)
    oldCol=len(data.fallingPiece[0])
    oldFallingRow= data.fallingPieceRow
    oldFallingCol= data.fallingPieceCol
    newRow= []
    for row in range(oldCol):
        temp=[]
        for col in range(oldRow):
            temp.append(None)
        newRow.append(temp)
    for br in range(oldRow):
        for uh in range(oldCol):
            newRow[len(newRow)-1-uh][br]= data.fallingPiece[br][uh]
    data.fallingPiece= newRow
    if (fallingPieceisLegal(data)==False):
        data.fallingPiece= oldPiece
        data.fallingPieceRow= oldFallingRow
        data.fallingCol=oldFallingCol
def placeFallingPiece(data):
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            if data.fallingPiece[row][col]:
                data.board[data.fallingPieceRow+row][data.fallingPieceCol+col]= data.fallingPieceColor
    removeRows(data)
def removeRows(data):
    for row in range(len(data.board)):
        if data.board[row].count("blue")==0:
            data.board[row]= [data.emptyColor]*data.cols
            for bruh in range(len(data.board)-1):
                if (bruh!=row):
                    data.board[bruh]=data.board[bruh+1]
                if (bruh==row):
                    data.board[bruh]= data.board[bruh-1]
            data.score+=1
def drawScore(canvas,data):
    canvas.create_text(data.margin/2, data.margin/2, font= "Times 33 italic bold", text= str(data.score))





####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
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
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

playTetris()