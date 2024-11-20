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


reset()
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
    
    #ErrorCorrect. Allows for a repeat if a ValueError occurs
    ec = 0
    while ec == 0:
        try:
            q("What would you like to do? ",0)
            option = int(input(''))
            ec = 1
            wait(.5)
        except ValueError:
            q("Please give a number.\n",0)
            oc = 0

    if option == 2:
        
        #Guide
        q("Guide coming soon\n",0)
    
    
    elif option == 3:

        #Options
        q("Options coming soon\n",0)
    
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
            oc = 0
            while oc == 0:
                
                #ErrorCorrect
                ec = 0
                while ec == 0:
                    try:
                        q("Please select a class, Player 1. ",0)
                        option = int(input(''))
                        ec = 1
                        wait(.5)
                    except ValueError:
                        q("Please give a number.\n",0)
                        ec = 0
                        wait(.5)
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
                        rc = 1
                        wait(.5)
                ync = 0
                while ync == 0:
                    q("1: Yes\n",0)
                    wait(.15)
                    q("2: No\n",0)
                    wait(.15)
                    ec = 0
                    while ec == 0:
                        try:
                            q("Player 1 has chosen the " + str(option) + " class, is this correct? ",0)
                            yesorno = int(input(''))
                            wait(.3)
                            if yesorno == 1:
                                q("Player 1 has chosen the " + str(option) + " class.\n",0)
                                wait(.5)
                                ync = 1
                                oc = 1
                            elif yesorno == 2:
                                q("Repeck your character.\n",0)
                                wait(.5)
                                ync = 1
                            else:
                                q("Please choose a valid option.\n",0)
                            ec = 1
                        except ValueError:
                            q("Please give a number.\n",0)
                            ec = 0
                            wait(.5)


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
                ec = 0
                while ec == 0:
                    try:
                        q("Please choose a class, player 2. ",0)
                        option = int(input(''))
                        ec = 1
                        wait(.5)
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
                ync = 0
                while ync == 0:
                    q("1: Yes\n",0)
                    wait(.15)
                    q("2: No\n",0)
                    wait(.15)
                    ec = 0
                    while ec == 0:
                        try:
                            q("Player 2 has chosen the " + str(option) + " class, is this correct? ",0)
                            yesorno = int(input(''))
                            wait(.3)
                            if yesorno == 1:
                                q("Player 2 has chosen the " + str(option) + " class.\n",0)
                                wait(.15)
                                ync = 1
                                oc = 1
                            elif yesorno == 2:
                                q("Repeck your character.\n",0)
                                wait(.15)
                                ync = 1
                            else:
                                q("Please choose a valid option\n",0)
                            ec = 1
                        except ValueError:
                            q("Please give a number.\n",0)
                            ec = 0
                            wait(.5)
    else:
        q("Please give a valid option.\n",0)
        wait(.5)
q("End of program\n",0)