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
def wait(temporal_distance):
    time.sleep(temporal_distance)
errmsg = "If you are seeing this, something went wrong. Please restart the program."

print("Welcome to Dungeons and Damage")
wait(.15)
print("Informally known as hell")
wait(.15)
#Adding menus
me = 0
while me == 0:
    print("1: Play game")
    wait(.15)
    print("2: Guide")
    wait(.15)
    print("3: Options")
    wait(.15)
    option = int(input("We need an option from you. Please give one. "))
    wait(.7)
    if option == 2:
        print("1: How to play")
        wait(.15)
        print("2: Attacking system")
        wait(.15)
        print("3: Magic system")
        wait(.15)
        print("4: Items and how to get them")
        wait(.15)
        print("5: Characters")
        wait(.15)
        print("6: Other features")
        wait(.15)
        option = int(input("What would you like to know more about? "))
        wait(.7)
        if option == 1:
            print("Give tutorial on a turn")
        elif option == 2:
            print("Explain how attack rolls are calculated")
        elif option == 3:
            print("Explain MP and MPBON, along with spell costs")
        elif option == 4:
            print("Explain items and the itemspin")
        elif option == 5:
            cc = 1
            print("1: Stats")
            wait(.15)
            print("2: Lore")
            wait(.15)
            while cc == 1:
                option = int(input("What would you like to learn more about? "))
                wait(.7)
                if option == 1:
                    print("Put stats here")
                    cc = 0
                elif option == 2:
                    print("Put backstories here")
                    cc = 0
                else:
                    print("Please give a valid option")
    elif option == 3:
        print("Give options to the player")
    
    
    
    elif option == 1:
        print("")
        me = 1
        print("Please select a class, player 1.")
        wait(.15)
        print("1: Knight")
        wait(.15)
        print("2: Peashooter")
        wait(.15)
        print("3: Mage")
        wait(.15)
        print("4: Rouge")
        wait(.15)
        print("5: Skele")
        wait(.15)
        print("6: Bard")
        wait(.15)
        print("7: Barbarian")
        wait(.15)
        print("8: Random")
        wait(.15)
        #Player 1 selects a class
        cc = 0
        ac = 0
        while ac == 0:
            while cc == 0:
                player1class = int(input("Choose a class from the list above (please choose a number): "))
                wait(.7)
                rc = 0
                while rc == 0:
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
                        cc = 1
                        rc = 1
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
                        cc = 1
                        rc = 1
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
                        cc = 1
                        rc = 1
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
                        cc = 1
                        rc = 1
                    elif player1class == 5:
                        player1class = "Skele"
                        P1HP = 33
                        P1MAXHP = P1HP
                        P1ATK = 20
                        P1ATKBON = 6
                        P1DEF = 20
                        P1MP = 15
                        P1MPBON = 3
                        P1MAXMP = P1MP
                        P1SPD = 4
                        cc = 1
                        rc = 1
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
                        cc = 1
                        rc = 1
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
                        cc = 1
                        rc = 1
                    elif player1class == 88224646790:
                        player1class = "Konami Code"
                        P1HP = 88224646790
                        P1MAXHP = P1HP
                        P1ATK = 88224646790
                        P1ATKBON = 88224646790
                        P1DEF = 88224646790
                        P1MP = 88224646790
                        P1MPBON = 88224646790
                        P1MAXMP = P1MP
                        P1SPD = 88224646790
                        cc = 1
                        rc = 1
                    elif player1class == 8:
                        player1class = random.randint(1,7)
                    else:
                        print("Please give a valid number.")
                        wait(.7)
            print("1: Yes")
            wait(.15)
            print("2: No")
            wait(.15)
            yesorno = int(input("You have chosen " + str(player1class) + ". Is this correct?: "))
            wait(.5)
            if yesorno == 1:
                print("Player 1 has chosen the " + str(player1class) + " class.")
                wait(.15)
                ac = 1
                rc = 1
                cc = 1
            elif yesorno == 2:
                print("Repick your charcter.")
                wait(.7)
                player1class = 0
                ac = 0
                rc = 1
                cc = 0
            else:
                print(errmsg)
                wait(.7)
                rc = 1
                cc = 0
        cc = 0
        ac = 0
        #Player 2 selects a class
        while ac == 0:
            while cc == 0:
                print("Please select a classs, player 2")
                wait(.15)
                player2class = int(input("Choose 1 from the list above (please choose a number): "))
                wait(.7)
                rc = 0
                while rc == 0:
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
                        cc = 1
                        rc = 1
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
                        cc = 1
                        rc = 1
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
                        cc = 1
                        rc = 1
                    elif player2class == 4:
                        player2class = "Rouge"
                        P2HP = 31
                        P2MAXHP = P2HP
                        P2ATK = 13
                        P2ATKBON = 4 
                        P2DEF = 13
                        P2MP = 6
                        P2MPBON = 1
                        P2MAXMP = P2MP
                        P2SPD = 7
                        cc = 1
                        rc = 1
                    elif player2class == 5:
                        player2class = "Skele"
                        P2HP = 33
                        P2MAXHP = P2HP
                        P2ATK = 20
                        P2ATKBON = 6
                        P2DEF = 12
                        P2MP = 15
                        P2MPBON = 3
                        P2MAXMP = P2MP
                        P2SPD = 4
                        cc = 1
                        rc = 1
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
                        cc = 1
                        rc = 1
                    elif player2class == 7:
                        player2class = "Barbrian"
                        P2HP = 52
                        P2MAXHP = P2HP
                        P2ATK = 14
                        P2ATKBON = 2
                        P2DEF = 11
                        P2MP = 2
                        P2MPBON = .25
                        P2MAXMP = P2MP
                        P2SPD = 4
                        cc = 1
                        rc = 1
                    elif player2class == 88224646790:
                        player2class = "Konami Code"
                        P2HP = 88224646790
                        P2MAXHP = P2HP
                        P2ATK = 88224646790
                        P2ATKBON = 88224646790
                        P2DEF = 88224646790
                        P2MP = 88224646790
                        P2MPBON = 88224646790
                        P2MAXMP = P2MP
                        P2SPD = 88224646790
                        cc = 1
                        rc = 1
                    elif player2class == 8:
                        player2class = random.randint(1,7)
                    else:
                        print(errmsg)
                        wait(.7)
            print("1: Yes")
            wait(.15)
            print("2: No")
            wait(.15)
            yesorno = int(input("You have chosen " + str(player2class) + ". Is this correct?: "))
            wait(.5)
            if yesorno == 1:
                print("Player 2 has chosen the " + str(player2class) + " class.")
                wait(.7)
                rc = 1
                cc = 1
                ac = 1
            elif yesorno == 2:
                player2class = 0
                print("Repick your charcter.")
                wait(.7)
                rc = 1
                cc = 0
            else:
                print("Please try again")
                wait(.7)
                rc = 1
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


        gc = 0
        while gc == 0:
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
                        wait(3)
                        cc = 0
                        while cc == 0:
                            print("1: Attack")
                            wait(.15)
                            print("2: Magic")
                            wait(.15)
                            print("3: Use an item")
                            wait(.15)
                            print("4: Pass turn")
                            wait(.15)
                            print("5: Run away (forfeit)")
                            wait(.15)
                            option = int(input("What would you like to do (give a number): "))
                            wait(.7)
                            if option == 1:
                                critnumber = critnum(P1AD)
                                print("You rolled a ", str(critnumber))
                                if critnumber == 20:
                                    print("Player 1 landed a critical hit, doing " + str((P1ATK+P1DMGBOOST)*2) + " damage to player 2")
                                    wait(.15)
                                    P2HP = P2HP - (P1ATK + P1DMGBOOST)*2
                                    wait(.7)
                                    cc = 1
                                elif critnumber + P1ATKBON > P2DEF:
                                    print("Player 1 rolled a " + str(critnumber) + ", landing a hit and doing " + str(P1ATK+P1DMGBOOST) + " damage to player 2.")
                                    wait(.15)
                                    P2HP = P2HP - (P1ATK + P1DMGBOOST)
                                    wait(.7)
                                    cc = 1
                                elif critnumber + P1ATKBON < P2DEF:
                                    print("Player 1 missed their attack")
                                    wait(.7)
                                    cc = 1
                                P1DMGBOOST = 0
                            elif option == 2:
                                mc = 0
                                while mc == 0:
                                    print("1: Cancel")
                                    wait(.15)
                                    print("2: Firball - 5MP")
                                    wait(.15)
                                    print("3: Summon a random item - 2MP")
                                    wait(.15)
                                    print("4: Gain advantage on your next turn - 5MP")
                                    wait(.15)
                                    print("5: Impose disadvantage on your opponent's  - 6MP")
                                    wait(.15)
                                    print("6: Heal 20 percent of your max health - 6MP")
                                    wait(.15)
                                    print("7: Gain a damage boost on your next attack - Varies")
                                    wait(.15)
                                    print("Currently 8 - Descriptions")
                                    wait(.15)
                                    magicOption = int(input("What would you like to do? "))
                                    wait(.7)
                                    if magicOption == 1:
                                        print("You canceled your magic")
                                        wait(.7)
                                        mc = 1
                                    elif magicOption == 2:
                                        if P1MP < 5:
                                            print("You don't have enough MP for that")
                                            wait(.7)
                                        else:
                                            critnumber = random.randint(12,18)
                                            print("Player 1 casted fireball, doing " + str(critnumber) + " damage to Player 2")
                                            wait(.7)
                                            P2HP = P2HP - critnumber
                                            P1MP = P1MP - 5
                                    elif magicOption == 3:
                                        if P1MP < 2:
                                            print("You don't have enough MP for that")
                                            wait(.7)
                                        else:
                                            itemSpin = random.randint(1,100)
                                            P1MP = P1MP - 2
                                            print("You rolled a ", str(itemSpin))
                                            wait(.7)
                                            if itemSpin >= 1 and itemSpin <= 20:
                                                print("You conjured a... rusty spoon?")
                                                wait(.15)
                                                print("This exists?")
                                                wait(.7)
                                                P1SPOON = P1SPOON + 1
                                            elif itemSpin >= 21 and itemSpin <= 65:
                                                print("You conjured up a few throwing knives")
                                                wait(.7)
                                                P1KNIVES = P1KNIVES + 3
                                            elif itemSpin >= 66 and itemSpin <= 99:
                                                print("You conjured up a Healing Potion")
                                                wait(.7)
                                                P1POTS = P1POTS + 1
                                            elif itemSpin == 100:
                                                if P1GLOCK == 0 and P2NARRATORS == 1:
                                                    print("Ok. Wow. Now the other guy has a gun")
                                                    wait(.7)
                                                    print("I'm leaving")
                                                    wait(.7)
                                                    P1NARRATORS = 1
                                                    P1GLOCK = 1
                                                elif P1GLOCK == 0 and not P2NARRATORS == 1:
                                                    print("You conjured a...")
                                                    wait(.7)
                                                    print("I'm sorry but wtf")
                                                    wait(.7)
                                                    print("That's a gun")
                                                    wait(.7)
                                                    print("Not even an old gun just a Glock-19")
                                                    wait(.7)
                                                    print("Alright I quit")
                                                    wait(.7)
                                                    P1NARRATORS = 1
                                                    P1GLOCK = 1
                                                elif P1NARRATORS == 1:
                                                    print("You did it again.")
                                                    wait(.7)
                                                    print("Land a 1 in 100 chance to make a gun appear")
                                                    wait(.7)
                                                    print("That thing could've instantly won you the game")
                                                    wait(.7)
                                                    print("And you KEPT GOING. WHY?")
                                                    wait(.7)
                                                    print("Alright, I'm ending this game for you now")
                                                    wait(.7)
                                                    P2HP = -999
                                                else:
                                                    print(errmsg)
                                                    wait(.7)
                                            else:
                                                print("Making something failed. Somhow")
                                                wait(.7)
                                            mc = 1
                                            cc = 1
                                    elif magicOption == 4:
                                        if P1MP < 5:
                                            print("You don't have enough MP for that")
                                            wait(.7)
                                        else:
                                            print("You gained advantage on your next turn")
                                            wait(.7)
                                            P1AD = 1
                                            P1ADTR = 2
                                            mc = 1
                                            cc = 1
                                    elif magicOption == 5:
                                        if P1MP < 6:
                                            print("You don't have enough MP for that.")
                                            wait(.7)
                                        else:
                                            print("You gave Player 2 disadvantage on their next turn")
                                            wait(.7)
                                            P2AD = 2
                                            P2ADTR = 1
                                            mc = 1
                                            cc = 1
                                    elif magicOption == 6:
                                        if P1MP < 6:
                                            print("You don't have enough MP for that")
                                            wait(.7)
                                        else:
                                            HEAL = int(P1MAXHP/5)
                                            print("Player 1 healed" + str(HEAL) + " HP")
                                            wait(.15)
                                            P1HP = P1HP + HEAL
                                            if P1HP > P1MAXHP:
                                                print("But, you would've gone over your HP maximum if you did that")
                                                wait(.7)
                                                P1HP = P1MAXHP
                                            else:
                                                P1HP = P1HP
                                                wait(.55)
                                            mc = 1
                                            cc = 1
                                    elif magicOption == 7:
                                        if P1MP < 1:
                                            print("You have no MP, and therfore cannot use this")
                                            wait(.7)
                                        else:
                                            print("The amount of MP you use for this will be doubled and added to your next attack")
                                            wait(.7)
                                            MPUSE = int(input("How much MP would you like to use for this? "))
                                            wait(.7)
                                            if MPUSE > P1MP:
                                                print("You don't have enough MP for doing that")
                                                wait(.7)
                                            else:
                                                P1DMGBOOST = MPUSE * 2
                                                print("Player 1 spent" + str(MPUSE) + " adding " + str(P1DMGBOOST) + " damage to their next attack")
                                                wait(.7)
                                                P1MP = P1MP - MPUSE
                                                mc = 1
                                                cc = 1
                                    elif magicOption == 8:
                                        print("Fireball: Cast a fireball, doing 12-18 damage and ignoring all defence. Costs 5MP")
                                        wait(.15)
                                        print("Random Item: Summon a random item, being a rusty spoon, 3 throwing knvies, or a healing potion. Costs 2MP")
                                        wait(.15)
                                        print("Gain Advantage: When attacking, you add your attack bonus to a random number, being 1-20. Advantage lets you roll twice and take the higher number. Costs 5MP")
                                        wait(.15)
                                        print("Impose Disadvantage: When attacking, you add your attack bonus to a random number, being 1-20. Disadvantage forces you to roll twice and take the lower number. This spell puts disadvantage on your opponent Costs 6MP")
                                        wait(.15)
                                        print("Heal: You may heal 20 percent of your max HP, rounded down. Costs 6MP")
                                        wait(.15)
                                        print("Damage Boost: For every point of MP you put into this spell, your next attack will do 2 more damage. Costs however much MP you want it to")
                                        wait(.7)
                                    else:
                                        print("Please choose a valid option")
                                        wait(.7)
                            elif option == 3:
                                ic = 0
                                while ic == 0:
                                    print("1: Spoons: ", str(P1SPOON))
                                    wait(.15)
                                    print("2: Knives: ", str(P1KNIVES))
                                    wait(.15)
                                    print("3: Healing Potions: ", str(P1POTS))
                                    wait(.15)
                                    if P1GLOCK > 0:
                                        print("4: Glock-19")
                                        wait(.15)
                                        P1SEEGUN = 1
                                        print("5: Cancel")
                                        wait(.15)
                                    else:
                                        print("4: Cancel")
                                        wait(.15)
                                    itemOption = int(input("What would you like to use? "))
                                    wait(.7)
                                    if itemOption == 1:
                                        if P1SPOON == 0:
                                            print("You have no spoons. That's kinda sad. No soup for you")
                                            wait(.7)
                                        else:
                                            print("Player 1 threw a rusty spoon, maybe giving Player 2 tetanus, but doing 1 point of damage for sure.")
                                            wait(.7)
                                            P2HP = P2HP - 1
                                            P1SPOON = P1SPOON - 1
                                    elif itemOption == 2:
                                        if P1KNIVES == 0:
                                            print("You don't have anything to cut people with.")
                                            wait(.7)
                                        else:
                                            print("Player 1 threw a knife")
                                            wait(.15)
                                            critnumber = random.randint(1,5)
                                            P2HP - P2HP - critnumber
                                            print("Player 1 did " + str(critnumber) + " damage to Player 2")
                                            wait(.7)
                                            P1KNIVES = P1KNIVES - 1
                                    elif itemOption == 3:
                                        if P1POTS == 0:
                                            print("You have no healing. Skill issue")
                                            wait(.7)
                                        else:
                                            HEAL = random.randint(3,7)
                                            print("Player 1 healed " + str(HEAL) + " HP.")
                                            wait(.15)
                                            P1HP = P1HP + HEAL
                                            if P1HP > P1MAXHP:
                                                print("But that would bring you over your max HP")
                                                wait(.7)
                                                P1HP = P1MAXHP
                                            else:
                                                P1HP = P1HP
                                                wait(.55)
                                    elif itemOption == 4:
                                        if P1SEEGUN == 1:
                                            print("Player 1 used their Glock-19, killing Player 2")
                                            wait(.7)
                                            P2HP = 0
                                            ic = 1
                                            cc = 1
                                        elif P1SEEGUN == 0:
                                            print("Player 1 canceled their item usage")
                                            wait(.7)
                                            ic = 0
                                    elif itemOption == 5 and P1SEEGUN == 1:
                                        print("Player 1 canceled their item usage")
                                        wait(.7)
                                        ic = 0
                                    else:
                                        print("Please choose a valid option")
                                        wait(.7)
                            elif option == 4:
                                print("Player 1 passed their turn")
                                wait(.7)
                                mc = 0
                                cc = 0
                            elif option == 5:
                                print("1: Yes")
                                wait(.15)
                                print("2: No")
                                wait(.15)
                                yesorno = int(input("Are you sure you want to forfeit the match"))
                                wait(.5)
                                if yesorno == 1:
                                    P1HP = 0
                                else:
                                    print("You do not run away")
                                    wait(.7)
                            else:
                                print("Please provide a valid number.")
                                wait(.7)
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
                            wait(.15)
                            print("Player 2 has " + str(P2HP) + " HP remaining, and " + str(P2MP) + " MP remaining")
                            wait(.15)
                            print("Player 2's turn")
                            wait(3)
                            cc = 0
                            mc = 0
                            ic = 0
                            while cc == 0:
                                print("1: Attack")
                                wait(.15)
                                print("2: Magic")
                                wait(.15)
                                print("3: Use an item")
                                wait(.15)
                                print("4: Pass turn")
                                wait(.15)
                                print("5: Run away (forfeit)")
                                wait(.15)
                                option = int(input("What would you like to do (give a number): "))
                                wait(.7)
                                if option == 1:
                                    critnumber = critnum(P2AD)
                                    print("You rolled a ", str(critnumber))
                                    if critnumber == 20:
                                        print("Player 2 landed a critical hit, doing " + str((P2ATK+P2DMGBOOST)*2) + " damage to player 1")
                                        wait(.15)
                                        P1HP = P1HP - (P2ATK + P2DMGBOOST)*2
                                        wait(.7)
                                        cc = 1
                                    elif critnumber + P2ATKBON > P1DEF:
                                        print("Player 2 rolled a " + str(critnumber) + ", landing a hit and doing " + str(P2ATK+P2DMGBOOST) + " damage to player 1.")
                                        wait(.7)
                                        P1HP = P1HP - (P2ATK + P2DMGBOOST)
                                        wait(.7)
                                        cc = 1
                                    elif critnumber + P2ATKBON < P2DEF:
                                        print("Player 2 missed their attack")
                                        wait(.7)
                                        cc = 1
                                    P2DMGBOOST = 0
                                elif option == 2:
                                    mc = 0
                                    while mc == 0:
                                        print("1: Cancel")
                                        wait(.15)
                                        print("2: Firball - 5MP")
                                        wait(.15)
                                        print("3: Summon a random item - 2MP")
                                        wait(.15)
                                        print("4: Gain advantage on your next turn - 5MP")
                                        wait(.15)
                                        print("5: Impose disadvantage on your opponent's  - 6MP")
                                        wait(.15)
                                        print("6: Heal 20 percent of your max health - 6MP")
                                        wait(.15)
                                        print("7: Gain a damage boost on your next attack - Varies")
                                        wait(.15)
                                        print("Currently 8 - Descriptions")
                                        wait(.15)
                                        magicOption = int(input("What would you like to do? "))
                                        wait(.7)
                                        if magicOption == 1:
                                            print("You canceled your magic")
                                            wait(.7)
                                            mc = 1
                                        elif magicOption == 2:
                                            if P2MP < 5:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                critnumber = random.randint(12,18)
                                                print("Player 2 casted fireball, doing " + str(critnumber) + " damage to Player 2")
                                                wait(.7)
                                                P1HP = P1HP - critnumber
                                                P2MP = P2MP - 5
                                        elif magicOption == 3:
                                            if P2MP < 2:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                itemSpin = random.randint(1,100)
                                                P2MP = P2MP - 2
                                                print("You rolled a ", str(itemSpin))
                                                wait(.7)
                                                if itemSpin >= 1 and itemSpin <= 20:
                                                    print("You conjured a... rusty spoon?")
                                                    wait(.2)
                                                    print("This exists?")
                                                    wait(.7)
                                                    P2SPOON = P2SPOON + 1
                                                elif itemSpin >= 21 and itemSpin <= 65:
                                                    print("You conjured up a few throwing knives")
                                                    wait(.7)
                                                    P2KNIVES = P2KNIVES + 3
                                                elif itemSpin >= 66 and itemSpin <= 99:
                                                    print("You conjured up a Healing Potion")
                                                    wait(.7)
                                                    P2POTS = P2POTS + 1
                                                elif itemSpin == 100:
                                                    if P2GLOCK == 0 and P1NARRATORS == 1:
                                                        print("Wow. Ok. Now the other guy has a gun")
                                                        wait(.2)
                                                        print("I'm leaving")
                                                        wait(.7)
                                                        P2NARRATORS = 1
                                                        P2GLOCK = 1
                                                    elif P2GLOCK == 0 and not P1NARRATORS == 1:
                                                        print("You conjured a...")
                                                        wait(.15)
                                                        print("I'm sorry but wtf")
                                                        wait(.15)
                                                        print("That's a gun")
                                                        wait(.15)
                                                        print("Not even an old gun just a Glock-19")
                                                        wait(.15)
                                                        print("Alright I quit")
                                                        wait(.7)
                                                        P2NARRATORS = 1
                                                        P2GLOCK = 1
                                                    elif P2NARRATORS == 1:
                                                        print("You did it again.")
                                                        wait(.15)
                                                        print("Land a 1 in 100 chance to make a gun appear")
                                                        wait(.15)
                                                        print("That thing could've instantly won you the game")
                                                        wait(.15)
                                                        print("And you KEPT GOING. WHY?")
                                                        wait(.15)
                                                        print("Alright, I'm ending this game for you now")
                                                        wait(.7)
                                                        P2HP = -999
                                                    else:
                                                        print(errmsg)
                                                else:
                                                    print("Making something failed. Somhow")
                                                    wait(.7)
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 4:
                                            if P2MP < 5:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                print("You gained advantage on your next turn")
                                                wait(.7)
                                                P2AD = 1
                                                P2ADTR = 2
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 5:
                                            if P2MP < 6:
                                                print("You don't have enough MP for that.")
                                                wait(.7)
                                            else:
                                                print("You gave Player 1 disadvantage on their next turn")
                                                wait(.7)
                                                P1AD = 2
                                                P1ADTR = 1
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 6:
                                            if P2MP < 6:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                HEAL = int(P2MAXHP/5)
                                                print("Player 2 healed" + str(HEAL) + " HP")
                                                wait(.15)
                                                P2HP = P2HP + HEAL
                                                if P2HP > P2MAXHP:
                                                    print("But, you would've gone over your HP maximum if you did that")
                                                    wait(.7)
                                                    P2HP = P2MAXHP
                                                else:
                                                    P2HP = P2HP
                                                    wait(.55)
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 7:
                                            if P2MP < 1:
                                                print("You have no MP, and therfore cannot use this")
                                                wait(.7)
                                            else:
                                                print("The amount of MP you use for this will be doubled and added to your next attack")
                                                wait(.15)
                                                MPUSE = int(input("How much MP would you like to use for this? "))
                                                wait(.7)
                                                if MPUSE > P2MP:
                                                    print("You don't have enough MP to do that")
                                                    wait(.7)
                                                else:
                                                    P2DMGBOOST = MPUSE * 2
                                                    print("Player 2 spent" + str(MPUSE) + " adding " + str(P2DMGBOOST) + " damage to their next attack")
                                                    wait(.7)
                                                    P2MP = P2MP - MPUSE
                                                    mc = 1
                                                    cc = 1
                                        elif magicOption == 8:
                                            print("Fireball: Cast a fireball, doing 12-18 damage and ignoring all defence. Costs 5MP")
                                            wait(.15)
                                            print("Random Item: Summon a random item, being a rusty spoon, 3 throwing knvies, or a healing potion. Costs 2MP")
                                            wait(.15)
                                            print("Gain Advantage: When attacking, you add your attack bonus to a random number, being 1-20. Advantage lets you roll twice and take the higher number. Costs 5MP")
                                            wait(.15)
                                            print("Impose Disadvantage: When attacking, you add your attack bonus to a random number, being 1-20. Disadvantage forces you to roll twice and take the lower number. This spell puts disadvantage on your opponent Costs 6MP")
                                            wait(.15)
                                            print("Heal: You may heal 20 percent of your max HP, rounded down. Costs 6MP")
                                            wait(.15)
                                            print("Damage Boost: For every point of MP you put into this spell, your next attack will do 2 more damage. Costs however much MP you want it to")
                                            wait(.15)
                                        else:
                                            print("Please choose a valid option")
                                            wait(.7)
                                elif option == 3:
                                    ic = 0
                                    while ic == 0:
                                        print("1: Spoons: ", str(P2SPOON))
                                        wait(.15)
                                        print("2: Knives: ", str(P2KNIVES))
                                        wait(.15)
                                        print("3: Healing Potions: ", str(P2POTS))
                                        wait(.15)
                                        if P2GLOCK > 0:
                                            print("4: Glock-19")
                                            wait(.15)
                                            P2SEEGUN = 1
                                            print("5: Cancel")
                                            wait(.15)
                                        else:
                                            print("4: Cancel")
                                            wait(.15)
                                        itemOption = int(input("What would you like to use? "))
                                        wait(.7)
                                        if itemOption == 1:
                                            if P2SPOON == 0:
                                                print("You have no spoons. That's kinda sad. No soup for you")
                                                wait(.7)
                                            else:
                                                print("Player 1 threw a rusty spoon, maybe giving Player 2 tetanus, but doing 1 point of damage for sure.")
                                                wait(.7)
                                                P1HP = P1HP - 1
                                                P2SPOON = P2SPOON - 1
                                        elif itemOption == 2:
                                            if P2KNIVES == 0:
                                                print("You don't have anything to cut people with.")
                                                wait(.7)
                                            else:
                                                print("Player 2 threw a knife")
                                                wait(.15)
                                                critnumber = random.randint(1,5)
                                                P1HP - P1HP - critnumber
                                                print("Player 2 did " + str(critnumber) + " damage to Player 1")
                                                wait(.7)
                                                P2KNIVES = P2KNIVES - 1
                                        elif itemOption == 3:
                                            if P2POTS == 0:
                                                print("You have no healing. Skill issue")
                                                wait(.7)
                                            else:
                                                HEAL = random.randint(3,7)
                                                print("Player 2 healed " + str(HEAL) + " HP.")
                                                wait(.15)
                                                P2HP = P2HP + HEAL
                                                if P2HP > P2MAXHP:
                                                    print("But that would bring you over your max HP")
                                                    wait(.7)
                                                    P2HP = P2MAXHP
                                                else:
                                                    P2HP = P2HP
                                                    wait(.55)
                                        elif itemOption == 4:
                                            if P2SEEGUN == 1:
                                                print("Player 2 used their Glock-19, killing Player 1")
                                                wait(.7)
                                                P1HP = 0
                                                ic = 1
                                                cc = 1
                                            elif P2SEEGUN == 0:
                                                print("Player 2 canceled their item usage")
                                                wait(.7)
                                                ic = 0
                                        elif itemOption == 5 and P2SEEGUN == 1:
                                            print("Player 2 canceled their item usage")
                                            wait(.7)
                                            ic = 0
                                        else:
                                            print("Please choose a valid option")
                                            wait(.7)
                                elif option == 4:
                                    print("Player 2 passed their turn")
                                    wait(.7)
                                    mc = 0
                                    cc = 0
                                elif option == 5:
                                    print("1: Yes")
                                    wait(.15)
                                    print("2: No")
                                    wait(.15)
                                    yesorno = int(input("Are you sure you want to forfeit the match"))
                                    wait(.5)
                                    if yesorno == 1:
                                        P2HP = 0
                                    else:
                                        print("You do not run away")
                                        wait(.7)
                                else:
                                    print("Please provide a valid number.")
                                    wait(.7)
                            if P2ADTR == 2:
                                P2ADTR == P2ADTR - 1
                            elif P2ADTR == 1:
                                P2AD = 0
                                P2ADTR = 0
                            else:
                                P2ADTR = 0
                            P2MP = P2MP + P2MPBON
                            if P2MP > P2MAXMP:
                                P2MP = P2MAXMP
                            cc = 0
                            if P1HP <= 0:
                                ac = 0
                                winner = "Player 2"
                            elif P2HP <= 0:
                                ac = 0
                                winner = "Player 1"
                            else:
                                print("Player 1 has " + str(P1HP) + " HP remaining, and " + str(P1MP) + " MP remaining")
                                wait(.15)
                                print("Player 2 has " + str(P2HP) + " HP remaining, and " + str(P2MP) + " MP remaining")
                                wait(.15)
                    elif P2SPD > P1SPD:
                            print("Player 2's turn")
                            wait(3)
                            cc = 0
                            mc = 0
                            ic = 0
                            while cc == 0:
                                print("1: Attack")
                                wait(.15)
                                print("2: Magic")
                                wait(.15)
                                print("3: Use an item")
                                wait(.15)
                                print("4: Pass turn")
                                wait(.15)
                                print("5: Run away (forfeit)")
                                wait(.15)
                                option = int(input("What would you like to do (give a number): "))
                                wait(.7)
                                if option == 1:
                                    critnumber = critnum(P2AD)
                                    print("You rolled a ", str(critnumber))
                                    if critnumber == 20:
                                        print("Player 2 landed a critical hit, doing " + str((P2ATK+P2DMGBOOST)*2) + " damage to player 1")
                                        wait(.15)
                                        P1HP = P1HP - (P2ATK + P2DMGBOOST)*2
                                        print("Player 1 has " + str(P1HP) + " HP left.")
                                        wait(.7)
                                        cc = 1
                                    elif critnumber + P2ATKBON > P1DEF:
                                        print("Player 2 rolled a " + str(critnumber) + ", landing a hit and doing " + str(P2ATK+P2DMGBOOST) + " damage to player 1.")
                                        wait(.7)
                                        P1HP = P1HP - (P2ATK + P2DMGBOOST)
                                        print("Player 1 has " + str(P1HP) + " HP left.")
                                        wait(.7)
                                        cc = 1
                                    elif critnumber + P2ATKBON < P2DEF:
                                        print("Player 2 missed their attack")
                                        wait(.15)
                                        cc = 1
                                    P2DMGBOOST = 0
                                elif option == 2:
                                    mc = 0
                                    while mc == 0:
                                        print("1: Cancel")
                                        wait(.15)
                                        print("2: Firball - 5MP")
                                        wait(.15)
                                        print("3: Summon a random item - 2MP")
                                        wait(.15)
                                        print("4: Gain advantage on your next turn - 5MP")
                                        wait(.15)
                                        print("5: Impose disadvantage on your opponent's  - 6MP")
                                        wait(.15)
                                        print("6: Heal 20 percent of your max health - 6MP")
                                        wait(.15)
                                        print("7: Gain a damage boost on your next attack - Varies")
                                        wait(.15)
                                        print("Currently 8 - Descriptions")
                                        wait(.15)
                                        magicOption = int(input("What would you like to do? "))
                                        wait(.7)
                                        if magicOption == 1:
                                            print("You canceled your magic")
                                            wait(.7)
                                            mc = 1
                                        elif magicOption == 2:
                                            if P2MP < 5:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                critnumber = random.randint(12,18)
                                                print("Player 2 casted fireball, doing " + str(critnumber) + " damage to Player 2")
                                                wait(.7)
                                                P1HP = P1HP - critnumber
                                                P2MP = P2MP - 5
                                        elif magicOption == 3:
                                            if P2MP < 2:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                itemSpin = random.randint(1,100)
                                                P2MP = P2MP - 2
                                                print("You rolled a ", str(itemSpin))
                                                wait(.7)
                                                if itemSpin >= 1 and itemSpin <= 20:
                                                    print("You conjured a... rusty spoon?")
                                                    wait(.2)
                                                    print("This exists?")
                                                    wait(.7)
                                                    P2SPOON = P2SPOON + 1
                                                elif itemSpin >= 21 and itemSpin <= 65:
                                                    print("You conjured up a few throwing knives")
                                                    wait(.7)
                                                    P2KNIVES = P2KNIVES + 3
                                                elif itemSpin >= 66 and itemSpin <= 99:
                                                    print("You conjured up a Healing Potion")
                                                    wait(.15)
                                                    P2POTS = P2POTS + 1
                                                elif itemSpin == 100:
                                                    if P2GLOCK == 0 and P1NARRATORS == 1:
                                                        print("Wow. Ok. Now the other guy has a gun")
                                                        wait(.2)
                                                        print("I'm leaving")
                                                        wait(.7)
                                                        P2NARRATORS = 1
                                                        P2GLOCK = 1
                                                    elif P2GLOCK == 0 and not P1NARRATORS == 1:
                                                        print("You conjured a...")
                                                        wait(.15)
                                                        print("I'm sorry but wtf")
                                                        wait(.15)
                                                        print("That's a gun")
                                                        wait(.15)
                                                        print("Not even an old gun just a Glock-19")
                                                        wait(.15)
                                                        print("Alright I quit")
                                                        wait(.7)
                                                        P2NARRATORS = 1
                                                        P2GLOCK = 1
                                                    elif P2NARRATORS == 1:
                                                        print("You did it again.")
                                                        wait(.15)
                                                        print("Land a 1 in 100 chance to make a gun appear")
                                                        wait(.15)
                                                        print("That thing could've instantly won you the game")
                                                        wait(.15)
                                                        print("And you KEPT GOING. WHY?")
                                                        wait(.15)
                                                        print("Alright, I'm ending this game for you now")
                                                        wait(.7)
                                                        P2HP = -999
                                                    else:
                                                        print(errmsg)
                                                else:
                                                    print("Making something failed. Somhow")
                                                    wait(.7)
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 4:
                                            if P2MP < 5:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                print("You gained advantage on your next turn")
                                                wait(.7)
                                                P2AD = 1
                                                P2ADTR = 2
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 5:
                                            if P2MP < 6:
                                                print("You don't have enough MP for that.")
                                                wait(.7)
                                            else:
                                                print("You gave Player 1 disadvantage on their next turn")
                                                wait(.7)
                                                P1AD = 2
                                                P1ADTR = 1
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 6:
                                            if P2MP < 6:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                HEAL = int(P2MAXHP/5)
                                                print("Player 2 healed" + str(HEAL) + " HP")
                                                wait(.15)
                                                P2HP = P2HP + HEAL
                                                if P2HP > P2MAXHP:
                                                    print("But, you would've gone over your HP maximum if you did that")
                                                    wait(.7)
                                                    P2HP = P2MAXHP
                                                else:
                                                    P2HP = P2HP
                                                    wait(.55)
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 7:
                                            if P2MP < 1:
                                                print("You have no MP, and therfore cannot use this")
                                                wait(.7)
                                            else:
                                                print("The amount of MP you use for this will be doubled and added to your next attack")
                                                wait(.15)
                                                MPUSE = int(input("How much MP would you like to use for this? "))
                                                wait(.7)
                                                if MPUSE > P2MP:
                                                    print("You don't have enough MP to do that")
                                                    wait(.7)
                                                else:
                                                    P2DMGBOOST = MPUSE * 2
                                                    print("Player 2 spent" + str(MPUSE) + " adding " + str(P2DMGBOOST) + " damage to their next attack")
                                                    wait(.7)
                                                    P2MP = P2MP - MPUSE
                                                    mc = 1
                                                    cc = 1
                                        elif magicOption == 8:
                                            print("Fireball: Cast a fireball, doing 12-18 damage and ignoring all defence. Costs 5MP")
                                            wait(.15)
                                            print("Random Item: Summon a random item, being a rusty spoon, 3 throwing knvies, or a healing potion. Costs 2MP")
                                            wait(.15)
                                            print("Gain Advantage: When attacking, you add your attack bonus to a random number, being 1-20. Advantage lets you roll twice and take the higher number. Costs 5MP")
                                            wait(.15)
                                            print("Impose Disadvantage: When attacking, you add your attack bonus to a random number, being 1-20. Disadvantage forces you to roll twice and take the lower number. This spell puts disadvantage on your opponent Costs 6MP")
                                            wait(.15)
                                            print("Heal: You may heal 20 percent of your max HP, rounded down. Costs 6MP")
                                            wait(.15)
                                            print("Damage Boost: For every point of MP you put into this spell, your next attack will do 2 more damage. Costs however much MP you want it to")
                                            wait(.15)
                                        else:
                                            print("Please choose a valid option")
                                            wait(.7)
                                elif option == 3:
                                    ic = 0
                                    while ic == 0:
                                        print("1: Spoons: ", str(P2SPOON))
                                        wait(.15)
                                        print("2: Knives: ", str(P2KNIVES))
                                        wait(.15)
                                        print("3: Healing Potions: ", str(P2POTS))
                                        wait(.15)
                                        if P2GLOCK > 0:
                                            print("4: Glock-19")
                                            wait(.15)
                                            P2SEEGUN = 1
                                            print("5: Cancel")
                                            wait(.15)
                                        else:
                                            print("4: Cancel")
                                            wait(.15)
                                        itemOption = int(input("What would you like to use? "))
                                        wait(.7)
                                        if itemOption == 1:
                                            if P2SPOON == 0:
                                                print("You have no spoons. That's kinda sad. No soup for you")
                                                wait(.7)
                                            else:
                                                print("Player 1 threw a rusty spoon, maybe giving Player 2 tetanus, but doing 1 point of damage for sure.")
                                                wait(.7)
                                                P1HP = P1HP - 1
                                                P2SPOON = P2SPOON - 1
                                        elif itemOption == 2:
                                            if P2KNIVES == 0:
                                                print("You don't have anything to cut people with.")
                                                wait(.7)
                                            else:
                                                print("Player 2 threw a knife")
                                                wait(.15)
                                                critnumber = random.randint(1,5)
                                                P1HP - P1HP - critnumber
                                                print("Player 2 did " + str(critnumber) + " damage to Player 1")
                                                wait(.7)
                                                P2KNIVES = P2KNIVES - 1
                                        elif itemOption == 3:
                                            if P2POTS == 0:
                                                print("You have no healing. Skill issue")
                                                wait(.7)
                                            else:
                                                HEAL = random.randint(3,7)
                                                print("Player 2 healed " + str(HEAL) + " HP.")
                                                wait(.15)
                                                P2HP = P2HP + HEAL
                                                if P2HP > P2MAXHP:
                                                    print("But that would bring you over your max HP")
                                                    wait(.7)
                                                    P2HP = P2HP
                                                else:
                                                    P2HP = P2HP
                                                    wait(.55)
                                        elif itemOption == 4:
                                            if P2SEEGUN == 1:
                                                print("Player 2 used their Glock-19, killing Player 1")
                                                wait(.7)
                                                P1HP = 0
                                                ic = 1
                                                cc = 1
                                            elif P2SEEGUN == 0:
                                                print("Player 2 canceled their item usage")
                                                wait(.7)
                                                ic = 0
                                        elif itemOption == 5 and P2SEEGUN == 1:
                                            print("Player 2 canceled their item usage")
                                            wait(.7)
                                            ic = 0
                                        else:
                                            print("Please choose a valid option")
                                            wait(.7)
                                elif option == 4:
                                    print("Player 2 passed their turn")
                                    wait(.7)
                                    mc = 0
                                    cc = 0
                                elif option == 5:
                                    print("1: Yes")
                                    wait(.15)
                                    print("2: No")
                                    wait(.15)
                                    yesorno = int(input("Are you sure you want to forfeit the match"))
                                    wait(.5)
                                    if yesorno == 1:
                                        P2HP = 0
                                    else:
                                        print("You do not run away")
                                        wait(.7)
                                else:
                                    print("Please provide a valid number.")
                                    wait(.7)
                            if P2ADTR == 2:
                                P2ADTR == P2ADTR - 1
                            elif P2ADTR == 1:
                                P2AD = 0
                                P2ADTR = 0
                            else:
                                P2ADTR = 0
                            P2MP = P2MP + P2MPBON
                            if P2MP > P2MAXMP:
                                P2MP = P2MAXMP
                            cc = 0
                            if P1HP <= 0:
                                ac = 0
                                winner = "Player 2"
                            elif P2HP <= 0:
                                ac = 0
                                winner = "Player 1"
                            else:
                                print("Player 1 has " + str(P1HP) + " HP remaining, and " + str(P1MP) + " MP remaining")
                                wait(.15)
                                print("Player 2 has " + str(P2HP) + " HP remaining, and " + str(P2MP) + " MP remaining")
                                wait(.15)
                            print("Player 1's turn")
                            wait(3)
                            cc = 0
                            while cc == 0:
                                print("1: Attack")
                                wait(.15)
                                print("2: Magic")
                                wait(.15)
                                print("3: Use an item")
                                wait(.15)
                                print("4: Pass turn")
                                wait(.15)
                                print("5: Run away (forfeit)")
                                wait(.15)
                                option = int(input("What would you like to do (give a number): "))
                                wait(.7)
                                if option == 1:
                                    critnumber = critnum(P1AD)
                                    print("You rolled a ", str(critnumber))
                                    if critnumber == 20:
                                        print("Player 1 landed a critical hit, doing " + str((P1ATK+P1DMGBOOST)*2) + " damage to player 2")
                                        wait(.15)
                                        P2HP = P2HP - (P1ATK + P1DMGBOOST)*2
                                        print("Player 2 has " + str(P2HP) + " HP left.")
                                        wait(.7)
                                        cc = 1
                                    elif critnumber + P1ATKBON > P2DEF:
                                        print("Player 1 rolled a " + str(critnumber) + ", landing a hit and doing " + str(P1ATK+P1DMGBOOST) + " damage to player 2.")
                                        wait(.15)
                                        P2HP = P2HP - (P1ATK + P1DMGBOOST)
                                        print("Player 2 has " + str(P2HP) + " HP left.")
                                        wait(.7)
                                        cc = 1
                                    elif critnumber + P1ATKBON < P2DEF:
                                        print("Player 1 missed their attack")
                                        wait(.7)
                                        cc = 1
                                    P1DMGBOOST = 0
                                elif option == 2:
                                    mc = 0
                                    while mc == 0:
                                        print("1: Cancel")
                                        wait(.15)
                                        print("2: Firball - 5MP")
                                        wait(.15)
                                        print("3: Summon a random item - 2MP")
                                        wait(.15)
                                        print("4: Gain advantage on your next turn - 5MP")
                                        wait(.15)
                                        print("5: Impose disadvantage on your opponent's  - 6MP")
                                        wait(.15)
                                        print("6: Heal 20 percent of your max health - 6MP")
                                        wait(.15)
                                        print("7: Gain a damage boost on your next attack - Varies")
                                        wait(.15)
                                        print("Currently 8 - Descriptions")
                                        wait(.15)
                                        magicOption = int(input("What would you like to do? "))
                                        wait(.7)
                                        if magicOption == 1:
                                            print("You canceled your magic")
                                            wait(.7)
                                            mc = 1
                                        elif magicOption == 2:
                                            if P1MP < 5:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                critnumber = random.randint(12,18)
                                                print("Player 1 casted fireball, doing " + str(critnumber) + " damage to Player 2")
                                                wait(.7)
                                                P2HP = P2HP - critnumber
                                                P1MP = P1MP - 5
                                        elif magicOption == 3:
                                            if P1MP < 2:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                itemSpin = random.randint(1,100)
                                                P1MP = P1MP - 2
                                                print("You rolled a ", str(itemSpin))
                                                wait(.2)
                                                if itemSpin >= 1 and itemSpin <= 20:
                                                    print("You conjured a... rusty spoon?")
                                                    wait(.15)
                                                    print("This exists?")
                                                    wait(.7)
                                                    P1SPOON = P1SPOON + 1
                                                elif itemSpin >= 21 and itemSpin <= 65:
                                                    print("You conjured up a few throwing knives")
                                                    wait(.7)
                                                    P1KNIVES = P1KNIVES + 3
                                                elif itemSpin >= 66 and itemSpin <= 99:
                                                    print("You conjured up a Healing Potion")
                                                    wait(.7)
                                                    P1POTS = P1POTS + 1
                                                elif itemSpin == 100:
                                                    if P1GLOCK == 0 and P2NARRATORS == 1:
                                                        print("Ok. Wow. Now the other guy has a gun")
                                                        wait(.7)
                                                        print("I'm leaving")
                                                        wait(.7)
                                                        P1NARRATORS = 1
                                                        P1GLOCK = 1
                                                    elif P1GLOCK == 0 and not P2NARRATORS == 1:
                                                        print("You conjured a...")
                                                        wait(.7)
                                                        print("I'm sorry but wtf")
                                                        wait(.7)
                                                        print("That's a gun")
                                                        wait(.7)
                                                        print("Not even an old gun just a Glock-19")
                                                        wait(.7)
                                                        print("Alright I quit")
                                                        wait(.7)
                                                        P1NARRATORS = 1
                                                        P1GLOCK = 1
                                                    elif P1NARRATORS == 1:
                                                        print("You did it again.")
                                                        wait(.7)
                                                        print("Land a 1 in 100 chance to make a gun appear")
                                                        wait(.7)
                                                        print("That thing could've instantly won you the game")
                                                        wait(.7)
                                                        print("And you KEPT GOING. WHY?")
                                                        wait(.7)
                                                        print("Alright, I'm ending this game for you now")
                                                        wait(.7)
                                                        P2HP = -999
                                                    else:
                                                        print(errmsg)
                                                        wait(.7)
                                                else:
                                                    print("Making something failed. Somhow")
                                                    wait(.7)
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 4:
                                            if P1MP < 5:
                                                print("You don't have enough MP for that")
                                                wait(.15)
                                            else:
                                                print("You gained advantage on your next turn")
                                                wait(.15)
                                                P1AD = 1
                                                P1ADTR = 2
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 5:
                                            if P1MP < 6:
                                                print("You don't have enough MP for that.")
                                                wait(.15)
                                            else:
                                                print("You gave Player 2 disadvantage on their next turn")
                                                wait(.15)
                                                P2AD = 2
                                                P2ADTR = 1
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 6:
                                            if P1MP < 6:
                                                print("You don't have enough MP for that")
                                                wait(.7)
                                            else:
                                                HEAL = int(P1MAXHP/5)
                                                print("Player 1 healed" + str(HEAL) + " HP")
                                                wait(.15)
                                                P1HP = P1HP + HEAL
                                                if P1HP > P1MAXHP:
                                                    print("But, you would've gone over your HP maximum if you did that")
                                                    wait(.7)
                                                    P1HP = P1MAXHP
                                                else:
                                                    P1HP = P1HP
                                                    wait(.55)
                                                mc = 1
                                                cc = 1
                                        elif magicOption == 7:
                                            if P1MP < 1:
                                                print("You have no MP, and therfore cannot use this")
                                                wait(.15)
                                            else:
                                                print("The amount of MP you use for this will be doubled and added to your next attack")
                                                wait(.15)
                                                MPUSE = int(input("How much MP would you like to use for this? "))
                                                wait(.7)
                                                if MPUSE > P1MP:
                                                    print("You don't have enough MP for doing that")
                                                    wait(.7)
                                                else:
                                                    P1DMGBOOST = MPUSE * 2
                                                    print("Player 1 spent" + str(MPUSE) + " adding " + str(P1DMGBOOST) + " damage to their next attack")
                                                    wait(.15)
                                                    P1MP = P1MP - MPUSE
                                                    mc = 1
                                                    cc = 1
                                        elif magicOption == 8:
                                            print("Fireball: Cast a fireball, doing 12-18 damage and ignoring all defence. Costs 5MP")
                                            wait(.15)
                                            print("Random Item: Summon a random item, being a rusty spoon, 3 throwing knvies, or a healing potion. Costs 2MP")
                                            wait(.15)
                                            print("Gain Advantage: When attacking, you add your attack bonus to a random number, being 1-20. Advantage lets you roll twice and take the higher number. Costs 5MP")
                                            wait(.15)
                                            print("Impose Disadvantage: When attacking, you add your attack bonus to a random number, being 1-20. Disadvantage forces you to roll twice and take the lower number. This spell puts disadvantage on your opponent Costs 6MP")
                                            wait(.15)
                                            print("Heal: You may heal 20 percent of your max HP, rounded down. Costs 6MP")
                                            wait(.15)
                                            print("Damage Boost: For every point of MP you put into this spell, your next attack will do 2 more damage. Costs however much MP you want it to")
                                            wait(.7)
                                        else:
                                            print("Please choose a valid option")
                                            wait(.7)
                                elif option == 3:
                                    ic = 0
                                    while ic == 0:
                                        print("1: Spoons: ", str(P1SPOON))
                                        wait(.15)
                                        print("2: Knives: ", str(P1KNIVES))
                                        wait(.15)
                                        print("3: Healing Potions: ", str(P1POTS))
                                        wait(.15)
                                        if P1GLOCK > 0:
                                            print("4: Glock-19")
                                            wait(.15)
                                            P1SEEGUN = 1
                                            print("5: Cancel")
                                            wait(.15)
                                        else:
                                            print("4: Cancel")
                                            wait(.15)
                                        itemOption = int(input("What would you like to use? "))
                                        wait(.7)
                                        if itemOption == 1:
                                            if P1SPOON == 0:
                                                print("You have no spoons. That's kinda sad. No soup for you")
                                                wait(.7)
                                            else:
                                                print("Player 1 threw a rusty spoon, maybe giving Player 2 tetanus, but doing 1 point of damage for sure.")
                                                wait(.7)
                                                P2HP = P2HP - 1
                                                P1SPOON = P1SPOON - 1
                                        elif itemOption == 2:
                                            if P1KNIVES == 0:
                                                print("You don't have anything to cut people with.")
                                                wait(.7)
                                            else:
                                                print("Player 1 threw a knife")
                                                wait(.15)
                                                critnumber = random.randint(1,5)
                                                P2HP - P2HP - critnumber
                                                print("Player 1 did " + str(critnumber) + " damage to Player 2")
                                                wait(.7)
                                                P1KNIVES = P1KNIVES - 1
                                        elif itemOption == 3:
                                            if P1POTS == 0:
                                                print("You have no healing. Skill issue")
                                                wait(.7)
                                            else:
                                                HEAL = random.randint(3,7)
                                                print("Player 1 healed " + str(HEAL) + " HP.")
                                                wait(.15)
                                                P1HP = P1HP + HEAL
                                                if P1HP > P1MAXHP:
                                                    print("But that would bring you over your max HP")
                                                    wait(.7)
                                                    P1HP = P1MAXHP
                                                else:
                                                    P1HP = P1HP
                                                    wait(.55)
                                        elif itemOption == 4:
                                            if P1SEEGUN == 1:
                                                print("Player 1 used their Glock-19, killing Player 2")
                                                wait(.7)
                                                P2HP = 0
                                                ic = 1
                                                cc = 1
                                            elif P1SEEGUN == 0:
                                                print("Player 1 canceled their item usage")
                                                wait(.7)
                                                ic = 0
                                        elif itemOption == 5 and P1SEEGUN == 1:
                                            print("Player 1 canceled their item usage")
                                            wait(.7)
                                            ic = 0
                                        else:
                                            print("Please choose a valid option")
                                            wait(.7)
                                elif option == 4:
                                    print("Player 1 passed their turn")
                                    wait(.7)
                                    mc = 0
                                    cc = 0
                                elif option == 5:
                                    print("1: Yes")
                                    wait(.15)
                                    print("2: No")
                                    wait(.15)
                                    yesorno = int(input("Are you sure you want to forfeit the match"))
                                    wait(.5)
                                    if yesorno == 1:
                                        P1HP = 0
                                    else:
                                        print("You do not run away")
                                        wait(.7)
                                else:
                                    print("Please provide a valid number.")
                                    wait(.7)
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
                    elif P1SPD == P2SPD:
                        critnumber = random.randint(1,2)
                        if critnumber == 1:
                            P1SPD = P1SPD + 1
                        elif critnumber == 2:
                            P2SPD = P2SPD + 1
                        else:
                            print(errmsg)
            print(winner + " won the game")
            wait(.15)
            print("1: Yes")
            wait(.15)
            print("2: No")
            wait(.15)
            yesorno = int(input("Would you like to play again? "))
            wait(.5)
            if yesorno == 1:
                gc = 0
                ac = 1
                cc = 0
                ic = 0
                mc = 0
            elif yesorno == 2:
                print("")
                gc = 1