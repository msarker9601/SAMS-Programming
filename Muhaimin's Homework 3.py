### SAMS Senior CS-Track Hw3
### Due Date: Friday 07/19 8:30pm
### Name:
### andrewID:

# Write code in each of the functions below such that they fulfill the
# instructions. You can run the file to test your code against the test cases
# at the bottom.

# Starting this week, you will need to write some test cases yourself to
# check your code! You can add them to the test functions at the bottom.

# Submit your work on Autolab. Autolab may contain additional test cases,
# so don't hard-code your solutions. We will manually grade any code that
# does not have tests, or does not pass the test cases on Autolab.

### Problem 1: Strings ###

"""
Write the function sameChars(s1, s2) that takes two strings and returns True if 
the two strings are composed of the same characters (though perhaps in 
different numbers and in different orders) -- that is, if every character that 
is in the first string, is in the second, and vice versa -- and False otherwise.
This test is case-sensitive, so "ABC" and "abc" do not contain the same 
characters.
"""

def sameChars(s1, s2):
    evaluation= 0
    for i in range(len(s1)):
        if not s1[i] in s2:
            return False
    for k in range(len(s2)):
        if not s2[k] in s1:
            return False
    return True

"""
Assume you're provided a string script that has been formatted in a specific 
way. Each line of the script begins with a character's name, followed by a 
colon, followed by their line of dialogue. Lines are separated by newlines, 
which are represented in Python by the string '\n'.
For example:

'''
Buttercup: You mock my pain.
Man in Black: Life is pain, Highness.
Man in Black: Anyone who says differently is selling something.
'''

Write the function getCharacterLines(script, character), which takes a 
script and a character name (both strings) and returns a list of the lines
spoken by that character. The lines should be stripped of the leading
character name and any leading/trailing whitespace. 
So if we use the following script:

'''
Burr: Can I buy you a drink?
Hamilton: That would be nice.
Burr: While we're talking, let me offer you some free advice: talk less.
Hamilton: What?
Burr: Smile more.
Hamilton: Ha.
Burr: Don't let them know what you're against or what you're for.
Hamilton: You can't be serious.
Burr: You want to get ahead?
Hamilton: Yes.
Burr: Fools who run their mouths oft wind up dead.
'''

Then:

getCharacterLines(script, "Hamilton") == [ "That would be nice.",
    "What?", "Ha.", "You can't be serious.", "Yes." ]
"""
def getCharacterLines(script, character):
    charLines= []
    betterScript=script.splitlines()
    for i in range(len(betterScript)):
        if character in betterScript[i]:
            newLine= betterScript[i].split(character +": ")
            charLines.append(newLine[1])
    return charLines
    
### Problem 2: Lists ###
"""
Write the function vectorSum(a,b) that takes two same-length lists of numbers,
a and b, and returns a new list c where c[i] is the sum of a[i] and b[i]. 
For example, vectorSum([2, 4], [20, 30]) returns [22, 34].
"""
def vectorSum(a, b):
    c=[]
    for i in range(len(a)):
        sum=a[i]+b[i]
        c.append(sum)
    return c
    

"""
Write the function histogram(grades) which takes a list of integers between
0-99 (a set of grades) and returns a string-histogram that buckets the grades
into groups of 10. For example, histogram([73, 62, 91, 74, 99, 77]) returns 
this multi-line string:

'''
60-69: *
70-79: ***
80-89:
90-99: **
'''

Note that the histogram should start with the first bucket that actually has a
value, and end with the last bucket that actually has a value. So
histogram([75, 20, 73, 50]) would return:

'''
20-29: *
30-39:
40-49:
50-59: *
60-69:
79-79: **
'''

"""
def histogram(grades):
    histoString= '''
    ''' #I'm trying to make it so that it starts at a new line
    greater= grades[0]
    less= grades[0]
    for i in range(len(grades)):
        if grades[i]>0 or grades[i]<100:
            return ""
    for i in range(len(grades)):
        if (grades[i]>greater):
            greater= grades[i]
        if (grades[i]<less):
            less= grades[i]
    rangeGreater= int(greater)//10
    rangeLess= int(less)//10
    for b in range(rangeLess,rangeGreater):
        lower= str(b*10)
        upper= str((b*10)+9)
        histoString+=lower+"-"+upper+":  "
        for k in range(len(grades)):
            if grades[k]>int(lower) or grades[k]<=int(upper):
                    histoString+="*"
        histoString+="\n"
    print(histoString)
    #Lets use //10 to find the thing that it starts with and then use the a for loop with that range
    

