##lens_formula(): Solves mirror/lens distance ($1/f = 1/v - 1/u$) and magnification.force_momentum(): Computes force ($F = ma$) and momentum ($p = mv$).unit_converter(): Converts basic SI units like Celsius to Kelvin or Joules.
def lens():
  try: 
       a = input('what do you want to find?\n1.object distance\n2.image distance\n3.Focal length\n\nenter in form of v,u,f')
       if a == 'v':
          f = float(input('enter focal length of mirror(follow sign convention):'))
          u = float(input('enter object distance(follow sign convention):'))
          if u+f==0:
             print('v = undefined')
          elif 0<u+f<0.000125:
             print('infinity as u+f is aprroximately 0')  
          else:    
            v =  (f * u) / (u + f)
            print('v=',v)
            print('mag. = ' ,v/u)
       elif a == 'u':
             f = float(input('enter focal length of mirror(follow sign convention):'))
             v = float(input('enter image distance:'))
             if (f-v)==0:
                print('undefined')
             else:    
               u = (f * v) / (f - v)
               print('u = ',u)
               print('mag. = ',v/u)
       elif a == 'f':
             v = float(input('enter image distance (follow sign convention): '))
             u = float(input('enter object distance (follow sign convention): '))
             if u - v == 0:
                 print('f = undefined (plane surface)')
             else:
                 f = (v * u) / (u - v)
                 print('f =', f)
                 print('mag. = ',v/u)
       else:
           print('invalid choice')          

  except ValueError:
     print('enter a integer or a decimal value please')
  except ZeroDivisionError:
     print('there is zero in denominator somewhere 404 NOT FOUND')
def mirror():
    try:
        a = input('what do you want to find?\n1.image distance (v)\n2.object distance (u)\n3.focal length (f)\n\nenter v, u, or f: ')
        if a == 'v':
            f = float(input('enter focal length (follow sign convention): '))
            u = float(input('enter object distance (follow sign convention): '))
            if u - f == 0:
                print('v = undefined (object at focus, image at infinity)')
            else:
                v = (f * u) / (u - f)
                print('v =', v)
                if u != 0:
                    print('magnification =', -v/u)
        elif a == 'u':
            f = float(input('enter focal length (follow sign convention): '))
            v = float(input('enter image distance (follow sign convention): '))
            if v - f == 0:
                print('u = undefined (image at focus, object at infinity)')
            else:
                u = (f * v) / (v - f)
                print('u =', u)
                if u != 0:
                    print('magnification =', -v/u)
        elif a == 'f':
            v = float(input('enter image distance (follow sign convention): '))
            u = float(input('enter object distance (follow sign convention): '))
            if u + v == 0:
                print('f = undefined (plane mirror)')
            else:
                f = (u * v) / (u + v)
                print('f =', f)
                if u != 0:
                    print('magnification =', -v/u)
        else:
            print('Invalid choice')
    except ValueError:
        print('Please enter a valid number')
    except ZeroDivisionError:
        print('Division by zero error')    
def force():
   try: 
    b = input('What do you want to find?\n1.force\n2.mass\n3.acceleration(ex:-write force to find force):').lower()    
    if b == 'force':
        m = float(input('enter mass of object(kg):'))
        a = float(input('enter acceleration(m/s^2):')) 
        print('f = ',m*a)
    elif b == 'mass':
        a = float(input('enter acceleration(m/s^2):'))
        f = float(input('enter force applied(N):'))   
        m = f/a
        print('m = ',m)
    elif b == 'acceleration':
        f = float(input('enter forced applied:'))
        m = float(input('enter mass(kg):'))
        a = f/m
        print('a = ',a)
    else:
        print('invalid choice')     
   except ValueError:
       print('Enter a number not a string fool')
   except ZeroDivisionError:
       print('There is zero in denominator please check it out and try again')     
def momentum():
    try:
        c = input('What do you want to find?\n1. momentum (p)\n2. mass (m)\n3. velocity (v)\n\nenter p, m, or v: ').lower()
        if c == 'p' or c == 'momentum':
            m = float(input('enter mass (kg): '))
            v = float(input('enter velocity (m/s): '))
            print('p =', m * v, 'kg·m/s')
        elif c == 'm' or c == 'mass':
            p = float(input('enter momentum (kg·m/s): '))
            v = float(input('enter velocity (m/s): '))
            if v == 0:
                print('Velocity zero → mass undefined (infinite)')
            else:
                print('m =', p / v, 'kg')
        elif c == 'v' or c == 'velocity':
            p = float(input('enter momentum (kg·m/s): '))
            m = float(input('enter mass (kg): '))
            if m == 0:
                print('Mass zero → velocity undefined (infinite)')
            else:
                print('v =', p / m, 'm/s')
        else:
            print('Invalid choice')
    except ValueError:
        print('Please enter a valid number')
    except ZeroDivisionError:
        print('Division by zero error')
def converter():
   try: 
    print('1.Celsius-->Kelvin\n2.Kelvin-->Celsius\n3.Joules-->Calories\n4.Calories-->Joules')
    a = int(input('enter 1,2,3,4:'))
    match a:
        case 1:
            c = float(input('enter C:'))
            k = c+273.15
            print('k=',k)
        case 2:
            k = float(input('enter K:'))
            c = k-273.15
            print('c=',c)
        case 3:
            j = float(input('enter J:'))
            cal = j/4.184
            print('cal = ',cal)
        case 4:
            cal = float(input('enter Cal:'))    
            j = cal*4.184
            print('J = ',j)
        case _:
            print('invalid output')    
   except ValueError:
        print('Please enter a valid number')
   except ZeroDivisionError:
        print('Division by zero error')          
print('welcome to this simple physics calculator suitale for classes 9th-11th')
while True:
   ch = input('what do you want to do \n\n1.operations with lens formula\n2.operations with mirror formula\n3.operations with force\n4.operations on momentum\n5.try converter\n6.exit\n\nenter in form of 1,2,3,4,5,6: ')
   match ch:
    case '1':
        lens()
    case '2':
        mirror()
    case '3':
        force()
    case '4':
        momentum()
    case '5':
        converter()   
    case '6':
           break
    case _:
           print('errro 404 not found')                   


         