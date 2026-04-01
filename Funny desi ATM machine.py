print('welcome to ATM mahine')
print('this ATM machine is secured 100%')
a = 1234
print('put your pin to interact with your account')
b = int(input('type your pin here:,please type only number if you enter a word the system will crash:'))

match b:
    case 1234:
        print('correct code your balance is 5000 rupees')
        j = str(input('choose if u want to withdraw or deposit amount:'))
        if j == ('withdraw'):
             o = int(input('how much money do you want to withdraw..?:'))
             if o > 5000:
              print('aukaat ke bahaar')   
              print('your balance go in negetive')
             else: 
              print('amount left =',5000 - o)  
        elif j == ('deposit'):
                
             print('how much do u want to add')
             x = int(input('enter amount u want to deposit:'))
             print('net balance:',x + 5000)
        else:
             print('invalid operation')     


    case _:
        print('oo bhai kyu chori krne aaya h chala jaa chup chaap ghar vrna police bulaadunga ek aur baar try krle bas LAST CHANCE')       
        c = int(input('enter pin LAST CHANCE:'))
        if c != 1234:
           print('no access wrong pin again')
        else:
           print('acces granted,sorry for doubting on u')  
           h = str(input('choose if u want to withdraw or deposit amount:'))
           if h == ('withdraw'):
             m = int(input('how much money do you want to withdraw..?:'))
             if m>5000:
                  print('aukaat ke bahaar')   
                  print('your balance go in negetive')
             else:    
              print('amount left =',5000 - m) 
           else:     
             print('how much do u want to add')
             x = int(input('enter amount you want to deposit:'))
             print('net balance:',x + 5000)
print('chal tera kaam hogya ab bhaag ja yaha se ghar ko chai aur khana khaane de🤣')
           
           