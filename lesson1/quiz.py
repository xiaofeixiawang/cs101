1.
# This is a Python comment. Lines that begin with a '#' are ignored by the
# Python interpreter. Comments are useful for documenting code or explaining
# quiz questions!
# 
# Write a Python program that prints out the number of minutes in seven weeks.
# Remember: 7 weeks 7 days in a week, 24 hours in a day, and 60 mins in an hour.
# Multiplying these numbers together will give you the result
#
# Click the "Test Run" button below to try running your code and see the output,
# and click "Submit" to submit your answer.

print 7*7*24*60

2.
# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the values
# defined below.    
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second
print 299792458*1.0/1000000000*100

3.
# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0
print speed_of_light/cycles_per_second

4.
# Write python code that defines the variable 
# age to be your age in years, and then prints 
# out the number of days you have been alive.

age=23
print age*365

5.
# Define a variable, name, and assign to it a string that is your name.

name='yifei wang'

6.
# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

s = 'audacity'
print 'U'+s[2:]

7.
# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

start_link =page.find('<a href=')

8.
# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to
# page = '<a href="http://udacity.com">Hello world</a>'
# that your code still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
end_link=page.find('"',start_link+9)
url=page[start_link+9:end_link]
print url