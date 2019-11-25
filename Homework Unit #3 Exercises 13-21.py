#!/usr/bin/env python
# coding: utf-8

# #  EXCERCISES 13 - 21.

# ## Exercise 13 "Parameters, Unpacking, Variables"

# We will learn about how we can add variables in an arguments through the import, unpaks and other things.
# 
# Here you can see an example:

# In[ ]:


from sys import argv

script, one, two = argv

print("The script is called:", script)
print("Your first variable is:", one)
print("Your second variable is:", two)


# ## Exercise 14 "Prompting and Passing"

# Now let´s do an exercise but giving data like how input slightly differently by having it print a simple  prompt.

# In[ ]:


from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.""")


# We make a variable prompt that is set to the prompt we want, and we give that to input instead of typing it over and over. Now if we want to make the prompt something else, we just change it in this one spot and return the script.

# ## Exercise 15 "Reading Files"

# Now we will try to enter a text file to avoid being transcribed from a document to the program, you should knows how make an arguments. This may take time and more dedication.

# In[ ]:


from sys import argv
script, links = argv
txt = open(links.txt)
print(f"Here's your file {links.txt}:")
print(txt.read())
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


# ## Exercise 16 "Reading and Writing Files"

# Now we will learn how to use commands such as "close, read, read-line, write" among others.
# 
#  Here’s the list of commands I want you to remember:
# 
# ![image.png](attachment:image.png)

# In[ ]:


from sys import argv
script, links = argv

print(f"We're going to erase {links}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(links, 'w')

("Truncating the file. Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()


# ## Exercise 17 "More Files"

# we will use a command called exist with this we can verify if the file is correct or notwell here we bring more things with files.

# In[ ]:


from sys import argv
from os.path import exists
script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


# ## Exercise 18 "Names, Variables, Code, Functions"

# Every programmer will go on and on about functions and all the different ideas about how they work and what they do, but I will give you the simplest explanation you can use right now.

# In[ ]:


def print_two(*args):
    arg1, arg2 = args
print(f"arg1: {arg1}, arg2: {arg2}")
def print_two_again(arg1, arg2):
print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
print(f"arg1: {arg1}")
def print_none():
print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()


# ## Exercise 19 "Functions and Variables"

# the variables many of the times are not between connected and here you will see an example of it

# In[ ]:


def cheese_and_crackers(cheese_count, boxes_of_crackers):
print(f"You have {cheese_count} cheeses!")
print(f"You have {boxes_of_crackers} boxes of crackers!")
print("Man that's enough for a party!")
print("Get a blanket.\n")
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# ## Exercise 20 "Functions and Files"

# To understand this lesson you need to pay attention to what happens

# In[ ]:


from sys import argv

script, input_file = argv

def print_all(f):
print(f.read())

def rewind(f):
f.seek(0)

def print_a_line(line_count, f):
print(line_count, f.readline())

current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)


# ## Exercise 21 "Functions Can Return Something"

# how to use = and a new Python word return to set variables to be a value from a function. 

# In[ ]:


def add(a, b):
print(f"ADDING {a} + {b}")
return a + b

def subtract(a, b):
print(f"SUBTRACTING {a} - {b}")
return a - b

def multiply(a, b):
print(f"MULTIPLYING {a} * {b}")
return a * b

def divide(a, b):
print(f"DIVIDING {a} / {b}")
return a / b
print("Let's do some math with just functions!")
 age = add(30, 5)
 height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")

