errmsg = "If you are seeing this, something went wrong. Please restart the program."
import random
print("Welcome to insert game title here")
print("")
print("Please select a class, player 1.")
print("1: Knight")
print("2: Peashooter")
print("3: Mage")
print("4: Rouge")
print("5: Sans")
print("6: Bard")
print("7: Barbarian")
#Player 1 selects a class
cc = 0
ac = 0
while ac == 0:
    while cc == 0:
        player1class = int(input("Choose a class from the list above (please choose a number): "))
        if player1class == 1:
            player1class = "Knight"
            P1HP = 42
            P1MAXHP = P1HP
            P1ATK = 12
            P1ATKBON = 2
            P1DEF = 14
            P1MP = 4
            P1MPBON = 1
            P1MAXMP = P1MP
            P1SPD = 3
            P1SPDBON = 2
            cc = 1
        elif player1class == 2:
            player1class = "Peashooter"
            P1HP = 35
            P1MAXHP = P1HP
            P1ATK = 10
            P1ATKBON = 1
            P1DEF = 14
            P1MP = 5
            P1MPBON = 1
            P1MAXMP = P1MP
            P1SPD = 6
            P1SPDBON = 2
            cc = 1
        elif player1class == 3:
            player1class = "Mage"
            P1HP = 29
            P1MAXHP = P1HP
            P1ATK = 7
            P1ATKBON = 2
            P1DEF = 10
            P1MP = 20
            P1MPBON = 5
            P1MAXMP = P1MP
            P1SPD = 2
            P1SPDBON = 2
            cc = 1
        elif player1class == 4:
            player1class = "Rouge"
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
            cc = 1
        elif player1class == 5:
            player1class = "Sans"
            P1HP = 1
            P1MAXHP = P1HP
            P1ATK = 20
            P1ATKBON = 4
            P1DEF = 20
            P1MP = 15
            P1MPBON = 3
            P1MAXMP = P1MP
            P1SPD = 4
            P1SPDBON = 2
            cc = 1
        elif player1class == 6:
            player1class = "Bard"
            P1HP = 37
            P1MAXHP = P1HP
            P1ATK = 7
            P1ATKBON = 1
            P1DEF = 13
            P1MP = 17
            P1MPBON = 4
            P1MAXMP = P1MP
            P1SPD = 5
            P1SPDBON = 2
            cc = 1
        elif player1class == 7:
            player1class = "Barbarian"
            P1HP = 52
            P1MAXHP = P1HP
            P1ATK = 14
            P1ATKBON = 2
            P1DEF = 11
            P1MP = 2
            P1MPBON = .25
            P1MAXMP = P1MP
            P1SPD = 4
            P1SPDBON = 2
            cc = 1
        else:
            print("Please give a valid number.")
            cc = 0
    print("1: Yes")
    print("2: No")
    yesorno = int(input("You have chosen " + str(player1class) + ". Is this correct?: "))
    if yesorno == 1:
        print("Player 1 has chosen the " + str(player1class) + " class.")
        print("")
        ac = 1
    elif yesorno == 2:
        print("Repick your charcter.")
        ac = 0
    else:
        print("Something went wrong please try again")
        ac = 0
