def add(a,b):
  print(a + b)
def sub(a,b):
  print(a-b)
def product(a,b):
  print(a * b)
def expo(a,b):
  print(a**b)
def division(a,b):
  print(a/b)
def remainder(a,b):
  print(a%b)
print("welcome to calculator") 
print("this can perform all basic calculation")
a = int(input("enter first number for operation"))
b = int(input('enter the second number for operation'))
c = input("the operation[%,x,-,+,/,*,**,==,!=,ect]")
if c == ('%'):
   remainder()
elif c == ('-'):
  sub(a,b)
elif c == ('*'):
  product(a,b)
elif c == ('/'):
  division(a,b)
elif c == ("**"):
  expo(a,b)
elif c == (' + '):
  add(a,b)
elif c == ('=='):
  print(a == b)    
elif c == ('!='):   
  print(a !=b) 
else:
  print("invalid operation")                   

print('thank you for using')