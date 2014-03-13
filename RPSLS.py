## Mini-project 1
## Rock-paper-scissors-lizard-Spock
## Developer: Randall Sewell
## Date: 20/4/13

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random
# helper functions

def rpsls(name):
    # convert name to player_number using name_to_number
    number = name_to_number(name) 

    # compute random guess for comp_number using random.randrange()
    comp_num = random.randint(0, 4)

    # compute difference of player_number and comp_number modulo five
    print "Player chooses", name
    
    # convert comp_number to name using number_to_name
    print "Computer chooses", number_to_name(comp_num)
    
    # use if/elif/else to determine winner
    if (number - comp_num) == 0:
        print "Player and computer tie!\n"
    elif (number - comp_num)%5 <= 2:
        print "Player wins!\n"
    else:
        print "Computer wins!\n"
    # print results

def name_to_number(name):
    # fill in your code below
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print "Bazinga!"
        exit

def number_to_name(number):
    # fill in your code below
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print "Checkmate."
        exit

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
# These are some changes, to see what git is doing
