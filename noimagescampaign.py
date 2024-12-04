#A big part of this game's loop control are Correct variables
#These are just variables with a binary (0 or 1) value.
#They allow the user to correct a bad input or lead them to a specific part of the program
#It's the break and continue commands with an argument you can put in

#Imports random, which is used to generate random numbers used for combat within the game
#Time, which is used in all points in the program. Literally. The q command has the wait command, and the wait command is after every q command or input command
#Sys, IDK what it does. All I know is that it's used in the 
import random, time, sys
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
    ec = 0
    while ec == 0:
        try:
            q("What would you like to do?: ",0)
            option = int(input(''))
            q("\n",0)
            ec = 1
             
        except ValueError:
            q("Please give a number.\n",0)

    if option == 2:
        
        #Guide
        q("Guide coming soon\n",.1)
    
    
    elif option == 3:

        #Options
        q("Options coming soon\n",.1)
    
    elif option == 4:
        #Ends program
        ac = 1
    
    
    elif option == 1:
        
        q("This is the campaign Version of the game if you would like the pvp or pvc version please go to combat.py\n",.5)
        q("\n",0)
        
        #Starts the game part of the program
        #GameCorrect. Allows for someone to go back and play the game again if they want to. 
        q("1: Single player\n",.1)
        q("2: Co-op\n",.1)
        q("How would you like to play?",0)
        multiplayer=int(input(": "))
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
                    
                    #ErrorCorrect
                    ec = 0
                    while ec == 0:
                        try:
                            q("Please select a class, Player 1: ",0)
                            option = int(input(''))
                            q("\n",0)
                            ec = 1
                            
                        except ValueError:
                            q("Please give a number.\n",0)
                            
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
                            knight1story=1
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
                            peashooter1story=1
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
                            mage1story=1
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
                            rouge1story=1
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
                            skele1story=1
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
                            bard1story=1
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
                            barbarian1story=1
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
                            secret1story=1
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
                                elif yesorno == 2:
                                    q("Repick your character.\n",0)
                                    
                                    ync = 1
                                else:
                                    q("Please choose a valid option.\n",0)
                                ec = 1
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
                    
                    ec = 0
                    while ec == 0:
                        try:
                            
                            q("Please choose a class, player 2: ",0)
                            option = int(input(''))
                            q("\n",0)
                            if option==Player1class:
                                q("this class has already been chosen\n",0)
                                q("Please try again\n",0)
                            else:
                                ec = 1

                        except ValueError:
                            q("Please give a number.\n",0)
                            ec = 0
                    rc = 0
                    while rc == 0:
                        if option == 1:
                            option = "Knight"
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
                            knight2story=1
                        elif option == 2:
                            option = "Peashooter"
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
                            peashooter2story=1
                        elif option == 3:
                            option = "Mage"
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
                            mage2story=1
                        elif option == 4:
                            option = "Rouge"
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
                            rouge2story=1
                        elif option == 5:
                            option = "Skele"
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
                            skele2story=1
                        elif option == 6:
                            option = "Bard"
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
                            bard2story=1
                        elif option == 7:
                            option = "Barbarian"
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
                            barbarian2story=1
                        elif option == 88224646790:
                            option = "-.- --- -. .- -- .. ....... -.-. --- -.. ."
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
                            secret2story=1
                        elif option == 8:
                            option = random.randint(1,7)
                        else:
                            q("Please choose a valid option.\n",0)
                            rc = 1
                            
                    ync = 0
                    while ync == 0:
                        q("1: Yes\n",0)
                        
                        q("2: No\n",0)
                        
                        ec = 0
                        while ec == 0:
                            try:
                                q("Player 2 has chosen the " + str(option) + " class, is this correct?: ",0)
                                yesorno = int(input(''))
                                q("\n",0)
                                if yesorno == 1:
                                    q("Player 2 has chosen the " + str(option) + " class.\n",0)
                                    
                                    ync = 1
                                    oc = 1
                                elif yesorno == 2:
                                    q("Repeck your character.\n",0)
                                    
                                    ync = 1
                                else:
                                    q("Please choose a valid option\n",0)
                                ec = 1
                            except ValueError:
                                q("Please give a number.\n",0)
                                ec = 0
                if knight1story==1:
                    if peashooter2story==1:
                        q("as the knight wanders through the mystical forest he comes across a weird looking vine but just as fast as he see's the vine in springs up and aims its mouth in a very threating way signaling that this plant is very dangeos but this plant has a mission to get to his home couidently enough the knight was heading the same way to meet the princess in the tower he needs to save so they embark on their journy to the town off neighborville\n",.2)
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
                                q("What would you like to do?: \n",.0)
                                turnmove=int(input(""))
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
                                elif turnmove==2:
                                    q("1: choose someone to gain 1 permanant defense (defense reduces damage effectivly agaisnt attacks but is only half as effective agaisnt magic attacks)\n",.1)
                                    q("2: Gain a random item\n",.1)
                                    q("3: Gain advantage\n",.1)
                                    q("4: Apply disadvantage\n")
                                    q("5: Heal your teammate or you for 20 pecent of health of max health\n",.1)
                                    q("6: Fireball\n",.1)
                                    q("0: Cancel\n",.1)
                                    q("What would you like to do?: \n",0)
                                    magicinput=int(input(""))
                                    q("\n",.1)
                                    if magicinput>P1MP:
                                        q("You can't do this\n",.1)
                                    if magicinput==1:
                                        P1MP=P1MP-magicinput
                                        q("1: You\n",0.1)
                                        q("2: Teammate",0.1)
                                        q("Who would you like to give the defense buff to?: ",.0)
                                        defchoose=int(input(""))
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
                                            q("What would you like to do?",0)
                                            w=int(input(""))

                                        P2SPOON = 0
                                        P1KNIVES = 0
                                        P1POTS = 0
                                        P1GLOCK = 0













                                elif turnmove==3:
                                    q("Items arnt ready yet O~O\n",.1)
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
                                    q("Player 2 gained " + str(P2SPDBON) + " Speed back" + " and now has " + str(P2SPD) + " Speed\n",.1)
                            else:
                                fight=2

                    elif mage2story==1:
                        q("\n",.2)
                    elif rouge2story==1:
                        q("\n",.2)
                    elif skele2story==1:
                        q("\n",.2)
                    elif bard2story==1:
                        q("\n",.2)
                    elif barbarian2story==1:
                        q("\n",.2)
                    elif secret2story==1:
                        q("\n",.2)
                elif peashooter1story==1:
                    if knight2story==1:
                        q("\n",.2)
                    elif mage2story==1:
                        q("\n",.2)
                    elif rouge2story==1:
                        q("\n",.2)
                    elif skele2story==1:
                        q("\n",.2)
                    elif bard2story==1:
                        q("\n",.2)
                    elif barbarian2story==1:
                        q("\n",.2)
                    elif secret2story==1:
                        q("\n",.2)
                elif mage1story==1:
                    if peashooter2story==1:
                        q("\n",.2)
                    elif knight2story==1:
                        q("\n",.2)
                    elif rouge2story==1:
                        q("\n",.2)
                    elif skele2story==1:
                        q("\n",.2)
                    elif bard2story==1:
                        q("\n",.2)
                    elif barbarian2story==1:
                        q("\n",.2)
                    elif secret2story==1:
                        q("\n",.2)
                elif rouge1story==1:
                    if peashooter2story==1:
                        q("\n",.2)
                    elif mage2story==1:
                        q("\n",.2)
                    elif knight2story==1:
                        q("\n",.2)
                    elif skele2story==1:
                        q("\n",.2)
                    elif bard2story==1:
                        q("\n",.2)
                    elif barbarian2story==1:
                        q("\n",.2)
                    elif secret2story==1:
                        q("\n",.2)
                elif skele1story==1:
                    if peashooter2story==1:
                        q("\n",.2)
                    elif mage2story==1:
                        q("\n",.2)
                    elif rouge2story==1:
                        q("\n",.2)
                    elif knight2story==1:
                        q("\n",.2)
                    elif bard2story==1:
                        q("\n",.2)
                    elif barbarian2story==1:
                        q("\n",.2)
                    elif secret2story==1:
                        q("\n",.2)
                elif bard1story==1:
                    if peashooter2story==1:
                        q("\n",.2)
                    elif mage2story==1:
                        q("\n",.2)
                    elif rouge2story==1:
                        q("\n",.2)
                    elif skele2story==1:
                        q("\n",.2)
                    elif knight2story==1:
                        q("\n",.2)
                    elif barbarian2story==1:
                        q("\n",.2)
                    elif secret2story==1:
                        q("\n",.2)
                elif barbarian1story==1:
                    if peashooter2story==1:
                        q("\n",.2)
                    elif mage2story==1:
                        q("\n",.2)
                    elif rouge2story==1:
                        q("\n",.2)
                    elif skele2story==1:
                        q("\n",.2)
                    elif bard2story==1:
                        q("\n",.2)
                    elif knight2story==1:
                        q("\n",.2)
                    elif secret2story==1:
                        q("\n",.2)
                elif secret1story==1:
                    if peashooter2story==1:
                        q("\n",.2)
                    elif mage2story==1:
                        q("\n",.2)
                    elif rouge2story==1:
                        q("\n",.2)
                    elif skele2story==1:
                        q("\n",.2)
                    elif bard2story==1:
                        q("\n",.2)
                    elif barbarian2story==1:
                        q("\n",.2)
                    elif knight2story==1:
                        q("\n",.2)
                #story starts
                
                q("er;lnjrgifdsgdsjgsdbosodhsdfhddsbsdbsdoubsdjfbdsjbfdsjklfbhdosbhosdfbhs\n",2)
        else:
            q("coming soon\n",.1)                     
    else:
        q("Please give a valid option.\n",0)
    q("1: Yes\n",.1)
    q("2: No\n",.1)
    q("Play again?: \n",0)
    ac=int(input(""))
    q("\n",.1)
q("End of program\n",0)
