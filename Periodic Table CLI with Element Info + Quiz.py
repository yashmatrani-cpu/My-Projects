try:
 import random
 class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def about(self):
        print(f"you're {self.name} of age {self.age}")    
 name = input('enter your name:')
 age = input('enter your age:')        
 u = user(name,age)        
 u.about()
        
 elements = {
    1:  {"symbol": "H",  "name": "Hydrogen",   "mass": 1.008,  "category": "Non-metal",      "config": "1s¹"},
    2:  {"symbol": "He", "name": "Helium",     "mass": 4.002,  "category": "Noble gas",       "config": "1s²"},
    3:  {"symbol": "Li", "name": "Lithium",    "mass": 6.941,  "category": "Alkali metal",    "config": "[He]2s¹"},
    4:  {"symbol": "Be", "name": "Beryllium",  "mass": 9.012,  "category": "Alkaline earth",  "config": "[He]2s²"},
    5:  {"symbol": "B",  "name": "Boron",      "mass": 10.81,  "category": "Metalloid",       "config": "[He]2s²2p¹"},
    6:  {"symbol": "C",  "name": "Carbon",     "mass": 12.011, "category": "Non-metal",       "config": "[He]2s²2p²"},
    7:  {"symbol": "N",  "name": "Nitrogen",   "mass": 14.007, "category": "Non-metal",       "config": "[He]2s²2p³"},
    8:  {"symbol": "O",  "name": "Oxygen",     "mass": 15.999, "category": "Non-metal",       "config": "[He]2s²2p⁴"},
    9:  {"symbol": "F",  "name": "Fluorine",   "mass": 18.998, "category": "Non-metal",       "config": "[He]2s²2p⁵"},
    10: {"symbol": "Ne", "name": "Neon",       "mass": 20.180, "category": "Noble gas",       "config": "[He]2s²2p⁶"},
    11: {"symbol": "Na", "name": "Sodium",     "mass": 22.990, "category": "Alkali metal",    "config": "[Ne]3s¹"},
    12: {"symbol": "Mg", "name": "Magnesium",  "mass": 24.305, "category": "Alkaline earth",  "config": "[Ne]3s²"},
    13: {"symbol": "Al", "name": "Aluminium",  "mass": 26.982, "category": "Post-transition", "config": "[Ne]3s²3p¹"},
    14: {"symbol": "Si", "name": "Silicon",    "mass": 28.085, "category": "Metalloid",       "config": "[Ne]3s²3p²"},
    15: {"symbol": "P",  "name": "Phosphorus", "mass": 30.974, "category": "Non-metal",       "config": "[Ne]3s²3p³"},
    16: {"symbol": "S",  "name": "Sulfur",     "mass": 32.065, "category": "Non-metal",       "config": "[Ne]3s²3p⁴"},
    17: {"symbol": "Cl", "name": "Chlorine",   "mass": 35.453, "category": "Non-metal",       "config": "[Ne]3s²3p⁵"},
    18: {"symbol": "Ar", "name": "Argon",      "mass": 39.948, "category": "Noble gas",       "config": "[Ne]3s²3p⁶"},
    19: {"symbol": "K",  "name": "Potassium",  "mass": 39.098, "category": "Alkali metal",    "config": "[Ar]4s¹"},
    20: {"symbol": "Ca", "name": "Calcium",    "mass": 40.078, "category": "Alkaline earth",  "config": "[Ar]4s²"},
}
 q = [
    ["What is the symbol of Hydrogen?", "A. H", "B. He", "C. Hy", "D. Hg", "A"],
    ["Which element has the symbol 'Na'?", "A. Nitrogen", "B. Nickel", "C. Sodium", "D. Neon", "C"],
    ["What is the atomic number of Carbon?", "A. 4", "B. 6", "C. 8", "D. 12", "B"],
    ["Which element is a Noble gas?", "A. Oxygen", "B. Chlorine", "C. Argon", "D. Sodium", "C"],
    ["What is the atomic mass of Magnesium (approx)?", "A. 22", "B. 24", "C. 26", "D. 28", "B"],
    ["Which element has the symbol 'K'?", "A. Potassium", "B. Krypton", "C. Calcium", "D. Chromium", "A"],
    ["What is the atomic number of Oxygen?", "A. 6", "B. 8", "C. 10", "D. 16", "B"],
    ["Which category does Silicon belong to?", "A. Metal", "B. Non-metal", "C. Metalloid", "D. Noble gas", "C"],
    ["What is the symbol of Calcium?", "A. Ca", "B. Cu", "C. C", "D. Cl", "A"],
    ["Which element is a halogen?", "A. Sodium", "B. Chlorine", "C. Argon", "D. Magnesium", "B"],
    ["What is the atomic number of Aluminium?", "A. 12", "B. 13", "C. 14", "D. 27", "B"],
    ["Which element has electron configuration [He]2s²2p⁴?", "A. Oxygen", "B. Nitrogen", "C. Fluorine", "D. Neon", "A"],
    ["What is the symbol for Beryllium?", "A. B", "B. Be", "C. Br", "D. Ba", "B"],
    ["Which alkali metal is in period 4?", "A. Lithium", "B. Sodium", "C. Potassium", "D. Rubidium", "C"],
    ["What is the atomic mass of Argon (approx)?", "A. 32", "B. 36", "C. 40", "D. 44", "C"],
    ["Which element has 8 protons?", "A. Nitrogen", "B. Oxygen", "C. Fluorine", "D. Neon", "B"],
    ["What is the symbol for Iron?", "A. Ir", "B. Fe", "C. In", "D. Fr", "B"],
    ["Which element is a liquid at room temperature (among these)?", "A. Mercury", "B. Bromine", "C. Gallium", "D. Cesium", "A"],
    ["What is the atomic number of Gold?", "A. 47", "B. 79", "C. 82", "D. 92", "B"],
    ["Which element is the lightest?", "A. Helium", "B. Hydrogen", "C. Lithium", "D. Beryllium", "B"],
]
 def quiz():
    points = 0
    for i in range(len(q)):
        e = q[i]
        print(
            e[0]
        )
        print(
            e[1],
            e[2],
            e[3],
            e[4]
        )
        ans = input('''enter option number(for exit press E):''').upper()
        if ans==e[5]:
            print('correct answer')
            points+=1
        elif ans=='E':
            print(f"your score is {points}")
            break    
        else:
            print('wrong answer')    
            points+=0
 print('welcome to preiodic table CLI programm here you can either participate in a quiz or gain knowledge about periodic table elements(1-20)')
 a = input('''press:
 1-for quiz programm.
 2-for search about any elements.''')
 match a:
    case '1':
        quiz()
    case '2':
      while True: 
          atomic_no = int(input('--press 100 for exit--enter atomic number of element(1-20):'))
          if atomic_no==100:
              break
          info = elements[atomic_no]
          print(f"Symbol: {info['symbol']}, Name: {info['name']}, Mass: {info['mass']},category: {info['category']} configuration:{info['config']} ")
except Exception as error:
   print(f"error {error} 404 not found")        


