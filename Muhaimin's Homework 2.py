### SAMS Senior CS-Track Hw2
### Due Date: Friday 07/12 8:30pm
### Name: Muhaimin Sarker
### andrewID: msarker

# Write code in each of the functions below such that they fulfill the
# instructions. You can run the file to test your code against the test cases
# at the bottom.

# Submit your work on Autolab. Autolab may contain additional test cases,
# so don't hard-code your solutions. We will manually grade any code that
# does not have tests, or does not pass the test cases on Autolab.

### Problem 1: Debugging and Testing ###

"""
The following two functions both have no test cases, and as a result, both have
bugs. The first function has exactly one bug; the second function has three.

For each function, add an appropriate set of test cases to the test function,
then use those tests along with debugging to find the problem. Fix the problem
in the code, then write in a comment above the code the 
 of the bug (syntax,
runtime, or logical), what the bug was, and how you fixed it.

You should not rewrite the program yourself beyond fixing the bugs- the point is 
to practice testing and debugging, not writing code.
"""

"""
This function should return True if the input x is either an even integer less 
than or equal to 10 or an odd integer greater than 10. The function should 
return False otherwise.
"""
# Bug 1: Logical Error: If you input a number greater than 10 and it's an even integer, then it doesn't return false. 
# This is because the if statement only accounts for odd numbers greater than 10 and not even numbers
def buggyFunction(x):
    if type(x) != int:
        return False
    if x <= 10:
        if x % 2 == 0:
            return True
    if x > 10:
        if x % 2 == 1:
            return True
        else:
            return False
    else: 
        return False

def testBuggyFunction():
    print("Testing buggyFunction()...", end="")
    assert(buggyFunction(1)==False)
    assert(buggyFunction(2)==True)
    assert(buggyFunction(10)==True)
    assert(buggyFunction(1.1)==False)
    assert(buggyFunction("500")==False)
    assert(buggyFunction(501)==True)
    assert(buggyFunction(500)==False)
    assert(buggyFunction("")==False)
    assert(buggyFunction(-2)==True)
    print("Passed")

"""
Remove the triple-quotes around the function when you are ready to attempt
this problem.

This program takes a positive integer, n, and determines whether that number is 
'multi-powerful', a made-up term. A multi-powerful number is one which is 
powerful (for every prime factor p which divides n, p**2 must also divide n) 
and also has more than one prime factor (not including 1, which is not prime). 
The first multi-powerful numbers are 36, 72, 100, and 108.
"""
# Bug 1: Syntax Error= if n%factor=0 and isPrime(factor): You have to have an double equals as the single equals is the assignment operator
# Bug 2: Runtime Error= if n % factor == 0 and isPrime(factor): Makes it so that you divide by 0 (which is undefined). You also divide by 1 which isn't a prime factor
'''Bug 3: Logical Error=   if n % factor == 0 and isPrime(factor):
            if n % (factor**2) != 0:
                return False
        factorCount += 1
    This makes it so that even if the factor isn't 0 '''
def isMultiPowerfulNumber(n):
    factorCount = 0
    for factor in range(2,n):
        if n % factor == 0 and isPrime(factor):
            if n % (factor**2) == 0:
                factorCount += 1
    return factorCount > 1
def isPrime(n):
    if n < 2:
        return False
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True



def testIsMultiPowerfulNumber():
    print("Testing isMultiPowerfulNumber()...", end="")
    assert(isMultiPowerfulNumber(36)==True)
    assert(isMultiPowerfulNumber(72)==True)
    assert(isMultiPowerfulNumber(100)==True)
    assert(isMultiPowerfulNumber(101)==False)
    assert(isMultiPowerfulNumber(16)==False)
    assert(isMultiPowerfulNumber(1)==False)
    assert(isMultiPowerfulNumber(0)==False)
    print("FINISHED")


### Problem 2: Simple Control Structures ###

