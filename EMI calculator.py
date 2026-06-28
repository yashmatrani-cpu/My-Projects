# ✅ Option 1: EMI / Loan Calculator (Banking)
# Kaam:
# User principal, interest rate (annual), tenure (months) daale
# Monthly EMI calculate karo
# Total interest aur total payment bhi dikhao
# Amortization schedule (month-by-month breakdown)

# Concepts:

# Math formula (EMI = P * r * (1+r)^n / ((1+r)^n - 1))
# Loops for amortization
# f-string formatting (₹, decimal places)
# File export (CSV)
# Real Use: Jab kabhi loan lena ho — apna EMI khud calculate kar sakta hai.
print('This is EMI calculator tell me your monthly tenure,principal,interest rate')
while True:
  a = input('enter 1 for continue the processes and 2 for exit:')
  match a:
    case '1':
       try:
        interest = float(input('enter Annual rate of interest:'))
        if interest<0:
         print('yeah have some fun bye')
         continue
        principal = float(input('enter principal:'))
        if principal == 0 or principal<0:
         print('then this makes no sense bye')
         continue
        tenure = int(input('enter tenure(months):'))
        if tenure == 0:
         print('if tenure is zero go to your home fool')
         continue
       except ValueError:
        print('Value error maybe you just entere a string')
       except Exception as error:
        print(f'{error} 404 not found') 
       try:          
           r1 = (interest/12)/100
           r = round(r1,2)
           print(f"your monthly interest is {r}%")
           emi1 = principal*r*(1 + r)**tenure/((1 + r)**tenure - 1)
           emi = round(emi1,2)
           print(f'your EMI is approximately {emi}')
           total_payment = round(emi*tenure)
           total_interest = total_payment-principal
       except Exception as error:
         print(f"{error} 404 not found")   
       print(f'''---summary---
            principal = {principal}rupees
            rate of interest(annual) = {interest}%
            tenure = {tenure}months
            EMI = {emi}rupees
            total payment = {total_payment}rupees
            total interest = {total_interest}rupees ''')  
       try:
         with open('loan_summary.txt','w') as f:
           f.write('Principal,Rate,Tenure,EMI,Total Payment,Total Interest\n')
           f.write(f'{principal},{interest},{tenure},{emi},{total_payment},{total_interest}\n')
       except Exception as error:
         print(f"{error} 404 not found")    
       continue  
    case'2':
      print('thanks for using')
      break
    case _:
      print('invalid input')
      continue
