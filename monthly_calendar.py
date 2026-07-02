try: 
 import calendar as cal
 print("welcome to this programm here we provide you 1" \
 "monthly calendar of your's choiceof year and month")
 while True: 
     a = int(input('''enter 1 for continue and 2 for exit:'''))
     match a:
        case 1:
           try: 
            yy = int(input('enter year(ex:2000):'))
            mm = int(input('enter month(ex:12):'))
            if mm>12 or mm<1:
                 print('enter month in between of 1-12')
                 continue
            print(cal.month(yy,mm))  
           except Exception as error:
               print(f"{error} 404 not found maybe you just enterd a string instead of integer") 
        case 2:
            print('thanks for using')
            break
except Exception as error:
   print(f"{error} 404 not found")  
##only for debugging
# import calendar
# print(calendar.__dir__)     
import os
files = os.listdir()
for f in files:
    print(f)
if "calendar.py" in files:
    os.remove('calendar.py')
   
