import random, time, sys

from campaign import EMAXHP
def explode():

    #A command used for crashing the game. Very useful if something seems impossible
    #I have no clue how it works
    print("Something went wrong. explodeing...")
    try:
        explode()
    except:
        explode()
def confirm():
    confirm = input("")
def critnum(AD,num1,num2):
    if AD == 1:
        critnumber1 = random.randint(num1,num2)
        critnumber2 = random.randint(num1,num2)
        if critnumber1 > critnumber2:
            critnumber = critnumber1
        elif critnumber2 > critnumber1:
            critnumber = critnumber2
        else:
            critnumber = critnumber1
    elif AD == 2:
        critnumber1 = random.randint(num1,num2)
        critnumber2 = random.randint(num1,num2)
        if critnumber1 > critnumber2:
            critnumber = critnumber2
        elif critnumber2 > critnumber1:
            critnumber = critnumber1
        else:
            critnumber = critnumber2
    else:
        critnumber = random.randint(num1,num2)
    return critnumber
def q(str,t):
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(.04)
    time.sleep(t)
def reset():
    P1AD = 0
    P2AD = 0
    P1ADTR = 0
    P2ADTR = 0
    P1DMGBOOST = 0
    P2DMGBOOST = 0
    P1SPOON = 0
    P2SPOON = 0
    P1KNIVES = 0
    P2KNIVES = 0
    P1POTS = 0
    P2POTS = 0
    P1GLOCK = 0
    P2GLOCK = 0
    P1SEEGUN = 0
    P2SEEGUN = 0
    P1NARRATORS = 0
    P2NARRATORS = 0
    return P1AD,P2AD,P1ADTR,P2ADTR,P1DMGBOOST,P2DMGBOOST,P1SPOON,P2SPOON,P1KNIVES,P2KNIVES,P1POTS,P2POTS,P1GLOCK,P2GLOCK,P1SEEGUN,P2SEEGUN,P1NARRATORS,P2NARRATORS
for i in range(1):
    P1AD = 0
    P2AD = 0
    EAD=0
    P1ADTR = 0
    P2ADTR = 0
    EADTR=0
    P1DMGBOOST = 0
    P2DMGBOOST = 0
    EDMGBOOST=0
    P1SPOON = 0
    P2SPOON = 0
    ESPOON=0
    P1KNIVES = 0
    P2KNIVES = 0
    EKNIVES=0
    P1POTS = 1
    P2POTS = 1
    EPOTS=1
    P1GLOCK = 0
    P2GLOCK = 0
    EGLOCK=0
    P1SEEGUN = 0
    P2SEEGUN = 0
    P1NARRATORS = 0
    P2NARRATORS = 0
    ENARRATORS=0
    barbarianstory=0
    secret="-.- --- -. .- -- .. ....... -.-. --- -.. ."
    knight="Knight"
    peashooter="Peashooter"
    mage="Mage"
    rouge="Rouge"
    skele="Skele"
    bard="Bard"
    barb="Barbarian"
    knightstory=0
    peashooterstory=0
    magestory=0
    rougestory=0
    skelestory=0
    bardstory=0
    secretstory=0
    playagain=0
def ask(question):
    return option
#intro to the game
q("Welcome to Dungeons and Damage.\n",.1)
 
q("Not to be confused with Dungeons and Dragons.\n",.1)
 
q("There are no dungeons here, but there is a lot of damage.\n",.1)

q("Informally known as HELL.\n",.1)

q("\n",.1)

