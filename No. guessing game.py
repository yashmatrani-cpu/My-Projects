print("welcome to this number guessing quiz")
print("in this quiz u have to guess a number guessed by this programm")
print("in this quiz python guess a number between 1-100","and u have to guess the number")
import random
number = random.randint(1,100)
attemps = 0
while True:
   a = int(input("guess the no."))
   attemps += 1
   if a>number:
      print("no wrong try agan,HINT:no. is smaller than this")
   elif a<number:
      print("wrong number try again,HINT:no. is larger than this")   
   else:
      print("correct")
      break
print("completed in",attemps,"attempts.")            