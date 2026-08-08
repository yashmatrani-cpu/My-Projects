def parser(formula):
   try: 
    elements = {}
    current_name = ''
    current_count = ''
    for i in formula:
          if i.isupper():
               if current_name!='':
                    if current_count == '':
                         count = 1
                    else:
                         count = int(current_count)
                    elements[current_name] = count          
               current_name = i
               current_count = ''     
          elif i.islower():
               current_name = current_name+i
          elif i.isdigit():
               current_count+=i
    if current_name:
        count = int(current_count) if current_count else 1
        elements[current_name] = elements.get(current_name, 0) + count
    return elements
   except Exception as error:
       print('error 404 not found');
# f = input('enter formula')     
# print(parser(f))      

def splitter(formula):
     left,right = formula.split('-->')
     left = left.strip()
     left_C = left.split('+')
     right = right.strip()
     right_C = right.split('+')
     reactants = []
     products = []
     for i in left_C:
         reactants.append(i.strip())
     for _ in right_C:
         products.append(_.strip()) 
     return reactants,products
      
def balancer(equation):
    left, right = equation.split('-->') 
    reactants = []
    products = []
    for i in right.split('+'):
        products.append(i.strip())
    for y in left.split('+'):
        reactants.append(y.strip())
    for y in reactants:
        parser(y) 
    for i in products:
        parser(i)       
    for lc in range(1,11):
        for rc in range(1,11):
            l_total = {}
            p_total = {}
            for i in reactants:
                    for elem, cnt in parser(i).items():
                       l_total[elem] = l_total.get(elem, 0) + cnt * lc    
            for comp in products:
                for elem, cnt in parser(comp).items():
                    p_total[elem] = p_total.get(elem, 0) + cnt * rc    
            if l_total==p_total:
                return lc,rc         
    return None,None              

def main():
    equation = input('enter equation (ex:-H20 --> H2 + O2):')
    reactants, products = splitter(equation) 
    print(f"reactants->{reactants} and products:{products}")  
    r_parsed = []
    p_parser = []
    for i in reactants:
       r_parsed.append(parser(i))
    for _ in products:
         p_parser.append(parser(_))
    print(f"reactants:{r_parsed} \n products:{p_parser}")
    lc, rc = balancer(equation)
    if lc and rc:
        left, right = equation.split('-->')
        print(f"Balanced: {lc} {left.strip()} --> {rc} {right.strip()}")
    else:
        print(" Could not balance (try increasing range")
while True:
   main()
   a = int(input('press 1 for balance an equation and 2 for exit:')) 
   match a:
       case 1:     
         continue    
       case 2:
         print('thanks for using')
         break  
              
         

     