"""
Write the function getInRange(x, bound1, bound2) which takes 3 int or float 
values, x, bound1, and bound2, and returns a version of x inside the specified
bounds. If x is already between bound1 and bound2, it is not changed. 
Otherwise, if x is less than the lower bound, return the lower bound, and if x 
is greater than the upper bound, return the upper bound. For example, 
getInRange(10, 3, 7) would return 7.
"""
def getInRange(x, bound1, bound2):
    greaterbound=0
    lessbound=0
    if (bound1>=bound2):
      greaterbound= bound1 
      lessbound= bound2
    elif (bound2>=bound1):
      greaterbound= bound2
      lessbound= bound1
    if (x<=greaterbound and x>=lessbound):
        return x
    elif x<lessbound:
        return lessbound
    elif x>greaterbound:
        return greaterbound
        

"""
Definition: For a positive integer n, n factorial, denoted n!, is the product 
n*(n-1)*(n-2)*...*1. If n = 0, then define 0! as 1.

Given a non-negative integer n, return n! (n factorial).

NOTE: you may not call math.factorial! That would be too easy. You must use a 
loop to get credit.
"""
def factorial(n):
    num= n-1;
    if n==0:
        return 1
    else:
        while (num>=1):
            n*=num
            num-=1
        return n

"""
Given a string s, return a new string, t, that contains each letter of s twice. 
For example, if doubleLetter is given the string 'apple', it will return 
'aappppllee'
"""
def doubleLetter(s):
    doubleString= ""
    for i in s:
        doubleString+=i
        doubleString+=i
    return doubleString