### Problem 3: 2D Lists ###

"""
Write the function nondestructiveRemoveRowAndCol(lst, row, col) that takes a 2D 
list lst, a row index, and a col index, and returns a new 2D list with the given 
row and column removed. So, if:

lst = [ [ 2, 3, 4, 5],
            [ 8, 7, 6, 5],
            [ 0, 1, 2, 3]
        ]

then nondestructiveRemoveRowAndCol(lst, 1, 2) would return the list

[ [ 2, 3, 5],
  [ 0, 1, 3]
]

This function is non-destructive, so the inputted list must not be changed.
You may assume the row and col are legal, in that they are non-negative integers 
no larger than the largest row and col index, respectively.
"""

def nondestructiveRemoveRowAndCol(lst, row, col):
    newLst= []
    for newrow in range(len(lst)):
        temp= []
        for newcol in range(len(lst[0])):
            if newrow!=row and newcol!=col:
                temp.append(lst[newrow][newcol])
            else:
                temp=None;
        newLst.append(temp)
    return newLst

"""
Now write destructiveRemoveRowAndCol, which is exactly like
nondestructiveRemoveRowAndCol, except that it is destructive. Instead of 
returning a list, it should modify the input list (lst) and return None.
"""

def destructiveRemoveRowAndCol(lst, row, col):
    for newrow in range(len(lst)):
        for newcol in range(len(lst[newrow])):
            if newrow==row or newcol==col:
                lst.remove(lst[newrow][newcol])
    return lst

### Note that Problem 3 continues in the graphics section ###


### Problem 4: Objects ###

"""
Choose a sport that is interesting to you. Common examples include soccer, 
baseball, football, hockey, basketball, rugby, cricket, ultimate, quidditch, 
and more! Write a Player class for that sport that has a constructor, at least
two properties, and at least two methods appropriate for an athlete playing 
that sport. Then write test code in testPlayer that creates at least two 
different Players and tests your methods and properties.

All properties and methods should be clearly named so that someone else would 
immediately understand their purpose and see its relevance to the class. If 
needed, feel free to add comments further explaining the purpose of a method or 
property. Get creative, and have fun!
"""

# Sport: 
class Player(object):
    def _init_(self,name):
        self.name= name
        self.threeprobability= len(name) *10
        self.twoprobability= len(name)*20
    def shoot(three, two):
        numThree=0
        numTwo= 0
        for i in range(three):
            if randint(0,100)<=self.threeprobability:
                numThree+=1
        for i in range(two):
            if randint(0,100)<=self.threeprobability:
                numTwo+=1
        #The randint makes it so that if the randomized thing is less than your probability, you get a 3 :D 
        print("I made"+ numThree+ "three-pointers")
        print("I made"+ numTwo+ "two-pointers")
    def points(street, numThree,numTwo):
        #Street ball makes 3 pointers 2 points and 2 pointers 1 point
        if numThree<0:
            numThree=0
        if numTwo<0:
            numTwo=0
        if street:
            numPoints= (numThree*2)+(numTwo*2)
        else:
            numPoints= (numThree*2)+(numTwo*2)
        return numPoints
def testPlayerClass():
    player1= Player("John")
    assert(player1.threeProbability== 40)
    assert(player1.twoProbability==60)
    assert(player1.points(True,3,2)==8)
    assert(player1.points(False,3,2)==13)
    player2= Player("Muhaimin")
    assert(player2.threeProbability==80)
    assert(player2.twoProbability==160)
    #I did this on purpose! :D
    assert(player1.points(True,50,2)==102)
    assert(player1.points(False, -1,-1)==0)
    
    

######################################################################
# GRAPHICS CODE
# ignore_rest: The autograder will ignore all code below here
######################################################################

### Problem 3 continued ###
from tkinter import *

