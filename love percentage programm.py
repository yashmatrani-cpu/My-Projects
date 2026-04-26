try:
  import random
  
  
  print('welcome to this programm\nthis programm will tell love percentage of two person')
  while True:
   a = str(input('enter the name of first person:')).lower()
   b = str(input('enter the name of second person:')).lower()
   o3 = random.randint(0,100)
   o4 = random.randint(91,100)
   if (a == 'yash' and b == 'yashika') or (a == 'yashika' and b == 'yash'):
    print('love percentage is',o4,'%')
   else: 
   
    print(f"love percentage is {o3}%")
   k = str(input('you want to find love percentage of more names...?')).lower()
   if k == 'yes':
     continue
   elif k == 'no':
     print('byee!!')
     break
   else:
    print('yes ya no likho')
    

except Exception as err:
 print('error 404 not found')
 print(a,b)