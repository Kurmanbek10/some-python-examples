# Fixed variable

number = 1

if int(number) >= 0:
    print("The number is positive")
else:
    print("The number is negative")

#With input option:
input_number = input("Provide your number here: ")

if int(input_number) >= 0:
    print("The number you have provided is positive")
else:
    print("The number you have provided is negative")

#With input option converting to intiger in the input section:
input_number_int = int(input("Provide your number here: "))

if input_number_int >= 0:
    print("The number you have provided is positive")
else:
    print("The number you have provided is negative")


# Now let's say you want to find out if the number is odd or even.
# In python we have different operators (+,-,*,/) the one we will use for this use case would be modulo.
# The Python modulo operator is the percent sign (%), and it returns the remainder of a division operation between two numbers. It works with both integers and floating-point numbers.

input_number_int1 = int(input("Provide your number here: "))

if input_number_int1 % 2 == 0:
    print("The number you have provided is even")
else:
    print("The number you have provided is odd")


# One more example. Check if old enough to vote:
your_age = int(input("Enter your age: "))

if your_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote yet")



# if, elif, else
# 90 and above is A
# between 89 and 80 is B
# between 79 and 70 is C
# betweend 69 and 60 is D

score = int(input("Enter your score ")) # Change type from int to float
if score >= 90: # first it checks if this true
    print("Grade: A")
elif score >= 80: # then it goes and check this step
    print("Grade: B")
elif score >= 70: # and so on before it find the true statement
    print("Grade: C")
elif score >= 60: # once it finds it will stop there
    print("Grade: D")
else:
    print("Grade: F")



# greeting = "hello"
# how to print out 'e' using indexing?

greeting = "hello"
print(greeting[1])

# how to reverse the string? [::-1] → reverse strings
# start, stop, step :: means from beginning to the end, -1 means going backwards

print(greeting[::-1])

# One more example with start, stop, step
morning_greeting = "goodmorning"
print(morning_greeting[::2])

# .reverse() → reverse lists (in place)




# dictionary = {"greeting":"hello"}
# print hello from this dictionary

dictionary = {"greeting":"hello"}

print(dictionary["greeting"])




# Create a variable called "username", the variable should be declared by the user input
# Create a variable called "password", the variable should be declared by the user input
# If the user input "admin" as the username and 1234 as the password it should print "Log in successful"
# Otherwise, it should print "Invalid username or password"


username = input("Enter username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234": #There is also 'or' 
    print("Log in successful")
else:
    print("Invalid username or password")


# Writing to files
with open("demofile.txt", "a") as f: # a for append, w for write. 'w' will overwrite it. 'f' is a variable
    f.write("Hey this is my first line")
    f.write("\nHey, this is my third line") #/n means a new line. 
    #Putting it in the beginning means that it will create a before printing that line
    #Putting it in the end means the next line will start with a new line



# For loop
services = ["docker", "nginx", "s3", "ec2", "ELB"]

for i in services:
    print(i)


numbers = [1,2,3,4,5]

for x in numbers:
    y = x + 5
    print(y)

# Python syntax
for x in numbers:
    x += 5
    print(x)



# Range
for c in range(10): # we can provide a different range e.g. (1, 10)
    c += 2
    print(c)


# for loop with if, else, elif
# fizzbuzz.py

#Print numbers from 1 to 100 but:
# for numbers which are multiples of both 3 and 5, print "FizzBuzz"
# for multiples of 3, print "Fizz" instead of the number.
# for multiples of 5, print "Buzz" instead of the number.

# You need to use combination of for loop + if,elif,else statement,
# you need to use modulo %.
# Do this task with vim only in your termnial, NO VISUAL STUDIO CODE!!!

# the output should look like this:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...

for e in range(1, 101):
    if e % 3 == 0 and e % 5 == 0:
        print("FizzBuzz")
    elif e % 3 == 0:
        print("Fizz")
    elif e % 5 == 0:
        print("Buzz")
    else:
        print(e)

# Boolean (bool) - True/False statements

# If else conditionals in Python

# + - * /
# % modulo ()
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# and -> both statements have to be true:
#         for example
#         if username == 'admin' and password == '1234' (means both statements have to be true)

# or -> either one of the statements has to be true (at least 1)
#         for example
#         if username == 'admin' or password == '1234' (at least 1 statement has to be true)

# if you have one equal sign =, that means you are assigning a value to a variable
# for example, name = "John", age = 41

# if you have two equal signs ==, that means you are giving arithmetic equal value
# for example, 2 + 2 == 4