"""
Write the function drawAsciiArt(canvas, width, height, artStr) which takes a 
string holding a piece of ascii art and draws that ascii art sized such that it
fits on the given canvas.

In a piece of ascii art, each character can be thought of as an oversized pixel
in the canvas. Each character will be either a newline, a space, or a number
from 0-7. A newline '\n' tells the ascii art to move on to the next line (or row
of pixels). A space represents a pixel that is left blank. The numbers 0-7 are
then used as standins for seven different colors:

Decimal value    Binary value    #RGB string    Color
0                000             #000           "black"
1                001             #00F           "blue"
2                010             #0F0           "green1"
3                011             #0FF           "cyan"
4                100             #F00           "red"
5                101             #F0F           "magenta"
6                110             #FF0           "yellow"
7                111             #FFF           "white"

Each pixel's height and width should be the same, where the height is determined
by the height of the canvas and the number of rows, while the width is
determined by the width of the canvas and the length of the longest row.

You can find several examples of ascii art strings and graphics here: 
http://www.krivers.net/15112-s19/notes/hw3.html
"""
    
def drawAsciiArt(canvas, width, height, artStr):
    return

######################################################################
# TEST CODE
######################################################################

def testSameChars():
    print("Testing sameChars()...", end="")
    assert(sameChars("heart", "earth") == True)
    assert(sameChars("tooth", "hot") == True)
    assert(sameChars("tooth", "too") == False)
    assert(sameChars("earth", "EARTH") == False)
    assert(sameChars("123", "312")==True)
    assert(sameChars("false", "safe")==False)
    assert(sameChars("", " ")==False)
    assert(sameChars("selfish", "fishesl")==True)
    print("Passed! (HAHA I ADDED MORE TEST CASES!!!!!)")

def testGetCharacterLines():
    print("Testing getCharacterLines()...", end="")
    s1 = '''
Buttercup: You mock my pain.
Man in Black: Life is pain, Highness.
Man in Black: Anyone who says differently is selling something.
'''
    print(getCharacterLines(s1, "Buttercup"))
    assert(getCharacterLines(s1, "Buttercup") == [ "You mock my pain." ])
    assert(getCharacterLines(s1, "Man in Black") == [ "Life is pain, Highness.",
        "Anyone who says differently is selling something." ])
        
    
    s2 = '''
Burr: Can I buy you a drink?
Hamilton: That would be nice.
Burr: While we're talking, let me offer you some free advice: talk less.
Hamilton: What?
Burr: Smile more.
Hamilton: Ha.
Burr: Don't let them know what you're against or what you're for.
Hamilton: You can't be serious.
Burr: You want to get ahead?
Hamilton: Yes.
Burr: Fools who run their mouths oft wind up dead.
'''
    assert(getCharacterLines(s2, "Hamilton") == [ "That would be nice.",
        "What?", "Ha.", "You can't be serious.", "Yes." ])    
    print("Passed! (OH YEAH I WROTE TEST CASESSSSSSSSS)")

def testVectorSum():
    print("Testing vectorSum()...", end="")
    assert(vectorSum([2, 4], [20, 30]) == [22, 34])
    assert(vectorSum([1, 2, 3], [4, 5, 6]) == [5, 7, 9])
    assert(vectorSum([-1], [4]) == [3])
    assert(vectorSum([], []) == [])
    print("Passed! (EZ TO MAKE TESTS!!!!!)")

def testHistogram():
    print("Testing histogram()... check the text to see if it looks right", end="")
    print(histogram([73, 62, 91, 74, 99, 77]))
    print(histogram([0,100,500,20]))
    print(histogram([75, 20, 73, 50]))
    print(histogram([60,20,50,77,55]))
    print(histogram([1,11,22,57,99]))
    print(histogram([10,20,30,40,50]))
    print("Passed! (HISTODONE MAKING THEM TESTS)")

def testNondestructiveRemoveRowAndCol():
    print('Testing nondestructiveRemoveRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5], [ 8, 7, 6, 5], [ 0, 1, 2, 3]]
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == [ [ 2, 3, 4, 5], [ 8, 7, 6, 5], [ 0, 1, 2, 3]])
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == [ [ 2, 3, 4, 5], [ 8, 7, 6, 5], [ 0, 1, 2, 3]])
    print('Passed! AND I WILL ADD MORE')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    a = [ [ 2, 3, 4, 5], [ 8, 7, 6, 5], [ 0, 1, 2, 3] ]
    assert(destructiveRemoveRowAndCol(a, 1, 2) == None)
    assert(a == [ [ 2, 3, 5], [ 0, 1, 3] ]) # but now A is changed!
    a = [ [ 1, 2 ], [3, 4] ]
    assert(destructiveRemoveRowAndCol(a, 0, 0) == None)
    assert(a == [ [ 4 ] ])
    print("Passed! AND I WILL ADD THE SAME TEST CASES AS THE PREVIOUS ONE")

