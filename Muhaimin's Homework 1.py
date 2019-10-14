### SAMS Senior CS-Track Hw1
### Due Date: Friday 07/05 8:30pm
### Name: Muhaimin Sarker
### andrewID: msarker

# Write code in each of the functions below such that they fulfill the
# instructions. You can run the file to test your code against the test cases
# at the bottom.

# Submit your work on Autolab. Autolab may contain additional test cases,
# so don't hard-code your solutions. We will manually grade any code that
# does not have tests, or does not pass the test cases on Autolab.


### Problem 1 - Booleans and Logic ###

"""
Given two booleans, b1 and b2, return True if exactly one of b1 and b2 is True,
and False otherwise.
"""
def justOneTrue(b1, b2):
    if (b1 and b2):
        return False
    elif (b1==True or b2==True):
        return True
    else:
        return False
    
"""
Write the program answerPhone that takes three parameters- a boolean (whether 
you know the caller), an integer (the hour in military time), and another 
integer (the area code)- and returns True if you should answer the phone, 
and False otherwise.

Your program should meet the following requirements:
- You generally answer the phone if you know the person calling.
- You don't answer the phone if it's before 10am.
- You generally answer the phone if it has your local area code, 412.
"""
def answerPhone(callerKnown, time, areaCode):
    if (callerKnown and time>=10):
        return True
    elif (time>=10 and areaCode==412):
        return True
    else: 
        return False


### Problem 2 - Math and Induction ###

"""
Given an integer n, return the ones-digit of n, which is the first digit of n 
from the right. onesDigit(1234) should return 4.
"""
def onesDigit(n):
    newNum= abs(n)
    return newNum%10

"""
Given an integer n, return the tens-digit of n, which is the second digit of n 
from the right. tensDigits(1234) should return 3.
"""
def tensDigit(n):
    tempNum= str(abs(n))
    if (len(tempNum)>=2):
        return int(tempNum[len(tempNum)-2])
    else: 
        return False

"""
Given two integers n and k, return the k'th digit of n from the right. We count
from 0, so k = 0 refers to the ones-digit, k = 1 refers to the tens-digit, etc.
You can assume n and k are non-negative. getKthDigit(1234, 2) should return 2.
"""
def getKthDigit(n, k):
    num= str(n)
    if (len(num)<=k):
        return False
    else:
        return int(num[(len(num))-k-1])
"""
Given three integers n, k and d, replace the k'th digit of n with d.
You can assume n and k are non-negative, and d is an integer between 0 and 9.
setKthDigit(1234, 2, 9) should return 1934.
"""
def setKthDigit(n, k, d):
    removeDigit = n - getKthDigit(n, k) * 10**k
    addDigit = removeDigit + d * 10**k
    return addDigit
       

### Problem 3 - Variables, Functions, and Top-Down Design ###

"""
Write a function that takes four int or float values representing 2 lines:

y = m1*x + b1
y = m2*x + b2

It returns the x value of the point of intersection of the two lines. You may
assume the lines do intersect (they are not parallel).

Need help? Try this: https://en.wikipedia.org/wiki/Line-line_intersection#Given_the_equations_of_the_lines
"""
def lineIntersection(m1, b1, m2, b2):
    return (b2-b1)/(m1-m2)

"""
Write a function that takes four int or float values representing two (x,y)
points and returns the distance between those points.

Need help? Try this: https://en.wikipedia.org/wiki/Distance#Geometry
"""
def distance(x1, y1, x2, y2):
    return (((x2-x1)**(2))+((y2-y1)**(2)))**(0.5)

"""
Write a function that takes three int or float values representing the side 
lengths of a triangle and returns the area of that triangle.

Need help? Try this: https://en.wikipedia.org/wiki/Heron's_formula#Formulation
"""
def triangleArea(s1, s2, s3):
    s= (s1+s2+s3)/2
    return (s*(s-s1)*(s-s2)*(s-s3))**(0.5)

