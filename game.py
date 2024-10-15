import random
import time
def critnum(AD):
    if AD == 1:
        critnumber1 = random.randint(1,20)
        critnumber2 = random.randint(1,20)
        if critnumber1 > critnumber2:
            critnumber = critnumber1
        elif critnumber2 > critnumber1:
            critnumber = critnumber2
        else:
            critnumber = critnumber1
    elif AD == 2:
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
    return critnumber
def sleep(time):
    time.sleep(time)
errmsg = "If you are seeing this, something went wrong. Please restart the program."

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
ic = 0
cc = 0
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




while ac == 1:
    if P1HP <= 0:
        ac = 0
        winner = "Player 2"
    elif P2HP <= 0:
        ac = 0
        winner = "Player 1"
    else:
        if P1SPD > P2SPD:
            print("Player 1's turn")
            cc = 0
            while cc == 0:
                print("1: Attack")
                print("2: Magic")
                print("3: Use an item")
                print("4: Pass turn")
                print("5: Run away (forfeit)")
                option = int(input("What would you like to do (give a number): "))
                if option == 1:
                    P1critnum(P1AD)
                    if critnumber == 20:
                        print("Player 1 landed a critical hit, doing " + str((P1ATK+P1DMGBOOST)*2) + " damage to player 2")
                        P2HP = P2HP - (P1ATK + P1DMGBOOST)*2
                        print("Player 2 has " + str(P2HP) + " HP left.")
                        cc = 1
                    elif critnumber + P1ATKBON > P2DEF:
                        print("Player 1 rolled a " + str(critnumber) + ", landing a hit and doing " + str(P1ATK+P1DMGBOOST) + " damage to player 2.")
                        P2HP = P2HP - (P1ATK + P1DMGBOOST)
                        print("Player 2 has " + str(P2HP) + " HP left.")
                        cc = 1
                    elif critnumber + P1ATKBON < P2DEF:
                        print("Player 1 missed their attack")
                        cc = 1
                    P1DMGBOOST = 0
                elif option == 2:
                    mc = 0
                    while mc == 0:
                        print("1: Cancel")
                        print("2: Firball - 5MP")
                        print("3: Summon a random item - 2MP")
                        print("4: Gain advantage on your next turn - 5MP")
                        print("5: Impose disadvantage on your opponent's  - 6MP")
                        print("6: Heal 20 percent of your max health - 6MP")
                        print("7: Gain a damage boost on your next attack - Varies")
                        print("Currently 8 - Descriptions")
                        magicOption = int(input("What would you like to do? "))
                        if magicOption == 1:
                            print("You canceled your magic")
                            mc = 1
                        elif magicOption == 2:
                            if P1MP < 5:
                                print("You don't have enough MP for that")
                            else:
                                critnumber = random.randint(12,18)
                                print("Player 1 casted fireball, doing " + str(critnumber) + " damage to Player 2")
                                P2HP = P2HP - critnumber
                                P1MP = P1MP - 5
                        elif magicOption == 3:
                            if P1MP < 2:
                                print("You don't have enough MP for that")
                            else:
                                itemSpin = random.randint(1,100)
                                P1MP = P1MP - 2
                                if itemSpin >= 1 and itemSpin <= 20:
                                    print("You conjured a... rusty spoon?")
                                    print("This exists?")
                                    P1SPOON = P1SPOON + 1
                                elif itemSpin >= 21 and itemSpin <= 65:
                                    print("You conjured up a few throwing knives")
                                    P1KNIVES = P1KNIVES + 3
                                    mc = 1
                                elif itemSpin >= 66 and itemSpin <= 99:
                                    print("You conjured up a Healing Potion")
                                    P1POTS = P1POTS + 1
                                    mc = 1
                                elif itemSpin == 100:
                                    if P1GLOCK == 0 and P2NARRATORS == 1:
                                        print("Ok. Wow. Now the other guy has a gun")
                                        print("I'm leaving")
                                        P1NARRATORS = 1
                                        P1GLOCK = 1
                                    elif P1GLOCK == 0 and not P2NARRATORS == 1:
                                        print("You conjured a...")
                                        print("I'm sorry but wtf")
                                        print("That's a gun")
                                        print("Not even an old gun just a Glock-19")
                                        print("Alright I quit")
                                        P1NARRATORS = 1
                                        P1GLOCK = 1
                                    elif P1NARRATORS == 1:
                                        print("You did it again.")
                                        print("Land a 1 in 100 chance to make a gun appear")
                                        print("That thing could've instantly won you the game")
                                        print("And you KEPT GOING. WHY?")
                                        print("Alright, I'm ending this game for you now")
                                        P2HP = -999
                                    else:
                                        print(errmsg)
                                else:
                                    print("Making something failed. Somhow")
                        elif magicOption == 4:
                            if P1MP < 5:
                                print("You don't have enough MP for that")
                            else:
                                print("You gained advantage on your next turn")
                                P1AD = 1
                                P1ADTR = 2
                                mc = 1
                                cc = 1
                        elif magicOption == 5:
                            if P1MP < 6:
                                print("You don't have enough MP for that.")
                            else:
                                print("You gave Player 2 disadvantage on their next turn")
                                P2AD = 2
                                P2ADTR = 1
                                mc = 1
                                cc = 1
                        elif magicOption == 6:
                            if P1MP < 6:
                                print("You don't have enough MP for that")
                            else:
                                HEAL = int(P1MAXHP/5)
                                print("Player 1 healed" + str(HEAL) + " HP")
                                P1HP = P1HP + HEAL
                                if P1HP > P1MAXHP:
                                    print("But, you would've gone over your HP maximum if you did that")
                                    P1HP = P1MAXHP
                                else:
                                    P1HP = P1HP
                                mc = 1
                                cc = 1
                        elif magicOption == 7:
                            if P1MP < 1:
                                print("You have no MP, and therfore cannot use this")
                            else:
                                print("The amount of MP you use for this will be doubled and added to your next attack")
                                MPUSE = int(input("How much MP would you like to use for this? "))
                                if MPUSE > P1MP:
                                    print("You don't have enough MP for doing that")
                                else:
                                    P1DMGBOOST = MPUSE * 2
                                    print("Player 1 spent" + str(MPUSE) + " adding " + str(P1DMGBOOST) + " damage to their next attack")
                                    P1MP = P1MP - MPUSE
                                    mc = 1
                                    cc = 1
                        elif magicOption == 8:
                            print("Spell #2: Cast a fireball, doing 12-18 damage and ignoring all defence. Costs 5MP")
                            print("Spell #3: Summon a random item, being a rusty spoon, 3 throwing knvies, or a healing potion. Costs 2MP")
                            print("Spell #4: When attacking, you add your attack bonus to a random number, being 1-20. Advantage lets you roll twice and take the higher number. Costs 5MP")
                            print("Spell #5: When attacking, you add your attack bonus to a random number, being 1-20. Disadvantage forces you to roll twice and take the lower number. This spell puts disadvantage on your opponent Costs 6MP")
                            print("Spell #6: You may heal 20 percent of your max HP, rounded down. Costs 6MP")
                            print("Spell #7: For every point of MP you put into this spell, your next attack will do 2 more damage. Costs however much MP you want it to")
                        else:
                            print("Please choose a valid option")
                elif option == 3:
                    ic = 0
                    while ic == 0:
                        print("1: Spoons: ", str(P1SPOON))
                        print("2: Knives: ", + str(P1KNIVES))
                        print("3: Healing Potions: ", str(P1POTS))
                        if P1GLOCK > 0:
                            print("4: Glock-19")
                            P1SEEGUN = 1
                            print("5: Cancel")
                        else:
                            print("4: Cancel")
                        itemOption = int(input("What would you like to use? "))
                        if itemOption == 1:
                            if P1SPOON == 0:
                                print("You have no spoons. That's kinda sad. No soup for you")
                            else:
                                print("Player 1 threw a rusty spoon, maybe giving Player 2 tetanus, but doing 1 point of damage for sure.")
                                P2HP = P2HP - 1
                                P1SPOON = P1SPOON - 1
                        elif itemOption == 2:
                            if P1KNIVES == 0:
                                print("You don't have anything to cut people with.")
                            else:
                                print("Player 1 threw a knife, doing")
                                critnumber = random.randint(1,5)
                                P2HP - P2HP - critnumber
                                print("Player 1 did " + str(critnumber) + " damage to Player 2")
                                P1KNIVES = P1KNIVES - 1
                        elif itemOption == 3:
                            if P1POTS == 0:
                                print("You have no healing. Skill issue")
                            else:
                                HEAL = random.randint(3,7)
                                print("Player 1 healed " + str(HEAL) + " HP.")
                                P1HP = P1HP + HEAL
                                if P1HP > P1MAXHP:
                                    print("But that would bring you over your max HP")
                                    P1HP = P1MAXHP
                                else:
                                    P1HP = P1HP
                        elif itemOption == 4:
                            if P1SEEGUN == 1:
                                print("Player 1 used their Glock-19, killing Player 2")
                                P2HP = 0
                                ic = 1
                                cc = 1
                            elif P1SEEGUN == 0:
                                print("Player 1 canceled their item usage")
                                ic = 0
                        elif itemOption == 5 and P1SEEGUN == 1:
                            print("Player 1 canceled their item usage")
                            ic = 0
                        else:
                            print("Please choose a valid option")
                elif option == 4:
                    print("Player 1 passed their turn")
                    mc = 0
                    cc = 0
                elif option == 5:
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
            if P1HP <= 0:
                ac = 0
                winner = "Player 2"
            elif P2HP <= 0:
                ac = 0
                winner = "Player 1"
            else:
                print("Player 1 has " + str(P1HP) + " HP remaining, and " + str(P1MP) + " MP remaining")
                print("Player 2 has " + str(P2HP) + " HP remaining, and " + str(P2MP) + " MP remaining")
                print("Player 2's turn")
                cc = 0
                mc = 0
                ic = 0
                while cc == 0:
                    print("1: Attack")
                    print("2: Magic")
                    print("3: Use an item")
                    print("4: Pass turn")
                    print("5: Run away (forfeit)")
                    option = int(input("What would you like to do (give a number): "))
                    if option == 1:
                        critnum(P2AD)
                        if critnumber == 20:
                            print("Player 2 landed a critical hit, doing " + str((P2ATK+P2DMGBOOST)*2) + " damage to player 1")
                            P1HP = P1HP - (P2ATK + P2DMGBOOST)*2
                            print("Player 1 has " + str(P1HP) + " HP left.")
                            cc = 1
                        elif critnumber + P2ATKBON > P1DEF:
                            print("Player 2 rolled a " + str(critnumber) + ", landing a hit and doing " + str(P2ATK+P2DMGBOOST) + " damage to player 1.")
                            P1HP = P1HP - (P2ATK + P2DMGBOOST)
                            print("Player 1 has " + str(P1HP) + " HP left.")
                            cc = 1
                        elif critnumber + P2ATKBON < P2DEF:
                            print("Player 2 missed their attack")
                            cc = 1
                        P2DMGBOOST = 0
                    elif option == 2:
                        mc = 0
                        while mc == 0:
                            print("1: Cancel")
                            print("2: Firball - 5MP")
                            print("3: Summon a random item - 2MP")
                            print("4: Gain advantage on your next turn - 5MP")
                            print("5: Impose disadvantage on your opponent's  - 6MP")
                            print("6: Heal 20 percent of your max health - 6MP")
                            print("7: Gain a damage boost on your next attack - Varies")
                            print("Currently 8 - Descriptions")
                            magicOption = int(input("What would you like to do? "))
                            if magicOption == 1:
                                print("You canceled your magic")
                                mc = 1
                            elif magicOption == 2:
                                if P2MP < 5:
                                    print("You don't have enough MP for that")
                                else:
                                    critnumber = random.randint(12,18)
                                    print("Player 2 casted fireball, doing " + str(critnumber) + " damage to Player 2")
                                    P1HP = P1HP - critnumber
                                    P2MP = P2MP - 5
                            elif magicOption == 3:
                                if P2MP < 2:
                                    print("You don't have enough MP for that")
                                else:
                                    itemSpin = random.randint(1,100)
                                    P2MP = P2MP - 2
                                    if itemSpin >= 1 and itemSpin <= 20:
                                        print("You conjured a... rusty spoon?")
                                        print("This exists?")
                                        P2SPOON = P2SPOON + 1
                                    elif itemSpin >= 21 and itemSpin <= 65:
                                        print("You conjured up a few throwing knives")
                                        P2KNIVES = P2KNIVES + 3
                                    elif itemSpin >= 66 and itemSpin <= 99:
                                        print("You conjured up a Healing Potion")
                                        P2POTS = P2POTS + 1
                                    elif itemSpin == 100:
                                        if P2GLOCK == 0 and P1NARRATORS == 1:
                                            print("Wow. Ok. Now the other guy has a gun")
                                            print("I'm leaving")
                                            P2NARRATORS = 1
                                            P2GLOCK = 1
                                        elif P2GLOCK == 0 and not P1NARRATORS == 1:
                                            print("You conjured a...")
                                            print("I'm sorry but wtf")
                                            print("That's a gun")
                                            print("Not even an old gun just a Glock-19")
                                            print("Alright I quit")
                                            P2NARRATORS = 1
                                            P2GLOCK = 1
                                        elif P2NARRATORS == 1:
                                            print("You did it again.")
                                            print("Land a 1 in 100 chance to make a gun appear")
                                            print("That thing could've instantly won you the game")
                                            print("And you KEPT GOING. WHY?")
                                            print("Alright, I'm ending this game for you now")
                                            P2HP = -999
                                        else:
                                            print(errmsg)
                                    else:
                                        print("Making something failed. Somhow")
                                    mc = 1
                                    cc = 1
                            elif magicOption == 4:
                                if P2MP < 5:
                                    print("You don't have enough MP for that")
                                else:
                                    print("You gained advantage on your next turn")
                                    P2AD = 1
                                    P2ADTR = 2
                                    mc = 1
                                    cc = 1
                            elif magicOption == 5:
                                if P2MP < 6:
                                    print("You don't have enough MP for that.")
                                else:
                                    print("You gave Player 2 disadvantage on their next turn")
                                    P1AD = 2
                                    P1ADTR = 1
                                    mc = 1
                                    cc = 1
                            elif magicOption == 6:
                                if P2MP < 6:
                                    print("You don't have enough MP for that")
                                else:
                                    HEAL = int(P2MAXHP/5)
                                    print("Player 2 healed" + str(HEAL) + " HP")
                                    P2HP = P2HP + HEAL
                                    if P2HP > P2MAXHP:
                                        print("But, you would've gone over your HP maximum if you did that")
                                        P2HP = P2MAXHP
                                    else:
                                        P2HP = P2HP
                                    mc = 1
                                    cc = 1
                            elif magicOption == 7:
                                if P2MP < 1:
                                    print("You have no MP, and therfore cannot use this")
                                else:
                                    print("The amount of MP you use for this will be doubled and added to your next attack")
                                    MPUSE = int(input("How much MP would you like to use for this? "))
                                    if MPUSE > P2MP:
                                        print("You don't have enough MP to do that")
                                    else:
                                        P2DMGBOOST = MPUSE * 2
                                        print("Player 2 spent" + str(MPUSE) + " adding " + str(P2DMGBOOST) + " damage to their next attack")
                                        P2MP = P2MP - MPUSE
                                        mc = 1
                                        cc = 1
                            elif magicOption == 8:
                                print("Spell #2: Cast a fireball, doing 12-18 damage and ignoring all defence. Costs 5MP")
                                print("Spell #3: Summon a random item, being a rusty spoon, 3 throwing knvies, or a healing potion. Costs 2MP")
                                print("Spell #4: When attacking, you add your attack bonus to a random number, being 1-20. Advantage lets you roll twice and take the higher number. Costs 5MP")
                                print("Spell #5: When attacking, you add your attack bonus to a random number, being 1-20. Disadvantage forces you to roll twice and take the lower number. This spell puts disadvantage on your opponent Costs 6MP")
                                print("Spell #6: You may heal 20 percent of your max HP, rounded down. Costs 6MP")
                                print("Spell #7: For every point of MP you put into this spell, your next attack will do 2 more damage. Costs however much MP you want it to")
                            else:
                                print("Please choose a valid option")
                    elif option == 3:
                        ic = 0
                        while ic == 0:
                            print("1: Spoons: ", str(P2SPOON))
                            print("2: Knives: ", + str(P2KNIVES))
                            print("3: Healing Potions: ", str(P2POTS))
                            if P2GLOCK > 0:
                                print("4: Glock-19")
                                P2SEEGUN = 1
                                print("5: Cancel")
                            else:
                                print("4: Cancel")
                            itemOption = int(input("What would you like to use? "))
                            if itemOption == 1:
                                if P1SPOON == 0:
                                    print("You have no spoons. That's kinda sad. No soup for you")
                                else:
                                    print("Player 1 threw a rusty spoon, maybe giving Player 2 tetanus, but doing 1 point of damage for sure.")
                                    P2HP = P2HP - 1
                                    P1SPOON = P1SPOON - 1
                            elif itemOption == 2:
                                if P1KNIVES == 0:
                                    print("You don't have anything to cut people with.")
                                else:
                                    print("Player 1 threw a knife, doing")
                                    critnumber = random.randint(1,5)
                                    P2HP - P2HP - critnumber
                                    print("Player 1 did " + str(critnumber) + " damage to Player 2")
                                    P1KNIVES = P1KNIVES - 1
                            elif itemOption == 3:
                                if P1POTS == 0:
                                    print("You have no healing. Skill issue")
                                else:
                                    HEAL = random.randint(3,7)
                                    print("Player 1 healed " + str(HEAL) + " HP.")
                                    P1HP = P1HP + HEAL
                                    if P1HP > P1MAXHP:
                                        print("But that would bring you over your max HP")
                                        P1HP = P1MAXHP
                                    else:
                                        P1HP = P1HP
                            elif itemOption == 4:
                                if P1SEEGUN == 1:
                                    print("Player 1 used their Glock-19, killing Player 2")
                                    P2HP = 0
                                    ic = 1
                                    cc = 1
                                elif P1SEEGUN == 0:
                                    print("Player 1 canceled their item usage")
                                    ic = 0
                            elif itemOption == 5 and P1SEEGUN == 1:
                                print("Player 1 canceled their item usage")
                                ic = 0
                            else:
                                print("Please choose a valid option")
                    elif option == 4:
                        print("Player 1 passed their turn")
                        mc = 0
                        cc = 0
                    elif option == 5:
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
                if P1HP <= 0:
                    ac = 0
                    winner = "Player 2"
                elif P2HP <= 0:
                    ac = 0
                    winner = "Player 1"
                else:
                    print("Player 1 has " + str(P1HP) + " HP remaining, and " + str(P1MP) + " MP remaining")
                    print("Player 2 has " + str(P2HP) + " HP remaining, and " + str(P2MP) + " MP remaining")