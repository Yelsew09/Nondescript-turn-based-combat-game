#A big part of this game's loop control are Correct variables
#These are just variables with a binary (0 or 1) value.
#They allow the user to correct a bad input or lead them to a specific part of the program
#It's the break and continue commands with an argument you can put in

#Imports random, which is used to generate random numbers used for combat within the game
#Imports time, which is used in a LOT of spots in the code, it's used for timings between text
#Imports sys, IDK what it does. All I know is that it's used in the q command
import random, time, sys
def q(str,temporal_distance):
    
    #Not entirely sure what this all does, all I know is that it rolls text instead of printing it all at once.
    
    #If I input 0, make it .02. I didn't want to write all that out every time
    if temporal_distance == 0:
        temporal_distance = .02
    
    #The actual text rolling
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(temporal_distance)
def explode():

    #A command used for crashing the game. Very useful if something seems impossible
    #Basically a failsafe
    #I have no clue how it works
    print("Something went wrong. explodeing...")
    try:
        explode()
    except:
        explode()
def wait(temporal_distance):
    
    #Literally just laziness. I don't want to type time.sleep(.15) every 5 seconds
    time.sleep(temporal_distance)
def confirm(temporal_distance):
    
    #Used as that arrow confirmation found in text bubbles in video games
    input(' >')
    time.sleep(temporal_distance)
def critnum(AD,num1,num2,show):
    
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
    if show:
        q("You rolled a " + str(critnumber) + "\n",0)
    return critnumber
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
            q("Please give a number.\n",0)
            ec = 0
    return option

