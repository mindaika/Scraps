## Mini-project 1
## Rock-paper-scissors-lizard-Spock
## Developer: Randall Sewell
## Date: 20/4/13

import math

print "Welcome to Rock-paper-scissors-lizard-Spock"

q = False
p = False

print not(p or not q)

n = 12323515234563467.35234562347356
print (n % 100 - n % 10) / 10
print (n // 10) % 10
print (n / 10) % 10


#print (123.4 // 10) % 10
#print (123.4 % 10) / 10
#print ((123.4 - 123.4 % 10) / 10) % 10

import random

# Preferred method. 0 <= var <= 10
print random.randint(0, 10)

# Deprecated method. 0 <= var < 10
print random.randrange(0, 10)

def func1(x):
    return -5 * math.pow(x, 5) + 69 * math.pow(x, 2) - 47

print "FU", func1(0)
print "FU", func1(1)
print "FU", func1(2)
print "FU", func1(3)



def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    
    
    return present_value * math.pow(((1 + rate_per_period)), periods)
    
    #future_value(500, .04, 10, 10)
    # Put your code here.
    
   
print future_value(500, .04, 10, 10)
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

def polyglot(sides, side_length):
    
    
    
    # ?? n s2 / tan(??/n).
    return ((1/4) * sides * math.pow(side_length, 2)) / (math.tan(math.pi/sides))

print polyglot(7,3)


def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))


def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)