#AllCorrect. The main while loop that loops the ENTIRE PROGRAM
ac = 0
while ac == 0:
    q("1: Play the game\n",0)
     
    q("2: Guide\n",0)
     
    q("3: Options\n",0)
     
    q("4: Quit\n",0)
     
    
    #ErrorCorrect. Allows for a repeat if a ValueError occurs
    co=1
    while co==1:
        option=ask("What would you like to do?: ")
        if option == 2:
            
            #Guide
            q("Guide coming soon\n",.1)
        
        
        elif option == 3:

            #Options
            q("Options coming soon\n",.1)
        
        elif option == 4:
            #Ends program
            ac = 1
            co=0
            playagain=1
        elif option == 1:
            
            q("This is the campaign Version of the game if you would like the pvp or pvc version please go to combat.py\n",.5)
            q("\n",0)
            
            #Starts the game part of the program
            #GameCorrect. Allows for someone to go back and play the game again if they want to. 
            q("1: Single player\n",.1)
            q("2: Co-op\n",.1)
            q("",0)
            co=1
            while co==1:    
                option=ask("How would you like to play?: ")
                multiplayer=option
                q("\n",0)
                if multiplayer==2:
                    gc = 0
                    while gc == 0:
                        q("1: Knight\n",0)
                        
                        q("2: Peashooter\n",0)
                        
                        q("3: Mage\n",0)
                        
                        q("4: Rouge\n",0)
                        
                        q("5: Skele\n",0)
                        
                        q("6: Bard\n",0)
                        
                        q("7: Barbarian\n",0)
                        
                        q("8: Random\n",0)
                        
                        #OptionCorrect. Used for when the user could give a bad input. Not needed in the menus b/c it can just loop to the begining of AllCorrect
                        oc = 0
                        while oc == 0:
                            co=1
                            while co==1:
                                #ErrorCorrect

                                option=ask("Select a class player 1: ")
                                rc = 0
                                while rc == 0:
                                    Player1class=option

                                    if option == 1:
                                        option = "Knight"
                                        P1HP = 42
                                        P1MAXHP = P1HP
                                        P1ATK = 12
                                        P1ATKBON = 2
                                        P1DEF = 14
                                        P1MP = 4
                                        P1MPBON = 1
                                        P1MAXMP = P1MP
                                        P1SPD = 3
                                        P1SPDBON = 3
                                        rc = 1
                                        co=0
                                        P1STORY = option
                                    elif option == 2:
                                        option = "Peashooter"
                                        P1HP = 35
                                        P1MAXHP = P1HP
                                        P1ATK = 10
                                        P1ATKBON = 1
                                        P1DEF = 14
                                        P1MP = 5
                                        P1MPBON = 1
                                        P1MAXMP = P1MP
                                        P1SPD = 6
                                        P1SPDBON = 3
                                        rc = 1
                                        P1STORY = option
                                        co=0
                                    elif option == 3:
                                        option = "Mage"
                                        P1HP = 29
                                        P1MAXHP = P1HP
                                        P1ATK = 7
                                        P1ATKBON = 2
                                        P1DEF = 10
                                        P1MP = 20
                                        P1MPBON = 5
                                        P1MAXMP = P1MP
                                        P1SPD = 2
                                        P1SPDBON = 3
                                        rc = 1
                                        P1STORY = option
                                        co=0
                                    elif option == 4:
                                        option = "Rouge"
                                        P1HP = 31
                                        P1MAXHP = P1HP
                                        P1ATK = 13
                                        P1ATKBON = 4
                                        P1DEF = 14
                                        P1MP = 6
                                        P1MPBON = 1
                                        P1MAXMP = P1MP
                                        P1SPD = 7
                                        P1SPDBON = 3
                                        rc = 1
                                        P1STORY = option
                                        co=0
                                    elif option == 5:
                                        option = "Skele"
                                        P1HP = 33
                                        P1MAXHP = P1HP
                                        P1ATK = 20
                                        P1ATKBON = 6
                                        P1DEF = 20
                                        P1MP = 15
                                        P1MPBON = 3
                                        P1MAXMP = P1MP
                                        P1SPD = 4
                                        P1SPDBON = 3
                                        rc = 1
                                        P1STORY = option
                                        co=0
                                    elif option == 6:
                                        option = "Bard"
                                        P1HP = 37
                                        P1MAXHP = P1HP
                                        P1ATK = 7
                                        P1ATKBON = 1
                                        P1DEF = 13
                                        P1MP = 14
                                        P1MPBON = 4
                                        P1MAXMP = P1MP
                                        P1SPD = 5
                                        P1SPDBON = 3
                                        rc = 1
                                        P1STORY = option
                                        co=0
                                    elif option == 7:
                                        option = "Barbarian"
                                        P1HP = 52
                                        P1MAXHP = P1HP
                                        P1ATK = 14
                                        P1ATKBON = 2
                                        P1DEF = 11
                                        P1MP = 2
                                        P1MPBON = .25
                                        P1MAXMP = P1MP
                                        P1SPD = 4
                                        P1SPDBON = 3
                                        rc = 1
                                        P1STORY = option
                                        co=0
                                    elif option == 88224646790:
                                        option = "-.- --- -. .- -- .. ....... -.-. --- -.. ."
                                        P1HP = 88224646790
                                        P1MAXHP = P1HP
                                        P1ATK = 88224646790
                                        P1ATKBON = 88224646790
                                        P1DEF = 88224646790
                                        P1MP = 88224646790
                                        P1MPBON = 88224646790
                                        P1MAXMP = P1MP
                                        P1SPD = 88224646790
                                        P1SPDBON = 3
                                        rc = 1
                                        P1STORY = option
                                        co=1
                                    elif option == 8:
                                        option = random.randint(1,7)
                                    else:
                                        q("Please choose a valid option\n",0)
                                        rc = 1
                                    
                            ync = 0
                            while ync == 0:
                                q("1: Yes\n",0)
                                
                                q("2: No\n",0)
                                
                                ec = 0
                                while ec == 0:
                                    try:
                                        q("Player 1 has chosen the " + str(option) + " class, is this correct?: ",0)
                                        yesorno = int(input(''))
                                        q("\n",0)
                                        if yesorno == 1:
                                            q("Player 1 has chosen the " + str(option) + " class.\n",0)
                                            q("\n",0)
                                            ync = 1
                                            oc = 1
                                            ec = 1
                                        elif yesorno == 2:
                                            q("Repick your character.\n",0)
                                            ec = 1
                                            ync = 1
                                        else:
                                            q("Please choose a valid option.\n",0)
                                        
                                    except ValueError:
                                        q("Please give a number.\n",0)
                                        ec = 0
                                        
                        
                        oc = 0
                        while oc == 0:
                            q("1: Knight\n",0)
                            
                            q("2: Peashooter\n",0)
                            
                            q("3: Mage\n",0)
                            
                            q("4: Rouge\n",0)
                            
                            q("5: Skele\n",0)
                            
                            q("6: Bard\n",0)
                            
                            q("7: Barbarian\n",0)
                            
                            q("8: Random\n",0)
                            co=1
                            while co==1:
                                co=1
                                while co==1:
                                    option2=ask("please select a class player 2: ")
                                    rc = 0
                                    while rc == 0:
                                        if option2 == 1:
                                            option2 = "Knight"
                                            P2HP = 42
                                            P2MAXHP = P2HP
                                            P2ATK = 12
                                            P2ATKBON = 2
                                            P2DEF = 14
                                            P2MP = 4
                                            P2MPBON = 1
                                            P2MAXMP = P2MP
                                            P2SPD = 3
                                            P2SPDBON = 3
                                            rc = 1
                                            P2STORY = option2
                                            co=0
                                        elif option2 == 2:
                                            option2 = "Peashooter"
                                            P2HP = 35
                                            P2MAXHP = P2HP
                                            P2ATK = 10
                                            P2ATKBON = 1
                                            P2DEF = 14
                                            P2MP = 5
                                            P2MPBON = 1
                                            P2MAXMP = P2MP
                                            P2SPD = 6
                                            P2SPDBON = 3
                                            rc = 1
                                            P2STORY = option2
                                            co=0
                                        elif option2 == 3:
                                            option2 = "Mage"
                                            P2HP = 29
                                            P2MAXHP = P2HP
                                            P2ATK = 7
                                            P2ATKBON = 2
                                            P2DEF = 10
                                            P2MP = 20
                                            P2MPBON = 5
                                            P2MAXMP = P2MP
                                            P2SPD = 2
                                            P2SPDBON = 3
                                            rc = 1
                                            P2STORY = option2
                                            co=0
                                        elif option2 == 4:
                                            option2 = "Rouge"
                                            P2HP = 31
                                            P2MAXHP = P2HP
                                            P2ATK = 13
                                            P2ATKBON = 4
                                            P2DEF = 14
                                            P2MP = 6
                                            P2MPBON = 1
                                            P2MAXMP = P2MP
                                            P2SPD = 7
                                            P2SPDBON = 3
                                            rc = 1
                                            P2STORY = option2
                                            co=0
                                        elif option2 == 5:
                                            option2 = "Skele"
                                            P2HP = 33
                                            P2MAXHP = P2HP
                                            P2ATK = 20
                                            P2ATKBON = 6
                                            P2DEF = 20
                                            P2MP = 15
                                            P2MPBON = 3
                                            P2MAXMP = P2MP
                                            P2SPD = 4
                                            P2SPDBON = 3
                                            rc = 1
                                            P2STORY = option2
                                            co=0
                                        elif option2 == 6:
                                            option2 = "Bard"
                                            P2HP = 37
                                            P2MAXHP = P2HP
                                            P2ATK = 7
                                            P2ATKBON = 1
                                            P2DEF = 13
                                            P2MP = 14
                                            P2MPBON = 4
                                            P2MAXMP = P2MP
                                            P2SPD = 5
                                            P2SPDBON = 3
                                            rc = 1
                                            P2STORY = option2
                                            co=0
                                        elif option2 == 7:
                                            option2 = "Barbarian"
                                            P2HP = 52
                                            P2MAXHP = P2HP
                                            P2ATK = 14
                                            P2ATKBON = 2
                                            P2DEF = 11
                                            P2MP = 2
                                            P2MPBON = .25
                                            P2MAXMP = P2MP
                                            P2SPD = 4
                                            P2SPDBON = 3
                                            rc = 1
                                            P2STORY = option2
                                            co=0
                                        elif option2 == 88224646790:
                                            option2 = "-.- --- -. .- -- .. ....... -.-. --- -.. ."
                                            P2HP = 88224646790
                                            P2MAXHP = P2HP
                                            P2ATK = 88224646790
                                            P2ATKBON = 88224646790
                                            P2DEF = 88224646790
                                            P2MP = 88224646790
                                            P2MPBON = 88224646790
                                            P2MAXMP = P1MP
                                            P2SPD = 88224646790
                                            P2SPDBON = 3
                                            rc = 1
                                            P2STORY = option2
                                            co=0
                                        elif option2 == 8:
                                            option2 = random.randint(1,7)
                                        else:
                                            q("Please choose a valid option.\n",0)
                                            rc = 1
                                if option2==option:
                                    q("Player 1 is already playing this character please try again\n",.1)
                                    rc=0
                                    co=1
                                else:
                                    ync = 0
                                    while ync == 0:
                                        q("1: Yes\n",0)
                                        
                                        q("2: No\n",0)
                                        
                                        ec = 0
                                        while ec == 0:
                                            try:
                                                q("Player 2 has chosen the " + str(option2) + " class, is this correct?: ",0)
                                                yesorno = int(input(''))
                                                q("\n",0)
                                                if yesorno == 1:
                                                    q("Player 2 has chosen the " + str(option2) + " class.\n",0)
                                                    co=0
                                                    ync = 1
                                                    oc = 1
                                                    ec = 1
                                                elif yesorno == 2:
                                                    q("Repeck your character.\n",0)
                                                    co=1
                                                    ync = 1
                                                    ec = 1
                                                else:
                                                    q("Please choose a valid option\n",0)
                                                
                                            except ValueError:
                                                q("Please give a number.\n",0)
                                                ec = 0
                                def whatenemy():
                                    enemychose=random.randint(1,5)
                                    if enemychose==1:
                                        enemy="spider"
                                        EHP = 20
                                        EMAXHP = EHP
                                        EATK = 15
                                        EATKBON = 5
                                        EDEF = 5
                                        EMP = 5
                                        EMPBON = 2
                                        EMAXMP = EMP
                                        ESPD = 4
                                        ESPDBON = 3
                                    elif enemychose==2:
                                        enemy="fairy"
                                        EHP = 10
                                        EMAXHP = EHP
                                        EATK = 10
                                        EATKBON = 6
                                        EDEF = 5
                                        EMP = 10
                                        EMPBON = 5
                                        EMAXMP = EMP
                                        ESPD = 15
                                        ESPDBON = 5
                                    elif enemychose==3:
                                        enemy="evil tree"
                                        EHP = 50
                                        EMAXHP = EHP
                                        EATK = 10
                                        EATKBON = 5
                                        EDEF = 20
                                        EMP = 3
                                        EMPBON = 3
                                        EMAXMP = EMP
                                        ESPD = 5
                                        ESPDBON = 2
                                    elif enemychose==4:
                                        enemy="wolf"
                                        EHP = 20
                                        EMAXHP = EHP
                                        EATK = 15
                                        EATKBON = 8
                                        EDEF = 9
                                        EMP = 4
                                        EMPBON = 2
                                        EMAXMP = EMP
                                        ESPD = 10
                                        ESPDBON = 3
                                    elif enemychose==5:
                                        enemy="evil version of the peashooter also known as the frozo pea"
                                        EHP = 35
                                        EMAXHP = EHP
                                        EATK = 10
                                        EATKBON = 1
                                        EDEF = 14
                                        EMP = 5
                                        EMPBON = 1
                                        EMAXMP = EMP
                                        ESPD = 6
                                        ESPDBON = 3
                                    return enemy,EHP, EMAXHP, EATK, EATKBON, EDEF, EMP,EMPBON, EMAXMP, ESPD,ESPDBON
                                enemy,EHP, EMAXHP, EATK, EATKBON, EDEF, EMP,EMPBON, EMAXMP, ESPD,ESPDBON = whatenemy()
                                def combat():
                                    print("testing")
                                
                                    q("while travling through the forest the 2 come across a " + str(enemy) + " you prepare for the fight\n",2)
                                    q("\n",0)
                                    q("Player 1's Health " + str(P1HP) + "\n",.1)
                                    q("Player 2's Health " + str(P2HP) + "\n",.1)
                                    q( str(enemy) + "'s Health " + str(EHP) + "\n",.1)
                                    q("\n",1)
                                    fight=1
                                    fightround=1
                                    while fight==1:
                                        q("Round " + str(fightround) + " fight\n",.1)
                                        q("\n",0)
                                        if P1SPD>ESPD and P1SPD>P2SPD:
                                            q("Player 1's turn\n",.1)
                                            q("\n",0)
                                            q("1: Attack\n",.1)
                                            q("2: Magic\n",.1)
                                            q("3: Items\n",.1)
                                            q("4: Pass turn\n",.1)
                                            co=1
                                            while co==1:
                                                option=ask("what would you like to do?: ")
                                                turnmove=option
                                                q("\n",0)
                                                if turnmove==1:
                                                    critnumber=critnum(P1AD,1,20)
                                                    if critnumber==1:
                                                        q("Crital fail!\n",.1)
                                                        q("You Wiffed hard and wasted your turn\n",.1)
                                                        q("\n",.1)
                                                        prevmp=P1MP

                                                        P1MP=P1MP+P1MPBON
                                                        prevmp=P1MP-prevmp
                                                        
                                                        q("\n")
                                                        if P1MP>P1MAXMP:
                                                            P1MP=P1MAXMP
                                                        q("You gained back " + str(prevmp) + " Mana Points back\n")
                                                        q("You now have " + str(P1MP) + "\n",.1)
                                                        ESPD=ESPD+ESPDBON
                                                        q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                        P2SPD=P2SPD+P2SPDBON
                                                        q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)       
                                                        co=0                           
                                                    elif critnumber==20:
                                                        q("Critical hit!\n",.1)
                                                        damage=(P1ATK*2)+critnumber
                                                        if damage>EDEF:
                                                            q("You Deal " + str(damage) + " Damage to the " + str(enemy) + "\n",.1)
                                                        elif damage<=EDEF:
                                                            q("The enemy blocked the hit\n",.1)
                                                            damage=0
                                                        EHP=EHP-damage
                                                        if EHP<0:
                                                            EHP=0
                                                        q("The " + str(enemy) + " Has " + str(EHP) + " Health left\n",.1)
                                                        prevmp=P1MP

                                                        P1MP=P1MP+P1MPBON
                                                        prevmp=P1MP-prevmp
                                                        
                                                        q("\n")
                                                        if P1MP>P1MAXMP:
                                                            P1MP=P1MAXMP
                                                        q("You gained back " + str(prevmp) + " Mana Points back\n")
                                                        q("You now have " + str(P1MP) + "\n",.1)
                                                        ESPD=ESPD+ESPDBON
                                                        q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                        P2SPD=P2SPD+P2SPDBON
                                                        q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                        co=0
                                                    elif critnumber>1 and critnumber<20:
                                                        damage=P1ATK+critnumber
                                                        if damage>EDEF:
                                                            q("You Deal " + str(damage) + " Damage to the " + str(enemy) + "\n",.1)
                                                        elif damage<=EDEF:
                                                            q("The enemy blocked the hit\n",.1)
                                                            damage=0
                                                        EHP=EHP-damage
                                                        if EHP<0:
                                                            EHP=0
                                                        q("The " + str(enemy) + " Has " + str(EHP) + " Health left\n",.1)
                                                        prevmp=P1MP

                                                        P1MP=P1MP+P1MPBON
                                                        prevmp=P1MP-prevmp
                                                        
                                                        q("\n")
                                                        if P1MP>P1MAXMP:
                                                            P1MP=P1MAXMP
                                                        q("You gained back " + str(prevmp) + " Mana Points back\n")
                                                        q("You now have " + str(P1MP) + "\n",.1)
                                                        ESPD=ESPD+ESPDBON
                                                        q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                        P2SPD=P2SPD+P2SPDBON
                                                        q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                        co=0
                                                    
                                                elif turnmove==2:
                                                    q("1: choose someone to gain 1 permanant defense (defense reduces damage effectivly agaisnt attacks but is only a quarter as effective agaisnt magic attacks)\n",.1)
                                                    q("2: Gain a random item\n",.1)
                                                    q("3: Gain advantage\n",.1)
                                                    q("4: Apply disadvantage\n")
                                                    q("5: Heal your teammate or you for 20 pecent of health of max health\n",.1)
                                                    q("6: Fireball-Does more damage the more mana you have\n",.1)
                                                    q("0: Cancel\n",.1)
                                                    co=1
                                                    while co==1:    
                                                        option=ask("What would you like to do?: ")
                                                        magicinput=option
                                                        q("\n",.1)
                                                        if magicinput>P1MP:
                                                            q("You can't do this\n",.1)
                                                        else:
                                                            if magicinput==1:
                                                                P1MP=P1MP-magicinput
                                                                q("1: You\n",0.1)
                                                                q("2: Teammate",0.1)
                                                                co=1
                                                                while co==1:
                                                                    option=ask("Who would you like to give the defense buff to?: ")
                                                                    defchoose=option
                                                                    if defchoose==1:
                                                                        q("You gain 1 defense\n",.1)
                                                                        P1DEF=P1DEF+1
                                                                        prevmp=P1MP
                                                                        P1MP=P1MP+P1MPBON
                                                                        prevmp=P1MP-prevmp
                                                                        q("\n")
                                                                        if P1MP>P1MAXMP:
                                                                            P1MP=P1MAXMP
                                                                        q("You gained back " + str(prevmp) + " Mana Points back\n",.1)
                                                                        q("You now have " + str(P1MP) + "\n",.1)
                                                                        ESPD=ESPD+ESPDBON
                                                                        q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                                        P2SPD=P2SPD+P2SPDBON
                                                                        q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                                        co=0
                                                                    elif defchoose==2:
                                                                        q("You give your teammate a defense buff\n",.1)
                                                                        P2DEF=P2DEF+1
                                                                        prevmp=P1MP
                                                                        P1MP=P1MP+P1MPBON
                                                                        prevmp=P1MP-prevmp
                                                                        q("\n",.1)
                                                                        if P1MP>P1MAXMP:
                                                                            P1MP=P1MAXMP
                                                                        q("You gained back " + str(prevmp) + " Mana Points back\n",.1)
                                                                        q("You now have " + str(P1MP) + "\n",.1)
                                                                        ESPD=ESPD+ESPDBON
                                                                        q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                                        P2SPD=P2SPD+P2SPDBON
                                                                        co=0
                                                                        q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                            elif magicinput==2:
                                                                P1MP=P1MP-magicinput
                                                                q("you conjour a random item to aid you in your fight",.1)
                                                                itemlist=random.randint(1,1000)

                                                                if itemlist>=1 and itemlist <=333:
                                                                    q("You conjured a spoon\n",.1)
                                                                    q("Who would you like to give the spoon to?\n",.1)
                                                                    q("1: You\n",.1)
                                                                    q("2: Your teammate\n",.1)
                                                                    q("3: Enemy\n",.1)
                                                                    co=1
                                                                    while co==1:
                                                                        option=ask("What would you like to do?")
                                                                        w=option
                                                                        if w==1:
                                                                            P1SPOON=P1SPOON+1
                                                                            q("you now have " + str(P1SPOON) +" spoons\n",.1)
                                                                            co=0
                                                                        elif w==2:    
                                                                            P2SPOON = P2SPOON+1
                                                                            q("you now have " + str(P2SPOON) +" spoons\n",.1)
                                                                            co=0
                                                                        elif w==3:    
                                                                            ESPOON = ESPOON+1
                                                                            q("you now have " + str(ESPOON) +" spoons\n",.1)
                                                                            co=0
                                                                elif itemlist>=334 and itemlist <=666:
                                                                    q("You conjured a knife\n",.1)
                                                                    q("Who would you like to give the knife to?\n",.1)
                                                                    q("1: You\n",.1)
                                                                    q("2: Your teammate\n",.1)
                                                                    q("3: Enemy\n",.1)
                                                                    co=1
                                                                    while co==1:
                                                                        option=ask("What would you like to do?")
                                                                        w=option
                                                                        if w==1:
                                                                            P1KNIVES=P1KNIVES+1
                                                                            q("you now have " + str(P1KNIVES) +" knife\n",.1)
                                                                            co=0
                                                                        elif w==2:    
                                                                            P2KNIVES = P2KNIVES+1
                                                                            q("you now have " + str(P2KNIVES) +" knife\n",.1)
                                                                            co=0
                                                                        elif w==3:    
                                                                            EKNIVES = EKNIVES+1
                                                                            q("you now have " + str(EKNIVES) +" knife\n",.1) 
                                                                            co=0
                                                                elif itemlist>=667 and itemlist <=999:
                                                                    q("You conjured a knife\n",.1)
                                                                    q("Who would you like to give the knife to?\n",.1)
                                                                    q("1: You\n",.1)
                                                                    q("2: Your teammate\n",.1)
                                                                    q("3: Enemy\n",.1)
                                                                    co=1
                                                                    while co==1:
                                                                        option=ask("What would you like to do?")
                                                                        w=option
                                                                        if w==1:
                                                                            P1POTS=P1POTS+1
                                                                            q("you now have " + str(P1POTS) +" healing potions\n",.1)
                                                                            co=0
                                                                        elif w==2:    
                                                                            P2POTS = P2POTS+1
                                                                            q("you now have " + str(P2POTS) +" healing potions\n",.1)
                                                                            co=0
                                                                        elif w==3:    
                                                                            EPOTS = EPOTS+1
                                                                            q("you now have " + str(EPOTS) +" healing potions\n",.1) 
                                                                            co=0
                                                                elif itemlist==1000:
                                                                    q("You conjured a\n",1)
                                                                    q("alright whos the funny guy trying to add this to the game\n",5)
                                                                    q("This is stupid im not giving them this\n",1)
                                                                    q("seriosly i have to do it or im fired\n",4)
                                                                    q("you know what",.5)
                                                                    q(" i quit get someone else to do this stupid job\n",10)
                                                                    q("alright so what am i doing?\n",2)
                                                                    q("that sounds pretty easy \n",3)
                                                                    q("Alright let me read the script here\n",.3)
                                                                    q("You Conjured a\n",2)
                                                                    q("am i reading this right?\n",2)
                                                                    q("you conjuered a",.8)
                                                                    q("...",.5)
                                                                    q("a glock-19 pistol with a switch and a scope\n",.5)
                                                                    q("Who would you like to give the glock to?\n",.1)
                                                                    q("1: You\n",.1)
                                                                    q("2: Your teammate\n",.1)
                                                                    q("3: Enemy\n",.1)
                                                                    co=1
                                                                    while co==1:
                                                                        option=ask("What would you like to do?")
                                                                        w=option
                                                                        if w==1:
                                                                            P1GLOCK=P1GLOCK+1
                                                                            q("you now have " + str(P1GLOCK) +" glocks\n",.1)
                                                                            co=0
                                                                        elif w==2:    
                                                                            P2GLOCK = P2GLOCK+1
                                                                            q("you now have " + str(P2GLOCK) +" glockS\n",.1)
                                                                            co=0
                                                                        elif w==3:    
                                                                            EGLOCK = EGLOCK+1
                                                                            q("uhhh weird choice but ok")
                                                                            q("you now have " + str(EGLOCK) +" glocks\n",.1) 
                                                                            co=0
                                                                P1MP=P1MP+P1MPBON
                                                                prevmp=P1MP-prevmp
                                                                q("\n",.1)
                                                                if P1MP>P1MAXMP:
                                                                    P1MP=P1MAXMP
                                                                    q("You gained back " + str(prevmp) + " Mana Points back\n",.1)
                                                                    q("You now have " + str(P1MP) + "\n",.1)
                                                                    ESPD=ESPD+ESPDBON
                                                                    q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                                    P2SPD=P2SPD+P2SPDBON
                                                                    q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                            elif magicinput==3:
                                                                P1AD=1
                                                                P1ADTR=2
                                                                prevmp=P1MP
                                                                P1MP=P1MP+P1MPBON
                                                                prevmp=P1MP-prevmp
                                                                q("\n",.1)
                                                                if P1MP>P1MAXMP:
                                                                    P1MP=P1MAXMP
                                                                q("You gained back " + str(prevmp) + " Mana Points back\n",.1)
                                                                q("You now have " + str(P1MP) + "\n",.1)
                                                                ESPD=ESPD+ESPDBON
                                                                q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                                P2SPD=P2SPD+P2SPDBON
                                                                q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                                co=0
                                                            elif magicinput==4:
                                                                EAD=2
                                                                EADTR=2
                                                                prevmp=P1MP
                                                                P1MP=P1MP+P1MPBON
                                                                prevmp=P1MP-prevmp
                                                                q("\n",.1)
                                                                if P1MP>P1MAXMP:
                                                                    P1MP=P1MAXMP
                                                                q("You gained back " + str(prevmp) + " Mana Points back\n",.1)
                                                                q("You now have " + str(P1MP) + "\n",.1)
                                                                ESPD=ESPD+ESPDBON
                                                                q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                                P2SPD=P2SPD+P2SPDBON
                                                                q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                                co=0
                                                            elif magicinput==5:
                                                                P1MP=P1MP-magicinput
                                                                q("1: You\n",0.1)
                                                                q("2: Teammate",0.1)
                                                                q("Who would you like to give the healing to?: ",.0)
                                                                defchoose=int(input(""))
                                                                if defchoose==1:
                                                                    P1HPGAIN=P1HP+round(P1MAXHP/5,0)
                                                                    P1HP=P1HP+P1HPGAIN
                                                                    if P1HP>P1MAXHP:
                                                                        P1HP=P1MAXHP
                                                                    q("You gain " + str(P1HPGAIN) + " health back\n",.1)
                                                                    q("you have " + str(P1HP) + " health\n",.3)
                                                                    prevmp=P1MP
                                                                    P1MP=P1MP+P1MPBON
                                                                    prevmp=P1MP-prevmp
                                                                    q("\n")
                                                                    if P1MP>P1MAXMP:
                                                                        P1MP=P1MAXMP
                                                                    q("You gained back " + str(prevmp) + " Mana Points back\n",.1)
                                                                    q("You now have " + str(P1MP) + "\n",.1)
                                                                    ESPD=ESPD+ESPDBON
                                                                    q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                                    P2SPD=P2SPD+P2SPDBON
                                                                    q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                                elif defchoose==2:
                                                                    P2HPGAIN=P2HP+round(P2MAXHP/5,0)
                                                                    P2HP=P2HP+P2HPGAIN
                                                                    if P2HP>P2MAXHP:
                                                                        P2HP=P2MAXHP
                                                                    q("You gain " + str(P2HPGAIN) + " health back\n",.1)
                                                                    q("you have " + str(P2HP) + " health\n",.3)
                                                                    prevmp=P1MP
                                                                    P1MP=P1MP+P1MPBON
                                                                    prevmp=P1MP-prevmp
                                                                    q("\n")
                                                                    if P1MP>P1MAXMP:
                                                                        P1MP=P1MAXMP
                                                                    q("You gained back " + str(prevmp) + " Mana Points back\n",.1)
                                                                    q("You now have " + str(P1MP) + "\n",.1)
                                                                    ESPD=ESPD+ESPDBON
                                                                    q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                                    P2SPD=P2SPD+P2SPDBON
                                                                    q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                            elif magicinput==6:
                                                                q("You Cast fire ball\n",.2)
                                                                fireballdamage=random.randint(round(P1MAXMP/2,0),P1MAXMP)
                                                                if fireballdamage<EDEF/4:
                                                                    q("the magic was blocked")
                                                                else:
                                                                    q("")
                                                                    co=0
                                                elif turnmove==3:
                                                    q("You have " + str(P1SPOON) + " spoons left\n",.1)
                                                    q("You have " + str(P1KNIVES) + " knives left\n",.1)
                                                    q("You have " + str(P1POTS) + " Healing potions left\n",.1)
                                                    if P1GLOCK>0:
                                                        q("You have " + str(P1GLOCK) + " Glock-19's left\n",.1)
                                                    q("\n",.2)
                                                    q("1: use spoon \n",.1)
                                                    q("2: use knife\n",.1)
                                                    q("3: use healing potion\n",.1)
                                                    if P1GLOCK>0:
                                                            q("1234567890: use Glock-19\n",.1)
                                                    option=ask("What would you like to use?: \n")
                                                    itemuse=option
                                                    if itemuse==1 and P1SPOON>0:
                                                        P1POTS=P1POTS-1
                                                        potionheal=random.randint(2,5)
                                                        Priorhp=P1HP
                                                        P1HP=P1HP+potionheal
                                                        if P1HP>P1MAXHP:
                                                            P1HP=P1MAXHP
                                                        Priorhp=P1HP-Priorhp
                                                        q("you drink a healing potion and heal for " + str(Priorhp) + " health and now have " + str(P1HP) + " health\n",.3)
                                                    elif itemuse==2 and P1KNIVES>0:
                                                        P1KNIVES=P1KNIVES-1
                                                        knifedamage=random.randint(1,50)
                                                        if knifedamage==1:
                                                            q("your throw was so weak it fell on the floor infront of your enemy and he picked it up\n",.2)
                                                            EKNIVES=EKNIVES+1
                                                            
                                                        else:
                                                            knifedamage=knifedamage/10
                                                            round(knifedamage,0)
                                                            EHP=EHP-knifedamage
                                                            if EHP<0:
                                                                EHP=0
                                                            q("You throw a knife at the enemy dealing " + str(knifedamage) + " damage to the enemy the enemy is left with " + str(EHP) + " Health left\n",.2)
                                                    elif itemuse==3 and P1SPOON>0:
                                                        P1SPOON=P1SPOON-1
                                                        spooncrit=random.randint(1,1000)
                                                        if spooncrit==1000:
                                                            q("You threw your spoon so well (or the rust on it) killed the enemy instantly\n",.1)
                                                            EHP=0
                                                            

                                                            
                                                        else:
                                                            spoondamage=random.randint(1,3)
                                                            EHP=EHP-spoondamage
                                                            if EHP<0:
                                                                EHP=0
                                                            q("You throw a spoon at the enemy dealing " + str(spoondamage) + " damage to the enemy the enemy is left with " + str(EHP) + " Health left\n",.2)
                                                    elif itemuse==1234567890 and P1GLOCK>0:
                                                        P1GLOCK=P1GLOCK-1
                                                        gunmiss=random.randint(1,1000)
                                                        if gunmiss==1000:
                                                            q("You...\n",2)
                                                            q("You somehow manegded to get a gun and you...\n",1)
                                                            q("You...\n",2)
                                                            q("You MISSED AHAHHAHAHAHAHAHAHAHAH LOOK AT THIS IDIOT AHAHAHAHAHHAAHHAHAHAHAHAH\n",2)
                                                            q("how did you even manage that\n",2)
                                                            q("well next time dont break the game and things like this wont happen\n",2)
                                                            q("Anyways back to the game\n",2)
                                                        else:
                                                            
                                                            q("oh...\n",2)
                                                            q("You used it...\n",2)
                                                            q("was it worth it?...\n",2)
                                                            q("You won the fight\n",2)
                                                            q("You killed them\n",2)
                                                            q("did you enjoy it?\n",2)
                                                            q("they probally had a family\n",2)
                                                            q("now there over no life in their eyes\n",2)
                                                            q("dead\n",2)
                                                            q("i quit im not doing this anymore\n",30)
                                                            q("Alrighty lets get started on this new job\n",.1)
                                                            q("lets see here\n",.2)
                                                            q("welcome...\n",.2)
                                                            q("too...\n",2)
                                                            q("dungeons...\n",2)
                                                            q("and--\n",2)
                                                            q("what?\n",2)
                                                            q("oh sorry let me find that\n",2)
                                                            q("ahh here it is\n",2)
                                                            q("You pulled out the glock with the switch and light them up?\n",2)
                                                            q("am i reading this right or is my demantia kicking in haha\n",2)
                                                            EHP=0
                                                elif turnmove==4:
                                                    q("You skip you're turn\n",.1)
                                                    prevmp=P1MP
                                                    P1MP=P1MP+P1MPBON
                                                    prevmp=P1MP-prevmp
                                                    
                                                    q("\n")
                                                    if P1MP>P1MAXMP:
                                                        P1MP=P1MAXMP
                                                    q("You gained back " + str(prevmp) + " Mana Points back\n")
                                                    q("You now have " + str(P1MP) + "\n",.1)
                                                    ESPD=ESPD+ESPDBON
                                                    q("The " + str(enemy) + " gained " + str(ESPDBON) + " Speed back" + " and now has " + str(ESPD) + " Speed\n",.1)
                                                    P2SPD=P2SPD+P2SPDBON
                                                    co=0
                                                    q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                                                else:
                                                    q("not an avilible option\n",.1)

                                            if P1ADTR>0:
                                                P1ADTR=P1ADTR-1
                                            if P1ADTR==0:
                                                P1AD=0
                                        
                                        
                                        
                                        else:
                                            fight=2

                        if P1STORY==knight or P2STORY==knight:
                            if P1STORY==peashooter or P2STORY==peashooter:
                                q("as the knight wanders through the mystical forest he comes across a weird looking vine but just as fast as he see's the vine in springs up and aims its mouth in a very threating way signaling that this plant is very dangeos but this plant has a mission to get to his home couidently enough the knight was heading the same way to meet the princess in the tower he needs to save so they embark on their journy to the town off neighborville\n",.2)
                                
                            elif P1STORY==mage or P2STORY==mage :
                                q("\n",.2)
                            elif P1STORY== rouge or P2STORY== rouge:
                                q("\n",.2)
                            elif P1STORY== skele or P2STORY== skele:
                                q("\n",.2)
                            elif P1STORY== bard or P2STORY== bard:
                                q("\n",.2)
                            elif P1STORY== barb or P2STORY== barb:
                                q("\n",.2)
                            elif P1STORY== secret or P2STORY== secret:
                                q("\n",.2)
                        elif peashooterstory==1:
                            if P1STORY==peashooter or P2STORY==peashooter:
                                q("as the knight wanders through the mystical forest he comes across a weird looking vine but just as fast as he see's the vine in springs up and aims its mouth in a very threating way signaling that this plant is very dangeos but this plant has a mission to get to his home couidently enough the knight was heading the same way to meet the princess in the tower he needs to save so they embark on their journy to the town off neighborville\n",.2)
                                
                            elif P1STORY==mage or P2STORY==mage :
                                q("\n",.2)
                            elif P1STORY== rouge or P2STORY== rouge:
                                q("\n",.2)
                            elif P1STORY== skele or P2STORY== skele:
                                q("\n",.2)
                            elif P1STORY== bard or P2STORY== bard:
                                q("\n",.2)
                            elif P1STORY== barb or P2STORY== barb:
                                q("\n",.2)
                            elif P1STORY== secret or P2STORY== secret:
                                q("\n",.2)
                        elif magestory==1:
                            if P1STORY==peashooter or P2STORY==peashooter:
                                q("as the knight wanders through the mystical forest he comes across a weird looking vine but just as fast as he see's the vine in springs up and aims its mouth in a very threating way signaling that this plant is very dangeos but this plant has a mission to get to his home couidently enough the knight was heading the same way to meet the princess in the tower he needs to save so they embark on their journy to the town off neighborville\n",.2)
                                
                            elif P1STORY==mage or P2STORY==mage :
                                q("\n",.2)
                            elif P1STORY== rouge or P2STORY== rouge:
                                q("\n",.2)
                            elif P1STORY== skele or P2STORY== skele:
                                q("\n",.2)
                            elif P1STORY== bard or P2STORY== bard:
                                q("\n",.2)
                            elif P1STORY== barb or P2STORY== barb:
                                q("\n",.2)
                            elif P1STORY== secret or P2STORY== secret:
                                q("\n",.2)
                        elif rougestory==1:
                            if P1STORY==peashooter or P2STORY==peashooter:
                                q("as the knight wanders through the mystical forest he comes across a weird looking vine but just as fast as he see's the vine in springs up and aims its mouth in a very threating way signaling that this plant is very dangeos but this plant has a mission to get to his home couidently enough the knight was heading the same way to meet the princess in the tower he needs to save so they embark on their journy to the town off neighborville\n",.2)
                                
                            elif P1STORY==mage or P2STORY==mage :
                                q("\n",.2)
                            elif P1STORY== rouge or P2STORY== rouge:
                                q("\n",.2)
                            elif P1STORY== skele or P2STORY== skele:
                                q("\n",.2)
                            elif P1STORY== bard or P2STORY== bard:
                                q("\n",.2)
                            elif P1STORY== barb or P2STORY== barb:
                                q("\n",.2)
                            elif P1STORY== secret or P2STORY== secret:
                                q("\n",.2)
                        elif skelestory==1:
                            if P1STORY==peashooter or P2STORY==peashooter:
                                q("as the knight wanders through the mystical forest he comes across a weird looking vine but just as fast as he see's the vine in springs up and aims its mouth in a very threating way signaling that this plant is very dangeos but this plant has a mission to get to his home couidently enough the knight was heading the same way to meet the princess in the tower he needs to save so they embark on their journy to the town off neighborville\n",.2)
                                
                            elif P1STORY==mage or P2STORY==mage :
                                q("\n",.2)
                            elif P1STORY== rouge or P2STORY== rouge:
                                q("\n",.2)
                            elif P1STORY== skele or P2STORY== skele:
                                q("\n",.2)
                            elif P1STORY== bard or P2STORY== bard:
                                q("\n",.2)
                            elif P1STORY== barb or P2STORY== barb:
                                q("\n",.2)
                            elif P1STORY== secret or P2STORY== secret:
                                q("\n",.2)
                        elif bardstory==1:
                            if P1STORY==peashooter or P2STORY==peashooter:
                                q("as the knight wanders through the mystical forest he comes across a weird looking vine but just as fast as he see's the vine in springs up and aims its mouth in a very threating way signaling that this plant is very dangeos but this plant has a mission to get to his home couidently enough the knight was heading the same way to meet the princess in the tower he needs to save so they embark on their journy to the town off neighborville\n",.2)
                                
                            elif P1STORY==mage or P2STORY==mage :
                                q("\n",.2)
                            elif P1STORY== rouge or P2STORY== rouge:
                                q("\n",.2)
                            elif P1STORY== skele or P2STORY== skele:
                                q("\n",.2)
                            elif P1STORY== bard or P2STORY== bard:
                                q("\n",.2)
                            elif P1STORY== barb or P2STORY== barb:
                                q("\n",.2)
                            elif P1STORY== secret or P2STORY== secret:
                                q("\n",.2)
                        elif barbarianstory==1:
                            if P1STORY==peashooter or P2STORY==peashooter:
                                q("as the knight wanders through the mystical forest he comes across a weird looking vine but just as fast as he see's the vine in springs up and aims its mouth in a very threating way signaling that this plant is very dangeos but this plant has a mission to get to his home couidently enough the knight was heading the same way to meet the princess in the tower he needs to save so they embark on their journy to the town off neighborville\n",.2)
                                
                            elif P1STORY==mage or P2STORY==mage :
                                q("\n",.2)
                            elif P1STORY== rouge or P2STORY== rouge:
                                q("\n",.2)
                            elif P1STORY== skele or P2STORY== skele:
                                q("\n",.2)
                            elif P1STORY== bard or P2STORY== bard:
                                q("\n",.2)
                            elif P1STORY== barb or P2STORY== barb:
                                q("\n",.2)
                            elif P1STORY== secret or P2STORY== secret:
                                q("\n",.2)
                        elif secretstory==1:
                            if P1STORY==peashooter or P2STORY==peashooter:
                                q("as the knight wanders through the mystical forest he comes across a weird looking vine but just as fast as he see's the vine in springs up and aims its mouth in a very threating way signaling that this plant is very dangeos but this plant has a mission to get to his home couidently enough the knight was heading the same way to meet the princess in the tower he needs to save so they embark on their journy to the town off neighborville\n",.2)
                                
                            elif P1STORY==mage or P2STORY==mage :
                                q("\n",.2)
                            elif P1STORY== rouge or P2STORY== rouge:
                                q("\n",.2)
                            elif P1STORY== skele or P2STORY== skele:
                                q("\n",.2)
                            elif P1STORY== bard or P2STORY== bard:
                                q("\n",.2)
                            elif P1STORY== barb or P2STORY== barb:
                                q("\n",.2)
                            elif P1STORY== secret or P2STORY== secret:
                                q("\n",.2)
                        #story starts
                        
                        q("er;lnjrgifdsgdsjgsdbosodhsdfhddsbsdbsdoubsdjfbdsjbfdsjklfbhdosbhosdfbhs\n",2)
                        co=0
                else:
                    q("this is currently not an avalible option \n",.1)
                                    
            else:
                q("Please give a valid option.\n",0)
    if playagain==0:    
        q("1: Yes\n",.1)
        q("2: No\n",.1)
        q("Play again?: \n",0)
        ac=int(input(""))
        q("\n",.1)
q("End of program OvO\n",10)
