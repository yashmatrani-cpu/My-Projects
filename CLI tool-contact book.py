contacts = []
while True:
 a = input('''---welcome to contact book---
       1.add contact
       2.search contact
       3.delete contact
       4.show all contacts
       5.exit
          
       press 1,2,3,4,5 for performing above tasks''')
 match a:
   case '1':
     try:  
      b = int(input('how many contacts o you want to add?:'))
      for i in range(b):
        c = input('enter name:').lower()
        d = (input('enter phone no.:')).lower()
        contact = (f'''name:{c}       phone no:{d}''')
        contacts.append(contact)
        print(contact)
        f =  open('Contact_book.txt','a')
        f.write(str(contacts))
        f.close()
        print('contact saved succesfully')
     except Exception as error:
       print(f"{error} 404 not found may be you just entered a sring or a integer")   
       continue
   case '2':
       try:  
         srch = input('enter name of which contact do have to search:').lower()
         for i in range(len(contacts)):
            if srch in contacts[i]:
               print(contacts[i])
            else:
              print('no contatc found')
              continue   
       except Exception as error:
         print(f"{error} 404 not found")  
         continue
   case '3':
    try: 
     scrch2 = input('enter name of contact which you want to remove:').lower()
     for i in range(len(contacts)):
       if scrch2 in contacts[i]:
         contacts.remove(contacts[i])
         with open('Contact_book.txt','a') as f:
           f.write(str(contacts))           
       else:
         print('not found try again')
         continue  
    except Exception as e:
      print(f"{e} 404 not found try again")   
      continue
       

   case '4':
     for i in range(len(contacts)):
       print(contacts[i])
       continue
   case '5':
     print('thanks for using') 
     break              

       