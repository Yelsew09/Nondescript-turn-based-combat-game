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
def wait(temporal_distance):
    time.sleep(temporal_distance)
def confirm():
    confirm = input("")
def critnum(AD,num1,num2):
    
    #Used to generate random numbers
    #If advantage isn't being used, put 0 in for the first number
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
def q(str,temporal_distance):
    if temporal_distance == 0:
        temporal_distance = .02
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(temporal_distance)
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
def ask(question):
    
    #Ask. Replaces error correct
    #Asks a question and repeats until the user gives a numerical input
    ec = 0
    while ec == 0:
        try:
            q(question,0)
            option = int(input(''))
            ec = 1
        except ValueError:
            wait(.5)
            q("Please give a numerical value.\n",0)
            ec = 0
    return option

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

#THE GAME
q("Welcome to Dungeons and Damage.\n",0)
wait(.5)
q("Not to be confused with Dungeons and Dragons.\n",0)
wait(.5)
q("There are no dungeons here, but there is a lot of damage.\n",0)
wait(.5)
q("Informally known as HELL.\n",0)
wait(.5)

#AllCorrect. The main while loop that loops the ENTIRE PROGRAM
ac = 0
while ac == 0:
    q("1: Play the game\n",0)
    wait(.15)
    q("2: Guide\n",0)
    wait(.15)
    q("3: Options\n",0)
    wait(.15)
    q("4: Quit\n",0)
    wait(.15)
    
    option = ask("What would you like to do? ")

    if option == 2:
        
        #Guide
        q("Guide coming soon\n",0)
        confirm()
        wait(.5)
    
    
    elif option == 3:

        #Options
        q("Options coming soon\n",0)
        confirm()
        wait(.5)
    
    elif option == 4:
        #Ends program
        ac = 1
    
    
    elif option == 1:
        
        #Starts the game part of the program
        #GameCorrect. Allows for someone to go back and play the game again if they want to. 
        gc = 0
        while gc == 0:
            q("1: Knight\n",0)
            wait(.15)
            q("2: Peashooter\n",0)
            wait(.15)
            q("3: Mage\n",0)
            wait(.15)
            q("4: Rouge\n",0)
            wait(.15)
            q("5: Skele\n",0)
            wait(.15)
            q("6: Bard\n",0)
            wait(.15)
            q("7: Barbarian\n",0)
            wait(.15)
            q("8: Random\n",0)
            
            #OptionCorrect. Used for when the user could give a bad input. Not needed in the menus b/c it can just loop to the begining of AllCorrect
            #Character select for player 1
            oc = 0
            while oc == 0:

                option = ask("Please select a class, player 1. ")
                
                #RandomCorrect. Used specifically here and used for determining a random character
                rc = 0
                while rc == 0:
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
                    elif option == 8:
                        option = random.randint(1,7)
                    
                    else:
                        q("Please choose a valid option\n",0)
                        confirm()
                        rc = 1
                        wait(.5)
                
                #YesNoCorrect. Used for a yes/no situation
                ync = 0
                while ync == 0:
                    q("1: Yes\n",0)
                    wait(.15)
                    q("2: No\n",0)
                    wait(.15)
                    yesorno = ask("Player 1 has choesn the " + str(option) + " class. Is this correct? ")
                    
                    if yesorno == 1:
                        q("Player 1 has chosen the " + str(option) + "class.\n",0)
                        confirm()
                        ync = 1
                        oc = 1
                    
                    elif yesorno == 2:
                        q("Repick your character.\n",0)
                        confirm()
                        oc = 0
                        ync = 1
                    
                    else:
                        q("Pleae give a valid number.\n",0)
                        confirm()
                    wait(.5)

            #OptionCorrect
            #Character select for player 2
            oc = 0
            while oc == 0:
                q("1: Knight\n",0)
                wait(.15)
                q("2: Peashooter\n",0)
                wait(.15)
                q("3: Mage\n",0)
                wait(.15)
                q("4: Rouge\n",0)
                wait(.15)
                q("5: Skele\n",0)
                wait(.15)
                q("6: Bard\n",0)
                wait(.15)
                q("7: Barbarian\n",0)
                wait(.15)
                q("8: Random\n",0)
                wait(.15)
                
                option = ask("Please select a class, player 2. ")
                
                #RandomCorrect
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
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
                        rc = 1
                    
                    elif option == 8:
                        option = random.randint(1,7)
                    
                    else:
                        q("Please choose a valid option.\n",0)
                        rc = 1
                        wait(.5)
                
                #YesNoCorrect
                ync = 0
                while ync == 0:
                    q("1: Yes\n",0)
                    wait(.15)
                    q("2: No\n",0)
                    wait(.15)
                    yesorno = ask("Player 2 has chosen the " + str(option) + " class, is this correct? ")
                    
                    if yesorno == 1:
                        q("Player 2 has chosen the " + str(option) + " class.\n",0)
                        oc = 1
                        ync = 1
                    
                    elif yesorno == 2:
                        q("Repick your character.\n",0)
                        ync = 1
                    
                    else:
                        q("Please give a valid number.\n",0)
                    wait(.5)
            
            #CombatCorrect. Used for combat
            #Will stop when either or both characters reach 0 HP
            cc = 0
            while cc == 0:
                if P1SPD > P2SPD:
                    
                    #Player 1's turn when they go first
                    #OptionCorrect
                    oc = 0
                    while oc == 0:
                        q("Player 1 has + " + str(P1HP) + "/" + str(P1MAXHP) + "HP left, and " + str(P1MP) + "/" + str(P1MAXMP) + "MP left\n",0)
                        confirm()
                        q("Player 2 has + " + str(P2HP) + "/" + str(P2MAXHP) + "HP left, and " + str(P2MP) + "/" + str(P2MAXMP) + "MP left\n",0)
                        confirm()
                        q("1: Attack\n",0)
                        wait(.15)
                        q("2: Magic\n",0)
                        wait(.15)
                        q("3: Use an item\n",0)
                        wait(.15)
                        q("4: Pass turn\n",0)
                        wait(.15)
                        
                        option = ask("What would you like to do? ")
                        if option == 1:

                            #Attack
                            critnumber = critnum(P1AD,1,20)
                            q("You rolled a " + str(critnumber) + "\n",0)
                            confirm()
                            wait(.5)
                            
                            if critnumber == 20:
        
                                #Critical hit
                                q("IT'S A CRITICAL HIT!!!\n",0)
                                wait(.15)
                                q("Player 1 did " + str(P1ATK*2) + " damage to player 2\n",0)
                                confirm()
                                wait(.5)
                                P2HP = P2HP - (P1ATK*2)
                                ec = 1
                                oc = 1
                            
                            elif critnumber + P1ATKBON > P2DEF:
                                    
                                #Hit
                                q("Player 1 landed a hit, doing " + str(P1ATK) + " damage to Player 2.\n")
                                confirm()
                                wait(.5)
                                P2HP = P2HP - P1ATK
                                ec = 1
                                oc = 1
                            
                            elif critnumber + P1ATKBON < P2DEF:
                                        
                                #Miss
                                q("Player 1 missed their attack.")
                                confirm()
                                wait(.5)
                                ec = 1
                                oc = 1
                            
                            else:
                                explode()
                            P1ATKBON = 0
                        
                        elif option == 2:

                            #Magic
                            q("1: Fireball - 5MP\n",0)
                            wait(.15)
                            q("2: Summon a random item - 2MP\n",0)
                            wait(.15)
                            q("3: Gain advantage on your next turn - 5MP\n",0)
                            wait(.15)
                            q("4: Impose disadvantage on your opponent's next attack - 5MP\n",0)
                            wait(.15)
                            q("5: Heal 20 percent of your max health - 5MP\n",0)
                            wait(.15)
                            q("6: Gain a damage boost on your next attack - Varies\n",0)
                            wait(.15)
                            q("Currently 7: Spell descriptions\n",0)
                            wait(.15)
                            q("0: Cancel\n",0)
                            wait(.15)
                                
                            #MagicCorrect. We can't use OptionCorrect, so we have to use a more specific variable
                            #On a basic level, its purpose is the same as OptionCorrect
                            mc = 0
                            while mc == 0:   
                                option = ask("What would you like to do? ")
                                if option == 1:
                                    
                                    #Fireball
                                    if P1MP < 5:
                                        q("You don't have enough MP for that.\n",0)
                                        confirm()
                                        wait(.5)
                                    else:
                                        critnumber = critnum(0,12,18)
                                        q("Player 1 did " + str(critnumber) + " damage to player 2.\n",0)
                                        confirm()
                                        wait(.5)
                                        P2HP = P2HP - critnumber
                                        P1MP = P1MP - 5
                                        oc = 1
                                    mc = 0

                                elif option == 2:
                                    
                                    #Random item
                                    if P1MP < 2:
                                        q("You don't have enough MP for that.")
                                        confirm()
                                        wait(.5)
                                    else:
                                        critnumber = critnum(0,1,100)
                                        q("You rolled a " + str(critnumber) + ".\n",0)
                                        confirm()
                                        wait(.5)
                                        if critnumber >= 1 and critnumber <= 10:
                                            
                                            #If critnumber is between 1 and 10:
                                            #Rusty Spoon
                                            q("You conjured up a...\n",0)
                                            wait(.5)
                                            q("Rusty...",.5)
                                            wait(.6)
                                            q("Spoon?\n",0)
                                            confirm()
                                            P1SPOON = P1SPOON + 1
                                            wait(.5)
                                        
                                        elif critnumber >= 11 and critnumber <= 55:
                                            
                                            #If critnumber is between 11 and 55:
                                            #Throwing knives
                                            q("You conjured up a few throwing knives\n",0)
                                            confirm()
                                            P1KNIVES = P1KNIVES + 3
                                            wait(.5)
                                        
                                        elif critnumber >= 56 and critnumber <= 99:
                                            
                                            #If critnumber is between 56 and 99:
                                            #Healing potion
                                            q("You got a healing potion!\n",0)
                                            confirm()
                                            P1POTS = P1POTS + 1
                                            wait(.5)
                                        
                                        elif critnumber == 100:
                                            
                                            #HE HAS A GUN
                                            if P1GLOCK == 0 and P2NARRATORS == 1:
                                                #If P2 has a gun, now they both do
                                                q("Ok, great. Now the OTHER guy has a gun.\n",.2)
                                                confirm()
                                                wait(.15)
                                                q("I'm leaving.\n",.2)
                                                confirm()
                                                wait(.5)
                                                P1NARRATORS = 1
                                            
                                            elif P1NARRATORS > 0:
                                                #If P1 already had a gun
                                                q("You did it again.\n",.4)
                                                confirm()
                                                wait(.15)
                                                q("Landed a 1 in 100 chance to get a literal GUN.\n",.3)
                                                confirm()
                                                wait(.15)
                                                q("That thing could've won you the game intstanly.\n",.1)
                                                confirm()
                                                wait(.15)
                                                q("And you kept going.",.1)
                                                confirm()
                                                wait(.15)
                                                print(" ")
                                                q("WHY?!?!?\n",0)
                                                confirm()
                                                wait(.15)
                                                q("Alright, I'm ending this here and now.\n",0)
                                                confirm()
                                                wait(.15)
                                                q("God landed a destructive hit, doing " + str(999+P2HP) + " damage to player 2.\n",0)
                                                confirm()
                                                wait(.5)
                                                for i in range (5):
                                                    print("Calculating, please wait.")
                                                    wait(.5)
                                                    print("Calculating failed.")
                                                    wait(.3)
                                                    print("Retrying...")
                                                    wait(.2)
                                                    if not i == 0 or not i == 5:
                                                        print("Attempt #", str(i))
                                                q("Player 2 has " + str(P2HP) + "HP left.\n",0)
                                                confirm()
                                                wait(.5)
                                            
                                            elif P1GLOCK == 0 and not P2NARRATORS == 1:
                                                
                                                #The first gun in the game
                                                q("You conjured up a...",0)
                                                wait(.2)
                                                q("GUN?!?!?!?\n",.01)
                                                wait(.2)
                                                q("Like, not even an old gun like a musket.\n",0)
                                                wait(.4)
                                                q("It's just a Glock-19\n",0)
                                                wait(5)
                                                q("I quit\n",0)
                                                wait(.5)
                                            
                                            else:
                                                
                                                #If all else fails...
                                                explode()
                                        else:

                                            #If all else fails...
                                            explode()
                                        oc = 1
                                    mc = 1

                                elif option == 3:
                                    q("You don't have enough MP for that")
                                    confirm()
                                    wait(.5)
                        elif option == 3:

                            #Use an item
                            q("Spoons: " + str(P1SPOON) + "\n",0)
                            wait(.15)
                            q("Knives: " + str(P1KNIVES) + "\n",0)
                            wait(.15)
                        elif option == 4:
                            q("Pass turn\n",0)
                        else:
                            q("Please give a valid number.\n",0)
                            ec = 0
                            oc = 0
                            wait(.5)
                elif P2SPD > P1SPD:
                    q("Player 2 first, then player 1\n",0)
                else:
                    q("Since you have the same speed, we are randomly going to pick a character to go first.\n",0)
                    option = random.randint(1,2)
                    if option == 1:
                        P1SPD = P1SPD + 1
                    elif option == 2:
                        P2SPD = P2SPD + 1
                    else:
                        explode()
    else:
        q("Please give a valid option.\n",0)
        wait(.5)
q("End of program\n",0)