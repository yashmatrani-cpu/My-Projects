try: 
 print('this programm will code your language and decode the coded language only coded by this programm')
 choice = str(input('enter if you want to code or decode any code code by this programm.?:'))
 import random
 words = ['qre','ree','eds','dsd','sfd','dsd','sdw' ,'sde','sdf','sdd',' ssd','ssd','ssd','ssd','swe']
 if choice == 'code':
  while True:
   a = (input('enter the secret word:'))
   fix = random.choice(words)
   if len(a) >= 3:
      a = a[::-1]
      a = fix + a + fix
      print(a)
      h = str(input('want to send some more messages..?'))
      match h:
          case 'yes':
              continue
          case 'no':
              break
          case _:
              print('write yes or no')
      
   elif len(a) == 2 or len(a) == 1:
     a = a[::-1]
     print(a)
     p = str(input('do you want to send more messages?:'))
     match p:
         case 'yes':
             continue
         case 'no':
             break
         case _:
             print('ENTER YES OR NO')
  else:
     print("this word can't be coded or decoded")          
           
 elif choice == 'decode':
    print('REMEMBER THIS CODE WILL ONLY DECODE CODE CODED BY THIS PROGRAMM ONLY else the decoded word will be wrong.')
    aa = input('enter your code')
    if len(aa) >= 3:
       aa = aa[::-1]
       aa = aa[3:-3]
       print(aa)
       print('ignore last and first three random lettters you will find the the word')
    elif len(aa)<3:
       print(aa[::-1])                                                                        
    else:
     print("this word can't be coded or decoded")          
except Exception as error:
   print("404 error not found may be this code or text can't be decode or coded")     


     
      