def makeCanvas(root, width, height):
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    return canvas

def testDrawAsciiArt():
    print("Testing drawAsciiArt... check the screen!", end="")
    root = Tk()
    w, h = 600, 300
    canvas = makeCanvas(root, w, h)
    artStr = ''' 
  1     2     4
 111   222   444
11111 22222 44444
 111   222   444
  1     2     4
 '''
    drawAsciiArt(canvas, w, h, artStr)
    root.mainloop()

    root = Tk()
    w, h = 600, 300
    canvas = makeCanvas(root, w, h)
    artStr = "0123\n4567"
    drawAsciiArt(canvas, w, h, artStr)
    root.mainloop()

    root = Tk()
    w, h = 800, 600
    canvas = makeCanvas(root, w, h)
    artStr = ''' 
                          0022222222222222222
                      02222222222222222222222220
                   02222222222222222222222222222220         02   02 02
   0 0 0        02222222222222222222222222222222222220       02 22 2202
0 2 2 02      0222222222    2222222222222    2222222220       02202202
022222202     0222222222      22222222222      22222222220    02222222
  0222222    02222222222      22222222222      22222222222222222222222
  02222222222222222222222    2222222222222    22222222222222  0222
   022202222222222222222222222222222222222222222222222222222    0222
    022   022222222222222222222222222222222222222222222222222     02220
   0220   222222222222222222222222222222222222222222222222222       2220
   022    222222222222222222222222222222222222222222222000222222022220
  0222022222  2222222222222222222222222222222222222   022222222222222222
  0222   202222   2222222222222222222222222222222222     02220
 0222       0222    022222222222222222222222222220      0222
            02220     02222222222222222220220           022
              0220          02202222220              0222
               02220                                02220
                022220      02222220022220        02222
                  0222220     022222222220   022220
                     0222220  022222222222220
                        02222222022222222222
                                022222222222
                                   022222222222
                                     02222222220
                                      02220
                                      
 '''
    drawAsciiArt(canvas, w, h, artStr)
    root.mainloop()

    root = Tk()
    w, h = 400, 600
    canvas = makeCanvas(root, w, h)
    artStr = ''' 
                            0000
        00000000000000000000    00
00000000            0000000000000 00
0 000000000000000000         000000 00
0000                11111    0 0   00 00
00 0        111111111111111110 0   0000 0
 0 000000111111111111111111110 00000 0000
 0 0   0 111111111111111111110 0   0 0
 0 0   0 111111111111111555550 0   0 0
 0 0   0 111111111555644644640 0   0 0
 0 0   0 111115546446446446440 0   0 0
 0 0   0 111546464464464464460 0   0 0
 0 0   0 154644644644644646660 0   0 0
 0 0   0 056446446446666666660 0   0 0
 0 0   0 0 5666666666666666650 0   0 0
 0 0   0 0  566666666666666510 0   0 0
 0 0   0 0   16666666666661  0 0   0 0
 0 0   0 0    116666666651   0 0   0 0
 0 0   0 0       1156111     0 0   0 0
 0 0   0 0         55        0 0   0 0
 0 0   0 0      11165111     0 0   0 0
 0 0   0 0    1111156111111  0 0   0 0
 0 0   0 0   111111551111111 0 0   0 0
 0 0   0 0  111111165111111110 0   0 0
 0 0   0 0 1111111155111111110 0   0 0
 0 0   0 011111111161111111110 0   0 0
 0 0   0 011111111161111111110 0   0 0
 0 0   0 111111115666511111110 0   0 0
 0 0   0 111111156666651111110 0   0 0
 0 0   0 111111566666665111110 0   0 0
 0 0   01111115666666666511110 0   0 0
 0 0 0001111156666666666651110 00000 0000
 0 00   1111566666666666665110 0   000 00
 0 0    1111566666666666666510 0     00 0
00000   0115666666666666666510 0   00  00
0    00000000006666660000    000 00  00
0000000000000  111111  0000000000  00
            00000000000000000000000
 '''
    drawAsciiArt(canvas, w, h, artStr)
    root.mainloop()
    print("Done.")
def testAll():
    # 1
    testSameChars()
    testGetCharacterLines()
    # 2
    testVectorSum()
    testHistogram()
    # 3
    testNondestructiveRemoveRowAndCol()
    ##testDestructiveRemoveRowAndCol()
    ##testDrawAsciiArt()
    # 4
    testPlayerClass()

testAll()