import random
import sympy
score = 0
print("this programm is for practicing quadratic and linear eqaution in a fun way there is a score sysytem in this programm.  HIGH SCORE=HIGH MARKS")
a = input('press 1 for linear eqautions practice and 2 for quadratic eqaution practice')
def linear():
    try:  
      score = 0
      x = sympy.symbols('x')
      while True:
            a = random.randint(-20,30)
            if a == 0:
                 continue
            b = random.randint(0,50)
            c = random.randint(-10,10)
            eqaution = f"{a}x + {b} = {c}"
            e = sympy.solve(sympy.Eq(a*x+b,c),x)[0]
            print(eqaution)
            ans = float(input('enter your value of x'))
            if abs(float(e) - ans) < 0.001:
                  print('correct answer')
                  score+=1
                  ch = input('wanna try more?').lower()
                  match ch:
                        case 'yes':
                              continue
                        case 'no':
                              print('hope for best try again!!')
                              print(f"your score is {score}")
                              break
                        case _:
                            print('invalid operation')
            else:
                  print(f"wrong right answer is {e}")
                  ch = input('try agin?').lower()
                  match ch:
                        case 'yes':
                              continue
                        case 'no':
                              print('hope for the best bye!!')
                              print(f"your score is {score}")
                              break
                        case _:
                              print('invalid operation')
                              continue
    except ValueError as error:
         print(f"{error} found may be you just entered a string in the place of an integer fool!")            
    except Exception as error:
         print('error 404 not found try again later')        
def quadratic():
      score = 0
      x = sympy.symbols('x')
      while True:
            a = random.randint(-20,30)
            if a == 0:
                 continue
            b = random.randint(0,50)
            c = random.randint(-10,10)
            equation = f"{a}x^2+{b}x-{c} = 0"
            print(f'your eqaution is {equation}')
            d = b**2 + 4*a*c
            if d < 0:
                 print('imagenary roots')
                 continue
            e = sympy.solve(sympy.Eq(a*x**2+b*x-c,0),x)
            ans = float(input('enter any 1 value of x'))
            if any(abs(float(root)-ans) < 0.001 for root in e):
                  print('correct answer')
                  score+=1
                  ch = input('wanna try more?').lower()
                  match ch:
                        case 'yes':
                              continue
                        case 'no':
                              print('hope for best try again!!')
                              print(f"your score is {score}")
                              break
                        case _:
                            print('invalid operation')
            else:
                  print(f"wrong right answer is {e}")
                  ch = input('try agin?').lower()
                  match ch:
                        case 'yes':
                              continue
                        case 'no':
                              print('hope for the best bye!!')
                              print(f"your score is {score}")
                              break
                        case _:
                              print('invalid operation')
                              continue     
match a:
     case'1':
          linear()
     case '2':
          quadratic()     
                                 