cc = 0
ac = 0
#Player 2 selects a class
while ac == 0:
    while cc == 0:
        print("Please select a classs, player 2")
        player2class = int(input("Choose 1 from the list above (please choose a number): "))
        if player2class == 1:
            player2class = "Knight"
            P2HP = 42
            P2MAXHP = P2HP
            P2ATK = 12
            P2ATKBON = 2 
            P2DEF = 14
            P2MP = 4
            P2MPBON = 1
            P2MAXMP = P2MP
            P2SPD = 3
            P2SPDBON = 2
            cc = 1
        elif player2class == 2:
            player2class = "Peashooter"
            P2HP = 35
            P2MAXHP = P2HP
            P2ATK = 10
            P2ATKBON = 1 
            P2DEF = 14
            P2MP = 5
            P2MPBON = 1
            P2MAXMP = P2MP
            P2SPD = 6
            P2SPDBON = 2
            cc = 1
        elif player2class == 3:
            player2class = "Mage"
            P2HP = 29
            P2MAXHP = P2HP
            P2ATK = 7
            P2ATKBON = 2
            P2DEF = 10
            P2MP = 20
            P2MPBON = 5
            P2MAXMP = P2MP
            P2SPD = 2
            P2SPDBON = 2
            cc = 1
        elif player2class == 4:
            player2class = "Rouge"
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
            cc = 1
        elif player2class == 5:
            player2class = "Sans"
            P2HP = 1
            P2MAXHP = P2HP
            P2ATK = 20
            P2ATKBON = 4
            P2DEF = 20
            P2MP = 15
            P2MPBON = 3
            P2MAXMP = P2MP
            P2SPD = 4
            P2SPDBON = 2
            cc = 1
        elif player2class == 6:
            player2class = "Bard"
            P2HP = 37
            P2MAXHP = P2HP
            P2ATK = 7
            P2ATKBON = 1
            P2DEF = 13
            P2MP = 17
            P2MPBON = 4
            P2MAXMP = P2MP
            P2SPD = 5
            P2SPDBON = 2
            cc = 1
        elif player2class == 7:
            player2class = "Barbrian"
            P2HP = 52
            P2MAXHP = P2HP
            P2ATK = 14
            P2ATKBON = 2
            P2DEF = 11
            P2MP = 2
            P2MPBON = 0
            P2MAXMP = P2MP
            P2SPD = 4
            P2SPDBON = 2
            cc = 1
        else:
            print("Please give a valid number.")
    print("1: Yes")
    print("2: No")
    yesorno = int(input("You have chosen " + str(player2class) + ". Is this correct?: "))
    if yesorno == 1:
        print("Player 2 has chosen the " + str(player2class) + " class.")
        print("")
        ac = 1
    elif yesorno == 2:
        print("Repick your charcter.")
        cc = 0
    else:
        print("Please try again")
        cc = 0
