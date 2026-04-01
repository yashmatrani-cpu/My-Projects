Money = 0
def na():
    print('your next question is on screen')
print('''welcome to KBC kaunb banega crorepati!!!!
      there are 4 levels
      level 1-10000 question
      level 2-50000 question
      level 3-100000 uestion
      level 4-1crore to 7 crore question''')
print('''rules:-
                 no cheating
                 one answer wrong you are disqualified
                 TO DEVIYO AUR SAJJANO APKA SWAGAT HAI KAUN BANEGA CROREPATI''')
print('to pehela prashn aapki screen ke upar')

##list/tuple-
q = [
["Who discovered gravity?", "A.Einstein", "B.Newton", "C.Galileo", "D.Tesla", "B"],
["Chemical formula of water?", "A.CO2", "B.H2O", "C.O2", "D.NaCl", "B"],
["Largest planet?", "A.Earth", "B.Mars", "C.Jupiter", "D.Venus", "C"],
["15 × 3 = ?", "A.30", "B.45", "C.60", "D.50", "B"],
["India got independence in?", "A.1945", "B.1946", "C.1947", "D.1950", "C"],

["Fastest land animal?", "A.Lion", "B.Cheetah", "C.Tiger", "D.Horse", "B"],
["Square root of 81?", "A.7", "B.8", "C.9", "D.10", "C"],
["Currency of USA?", "A.Euro", "B.Rupee", "C.Dollar", "D.Yen", "C"],
["Gas essential for breathing?", "A.Nitrogen", "B.Oxygen", "C.Carbon", "D.Helium", "B"],
["First man on moon?", "A.Armstrong", "B.Newton", "C.Edison", "D.Tesla", "A"],

["7 × 8 = ?", "A.54", "B.56", "C.64", "D.48", "B"],
["Capital of Japan?", "A.Seoul", "B.Tokyo", "C.Beijing", "D.Bangkok", "B"],
["Which is a programming language?", "A.HTML", "B.CSS", "C.Python", "D.HTTP", "C"],
["Human heart chambers?", "A.2", "B.3", "C.4", "D.5", "C"],
["Boiling point of water?", "A.90°C", "B.50°C", "C.100°C", "D.80°C", "C"],

["Largest ocean?", "A.Atlantic", "B.Indian", "C.Pacific", "D.Arctic", "C"],
["5² = ?", "A.10", "B.20", "C.25", "D.15", "C"],
["Which device used to call?", "A.Mouse", "B.Keyboard", "C.Phone", "D.Monitor", "C"],
["Sun is a?", "A.Planet", "B.Star", "C.Asteroid", "D.Comet", "B"],
["National sport of India (commonly known)?", "A.Cricket", "B.Hockey", "C.Football", "D.Kabaddi", "B"]
]
levels = [10000,50000,100000,'SAAT CRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRREEEEEE']
for i in range(len(q)):
    e = q[i]
    print(e[0])
    print(e[1],
          e[2],
          e[3],
          e[4])
    ans1 = str(input('lock kiya jaaye..?')).upper()
    if ans1 == e[5]:
        print('''yeh jawaab.........BILKUL SAHI HAIII!!!
                 ab chalte hai agle padaav ki taraf''')

        if i == 4:
            Money = levels[0]
        elif i == 9:
            Money = levels[1]
        elif i == 14:
            Money = levels[2]
        elif i == 19:
            Money = levels[3]
                      
        na()
    else:
        print('wrong answer') 
        print('AAP',Money,'dhanrashi aaj apne saath le jaa sakte h,yeh aapke bank m',Money,'rupay transfer ho gaye h, kbc m aane ke liye apka dhanyavaad')  
        break    
    