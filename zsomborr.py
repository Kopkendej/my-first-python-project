
import emoji
from art import *
import random
import pyjokes as pj

a=5
print(emoji.emojize(f'Python is a {a} :star2: language.',language='alias'))
print(emoji.emojize(':lion::crown:', language='alias'))
print(emoji.emojize(':monkey::genie::princess::heart::man:', language='alias'))
print(emoji.emojize(':girl::heart::ogre::rose::prince:', language='alias'))
print(emoji.emojize(':princess::pick::pick::pick::pick::pick::pick::pick::apple:', language='alias'))
print(emoji.emojize(f'Python is a :snake: language.', language='alias'))
print(emoji.demojize("🐍"))
# Emoji cheat sheet: https://www.webfx.com/tools/emoji-cheat-sheet/

# Task 2 - Art printing
a = 7
tprint(f"Logiscool is {a} years old.")

# Task 3 - Computer science jokes
print(pj.get_joke())

# Task 8 - Master mind
tprint("Master Mind")
solution = ""
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
output = []
difficulty = int(input("Enter difficulty (1-3):\n"))
if difficulty > 3:
    difficulty = 3
    for i in range(4):
        solution = solution + num_list.pop(random.randrange(len(num_list)))
elif difficulty < 1:
        difficulty = 1
        for i in range(2):
            solution = solution + num_list.pop(random.randrange(len(num_list)))
else:
    difficulty = 2
    for i in range(3):
        solution = solution + num_list.pop(random.randrange(len(num_list)))
guess = ""
while guess != solution:
        output = []
        guess = input(f"Enter a {difficulty + 1} digit number (don't repeat digits):\n")
        for i in range(difficulty + 1):
            if solution[i] == guess[i]:
                output.append("yes")
            elif solution.__contains__(guess[i]):
                output.append("ok")
            else:
                output.append("no")
        random.shuffle(output)
        for i in output:
            print(i,end=" ")

