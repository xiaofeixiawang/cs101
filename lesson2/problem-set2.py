1.
# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # your code here
    if(day=='Saturday' or day=='Sunday'):
        return True
    return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

2.
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(n):
    # Your code here
    five=0
    two=0
    one=0
    while(n>=5):
        five+=1
        n-=5
    while(n>=2):
        two+=1
        n-=2
    while(n>=1):
        one+=1
        n-=1
    return five,two,one

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps

3.
# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def set_range(a,b,c):
    # Your code here
    if(a>b):
        if(b>c):
            return a-c
        return a-b
    if(a>c):
        return b-c
    return b-a

print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6

4.
# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: # 
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #

def fix_machine(debris, product):
    ### WRITE YOUR CODE HERE ###
    i=0
    while(i<len(product)):
        if(debris.find(product[i])==-1):
            return "Give me something that's not useless next time."
        i+=1
    return product

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'

5.
# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def isLeapYear(year):
    if year%4==0 and (year%400==0 or year%100!=0):
        return True
    return False

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day < 31:
            return year, month, day + 1
        if month!=12:
            return year,month+1,1
        return year+1,1,1
    if month == 4 or month==6 or month==9 or month==11:
        if day<30:
            return year,month,day+1
        return year, month + 1, 1
    if isLeapYear(year):
        if(day<29):
            return year,month,day+1
        return year,month+1,1
    if(day<28):
        return year,month,day+1
    return year,month+1,1
        
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

6.
#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def helper(value,n):
    if(n>0):
        helper(value/10,n-1)
    if(value%10==0):
        print '|00000*****   |'
    if(value%10==1):
        print '|00000****   *|'
    if(value%10==2):
        print '|00000***   **|'
    if(value%10==3):
        print '|00000**   ***|'
    if(value%10==4):
        print '|00000*   ****|'
    if(value%10==5):
        print '|00000   *****|'
    if(value%10==6):
        print '|0000   0*****|'
    if(value%10==7):
        print '|000   00*****|'
    if(value%10==8):
        print '|00   000*****|'
    if(value%10==9):
        print '|0   0000*****|'

def print_abacus(value):
       #
       ### Add you code here 
       #
        helper(value,9)
        

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|

7.
# By AnnaGajdova from forums
# You are in the middle of a jungle. 
# Suddenly you see an animal coming to you. 
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!" 
#            If you are not: "Stay calm and wait!". 
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal, 
# that takes as input a string and a number, 
# an animal and your speed (in km/h), 
# and prints out what to do.

def jungle_animal(animal, my_speed):
    # YOUR CODE HERE
    if(animal=='zebra'):
        print "Try to ride a zebra!"
    if(animal=='cheetah'):
            if(my_speed>115):
                print "Run!"
            else:
                print "Stay calm and wait!"
    else: 
        print "Introduce yourself!"


jungle_animal('cheetah', 30)
#>>> "Stay calm and wait!"

#jungle_animal('gorilla', 21)
#>>> "Introduce yourself!"

8.
# By Ashwath from forums

# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.

# Define a procedure is_leap_baby that takes 3 inputs: day, month and year
# and returns True if the date is a leap day (Feb 29 in a valid leap year)
# and False otherwise.

# A year that is a multiple of 4 is a leap year unless the year is
# divisible by 100 but not a multiple of 400 (so, 1900 is not a leap
# year but 2000 and 2004 are).

def is_leap_baby(day,month,year):
    # Write your code after this line.
    if(month==2 and day==29 and (year%400==0 or year%100!=0)):
        return True
    return False


# The function 'output' prints one of two statements based on whether 
# the is_leap_baby function returned True or False.

def output(status,name):
    if status:
        print "%s is one of an extremely rare species. He is a leap year baby!" % name
    else:
        print "There's nothing special about %s's birthday. He is not a leap year baby!" % name

# Test Cases

output(is_leap_baby(29, 2, 1996), 'Calvin')
#>>>Calvin is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(19, 6, 1978), 'Garfield')
#>>>There's nothing special about Garfield's birthday. He is not a leap year baby!

output(is_leap_baby(29, 2, 2000), 'Hobbes')
#>>>Hobbes is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(29, 2, 1900), 'Charlie Brown')
#>>>There's nothing special about Charlie Brown's birthday. He is not a leap year baby!

output(is_leap_baby(28, 2, 1976), 'Odie')
#>>>There's nothing special about Odie's birthday. He is not a leap year baby!