"""
Given an integer n, return the number of digits of n. 
You must use a loop to get credit.
"""
def numberLength(n):
    lengthNum= 0;
    num= abs(n)
    if (num==1 or num==0):
        return 1
    else:
        for i in range(num+1):
            if (num//(10**lengthNum)>=1):
                lengthNum+=1
            else:
                return lengthNum

### Problem 3: Complex Control Flow ###

"""
Return True if all alphabetic characters in the string s are uppercase 
and there is at least one alphabetic character. Otherwise return False.
"""
def isUpper(s):
    numAlphabetic= 0
    for c in s:
        if ord(c)>=65 and ord(c)<=90:
            numAlphabetic+=1
    return numAlphabetic>=1

"""
Write the function nthHappyPrime(n) that, of course, finds the nth happy 
prime. Prime we know already, but what is a happy number? To find out, read 
the first paragraph on the Wikipedia page: 
https://en.wikipedia.org/wiki/Happy_number

For our purposes, we can simplify the process of finding a happy number by 
saying that a cycle which reaches 1 indicates a happy number, while a cycle 
which reaches 4 indicates a number that is unhappy.

To solve this problem, you should use top-down design to split this problem 
into four functions. One should be nthHappyPrime(n) (the main function); one 
should be isPrime(n) (which is given to you here). The other two functions 
should be set up in a way that you think makes the problem easier to solve.
"""
def isPrime(n):
    if n < 2:
        return False
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True
'''def nthPrime(n):
    guess = 0
    found = 0
    while found < n:
        guess += 1
    if isPrime(guess):
        found += 1
    return guess'''
def findDigit(n,k):
    num= str(n)
    if (len(num)<=k):
        return False
    else:
        return int(num[(len(num))-k-1])
def happy(n):
    sum=0
    while(sum!=1 or sum!=4):
        for i in range(numberLength(n+1)):
            sum+=findDigit(n,i)**2
        n=sum
        if (sum==4):
            return False
        if (sum==1):
            return True
        sum=0
        
def nthHappyPrime(n):
    guess=0
    found=0
    while found < n:
        guess += 1
        if isPrime(guess) and happy(guess):
            found += 1
    return guess

######################################################################
# GRAPHICS CODE
# ignore_rest: The autograder will ignore all code below here
######################################################################

### Problem 3 Continued ###
from tkinter import *

"""
Using tkinter, draw a checkerboard with checkers in the starting positions
on the given canvas. The checkerboard should resize based on the given width
and height. You are guaranteed that the canvas will be square.

A checkerboard alternates light and dark spaces in an 8x8 grid. Pieces are
placed on the dark spaces, with pieces of one color in the top three rows and
pieces of a different color in the bottom three rows.

Examples of checkerboards and checkers can be found here:
https://en.wikipedia.org/wiki/Draughts

To get full credit, you can't have more than 10 create_rectangle or create_oval
calls. You must use loops instead!
"""
def drawCheckerboard(canvas, width, height):
    fillNumber=0
    for row in range(9):
        for col in range(9):
            fillNumber+=1
            newHeight = row*(width/8) #Takes the value of the row and multiplies it
            newWidth = col*(width/8) #Takes the value of the column and multiples it
            if (fillNumber%2==1):
                canvas.create_rectangle(newWidth, newHeight, newWidth + (width/8), newHeight + (width/8), fill= "white")
            else: 
                 canvas.create_rectangle(newWidth, newHeight, newWidth + (width/8), newHeight + (width/8), fill= "black")
                 if(row>=5):
                     canvas.create_oval(newWidth, newHeight, newWidth + (width/8), newHeight + (width/8), fill= "red")
                 if(row<=2): 
                    canvas.create_oval(newWidth, newHeight, newWidth + (width/8), newHeight + (width/8), fill= "blue")
    


######################################################################
# TEST CODE
######################################################################

def testGetInRange():
    print("Testing getInRange()...", end="")
    assert(getInRange(10, 3, 7) == 7)
    assert(getInRange(1, 3, 5) == 3)
    assert(getInRange(4, 3, 5) == 4)
    assert(getInRange(7, 7, 7) == 7)
    assert(getInRange(10, 1, 10) == 10)
    assert(getInRange(0, 0, 100) == 0)
    print("Passed.")

def testFactorial():
    import math
    print("Testing factorial()...", end="")
    assert(factorial(0) == math.factorial(0))
    assert(factorial(1) == math.factorial(1))
    assert(factorial(2) == math.factorial(2))
    assert(factorial(3) == math.factorial(3))
    assert(factorial(4) == math.factorial(4))
    assert(factorial(5) == math.factorial(5))
    assert(factorial(10) == math.factorial(10))
    print("Passed.")

def testDoubleLetter():
    print("Testing doubleLetter()...", end="")
    assert(doubleLetter("apple") == "aappppllee")
    assert(doubleLetter("test") == "tteesstt")
    assert(doubleLetter("12.34") == "1122..3344")
    assert(doubleLetter("") == "")
    print("Passed.")

def testNumberLength():
    print("Testing numberLength()...", end="")
    assert(numberLength(0) == 1)
    assert(numberLength(1) == 1)
    assert(numberLength(9) == 1)
    assert(numberLength(10) == 2)
    assert(numberLength(1001) == 4)
    assert(numberLength(999) == 3)
    assert(numberLength(-1) == 1)
    assert(numberLength(-123) == 3)
    assert(numberLength(-123456789) == 9)
    print("Passed.")

def testIsUpper():
    print("Testing isUpper()... ", end="")
    assert(not isUpper(""))
    assert(not isUpper(" "))
    assert(isUpper("ABCD"))
    assert(not isUpper("abcd"))
    assert(not isUpper("1234"))
    assert(not isUpper("!*&$"))
    assert(isUpper("AB12"))
    assert(not isUpper("ab12"))
    assert(not isUpper("!*12"))
    assert(not isUpper("!*ab"))
    assert(isUpper("!*AB"))
    print("Passed!")

def testNthHappyPrime():
    print('Testing nthHappyPrime()... ', end="")
    assert(nthHappyPrime(1) == 7)
    assert(nthHappyPrime(2) == 13)
    assert(nthHappyPrime(3) == 19)
    assert(nthHappyPrime(4) == 23)
    assert(nthHappyPrime(5) == 31)
    assert(nthHappyPrime(6) == 79)
    assert(nthHappyPrime(7) == 97)
    print('Passed!')
def makeCanvas(root, width, height):
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    return canvas

def testDrawCheckerboard():
    print("Testing drawCheckerboard... check the screen!", end="")
    root = Tk()
    w, h = 400, 400
    canvas = makeCanvas(root, w, h)
    drawCheckerboard(canvas, w, h)
    root.mainloop()

    root = Tk()
    w, h = 600, 600
    canvas = makeCanvas(root, w, h)
    drawCheckerboard(canvas, w, h)
    root.mainloop()
    print("Done.")


def testAll():
    # 1
    testBuggyFunction()
    testIsMultiPowerfulNumber()
    # 2
    testGetInRange()
    testFactorial()
    testDoubleLetter()
    testNumberLength()
    # 3
    testIsUpper()
    testNthHappyPrime()
    testDrawCheckerboard()

testAll()