"""
Write the function threeLinesArea(m1, b1, m2, b2, m3, b3) that takes six int or 
float values representing 3 lines:

   y = m1*x + b1
   y = m2*x + b2
   y = m3*x + b3
   
First find the points where each pair of lines intersects, then return the area 
of the triangle formed by connecting these three points. You may assume that 
the lines definitely form a triangle (the lines are not parallel).

Hint: use the three functions you wrote above!
"""
def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1=  (b2-b1)/(m1-m2)
    y1=  (m1*x1)+b1
    x2= (b3-b2)/(m2-m3)
    y2= (m2*x2)+b2
    x3= (b1-b3)/(m3-m1)
    y3= (m3*x3)+b3
    s1= (((x2-x1)**(2))+((y2-y1)**(2)))**(0.5)
    s2= (((x3-x1)**(2))+((y3-y1)**(2)))**(0.5)
    s3= (((x2-x3)**(2))+((y2-y3)**(2)))**(0.5)
    s= (s1+s2+s3)/2
    return (s*(s-s1)*(s-s2)*(s-s3))**(0.5)


######################################################################
# GRAPHICS CODE
# ignore_rest: The autograder will ignore all code below here
######################################################################

### Problem 4 - Graphics and Human Computer ###
from tkinter import *
"""
Using tkinter, draw the flag of Norway on the given canvas.
The flag should fill the screen based on the given width and height.
You have to use drawing commands, not create_image.

Here's the flag of Norway: http://flagpedia.net/norway
"""
def drawNorwayFlag(canvas, width, height): 
    canvas.create_rectangle(0, 0, width, height, fill= "red")
    canvas.create_rectangle(0, height/3, width,height/2, fill= "white", width= 0)
    canvas.create_rectangle(width/4, 0, width/2.5,height, fill= "white", width= 0)
    canvas.create_rectangle(0, height/2.75, width,height/2.1, fill= "blue", width= 0)
    canvas.create_rectangle(width/3.5, 0, width/2.75,height, fill= "blue", width= 0)
"""
Using tkinter, draw a robot of your own design on the given canvas.
The robot should resize with the canvas and fit in the given width and height.
You are guaranteed that the canvas will be square.

Your robot can look like whatever you want, but for full credit it should use:
 - At least 10 shapes total, including at least one oval, one rectangle, 
   one non-rectangular polygon, and one line.
 - At least 2 different optional parameters (like fill or width).
"""
def drawCoolRobot(canvas, width, height):
    canvas.create_oval(width/4, 0, width/2, height/4)
    canvas.create_oval(width/3.75, height/10, width/2.5, height/9.5)
    canvas.create_oval(width/3, height/10, width/2.25, height/9.5)
    canvas.create_oval(width/2.5, height/10, width/2.25, height/9.5)
    canvas.create_polygon(width, height, width/2, 0, 0, height,fill= "black", width=0)
    canvas.create_oval(width/2, 0, 3*(width/4), height/4)
    canvas.create_oval(width*0.5, height/10, width*.75, height/9.5)
    canvas.create_line(0,height/2, width/4, height/2, fill= "red")
    canvas.create_line(width,height/2, 3*(width/4), height/2, fill= "blue")
    canvas.create_rectangle(width/2, height/2, 3*(height/4),3*(height/4) ,fill= "green")
    canvas.create_text(width*0.625, height*0.625, text="PUSH ME")
    canvas.create_text(width*0.625, height*0.675, text="I'M BAD")
    
######################################################################
# TEST CODE
######################################################################

def testJustOneTrue():
    print("Testing justOneTrue()...", end="")
    assert(justOneTrue(True, False) == True)
    assert(justOneTrue(False, True) == True)
    assert(justOneTrue(False, False) == False)
    assert(justOneTrue(True, True) == False)
    print("Passed.")

def testAnswerPhone():
    print("Testing answerPhone()...", end="")
    assert(answerPhone(True, 12, 412) == True)
    assert(answerPhone(True, 8, 504) == False)
    assert(answerPhone(False, 6, 206) == False)
    assert(answerPhone(False, 7, 100) == False)
    assert(answerPhone(True, 15, 504) == True)
    assert(answerPhone(False, 14, 412) == True)
    assert(answerPhone(True, 9, 206) == False)
    assert(answerPhone(False, 10, 412) == True)
    print("Passed.")