#Do you want to see random numbers after their generated or not?
print_random = False

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
    
    #Reseting everything
    for i in range (1):
        P1AD = 0
        P2AD = 0
        P1ADTR = 0
        P2ADTR = 0
        P1DMGBOOST = 0
        P2DMGBOOST = 0
        P1SPOONS = 0
        P2SPOONS = 0
        P1KNIVES = 0
        P2KNIVES = 0
        P1POTS = 0
        P2POTS = 0
        P1GLOCK = 0
        P2GLOCK = 0
    
    q("1: Play the game\n",0)
    wait(.15)
    q("2: Guide\n",0)
    wait(.15)
    q("3: Options\n",0)
    wait(.15)
    q("4: Quit\n",0)
    wait(.15)
    option = ask("What would you like to do? ")
    wait(.5)

    #Guide
    if option == 2:
        q("Guide coming soon",0)
        confirm(.5)

    #Options
    elif option == 3:
        q("0: Cancel\n",0)
        wait(.15)
        q("1: Print randomly generated numbers. Currently set to - " + str(print_random) + "\n",0)
        wait(.15)
        
        #MenuCorrect
        #I know it's MagicCorrect later, but we'll ignore that
        mc = 0
        while mc == 0:
            option = ask("What would you like to change? ")
            
            #Cancel
            if option == 0:
                mc = 1
            
            #Print random numbers
            elif option == 1:
                
                if print_random:
                    q("print_random has been set to False\n",0)
                    print_random = False
                    mc = 1
                
                elif not print_random:
                    q("print_random has been set to True\n",0)
                    print_random = True
                    mc = 1
                
                else:
                    explode()
            
            else:
                q("Please give an option we can use.",0)
                wait(.5)

    #Ends program
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
                        q("Please choose a valid option",0)
                        confirm(.5)
                        rc = 1
                
                #YesNoCorrect. Used for a yes/no situation
                ync = 0
                while ync == 0:
                    q("1: Yes\n",0)
                    wait(.15)
                    q("2: No\n",0)
                    wait(.15)
                    yesorno = ask("Player 1 has choesn the " + str(option) + " class. Is this correct? ")
                    
                    if yesorno == 1:
                        q("Player 1 has chosen the " + str(option) + " class.",0)
                        confirm(.5)
                        ync = 1
                        oc = 1
                    
                    elif yesorno == 2:
                        q("Repick your character.",0)
                        confirm(.5)
                        oc = 0
                        ync = 1
                    
                    else:
                        q("Pleae give a valid number.\n",0)
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
                        q("Player 2 has chosen the " + str(option) + " class.",0)
                        confirm(.5)
                        oc = 1
                        ync = 1
                    
                    elif yesorno == 2:
                        q("Repick your character.",0)
                        confirm(.5)
                        ync = 1

                    else:
                        q("Please give an option we can use.\n",0)
                        wait(.5)


            #CombatCorrect. Used for combat
            #Will stop when either or both characters reach 0 HP
            cc = 0
            while cc == 0:
                turn = 0
                if P1SPD > P2SPD:

                    #Player 1's turn when they go first
                    #Otherwise just setting up variables for the turn
                    items_left = 3
                    turn = turn + 1
                    q("This is turn " + str(turn) + "\n",0)
                    wait(.3)
                    q("Player 1 has + " + str(P1HP) + "/" + str(P1MAXHP) + "HP left, and " + str(P1MP) + "/" + str(P1MAXMP) + "MP left",0)
                    confirm(.3)
                    q("Player 2 has + " + str(P2HP) + "/" + str(P2MAXHP) + "HP left, and " + str(P2MP) + "/" + str(P2MAXMP) + "MP left",0)
                    confirm(.3)

                    #OptionCorrect to mark the start of the turn
                    oc = 0
                    while oc == 0:
                        q("1: Attack\n",0)
                        wait(.15)
                        q("2: Magic\n",0)
                        wait(.15)
                        q("3: Use an item\n",0)
                        wait(.15)
                        q("4: Pass turn\n",0)
                        wait(.15)
                        option = ask("What would you like to do? ")

                        #Attack
                        if option == 1:

                            critnumber = critnum(P1AD,1,20,print_random)
                            
                            #Even if you don't want to see a random number printed, you need to see this one
                            if not print_random:
                                q("You rolled a " + str(critnumber),0)
                            confirm(.5)

                            #Critical hit
                            if critnumber == 20:
                                q("IT'S A CRITICAL HIT!!!",0)
                                confirm(.15)
                                q("Player 1 did " + str(P1ATK*2) + " damage to player 2",0)
                                confirm(.5)
                                P2HP = P2HP - (P1ATK*2)
                                ec = 1
                                oc = 1
                                
                            #Hit
                            elif critnumber + P1ATKBON > P2DEF:
                                q("Player 1 landed a hit, doing " + str(P1ATK) + " damage to Player 2.",0)
                                confirm(.5)
                                P2HP = P2HP - P1ATK
                                ec = 1
                                oc = 1
                                
                            #Miss
                            elif critnumber + P1ATKBON < P2DEF:
                                q("Player 1 missed their attack.",0)
                                confirm(.5)
                                ec = 1
                                oc = 1
                                
                            #If all else fails...
                            else:
                                explode()
                            P1ATKBON = 0
                            
                        #Magic
                        elif option == 2:
                            q("1: Fireball - 5MP\n",0)
                            wait(.15)
                            q("2: Summon a random item - 2MP\n",0)
                            wait(.15)
                            q("3: Gain advantage on your next turn - 5MP\n",0)
                            wait(.15)
                            q("4: Impose disadvantage on your opponent's next turn - 5MP\n",0)
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
    
                                #Fireball - 5MP
                                if option == 1:
                                        
                                    #Not enough MP
                                    if P1MP < 5:
                                        q("You don't have enough MP for that.",0)
                                        confirm(.5)
                                    
                                    else:
                                        critnumber = critnum(0,round(P1MAXMP/2,0),P1MAXMP,print_random)

                                        #If the magic is so bad, it will get blocked
                                        if round(P2DEF/4,0) >= critnumber:
                                            q("Your opponent's defence blocked the " + str(critnumber) + " damage you tried to do.",0)
                                            confirm(.5)
                                        
                                        #If you are competent enough to make an effective fireball
                                        else:
                                            q("Player 1 did " + str(critnumber) + " damage to player 2.",0)
                                            confirm(.5)
                                            P2HP = P2HP - critnumber
                                            P1MP = P1MP - 5
                                            oc = 1
                                            mc = 0

                                #Make a random item - 2MP
                                elif option == 2:

                                    #Not enough MP
                                    if P1MP < 2:
                                        q("You don't have enough MP for that.",0)
                                        confirm(.5)
                                        
                                    else:
                                        critnumber = critnum(0,1,100,print_random)
                                        q("You rolled a " + str(critnumber),0)
                                        confirm(.5)
                                            
                                        #If critnumber is between 1 and 10:
                                        #Rusty Spoon
                                        if critnumber >= 1 and critnumber <= 10:                                                
                                            q("You conjured up a...\n",0)
                                            wait(.5)
                                            q("Rusty...",.5)
                                            wait(.6)
                                            q("Spoon?",0)
                                            confirm(.5)
                                            P1SPOONS = P1SPOONS + 1
                                            
                                        #If critnumber is between 11 and 55:
                                        #Throwing knives
                                        elif critnumber >= 11 and critnumber <= 55:
                                            q("You conjured up a few throwing knives",0)
                                            confirm(.5)
                                            P1KNIVES = P1KNIVES + 3
                                            
                                        #If critnumber is between 56 and 99:
                                        #Healing potion
                                        elif critnumber >= 56 and critnumber <= 99:
                                            q("You got a healing potion!",0)
                                            confirm(.5)
                                            P1POTS = P1POTS + 1
                                            
                                        #HE HAS A GUN
                                        elif critnumber == 100:

                                            #If P2 has a gun, now they both do
                                            if P1GLOCK == 0 and P2GLOCK == 1:
                                                q("Ok, great. Now the OTHER guy has a gun.\n",.2)
                                                wait(.3)
                                                wait(.15)
                                                q("I'm leaving.",.2)
                                                confirm(.5)
                                                P1GLOCK = P1GLOCK + 1
                                                
                                            #If P1 already had a gun
                                            elif P1GLOCK > 0:
                                                q("You did it again.\n",.4)
                                                wait(1)
                                                q("Landed a 1 in 100 chance to get a literal GUN.\n",.3)
                                                wait(.5)
                                                q("That thing could've won you the game intstanly.\n",.1)
                                                wait(.3)
                                                wait(.15)
                                                q("And you kept going.\n",.1)
                                                wait(2)
                                                q("\n",0)
                                                print("WHY?!?!?")
                                                wait(.5)
                                                q("Alright, I'm ending this here and now.\n",0)
                                                wait(.8)
                                                q("God landed a destructive hit, doing " + str(999+P2HP) + " damage to player 2.",0)
                                                confirm(1)
                                                for i in range (5):
                                                    print("Calculating, please wait.")
                                                    wait(.5)
                                                    print("Calculating failed.")
                                                    wait(.3)
                                                    if i > 5:
                                                        print("Retrying...")
                                                        wait(.2)
                                                q("Player 2 has ValueError HP left.",0)
                                                confirm(.5)
                                                
                                            #The first gun in the game
                                            elif P1GLOCK == 0 and not P2GLOCK == 1:
                                                q("You conjured up a... ",0)
                                                wait(.3)
                                                print("GUN?!?!?!?")
                                                wait(.3)
                                                q("Like, not even an old gun like a musket.",0)
                                                wait(.3)
                                                q("It's just a Glock-19",0)
                                                wait(.3)
                                                q("I quit",0)
                                                confirm(.5)
                                                P1GLOCK = P1GLOCK + 1
                                                
                                            #If all else fails...
                                            else:
                                                explode()
                                        
                                        #If all else fails...
                                        else:
                                            explode()
                                        oc = 1
                                        P1MP = P1MP - 2
                                        mc = 1

                                #Gain advantage - 5MP
                                elif option == 3:
                                    
                                    #Not enough MP
                                    if P1MP < 5:
                                        q("You don't have enough MP for that")
                                        confirm(.5)
                                        
                                    else:
                                        q("You gained advantage on your next turn.",0)
                                        confirm(.5)
                                        P1AD = 1
                                        P1ADTR = 2
                                        oc = 0
                                        P1MP = P1MP - 5
                                    mc = 0
                                    
                                #Impose disadvantage - 5MP
                                elif option == 4:

                                    #Not enough MP
                                    if P1MP < 5:
                                        q("You don't have enough MP for that",0)
                                        confirm(.5)

                                    else:

                                        #If Player 2 already had advantage
                                        if P2AD == 1:
                                            q("You got rid of Player 2's advantage.",0)
                                            confirm(.5)
                                            P2AD = 0
                                            P2ADTR = 0

                                        #If Player 2 already had disadvantage or neutral advantage
                                        else:
                                            q("You gave Player 2 disadvantage on their next turn.",0)
                                            confirm(.5)
                                            P2AD = 2
                                            P2ADTR = 1
                                        oc = 0
                                        P1MP = P1MP - 5
                                    mc = 0

                                #Heal 20% of max HP - 5MP
                                elif option == 5:

                                    #Not enough MP
                                    if P1MP < 5:
                                        q("You don't have enough MP for that.",0)
                                        confirm(.5)
                                    
                                    elif P1HP >= P1MAXHP:
                                        q("You are already at maximum HP.",0)
                                        confirm(.5)
                                        P1HP = P1MAXHP
                                    
                                    else:
                                        HEAL = round(P1MAXHP/5)
                                        q("You healed " + str(HEAL) + " damage.",0)
                                        confirm(.2)
                                        P1HP = P1HP + HEAL

                                        #If healing would put you over your MAXHP
                                        if P1HP > P1MAXHP:
                                            q("But, that would've brought you over your maximum health.",0)
                                            confirm(.2)
                                            P1HP = P1MAXHP
                                        wait(.3)
                                        P1MP = P1MP - 5
                                        oc = 1
                                    mc = 1

                                #Damage boost - Varies
                                elif option == 6:

                                    #If P1 has NO MP
                                    if P1MP < 1:
                                        q("You have no MP, so therefor you cannot use this spell.",0)
                                        confirm(.5)

                                    else:
                                        q("For every MP you put into this spell, you will get a +2 damage boost to your next attack.\n",0)
                                        wait(.15)
                                        P1DMGBOOST = ask("How much MP would you like to put into this spell? ")
                                        wait(.5)

                                        #Cancel
                                        if P1DMGBOOST == 0:
                                            q("You canceled your damage boost.\n",0)

                                        else:

                                            #If P1 tries to spend more MP than they have
                                            if P1MP < P1DMGBOOST:
                                                q("You don't have enough MP for that amount of damage boost.",0)
                                                confirm(.5)
                                            
                                            #Sucess!
                                            else:
                                                P1MP = P1MP - P1DMGBOOST
                                                P1DMGBOOST = P1DMGBOOST * 1.25
                                                q("You gained a buff of +" + str(P1DMGBOOST) + " damage on your next attack.",0)
                                                confirm(.5)
                                                mc = 1
                                                oc = 1
                                    wait(.5)
                                                
                                #Spell descriptions
                                elif option == 7:
                                    q("Spell descriptions: \n",0)
                                    wait(.15)
                                    q("Fireball - 5MP. Create a ball of fire that crashes down on the target. This will do anywhere from half of your MAXMP to your MAXMP of almost unblockable damage. If you are to create a fireball that does so little damage, it will get blocked\n",0)
                                    wait(.15)
                                    q("Conjure a random item - 2 MP. Conjure a random item that can be used on your next turn.\n",0)
                                    wait(.15)
                                    q("Gain advantage - 5MP. Gain advantage until the end of your next turn. For more information on advantage, visit the guide in the Main Menu.\n",0)
                                    wait(.15)
                                    q("Impose disavantage - 5MP. Give your opponent disavnatage on their next turn, or get rid of thier advantage. For more information on advnatages, visit the guide in the Main Menu.\n",0)
                                    wait(.15)
                                    q("Heal 20 percent of MAXHP - 5MP. Heal 20 percent of your max HP. This cannot take you above your maximum, though.\n",0)
                                    wait(.15)
                                    q("Damage boost - Varies. Put as much MP as you want (and can) into this move, and have that amount multiplied by 1.25 and added to your next attack.",0)
                                    confirm(.5)
                                
                                else:
                                    q("Please give an option we can use.\n",0)
                                    wait(.5)

                        #Item
                        elif option == 3:
                            
                            yesorno = 1

                            #If there are no item uses left and you just selected it from the menu
                            if items_left == 0 and yesorno == 1:
                                q("You've used all your items this turn.",0)
                                confirm(.5)
                                ic = 0
                                yesorno = 0
                            
                            #If that was your last item usage
                            elif items_left == 0 and not yesorno == 1:
                                ic = 0
                                yesorno = 0
                            
                            #If you have items left to use
                            else:
                                q("You can use " + str(items_left) + " more items on this turn")
                                confirm(.3)
                                q("1: Spoons - " + str(P1SPOONS) + "\n",0)
                                wait(.15)
                                q("2: Knives - " + str(P1KNIVES) + "\n",0)
                                wait(.15)
                                q("3: Healing Potions - " + str(P1POTS) + "\n",0)
                                wait(.15)
                                
                                #Print properly if the gun is in play
                                if P1GLOCK >= 1:
                                    q("4: Glock 19\n",0)
                                    wait(.15)
                                    q("5: Cancel\n",0)
                                
                                #Print properly if the gun is not in play
                                else:
                                    q("4: Cancel\n",0)
                                wait(.15)
                                
                                #ItemCorrect
                                #The specific correct for item usage
                                ic = 0
                                while ic == 0:
                                    
                                    #If you just used an item and that was your last one
                                    if items_left == 0:
                                        ic = 1
                                        option = 0
                                    
                                    #If you have items left
                                    else:
                                        option = ask("What would you like to use? ")
                                        
                                        #Spoon
                                        if option == 1:
                                            
                                            #No spoons
                                            if P1SPOONS < 1:
                                                q("You don't have any spoons. No soup for you.",0)
                                                confirm(.5)
                                            
                                            else:
                                                critnumber = critnum(0,1,1000,print_random)
                                                
                                                #The 1 in 1000 chance to kill player 2 with tetanus
                                                if critnumber == 1000:
                                                    q("Player 2 got tetanus, dying on the spot.",0)
                                                    confirm(.5)
                                                    ic = 1
                                                    oc = 1
                                                    P2HP = P2HP - P2HP
                                                
                                                #The 1 in 1000 chance to die from tetanus due to holding the spoon
                                                elif critnumber == 1:
                                                    q("Player 1 got tetanus, dying on the spot.",0)
                                                    confirm(.5)
                                                    ic = 1
                                                    oc = 1
                                                    P1HP = P1HP - P1HP
                                                
                                                #If it all goes normally
                                                else:
                                                    q("You threw a spoon, doing 1 point of damage to Player 2",0)
                                                    confirm(.5)
                                                    P2HP = P2HP - 1
                                                items_left = items_left - 1
                                                P1SPOON = P1SPOON - 1
                                        
                                        #Knife
                                        elif option == 2:
                                            
                                            #No knives
                                            if P1KNIVES < 1:
                                                input("You don't have any knives. Want a pencil instead? ")
                                                wait(.3)
                                                q("Well I don't have any.\n",0)
                                                wait(.5)
                                            
                                            else:
                                                critnumber = critnum(0,1,50,print_random)
                                                
                                                #Miss
                                                if critnumber == 50:
                                                    q("You threw a knive, completely missing your opponent.",0)
                                                    confirm(.3)
                                                    items_left = items_left - 1
                                                
                                                #Hit
                                                else:
                                                    critnumber = critnum(0,1,5,print_random)
                                                    q("Player 1 threw a knife, doing " + str(critnumber) + " damage to player 2",0)
                                                    confirm(.5)
                                                    P2HP = P2HP - critnumber
                                                    P1KNIVES = P1KNIVES - 1
                                                    items_left = items_left - 1
                                        
                                        #Healing Potion
                                        elif option == 3:
                                            
                                            #No healing potions
                                            if P1POTS < 1:
                                                q("You don't have any healing potions.",0)
                                                confirm(.5)
                                            
                                            #Already at max health
                                            elif P1HP >= P1MAXHP:
                                                q("You are already at maximum health.",0)
                                                confirm(.5)
                                                P1HP = P1MAXHP
                                            
                                            else:
                                                HEAL = critnum(0,2,5,print_random)
                                                q("Player 1 healed " + str(HEAL) + " damage")
                                                confirm(.2)
                                                
                                                #If healing would've brought you over maximum HP
                                                if P1HP > P1MAXHP:
                                                    q("But that would've taken you over your maximum HP.",0)
                                                    confirm(.2)
                                                    P1HP = P1MAXHP
                                                wait(.3)
                                                P1POTS = P1POTS - 1
                                                items_left = items_left - 1
                                        
                                        #Shoot the gun (if you have it)
                                        elif option == 4 and P1GLOCK > 0:
                                            critnumber = critnum(0,1,1000)
                                            
                                            #You landed the 1 in 1000 chance to MISS
                                            if critnumber == 1:
                                                q("You missed.",0)
                                                confirm(.2)
                                                q("And that's the last shot in the clip.",0)
                                                wait(.5)
                                                q("My man really conjured up a one shot weapon with one shot",0)
                                                confirm(.5)
                                                P1GLOCK = P1GLOCK - 1
                                            
                                            #So anyway, I started blasting
                                            else:
                                                q("Player 1 shot their gun, hitting player 2 and doing " + str(P2HP) + " damage to player 2",0)
                                                confirm(.5)
                                                P1GLOCK = P1GLOCK - 1
                                                items_left = 0
                                        
                                        #Cancels item usage (if you have the gun)
                                        elif option == 5 and P1GLOCK > 0:
                                            q("You canceled your item usage\n",0)
                                            ic = 1
                                        
                                        #Cancels item usage (if you don't have the gun)
                                        elif option == 4 and not P1GLOCK > 0:
                                            q("You canceled your item usage\n",0)
                                            ic = 1
                                        
                                        else:
                                            q("Please give an option we can use.\n",0)

                        #Pass turn
                        elif option == 4:
                                q("You passed your turn.\n",0)
                                oc = 1
                            
                        #Not a valid input
                        else:
                                q("Please give an option we can use.\n",0)
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
        q("Please give an option we can use.\n",0)
        wait(.5)
q("End of program\n",0)