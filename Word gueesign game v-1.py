import random
food = ["PIZZA", "BURGER", "PASTA", "SUSHI", "TACO", "DOSA", "IDLI", "BIRYANI", "KOFTA", "NACHOS"]
sports = ["CRICKET", "FOOTBALL", "TENNIS", "BADMINTON", "HOCKEY", "KABADDI", "CHESS", "BOXING", "SWIMMING", "CYCLING"]
politics = ["MODI", "RAHUL", "KEJRIWAL", "MAMATA", "SHAH", "GANDHI", "NEHRU", "PATEL", "BOSE", "TILAK"]

try:
 ch = int(input('''Welcome to this guess the word game 1st version:
     press:
       1.for guess word of food items
       2.guess a word in politics sector
       3.guess a word in sports sector::'''))
except ValueError as error:       
 print(f"Maybe you just entered a worng input error {error} 404 not found")

def food_func():
  tries = 5
  food = ["PIZZA", "BURGER", "PASTA", "SUSHI", "TACO", "DOSA", "IDLI", "BIRYANI", "KOFTA", "NACHOS"]
  a = random.choice(food).upper()
  guessed = ["_"]*len(a)
  print(f"This word looks like this:{"_"*len(a)} and it has {len(a)} chars")
  while tries>0 and "_" in guessed:
    g1 = input("guess letters(first-last):").upper()
  
    if g1 in a:
      for char in range(len(a)):
        if a[char] == g1:
          guessed[char] =g1
          print(guessed)
          tries+=0
    else:
     print("wrong guess")
     tries-=1
  if not "_" in guessed:
    print(f"you've guessed a word {guessed}") 
  else:
    print(f"you've lost a word {a}")      
       
def sports_func():
  tries = 5
  sports = ["CRICKET", "FOOTBALL", "TENNIS", "BADMINTON", "HOCKEY", "KABADDI", "CHESS", "BOXING", "SWIMMING", "CYCLING"]
  a = random.choice(sports).upper()
  guessed = ["_"]*len(a)
  print(f"This word looks like this:{"_"*len(a)} and it has {len(a)} chars")
  while tries>0 and "_" in guessed:
    g1 = input("guess letters(first-last):").upper()
  
    if g1 in a:
      for char in range(len(a)):
        if a[char] == g1:
          guessed[char] =g1
          print(guessed)
          tries+=0
    else:
     print("wrong guess")
     tries-=1
  if not "_" in guessed:
    print(f"you've guessed a word {guessed}") 
  else:
    print(f"you've lost a word {a}")      
       
def politics_func():
  tries = 5
  politics = ["MODI", "RAHUL", "KEJRIWAL", "MAMATA", "SHAH", "GANDHI", "NEHRU", "PATEL", "BOSE", "TILAK"]  
  a = random.choice(politics).upper()
  guessed = ["_"]*len(a)
  print(f"This word looks like this:{"_"*len(a)} and it has {len(a)} chars")
  while tries>0 and "_" in guessed:
    g1 = input("guess letters(first-last):").upper()
  
    if g1 in a:
      for char in range(len(a)):
        if a[char] == g1:
          guessed[char] =g1
          print(guessed)
          tries+=0
    else:
     print("wrong guess")
     tries-=1
  if not "_" in guessed:
    print(f"you've guessed a word {guessed}") 
  else:
    print(f"you've lost a word {a}")      
    
match ch:
  case 1:
    food_func()
  case 2:
    politics_func()
  case 3:
    sports_func()
  
  

  