ac = 1
mc = 0
cc = 0
P1AD = 0
P2AD = 0
P1ADTR = 0
P2ADTR = 0
P1DMGBOOST = 0
P2DMGBOOST = 0
while ac == 1:
    if P1HP <= 0:
        ac = 0
        winner = "Player 2"
    elif P2HP <= 0:
        ac = 0
        winner = "Player 1"
    else:
        if P1SPD > P2SPD:
            while cc == 0:
                print("1: Attack")
                print("2: Magic")
                print("3: Run away (forfeit)")
                option = int(input("What would you like to do (give a number): "))
                if option == 1:
                    if P1AD == 1:
                        critnumber1 = random.randint(1,20)
                        critnumber2 = random.randint(1,20)
                        if critnumber1 > critnumber2:
                            critnumber = critnumber1
                        elif critnumber2 > critnumber1:
                            critnumber = critnumber2
                        else:
                            critnumber = critnumber1
                    elif P1AD == 2:
                        critnumber1 = random.randint(1,20)
                        critnumber2 = random.randint(1,20)
                        if critnumber1 > critnumber2:
                            critnumber = critnumber2
                        elif critnumber2 > critnumber1:
                            critnumber = critnumber1
                        else:
                            critnumber = critnumber2
                    else:
                        critnumber = random.randint(1,20)
                    if critnumber == 20:
                        print("Player 1 landed a critical hit, doing " + str((P1ATK+P1DMGBOOST)*2) + " damage to player 2")
                        P2HP = P2HP - (P1ATK + P1DMGBOOST)*2
                        print("Player 2 has " + str(P2HP) + "HP left.")
                        cc = 1
                    elif critnumber + P1ATKBON > P2DEF:
                        print("Player 1 rolled a " + str(critnumber) + ", landing a hit and doing " + str(P1ATK+P1DMGBOOST) + " damage to player 2.")
                        P2HP = P2HP - (P1ATK + P1DMGBOOST)
                        print("Player 2 has " + str(P2HP) + "HP left.")
                        cc = 1
                    elif critnumber + P1ATKBON < P2DEF:
                        print("Player 2 missed thier attack")
                        cc = 1
                    P1DMGBOOST = 0
                elif option == 2:
                    print("I need to import the magic system from Emilio's branch.")
                elif option == 3:
                    print("1: Yes")
                    print("2: No")
                    yesorno = int(input("Are you sure you want to forfeit the match"))
                    if yesorno == 1:
                        break
                    else:
                        print("You do not run away")
                else:
                    print("Please provide a valid number.")
            if P1ADTR == 2:
                P1ADTR == P1ADTR - 1
            elif P1ADTR == 1:
                P1AD = 0
                P1ADTR = 0
            else:
                P1ADTR = 0
            P1MP = P1MP + P1MPBON
            if P1MP > P1MAXMP:
                P1MP = P1MAXMP
            cc = 0
            while cc == 0:
                print("1: Attack")
                print("2: Magic")
                print("3: Run away (forfeit)")
                option = int(input("What would you like to do (give a number): "))
                if option == 1:
                    if P2AD == 1:
                        critnumber1 = random.randint(1,20)
                        critnumber2 = random.randint(1,20)
                        if critnumber1 > critnumber2:
                            critnumber = critnumber1
                        elif critnumber2 > critnumber1:
                            critnumber = critnumber2
                        else:
                            critnumber = critnumber1
                    elif P2AD == 2:
                        critnumber1 = random.randint(1,20)
                        critnumber2 = random.randint(1,20)
                        if critnumber1 > critnumber2:
                            critnumber = critnumber2
                        elif critnumber2 > critnumber1:
                            critnumber = critnumber1
                        else:
                            critnumber = critnumber2
                    else:
                        critnumber = random.randint(1,20)
                    if critnumber == 20:
                        print("Player 2 landed a critical hit, doing " + str((P2ATK+P2DMGBOOST)*2) + " damage to player 1")
                        P1HP = P1HP - (P2ATK+P2DMGBOOST)*2
                        print("Player 1 has " + str(P1HP) + "HP left")
                        cc = 1
                    elif critnumber + P2ATKBON > P1DEF:
                        print("Player 2 did " + str(P2ATK + P2DMGBOOST))
                        P1HP = P1HP - (P2ATK+P2DMGBOOST)
                        print("Player 1 has " + str(P1HP) + "HP left")
                        cc = 1
                    elif critnumber + P2ATKBON < P1DEF:
                        print("Player 2 missed their attack")
                        cc = 1
                    else:
                        print(errmsg)
                elif option == 2:
                    print("I need to import the magic system from Emilio's branch")
                elif option == 3:
                    print("1: Yes")
                    print("2: No")
                    yesorno = int(input("Are you sure you want to forfeit the match"))
                    if yesorno == 1:
                        break
                    else:
                        print("You do not run away")
            if P1ADTR == 2:
                P1ADTR == P1ADTR - 1
            elif P1ADTR == 1:
                P1AD = 0
                P1ADTR = 0
            else:
                P1ADTR = 0
            P1MP = P1MP + P1MPBON
            if P1MP > P1MAXMP:
                P1MP = P1MAXMP
            cc = 0
        elif P2SPD > P1SPD:
            cc = 0
            while cc == 0:
                print("1: Attack")
                print("2: Magic")
                print("3: Run away (forfeit)")
                option = int(input("What would you like to do (give a number): "))
                if option == 1:
                    if P2AD == 1:
                        critnumber1 = random.randint(1,20)
                        critnumber2 = random.randint(1,20)
                        if critnumber1 > critnumber2:
                            critnumber = critnumber1
                        elif critnumber2 > critnumber1:
                            critnumber = critnumber2
                        else:
                            critnumber = critnumber1
                    elif P2AD == 2:
                        critnumber1 = random.randint(1,20)
                        critnumber2 = random.randint(1,20)
                        if critnumber1 > critnumber2:
                            critnumber = critnumber2
                        elif critnumber2 > critnumber1:
                            critnumber = critnumber1
                        else:
                            critnumber = critnumber2
                    else:
                        critnumber = random.randint(1,20)
                    if critnumber == 20:
                        print("Player 2 landed a critical hit, doing " + str((P2ATK+P2DMGBOOST)*2) + " damage to player 1")
                        P1HP = P1HP - (P2ATK+P2DMGBOOST)*2
                        print("Player 1 has " + str(P1HP) + "HP left")
                        cc = 1
                    elif critnumber + P2ATKBON > P1DEF:
                        print("Player 2 did " + str(P2ATK + P2DMGBOOST))
                        P1HP = P1HP - (P2ATK+P2DMGBOOST)
                        print("Player 1 has " + str(P1HP) + "HP left")
                        cc = 1
                    elif critnumber + P2ATKBON < P1DEF:
                        print("Player 2 missed their attack")
                        cc = 1
                    else:
                        print(errmsg)
                elif option == 2:
                    while mc == 0:
                        print("0: Cancel")
                        print("1: Gain +1 permanent defence (Max of 15) - 1MP")
                        print("2: Damage boost on your next attack - Varies")
                        print("3: Gain advantage on your next turn - 3MP")
                        print("4: Heal 20 percent of your maximum HP - 4MP")
                        print("5: Fireball - 5MP")
                        print("6: Provide descriptions")
                        magicOption = int(input("What would you like to do?"))
                        if magicOption == 0:
                            print("You canceled your magic")
                        elif magicOption == 1:
                            if P2MP < 1:
                                print("You don't have enough MP for that")
                            else:
                                print("You got a boost to your defence")
                                P1DEF = P1DEF + 1
                                if P1DEF > 15:
                                    P1DEF = 15
                                    print("Nope. Too much")
                                else:
                                    mc = 1
                        elif magicOption == 2:
                            P2DMGBOOST = int(input("The amount of MP you spend on this is doubled and added to your next attack: "))*2
                            if P2DMGBOOST/2 > P2MP:
                                print("You don't have enough MP for that")
                            else:
                                P2MP = P2MP - (P2DMGBOOST/2)
                                if P2MP < 0:
                                    P2MP = 0
                                print("P2 will do " + str(P2DMGBOOST) + " more damage with their next attack")
                                mc = 1
                                cc = 1
                elif option == 3:
                    print("1: Yes")
                    print("2: No")
                    yesorno = int(input("Are you sure you want to forfeit the match"))
                    if yesorno == 1:
                        break
                    else:
                        print("You do not run away")
            if P1ADTR == 2:
                P1ADTR == P1ADTR - 1
            elif P1ADTR == 1:
                P1AD = 0
                P1ADTR = 0
            else:
                P1ADTR = 0
            P1MP = P1MP + P1MPBON
            if P1MP > P1MAXMP:
                P1MP = P1MAXMP
            cc = 0
            mc = 0
            while cc == 0:
                print("1: Attack")
                print("2: Magic")
                print("3: Run away (forfeit)")
                option = int(input("What would you like to do (give a number): "))
                if option == 1:
                    if P1AD == 1:
                        critnumber1 = random.randint(1,20)
                        critnumber2 = random.randint(1,20)
                        if critnumber1 > critnumber2:
                            critnumber = critnumber1
                        elif critnumber2 > critnumber1:
                            critnumber = critnumber2
                        else:
                            critnumber = critnumber1
                    elif P1AD == 2:
                        critnumber1 = random.randint(1,20)
                        critnumber2 = random.randint(1,20)
                        if critnumber1 > critnumber2:
                            critnumber = critnumber2
                        elif critnumber2 > critnumber1:
                            critnumber = critnumber1
                        else:
                            critnumber = critnumber2
                    else:
                        critnumber = random.randint(1,20)
                    if critnumber == 20:
                        print("Player 1 landed a critical hit, doing " + str((P1ATK+P1DMGBOOST)*2) + " damage to player 2")
                        P2HP = P2HP - (P1ATK + P1DMGBOOST)*2
                        print("Player 2 has " + str(P2HP) + "HP left.")
                        cc = 1
                    elif critnumber + P1ATKBON > P2DEF:
                        print("Player 1 rolled a " + str(critnumber) + ", landing a hit and doing" + str(P1ATK+P1DMGBOOST) + " damage to player 2.")
                        P2HP = P2HP - (P1ATK + P1DMGBOOST)
                        print("Player 2 has " + str(P2HP) + "HP left.")
                        cc = 1
                    elif critnumber + P1ATKBON < P2DEF:
                        print("Player 2 missed thier attack")
                        cc = 1
                    P1DMGBOOST = 0
                elif option == 2:
                    print("I need to import the magic system from Emilio's branch.")
                elif option == 3:
                    print("1: Yes")
                    print("2: No")
                    yesorno = int(input("Are you sure you want to forfeit the match"))
                    if yesorno == 1:
                        break
                    else:
                        print("You do not run away")
                else:
                    print("Please provide a valid number.")
            if P1ADTR == 2:
                P1ADTR == P1ADTR - 1
            elif P1ADTR == 1:
                P1AD = 0
                P1ADTR = 0
            else:
                P1ADTR = 0
            P1MP = P1MP + P1MPBON
            if P1MP > P1MAXMP:
                P1MP = P1MAXMP
            cc = 0
        elif P1SPD == P2SPD:
            first = random.randint(1,2)
            if first == 1:
                P1SPD = P1SPD + 1
            elif first == 2:
                P2SPD = P2SPD + 1
        else:
            print(errmsg)
print(winner + " won the game!")
