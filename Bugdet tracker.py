try:
 transaction = []
 def choice():
    print('''what do you want to do?
         press 1 for add budget 
         press 2 for spend money
         press 3 for see your money left
         press 4 for exit''')
 def bye():
    print('bye thanks for using')    
 init_budget = int(input('enter your todays budget:'))      
 while True:
    choice()
    a = int(input('enter your choice:'))
    match a:
        case 1:
            add_budget = int(input("how many money do you wan't to add in your budget:"))
            init_budget = add_budget + init_budget
            print(f'now your budget is{init_budget}')
        case 2:
            spend = int(input('how much you want to spend money:'))
            on_what = str(input(f"on what activity do you wan't to spend {spend}rupees..?"))
            transaction.append(on_what)
            if spend>init_budget:
                print('not enough money try next time with more budget this programm is closing automatically')
                bye()
                break
            elif spend==init_budget:
                confirmation = input("are you sure about your descision..? after this you've left with no money type yes for continue and no for closing the programm ")
                match confirmation:
                   case 'yes':
                        print(f'current balance is{0}')
                        init_budget = 0
                        continue
                   case 'no':
                        bye()
                        break
            else:
                print(f'money left = {init_budget - spend}')
                init_budget = init_budget - spend
                continue                          
        case 3:
            print(f'money left = {init_budget}')    
        case 4:
            bye()
            print(f'you have spent your money on {','.join(transaction)} ')   
            break
            
 print(f"you have spent your money on {', '.join(transaction)}")      
except Exception as error:
    print(f'''error {error} found 404 not found programm crashed
          may be you just enterd a string at a integer section''')
        
            