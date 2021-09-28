from random import randint
import turtle
import time

instructions = open('instructions.txt','r')
exec(instructions.read())
instructions.close()

print('Enter index')
n = input()
drawing(n)

time.sleep(3)