def testOnesDigit():
    print("Testing onesDigit()...", end="")
    assert(onesDigit(0) == 0)
    assert(onesDigit(789) == 9)
    assert(onesDigit(7) == 7)
    assert(onesDigit(-1234) == 4)
    assert(onesDigit(-3) == 3)
    print("Passed.")

def testTensDigit():
    print("Testing tensDigit()...", end="")
    assert(tensDigit(0) == 0)
    assert(tensDigit(1) == 0)
    assert(tensDigit(10) == 1)
    assert(tensDigit(21) == 2)
    assert(tensDigit(-1234) == 3)
    assert(tensDigit(-3) == 0)
    assert(tensDigit(-10) == 1)
    print("Passed.")

def testGetKthDigit():
    print("Testing getKthDigit()...", end="")
    assert(getKthDigit(0, 0) == 0)
    assert(getKthDigit(789, 0) == 9)
    assert(getKthDigit(789, 1) == 8)
    assert(getKthDigit(789, 2) == 7)
    assert(getKthDigit(789, 3) == 0)
    assert(getKthDigit(1234, 3) == 1)
    assert(getKthDigit(3, 1) == 0)
    print("Passed.")

def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert(setKthDigit(468, 0, 1) == 461)
    assert(setKthDigit(468, 1, 1) == 418)
    assert(setKthDigit(468, 2, 1) == 168)
    assert(setKthDigit(468, 3, 1) == 1468)
    assert(setKthDigit(777, 1, 7) == 777)
    assert(setKthDigit(98765, 4, 3) == 38765)
    print("Passed.")

def testLineIntersection():
    import math
    print("Testing lineIntersection()...", end="")
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(math.isclose(lineIntersection(3, -5, 1, 5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(math.isclose(lineIntersection(10, 0, -4, 35), 2.5))
    print("Passed.")

def testDistance():
    import math
    print("Testing distance()...", end="")
    assert(math.isclose(distance(0, 0, 1, 1), 2**0.5))
    assert(math.isclose(distance(3, 3, -3, -3), 6*2**0.5))
    assert(math.isclose(distance(20, 20, 23, 24), 5))
    print("Passed.")

def testTriangleArea():
    import math
    print("Testing triangleArea()...", end="")
    assert(math.isclose(triangleArea(3, 4, 5), 6))
    assert(math.isclose(triangleArea(2**0.5, 1, 1), 0.5))
    assert(math.isclose(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed.")

def testThreeLinesArea():
    import math
    print("Testing threeLinesArea()...", end="")
    assert(threeLinesArea(1, 2, 3, 4, 5, 6) < 0.0001) # == 0
    assert(math.isclose(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(math.isclose(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(math.isclose(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(math.isclose(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed.")

def makeCanvas(root, width, height):
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    return canvas

def testDrawNorwayFlag():
    print("Testing drawNorwayFlag... check the screen!", end="")
    root = Tk()
    w, h = 220, 160
    canvas = makeCanvas(root, w, h)
    drawNorwayFlag(canvas, w, h)
    root.mainloop()

    root = Tk()
    w, h = 660, 480
    canvas = makeCanvas(root, w, h)
    drawNorwayFlag(canvas, w, h)
    root.mainloop()
    print("Done.")

def testDrawCoolRobot():
    print("Testing drawCoolRobot... check the screen!", end="")
    root = Tk()
    w, h = 400, 400
    canvas = makeCanvas(root, w, h)
    drawCoolRobot(canvas, w, h)
    root.mainloop()

    root = Tk()
    w, h = 200, 200
    canvas = makeCanvas(root, w, h)
    drawCoolRobot(canvas, w, h)
    root.mainloop()

    root = Tk()
    w, h = 600, 600
    canvas = makeCanvas(root, w, h)
    drawCoolRobot(canvas, w, h)
    root.mainloop()
    print("Done.")

def testAll():
    # 1
    testJustOneTrue()
    testAnswerPhone()
    # 2
    testOnesDigit()
    testTensDigit()
    testGetKthDigit()
    testSetKthDigit()
    # 3
    testLineIntersection()
    testDistance()
    testTriangleArea()
    testThreeLinesArea()
    # 4
    testDrawNorwayFlag()
    testDrawCoolRobot()
    
testAll()