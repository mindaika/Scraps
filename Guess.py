# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import random
import simplegui
# simplegui is a custom object from http://www.codeskulptor.org/


# initialize global variables used in your code
comp_number = random.randrange(0, 100)
guess = 0
attempt = 0

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global comp_number, attempt
    attempt = math.ceil(math.log(100,2))
    comp_number = random.randrange(0, 100)
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is " + str(attempt) + "\n"
    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global comp_number, attempt
    attempt = math.ceil(math.log(1000,2))
    comp_number = random.randrange(0, 1000)
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is " + str(attempt) + "\n"
    
    
def get_input(guess):
    # main game logic goes here    
    global attempt
    print "Guess was " + str(guess)
    if attempt > 1:
        attempt -= 1
        if comp_number == float(guess):
            print "Correct!"+ "\n"
            range100()
        elif comp_number < float(guess):
            print "Number of remaining guesses is " + str(attempt) + "\nLower!\n"
        elif comp_number > float(guess):
            print "Number of remaining guesses is " + str(attempt) + "\nHigher!\n"
        else:
            print "Error 0"
    else:
        print "You ran out of guesses. The number was " + str(comp_number) + "\n"
        range100()
        

    
# create frame
frame = simplegui.create_frame("Guess the Number! v0.2", 200, 200)


# register event handlers for control elements
frame.add_input("Enter a guess", get_input, 50)
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)

# start frame
frame.start()
range100()



# always remember to check your completed program against the grading rubric
