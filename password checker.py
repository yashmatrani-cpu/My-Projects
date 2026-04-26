try:
 while True:
  import random
  o = random.randint(1,3)
  o2 = random.randint(3,5)
  o3 = random.randint(5,7)
  o4 = random.randint(5,8)
  spssecial = '!@#$%^&*()'
  print('this programm can rate your password strength from 1-10')
  p = (input('enter your password here:'))
  Has_special = False
  for i in p:
    if i in spssecial:
        Has_special = True
  if Has_special == True and len(p)>5:
     print(10,'number good password')
  elif Has_special == False and len(p)>5:
    print(o4,'good but can add special characters')
  elif Has_special == True and len(p)<5:
    print(o3,'good but length of password is very short')
  elif Has_special == False and len(p)<5:
    print(o,'change it add some special characters and increase the length of your password')
  else:
    print("it's okok but definately you can improve it")
  choice = str(input('want to rate some more passwords..?')).lower() 
  match choice:
    case 'yes':
      continue
    case 'no':
      break
    case _:
      print('some error occured')
      break   
except Exception as error:
   print(error,'404 not found')