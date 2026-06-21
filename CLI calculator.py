def float_binary():
    try: 
     num = float(input('enter number(only positive values)'))
     if num<0:
          print('enter only positive number please')
          return
     else:
         try:
          precision = int(input('enter your precesion:'))
         except ValueError:
          print('invalid precision your defualt precision is 20')  
          precision = 20  
         int_binary = (bin(int(num)))  
         int_part = int(num)
         frac_part = num - int_part
         bits = ""
         for i in range(precision):
           frac_part *= 2
           if frac_part >= 1:
               bits += "1"
               frac_part -= 1
           else:
               bits += "0"   
         answer = (f"{int_binary}.{bits}")  
         print(answer)
    except ValueError:
        print('maybe you just enter a string')     
def int_binary():
   try: 
    num = int(input('enter number positively only:'))
    if num<0:
        print('positive only')
        return
    else:
        print(bin(num))
   except ValueError:
       print('maybe you just enter a string')     
def float_octal():
   try: 
    num = float(input('enter number:'))    
    if num<0:
        print('positive only')       
        return          
    else:
        try:
         precision = int(input('enter your precision:'))
        except ValueError:
           print('invalid precision your default presicion is 20') 
           precision = 20
        int_part = int(num)
        frac_part = num-int_part
        int_oct = (oct(int_part))
        digits = ""

        for i in range(precision):  
           frac_part *= 8

           digit = int(frac_part)
           digits += str(digit)

           frac_part -= digit

        answer = f"{int_oct}.{digits}"
        print(answer)
   except ValueError :
       print('MAYBE YOU JUST ENTERED A STRING')
def int_octal():
   try: 
    num = int(input('enter number(positive):'))
    if num<0:
        return
    else:
        print(oct(num))
   except ValueError:
       print("maybe you just entered a string")     
def float_hex():
   try: 
    num = float(input('enter number positive only'))       
    if num<0:
        print('positive number only please')
        return
    else:
        try:
         precision = int(input('enter your presicion'))
        except ValueError:
           print('invalid precision your default precision is 20') 
           precision = 20
        hex_digits = "0123456789ABCDEF"
        int_part = int(num)
        frac_part = num-int_part
        int_hex = (hex(int_part))
        digits = ''
        for i in range(precision):
            frac_part = frac_part*16
            digit = int(frac_part)
            frac_part-=digit
            digits += hex_digits[digit]
        answer = f"{int_hex}.{digits}"
        print(answer)
   except ValueError  :
       print('maybe you just entered a string')  
def int_hex():
   try: 
    num = int(input('enter number(positively):'))         
    if num<0:
        print("positive only")
        return   
    else:
        print(hex(num).upper())
   except ValueError:
       print('maybe you just entered a string')     
try:        
 print('welcon to CLI calculator')
 print('''this calculator can perform following tasks:-
      1.decimal-->binary
      2.decimal-->hexdecimal
      3.decimal-->octal
      4.exit''')
 while True:
  choice = int(input('enter 1,2,3,4 for respective tasks:'))
  match choice:
    case 1:
          choice1 = input("tell us wheather you're entering a float or integer? type int for integer and float for float:").lower()      
          match choice1:
              case 'float':
                  float_binary()
                  continue
              case 'int':
                  int_binary()
                  continue
              case _:
                  print('invalid output')  
                  continue      
    case 2:
          choice1 = input("tell us wheather you're entering a float or integer? type int for integer and float for float:").lower()      
          match choice1:
              case 'float':
                  float_hex()
                  continue
              case 'int':
                  int_hex()
                  continue
              case _:
                  print('invalid output') 
                  continue     
    case 3:
          choice1 = input("tell us wheather you're entering a float or integer? type int for integer and float for float:").lower()     
          match choice1:
              case 'float':
                  float_octal()
                  continue
              case 'int':
                  int_octal()
                  continue
              case _:
                  print('invalid output')  
                  continue          
    case 4:
          break
    case _:
          print('invalid operation')
          continue   
except ValueError:
    print('maybey you just entered a string instead of integer')                                       
except Exception as error:
    print(f'{error} not found')      