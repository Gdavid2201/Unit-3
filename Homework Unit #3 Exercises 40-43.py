#!/usr/bin/env python
# coding: utf-8

# # Exercises 40-43

# ## Exercise 40 "Modules, Classes, and Objects"

# pay attention to this example since it is somewhat complicated

# In[ ]:


class Song(object):

def __init__(self, lyrics):
self.lyrics = lyrics

def sing_me_a_song(self):
for line in self.lyrics:
print(line)
 happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
 "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


# ## Exercise 41 "Learning to Speak Object-Oriented"

# Through a series of words you must form a printed text

# In[ ]:


import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {"class %%%(%%%):": "Make a class named %%% that is-a %%%.","class %%%(object):\n\tdef __init__(self, ***)" :"class %%% has-a __init__ that takes self and *** params.",
"class %%%(object):\n\tdef ***(self, @@@)":
"class %%% has-a function *** that takes self and @@@ params.",
"*** = %%%()":
"Set *** to an instance of class %%%.",
"***.***(@@@)":
"From *** get the *** function, call it with params self, @@@.",
"***.*** = '***'":
"From *** get the *** attribute and set it to '***'."}
if len(sys.argv) == 2 and sys.argv[1] == "english":
PHRASE_FIRST = True
else:
PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
 WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
class_names = [w.capitalize() for w in
random.sample(WORDS, snippet.count("%%%"))]
other_names = random.sample(WORDS, snippet.count("***"))
results = []
param_names = []

for i in range(0, snippet.count("@@@")):
param_count = random.randint(1,3)
param_names.append(', '.join(
random.sample(WORDS, param_count)))
for sentence in snippet, phrase:
 result = sentence[:]

for word in class_names:
 result = result.replace("%%%", word, 1)

 for word in other_names:
 result = result.replace("***", word, 1)

for word in param_names:
 result = result.replace("@@@", word, 1)

results.append(result)

 return results

 try:
 while True:
snippets = list(PHRASES.keys())
random.shuffle(snippets)

 for snippet in snippets:
 phrase = PHRASES[snippet]
question, answer = convert(snippet, phrase)
if PHRASE_FIRST:
question, answer = answer, question
print(question)


# ## Exercise 42 "Is-A, Has-A, Objects, and Classes"

# in this topic we will see the difference between class and an object

# In[ ]:


class Animal(object):
 pass

class Dog(Animal):

def __init__(self, name):
 self.name = name
class Cat(Animal):
def __init__(self, name):
self.name = name
 class Person(object):
def __init__(self, name):
self.name = name
self.pet = None

class Employee(Person):

 def __init__(self, name, salary):
 super(Employee, self).__init__(name)
self.salary = salary

class Fish(object):
 pass

class Salmon(Fish):
 pass

class Halibut(Fish):
 pass
 rover = Dog("Rover")
 satan = Cat("Satan")

 mary = Person("Mary")
mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover
 flipper = Fish()
crouse = Salmon()
harry = Halibut()


# ## Exercise 43 "Basic Object-Oriented Analysis and Design"

# how to solve a good problem easily now in this topic we will give you a series that you will grow as a programmer

# In[ ]:


class Map(object):

scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(), }
def __init__(self, start_scene):
    self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
return val
def opening_scene(self):
    return self.next_scene(self.start_scene)

