try:
 print('welcome to rock,paper,scissor game')
 print('you are playing with python')
 print("this game doesn't contain score system,but we are sure that you enjoy this game")
 while True:
  import random
  x = ['rock','paper','scissor']
  comp = random.choice(x).lower()
  user = str(input('enter your choice:')).lower()
  if comp == user:
   print('computer choice is',comp,'and your choice is',user,)
   print('tie')
  elif  comp == 'rock' and user == 'paper':
   print('computer choice is',comp,'and your choice is',user,)
   print('you win')
  elif comp == 'paper' and user == 'scissor':
   print('computer choice is',comp,'and your choice is',user,)
   print('you win')
  elif comp == 'scissor' and user == 'rock':
   print('computer choice is',comp,'and your choice is',user,)
   print('you win')  
  else:
   print('computer choice is',comp,'and your choice is',user,)
   print('you lose')
   
  uc = input('do you want to play again - yes or no:').lower()
  if uc == 'yes':  
   continue
 else:
   print('thank you for playing')
   print('hope you enjoyed')
   break
  
  
   