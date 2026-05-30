##ALEBRAIC CALCULATOR PROJECT NUMBER 34TH
try:
 import sympy
 import time
 exit_programm = False
 x,y = sympy.symbols('x y')
 print('''this programm can perform these simple tasks:
         1-solve linear eqaution in one variable
         2-solve pair of linear eq in two variable with graph
         3-can tell you identies
         4-factorise
         5-simplify
         6-simple calculate anything like 123x323
         7-exit
         ''')
 while not exit_programm:
  jmc = (input("what do you want to do,press 1,2,3,4,5 for each tasks respectively.ex-I want to do simplify so I will press '5' "))
  match jmc:
    case '1':
        try: 
            print('standard form of equation is ax+b = c write co efficients')
            a = int(input('enter a:'))
            b = int(input('enter b:'))
            c = int(input('enter c:'))
            eq1 = sympy.Eq(a*x+b,c)
            sol1 = sympy.solve(eq1,x)
            print(f"value of variable is {sol1}")  
        except ValueError:
                 print('maybe you just entered a string instead of integer')  
    case '2':
      try:  
        pair_x, pair_y = sympy.symbols('x,y')

        print('enter coefficients of first equation (a1, b1, c1)')
        pair_a1 = int(input('enter a1 of equation 1:'))
        time.sleep(0.75)
        pair_b1 = int(input('enter b1 of equation 1:'))
        time.sleep(0.75)
        pair_c1 = int(input('enter c1 of equation 1:'))
        time.sleep(0.75)

        pair_eq1 = sympy.Eq(pair_a1*pair_x + pair_b1*pair_y + pair_c1, 0)

        print('processing.....')
        time.sleep(2)
        print(f'first equation: {pair_a1}x + {pair_b1}y + {pair_c1} = 0')
        print('now second equation')
        pair_a2 = int(input('enter a2:'))
        time.sleep(0.75)
        pair_b2 = int(input('enter b2:'))
        time.sleep(0.75)
        pair_c2 = int(input('enter c2:'))
        time.sleep(3)
        print('processing......')
        time.sleep(4)
        print(f'''equations:
{pair_a1}x + {pair_b1}y + {pair_c1} = 0
{pair_a2}x + {pair_b2}y + {pair_c2} = 0''')

        pair_eq2 = sympy.Eq(pair_a2*pair_x + pair_b2*pair_y + pair_c2, 0)

        pair_sol = sympy.solve((pair_eq1, pair_eq2), (pair_x, pair_y))
        pair_det = pair_a1*pair_b2 - pair_a2*pair_b1

        if pair_det != 0:
            print(f"Unique solution: x = {pair_sol[pair_x]}, y = {pair_sol[pair_y]}")
        elif (pair_a1*pair_b2 == pair_a2*pair_b1) and (pair_b1*pair_c2 == pair_b2*pair_c1):
            print("Infinite solutions (coincident lines)")
        else:
            print("No solution (parallel lines)")

        
        ROWS = 20
        COLS = 80
        grid = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

        x_min, x_max = -10, 10
        y_min, y_max = -10, 10
        scale_x = COLS / (x_max - x_min)
        scale_y = ROWS / (y_max - y_min)

        def to_grid(x_val, y_val):
            col = int((x_val - x_min) * scale_x)
            row = ROWS - 1 - int((y_val - y_min) * scale_y)   # flip vertical
            return col, row

        # draw axes
        for i in range(COLS):
            x_plt = x_min + i / scale_x
            c, r = to_grid(x_plt, 0)
            if 0 <= r < ROWS: grid[r][c] = '-'
        for j in range(ROWS):
            y_plt = y_max - j / scale_y
            c, r = to_grid(0, y_plt)
            if 0 <= c < COLS: grid[r][c] = '|'
        c0, r0 = to_grid(0, 0)
        grid[r0][c0] = '+'

        def plot_line(grid, a, b, c, sym):
            if b != 0:
                step = 0.1
                x_plt = x_min
                while x_plt <= x_max:
                    y_plt = (-a * x_plt - c) / b
                    col, row = to_grid(x_plt, y_plt)
                    if 0 <= col < COLS and 0 <= row < ROWS:
                        grid[row][col] = sym
                    x_plt += step
            else:  # vertical line
                x_const = -c / a
                step = 0.1
                y_plt = y_min
                while y_plt <= y_max:
                    col, row = to_grid(x_const, y_plt)
                    if 0 <= col < COLS and 0 <= row < ROWS:
                        grid[row][col] = sym
                    y_plt += step

        plot_line(grid, pair_a1, pair_b1, pair_c1, '*')
        plot_line(grid, pair_a2, pair_b2, pair_c2, '#')

        if pair_det != 0:
            ix = pair_sol[pair_x]
            iy = pair_sol[pair_y]
            col, row = to_grid(ix, iy)
            if 0 <= col < COLS and 0 <= row < ROWS:
                grid[row][col] = 'X'

        for row in grid:
            print(''.join(row))

        if pair_det != 0:
         print(f"Intersection at x = {float(ix):.2f}, y = {float(iy):.2f}")
      except ValueError:
                print('maybe you just entered a string instead of integer')  
    case '3':
     try:   
        a,b,c = sympy.symbols('a b c')
        v = sympy.symbols('v')
        print('''this can expand these identities:
              1.(a+b)^2
              2.a^2-b^2
              3.(a-b)^2
              4.(a+b)^3
              5.(a-b)^3
              6.(a+b+c)^2
              7.(v+a)(v+b) where 'v' is variable''')
        aa = (input('enter expression to expand , for ex press 1 for-(a+b)^2 on your keyboard for expansion write expression here:')).lower()
        if aa == '1':
         expansion1 = sympy.expand((a+b)**2)
         print(expansion1)
        elif aa == '2':
         expansion2 = sympy.expand(a**2-b**2)
         print(expansion2)
        elif aa == '3':
         expansion3 = sympy.expand((a-b)**2)
         print(expansion3)
        elif aa == '4':
         expansion4 = sympy.expand((a+b)**3)
         print(expansion4)
        elif aa == '5':
         expansion5 =sympy.expand((a-b)**3)
         print(expansion5)
        elif aa == '6':
         expansion6 = sympy.expand((a+b+c)**2)
         print(expansion6)     
        elif aa == '7':
         expansion7 = sympy.expand((v+a)*(v+b))
         print(expansion7)
        else:
           print('invalid operation')                  
     except Exception as error3:
        print(f"{error3} 404 not found")      
    case '4':
     try:   
        expr = input("enter expression: ")
        expr = expr.replace("^", "**")
        result = sympy.factor(sympy.sympify(expr))
        print(result)
     except Exception as error4:
        print(f"{error4} 404 not found")       
    case '5':
        try:    
            expr = input("enter expression: ")
            expr = expr.replace("^", "**")
            result = sympy.simplify(sympy.sympify(expr))
            print(result)
        except Exception as error5:
           print(f"{error5} 404 not found")         
    case '6':
      try:    
         yc = input('what do you want,press 1-submission,2-subtraction,3-multiplication,4-division')
         match yc:
             case '1':  
              try:             
                    def sum():
                      total = 0
                      d = int(input('how many numbers do you want to add?:'))
                      for _ in range(1,d+1):
                        num = int(input(f'enter {_} number'))
                        total+=num
                      return f"total = {total}" 
                    print(sum()) 
              except ValueError:
                    print('maybe you just entered a string instead of integer')  
             case '2':
              try:     
               def sub():

                     e = int(input("How many numbers do you want to subtract?: "))

                     first = int(input("Enter 1 number: "))

                     total_2 = first

                     for i in range(2, e + 1):
                         num2 = int(input(f"Enter {i} number: "))
                         total_2 -= num2

                     return f"Answer = {total_2}"
               print(sub())
              except ValueError:
                 print('maybe you just entered a string instead of integer')  
             case '3':
                try: 
                      def mul():
                         e = int(input("How many numbers do you want to multiply?: "))
                         total_3 = 1
                         for i in range(1, e + 1):
                          num = int(input(f"Enter {i} number: "))
                          total_3 *= num

                         return f"Answer = {total_3}"
                      print(mul())
                except ValueError:
                 print('maybe you just entered a string instead of integer')  
                  
             case '4':
              try:
               def div():
                   e = int(input("How many numbers do you want to divide?: "))
                   first = float(input("Enter 1 number: "))
                   total = first
                   for i in range(2, e + 1):
                       num = float(input(f"Enter {i} number: "))
                       if num == 0:                     
                          return "Cannot divide by zero"
                       total /= num
                   return f"Answer = {total}"
               print(div())
              except ValueError:
                 print('maybe you just entered a string instead of integer')  
             case _:
               print("invalid operation")   
      except Exception as error6:
          print(f"{error6} 404 not found")      
    case '7':
        exit_programm = True             
    case _:
      print('invalid option') 
except Exception as univresal_error:
   print(f"{univresal_error} 404 not found")        

