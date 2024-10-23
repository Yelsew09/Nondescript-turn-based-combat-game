"""
                                            poisun mechanic-damage every turn
                                            avocado-heal and gain pit
                                            pit-throw for damage
                                            can of whipped cream-heal 5 + 1 spd
                                            slowdown- slow enemy
                                            bandana-+1 def - 1 to enemy atk
                                            plastic fork- throw to -1hp
                                            steakknife- 5 damage
                                            pants- +1 def
                                            pair of tongs- steal an item from enemy
                                            bag of popcorn-heal 1-5
                                            container of pudding- heal 8
                                            dog- +1 max hp
                                            handheld game system- -1 def
                                            pair of scissors- 1-10 damage
                                            toothpick- +1 hp
                                            incense holder- - both players spd
                                            cookie jar- open for 1-5 cookies
                                            cookies-heal 1-3 health
                                            spool of ribbon- -speed 5-20
                                            chair- chair
                                            pillow- sleep-- -30 spd go back to max health
                                            wishbone- one player gets a wish
                                            bag-get 1-5 items (random)
                                            umbrella-chance to remove all enemy mana
                                            hamster- deal 3-7 damage but they heal 1-5 health
                                            cat- deals 5 damage to both players
                                            dictionary- increase max mana by 1
                                            candle- use 3 mana to light it once you light it you gain +1 to spdbon
                                            marble- chance to make the enemy slip
                                            nail clippers- -1 atk +1 looking nice
                                            feather duster- clean up the place
                                            pool stick- 50/50 to do 1 damage or nothing
                                            spool of string- chance to knit a sweater
                                            sweater- +1 drip
                                            glasses- +1 max mana
                                            shopping bag- -all your mana for 5 items
                                            game cd- throw for 1-3 damage if you have handheld consol you can input one code 
                                            lace-thats some weird fabric -10000 aura
                                            picture frame- you think back to better times +1 mana
                                            toilet- you become very skibidi do 5 damge
                                            tennis ball- 3 damage but they enemy gets the ball afterward
                                            drawer-chance to get an item or throw for 4 damage
                                            rubber stamp- -1 spd
                                            pocket watch- +1spd bon +3spd
                                            lotion- does nothing or -1 spd if you have tissues AYO
                                            tissues- +1 health
                                            statuette- deal 3 damage chance to split and deal an extra 3 damage
                                            beaded bracelet- throw with a chance to exsplode dealing 10 damage to everyone
                                            game cartidge- PUT IT BACKKKK set health to 1
                                            bottle of lotion- gain 1-10 lotions
                                            thread- chance to gain 2def
                                            shell- it crumbles into dust
                                            glass- throw to deal 2 damage but they gain 1-3 broken glass
                                            stop sign- both players reset to 0 spd
                                            safty pin- reset both player to max health
                                            sheet of paper- write down enemy weaknesses -enemy defense
                                            mirror- you mirror your enemys health
                                            confetti-swap health with enemy
                                            """
import random
import time
def s():
    time.sleep(.15)
game=1
while game==1:    
    print("")
    playagain=0
    print("Welcome to insert game title here")
    s()
    print("or the more commonly used name HELL")
    print("")
    s()
    print("1: Start")
    s()
    print("2: Tutorial")
    s()
    print("3: options")
    s()
    print("4: Exit")
    s()
    start=int(input("What would you like to do?: "))
    s()
    if start==1:
        print("1: PVP")
        s()
        print("2: PVC")
        s()
        print("0: Back")
        s()
        start=int(input("what would you ;ike to play: "))
        s()
        if start==1:
            playagain=1
        elif start==2:
            print("coming soon")
        elif start==0:
            print("")
        else:
            print("error")
    elif start==2:
        print("What would you like to know about?")
        s()
        print("1: How to play?")
        s()
        print("2: Characters")
        s()
        print("3: Attack System")
        s()
        print("4: Magic System")
        s()
        print("5: Item system")
        s()
        print("6: Other features")
        s()
        print("0: Back")
        s()
        print("")
        info=int(input("What would you like to do?: "))
        s()
        if info==1:
            print("You will start by selecting your charcters, once you have picked your charcter you will fight you can attack use magic use items forfiet or pass your turn when someone runs out of health the other player wins.")
            s()
            placeholder=input("Are you done reading")
            s()
        elif info==2:
            print("what would you like to know about the characters?")
            s()
            print("1: Stats")
            s()
            print("2: Backstories")
            s()
            print("0: Back")
            s()
            info=int(input("What would you like to do?: "))
            s()
            if info==1:
                print("Which Charcter's stats would you like to see")
                s()
                print("1: General")
                s()
                print("2: Knight")
                s()
                print("3: Peashooter")
                s()
                print("4: Mage")
                s()
                print("5: Rouge")
                s()
                print("6: Skele")
                s()
                print("7: Bard")
                s()
                print("8: Barbarain")
                s()
                print("9: Random system")
                s()
                print("0: Back")
                s()
                info=int(input("What would you like to know about?: "))
                if info==1:
                    print("Every Charcter has 10 stats most are hidden the stats are")
                    print("1: HP")
                    print("2: MAXHP")
                    print("3: ATK")
                    print("4: ATKBON")
                    print("5: DEF")
                    print("6: MP")
                    print("7: MAXMP")
                    print("8: MPBON")
                    print("9: SPD")
                    print("10: SPDBON")
                    info=int(input("What would you like to know about"))
                    if info==1:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==2:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==3:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==4:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==5:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==6:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==7:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==8:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==9:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==10:
                        print("coming soon")
                        placeholder=input("Are you done reading")
                        s()
                    elif info==0:
                        print("")
                    else:
                        print("error")
            elif info==2:
                print("Which Charcter's would you like to know about")
                s()
                print("1: General")
                s()
                print("2: Knight")
                s()
                print("3: Peashooter")
                s()
                print("4: Mage")
                s()
                print("5: Rouge")
                s()
                print("6: Skele")
                s()
                print("7: Bard")
                s()
                print("8: Barbarain")
                s()
                print("0: Back")
                s()
                info=int(input("What would you like to know about?: "))
                if info==1:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==2:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==3:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==4:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==5:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==6:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==7:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==8:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==9:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==10:
                    print("coming soon")
                    placeholder=input("Are you done reading")
                    s()
                elif info==0:
                    print("")
                else:
                    print("error")
            elif info==0:
                print("")
            else:
                print("try again")
                s()
        elif info==3:
            print("what would you like to know about attacking?")
            s()
            print("1: Damage system")
            s()
            print("2: Crit system")
            s()
            print("3: Damage boost")
            s()
            print("4: Advantage")
            s()
            print("0: Back")
            s()
            info=int(input("What would you like to do?: "))
            s()
        elif info==4:
            print("what would you like to know about magic?")
            s()
            print("1: MP system")
            s()
            print("2: Gain defense")
            s()
            print("3: Gain an item")
            s()
            print("4: Advantage")
            s()
            print("5: Heal")
            s()
            print("6: Fireball")
            s()
            print("7: Damage Boost")
            s()
            print("0: Back")
            s()
            info=int(input("What would you like to do?: "))
            s()
        elif info==5:
            print("What would you like to know about items?")
            s()
            print("1: item chances")
            s()
            print("2: Heal potion")
            s()
            print("3: Knives")
            s()
            print("4: Rusty spoon")
            s()
            print("0: Back")
            s()
            info=int(input("What would you like to do?: "))
            s()
        elif info==6:
            print("What would you like to know about other features")
            s()
            print("1: Healing")
            s()
            print("2: Speed")
            s()
            print("3: coming soon")
            s()
            print("0: Back")
            s()
            info=int(input("What would you like to do?: "))
            s()
        elif info==0:
            print("")
        else:
            print("ERROR")
    elif start==3:
        print("No Options at the moment")
        s()
    elif start==4:
        print("")
        s()
        playagain=0
        game=2
    while playagain==1:
        s()
        print("")
        s()
        print("Please select a class, player 1.")
        s()
        print("1: Knight")
        s()
        print("2: Peashooter")
        s()
        print("3: Mage")
        s()
        print("4: Rouge")
        s()
        print("5: Skele")
        s()
        print("6: Bard")
        s()
        print("7: Barbarain")
        s()
        print("8: Random")
        #Player 1 selects a class
        cc=1
        rc=1
        allcorrect=1
        while allcorrect==1:
            while cc==1:
                player1class = int(input("Choose a class from the list above (please choose a number): "))
                s()
                while rc==1:
                    if player1class == 1:
                        player1class = "Knight"
                        P1HP = 42
                        P1MAXHP = P1HP
                        P1ATK = 12
                        P1ATKBON = P1ATK + 2
                        P1DEF = 14
                        P1MP = 4
                        P1MAXMP = P1MP
                        P1MPBON = 1
                        P1SPD = 3
                        P1SPDBON = 2
                        cc=2
                        rc=2
                    elif player1class == 2:
                        player1class = "Peashooter"
                        P1HP = 35
                        P1MAXHP = P1HP
                        P1ATK = 10
                        P1ATKBON = P1ATK + 2
                        P1DEF = 14
                        P1MP = 5
                        P1MAXMP = P1MP
                        P1MPBON = 1
                        P1SPD = 6
                        P1SPDBON = 2
                        cc=2
                        rc=2
                    elif player1class == 3:
                        player1class = "Mage"
                        P1HP = 29
                        P1MAXHP = P1HP
                        P1ATK = 7
                        P1ATKBON = P1ATK + 2
                        P1DEF = 10
                        P1MP = 20
                        P1MAXMP = P1MP
                        P1MPBON = 5
                        P1SPD = 2
                        P1SPDBON = 2
                        cc=2
                        rc=2
                    elif player1class == 4:
                        player1class = "Rouge"
                        P1HP = 31
                        P1MAXHP = P1HP
                        P1ATK = 13
                        P1ATKBON = P1ATK + 2
                        P1DEF = 14
                        P1MP = 6
                        P1MAXMP = P1MP
                        P1MPBON = 1
                        P1SPD = 7
                        P1SPDBON = 3
                        cc=2
                        rc=2
                    elif player1class == 5:
                        player1class = "skele"
                        P1HP = 20
                        P1MAXHP = P1HP
                        P1ATK = 20
                        P1ATKBON = P1ATK + 2
                        P1DEF = 10
                        P1MP = 15
                        P1MAXMP = P1MP
                        P1MPBON = 3
                        P1SPD = 8
                        P1SPDBON = 4
                        cc=2
                        rc=2
                    elif player1class == 6:
                        player1class = "Bard"
                        P1HP = 37
                        P1MAXHP = P1HP
                        P1ATK = 7
                        P1ATKBON = P1ATK + 2
                        P1DEF = 13
                        P1MP = 17
                        P1MAXMP = P1MP
                        P1MPBON = 4
                        P1SPD = 5
                        P1SPDBON = 2
                        cc=2
                        rc=2
                    elif player1class == 7: 
                        player1class = "Barbarian"
                        P1HP = 52
                        P1MAXHP = P1HP
                        P1ATK = 14
                        P1ATKBON = P1ATK + 2
                        P1DEF = 11
                        P1MP = 2
                        P1MAXMP = P1MP
                        P1MPBON = .25
                        P1SPD = 4
                        P1SPDBON = 2
                        cc=2
                        rc=2
                    elif player1class ==88224646790:
                        player1class = "Sigma"
                        P1HP= 88224646790
                        P1MAXHP = P1HP
                        P1ATK= 88224646790
                        P1ATKBON = 88224646790
                        P1DEF= 88224646790
                        P1MP= 88224646790
                        P1MAXMP = P1MP
                        P1MPBON= 88224646790
                        P1SPD= 88224646790
                        P1SPDBON = 88224646790
                        cc=2
                        rc=2
                    elif player1class == 8:
                        player1class=random.randint(1,7)
                        cc=2
                    else:
                        print("Please give a valid number.")
                        cc=1
                        rc=1
                        s()
                print("1: Yes")
                s()
                print("2: No")
                s()
                yesorno = int(input("You have chosen " + str(player1class) + ". Is this correct?: "))
                s()
                if yesorno == 1:
                    print("Player 1 has chosen the " + str(player1class) + " class.")
                    s()
                    print("")
                    s()
                    allcorrect=2
                elif yesorno == 2:
                    print("repick your charcter.")
                    s()
                    cc=1
                    rc=1
                else:
                    print("Something went wrong please try again")
                    s()
                    cc=1
        cc=1
        rc=1
        allcorrect=1
        #Player 2 selects a class
        while allcorrect==1:
            while cc==1:
                print("Please select a classs, player 2")
                s()
                rc=1
                player2class = int(input("Choose 1 from the list above (please choose a number): "))
                while rc==1:
                    s()
                    if player2class == 1:
                        player2class = "Knight"
                        P2HP = 42
                        P2MAXHP = P2HP
                        P2ATK = 12
                        P2ATKBON = P2ATK + 2
                        P2DEF = 14
                        P2MP = 4
                        P2MAXMP = P2MP
                        P2MPBON = 1
                        P2SPD = 3
                        P2SPDBON = 2
                        cc=2
                        rc=2
                    elif player2class == 2:
                        player2class = "Peashooter"
                        P2HP = 35
                        P2MAXHP = P2HP
                        P2ATK = 10
                        P2ATKBON = P2ATK + 2
                        P2DEF = 14
                        P2MP = 5
                        P2MAXMP = P2MP
                        P2MPBON = 1
                        P2SPD = 6
                        P2SPDBON = 2
                        cc=2
                        rc=2
                    elif player2class == 3:
                        player2class = "Mage"
                        P2HP = 29
                        P2MAXHP = P2HP
                        P2ATK = 7
                        P2ATKBON = P2ATK + 2
                        P2DEF = 10
                        P2MP = 20
                        P2MAXMP = P2MP
                        P2MPBON = 5
                        P2SPD = 2
                        P2SPDBON = 2
                        cc=2
                        rc=2
                    elif player2class == 4:
                        player2class = "Rouge"
                        P2HP = 31
                        P2MAXHP = P2HP
                        P2ATK = 13
                        P2ATKBON = P2ATK + 2
                        P2DEF = 14
                        P2MP = 6
                        P2MAXMP = P2MP
                        P2MPBON = 1
                        P2SPD = 7
                        P2SPDBON = 3
                        cc=2
                    elif player2class == 5:
                        player2class = "Skele"
                        P2HP = 20
                        P2MAXHP = P2HP
                        P2ATK = 20
                        P2ATKBON = P2ATK + 2
                        P2DEF = 10
                        P2MP = 15
                        P2MAXMP = P2MP
                        P2MPBON = 3
                        P2SPD = 8
                        P2SPDBON = 4
                        cc=2
                        rc=2
                    elif player2class == 6:
                        player2class = "Bard"
                        P2HP = 37
                        P2MAXHP = P2HP
                        P2ATK = 7
                        P2ATKBON = P2ATK + 2
                        P2DEF = 13
                        P2MP = 17
                        P2MAXMP = P2MP
                        P2MPBON = 4
                        P2SPD = 5
                        P2SPDBON = 2
                        cc=2
                        rc=2
                    elif player2class ==7:
                        player2class = "Barbrian"
                        P2HP= 52
                        P2MAXHP = P2HP
                        P2ATK= 14
                        P2ATKBON = P2ATK + 2
                        P2DEF= 11
                        P2MP= 2
                        P2MAXMP = P2MP
                        P2MPBON= 0.25
                        P2SPD= 4
                        P2SPDBON = 2
                        cc=2
                        rc=2
                    elif player2class ==88224646790:
                        player2class = "Sigma"
                        P2HP= 88224646790
                        P2MAXHP = P2HP
                        P2ATK= 88224646790
                        P2ATKBON= 88224646790
                        P2DEF= 88224646790
                        P2MP= 88224646790
                        P2MAXMP = P2MP
                        P2MPBON= 88224646790
                        P2SPD= 88224646790
                        P2SPDBON = 88224646790
                        cc=2
                        rc=2
                    elif player2class==8:
                        print("you have chosen random")
                        player2class=random.randint(1,7)
                        cc=2
                    else:
                        print("Next time put in a valid number ")
                        s()
                print("1: Yes")
                s()
                print("2: No")
                s()
                yesorno = int(input("you have chosen " + str(player2class) + ". Is this correct?: "))
                s()
                if yesorno == 1:
                    print("Player 2 has chosen the " + str(player2class) + " class.")
                    s()
                    print("")
                    allcorrect=2
                elif yesorno == 2:
                    print("repick your charcter.")
                    s()
                    cc=1
                    rc=1
                else:
                    print("please try again")
                    s()
                    cc=1
                    rc=1
        for i in range(1):
            winner=1
            roundnumber = 1  
            DMGBUFFP1=0
            DMGBUFFP2=0
            dmgp1=1
            dmgp2=1
            rollp1=1
            rollp2=1
            rolladp1=1
            rolladp2=2
            p1pots=1
            p2pots=1
            p1spoons=0
            p2spoons=0
            p1GLOCK19s=0
            p2GLOCK19s=0
            p1knives=0
            p2knives=0
            p1bows=0
            p2bows=0 
            p1arrows=0
            p2arrows=0
            p1mpots=0
            p2mpots=0
            p1hats=0
            p2hats=0
            p1sheilds=0
            p2sheilds=0
            p1shoes=0
            p2shoes=0
            p1avocado=0
            p2avocado=0
            p1pits=0
            p2pits=0
            p1creams=0
            p2creams=0
        print("Player 1 HP ",P1HP)
        s()
        print("Player 2 HP ",P2HP)
        s()
        print("")
        #round start
        print("Player 1 Speed ",P1SPD)
        s()
        print("Player 2 Speed ",P2SPD )
        s()
        while roundnumber < 100:
            turn=1
            print("Round " + str(roundnumber) + " ")
            s()
            if P1HP <= 0:
                print("Player 2 wins the game")
                s()
                winner=player2class
                break
            elif P2HP <= 0:
                print("Player 1 wins the game")
                s()
                winner=player2class
                break
            else:
                print("")
                if P1SPD > P2SPD:
                    print("player 1's turn")
                    s()
                    print("player 1 has "+ str(P1MP) +" MP left")
                    s()
                    print("do one of the following")
                    s()
                    print("1: Attack")
                    s()
                    print("2: Magic")
                    s()
                    print("3: Use an item")
                    s()
                    print("4: Run Away")
                    s()
                    print("5: pass turn")
                    while turn == 1:
                        option=int(input("what would player 1 like to do?: "))
                        print("")
                        s()
                        critnumber=random.randint(rollp1,20)
                        if option == 1 and critnumber==20:
                            print("")
                            print("Player 1 used Attack")
                            s()
                            print("Player 1 Rolled a ",critnumber)
                            s()
                            print("Its a Criticle hit!!!")
                            s()
                            TOTDMG = (critnumber+(P1ATK*2))-P2DEF
                            if TOTDMG < 0:
                                TOTDMG = 0
                            print("Player 1 did " + str(TOTDMG) + " Damage to Player 2")
                            s()
                            P2HP = P2HP-TOTDMG
                            print("player 2 has " + str(P2HP) + " HP Left")
                            s()
                            P2SPD = P2SPD + P2SPDBON
                            if rolladp1==2:
                                rolladp1=1
                                rollp1=1
                            if dmgp1 >= 2:
                                P1ATK=P1ATK-DMGBUFFP1
                                dmgp1=dmgp1-1
                            turn=2
                            roundnumber=roundnumber + 1
                            P1MP = P1MP + P1MPBON
                            print("")
                            print("Player 1 gained " + str(P1MPBON) + " MP back")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            print("Player 1 has " + str(P1MP) + " MP left")
                            s()
                        elif option == 1 and critnumber<20 and critnumber>=2:
                            print("Player 1 used Attack")
                            s()
                            print("Player 1 Rolled a ",critnumber)
                            s()
                            TOTDMG = (critnumber+(P1ATK))-P2DEF
                            if TOTDMG < 0:
                                TOTDMG = 0
                            print("Player 1 did " + str(TOTDMG) + " Damage to Player 2")
                            s()
                            P2HP = P2HP-TOTDMG
                            print("Player 2 has " + str(P2HP) + " HP left")
                            s()
                            P2SPD = P2SPD + P2SPDBON
                            if rolladp1==2:
                                rolladp1=1
                                rollp1=1
                            if dmgp1 >= 2:
                                P1ATK==P1ATK-DMGBUFFP1
                                dmgp1=dmgp1-1
                            turn=2
                            roundnumber=roundnumber+1
                            P1MP = P1MP + P1MPBON
                            print("")
                            print("Player 1 gained " + str(P1MPBON) + " MP back")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            print("Player 1 has " + str(P1MP) + " MP left")
                            s()
                        elif option == 1 and critnumber == 1:
                            print("Player 1 used Attack")
                            s()
                            print("Player 1 Rolled a 1")
                            s()
                            print("Player 1 missed")
                            s()
                            print("Player 1 did 0 Damage to Player 2")
                            s()
                            print("Player 2 has " + str(P2HP) + " HP left")
                            s()
                            P2SPD = P2SPD + P2SPDBON
                            if dmgp1 >= 2:
                                P1ATK=P1ATK-DMGBUFFP1
                                dmgp1 = dmgp1-1
                            turn=2
                            roundnumber=roundnumber+1
                            P1MP = P1MP + P1MPBON
                            print("")
                            print("Player 1 gained "+ str(P1MPBON) + " MP back")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            print("Player 1 has " + str(P1MP) + " MP left")
                            s()
                        elif option == 2:
                            print("Please do one of the following")
                            s()
                            print("0: Cancel")
                            s()
                            print("1: Gain +1 DEF")
                            s()
                            print("2: Gain an item")
                            s()
                            print("3: Better Roll Next Turn-3MP")
                            s()
                            print("4: Heal 20 percent of max health-4MP")
                            s()
                            print("5: FireBall-5MP")
                            s()
                            print("6: Damage boost for every MP you have-2MP")
                            s()
                            magic_option=int(input("What would you like to do?: "))
                            print("")
                            s()
                            if P1MP < magic_option:
                                print("you dont have enough Mana")
                                s()
                            elif P1MP >= magic_option:
                                if magic_option == 1:
                                    P1DEF=P1DEF+1
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    print("")
                                    print("Player 1 gained " + str(P1MPBON) + " MP back")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    print("Player 1 has " + str(P1MP) + " MP left")
                                    s()
                                elif magic_option==6:
                                    print("Player 1 used Damage boost")
                                    s()
                                    P1MP = P1MP - magic_option
                                    DMGBUFFP1=P1ATKBON+P1MP
                                    P1MP=0
                                    dmgp1 = dmgp1+1
                                    P1ATK=DMGBUFFP1 + P1ATK
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    print("")
                                    print("Player 1 gained " + str(P1MPBON) + " MP back")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    print("Player 1 has " + str(P1MP) + " MP left")
                                    s()
                                elif magic_option==3:
                                    print("Player 1 used Advantage")
                                    rolladp1=2
                                    rollp1=10
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    print("")
                                    print("Player 1 gained " + str(P1MPBON) + " MP back")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    print("Player 1 has " + str(P1MP) + " MP left")
                                    s()
                                    turn = 2
                                elif magic_option==5:
                                    print("Player 1 used fireball")
                                    s()
                                    fireballdmg = random.randint(12,18)
                                    print("Player 1 did " + str(fireballdmg) + " Damage to Player 2")
                                    s()
                                    P2HP=P2HP-fireballdmg
                                    print("Player 2 has " + str(P2HP) + " HP left")
                                    s()
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    print("")
                                    print("Player 1 gained " + str(P1MPBON) + " MP back")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    print("Player 1 has " + str(P1MP) + " MP left")
                                    s()
                                elif magic_option==4:
                                    print("Player 1 used heal")
                                    s()
                                    P1HP = P1HP + (P1MAXHP/5)
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    if P1MAXHP < P1HP:
                                        P1HP = P1MAXHP
                                elif magic_option==0:
                                    print("")
                                elif magic_option==2:
                                    """
                                            slowdown- slow enemy
                                            bandana-+1 def - 1 to enemy atk
                                            plastic fork- throw to -1hp
                                            steakknife- 5 damage
                                            pants- +1 def
                                            pair of tongs- steal an item from enemy
                                            bag of popcorn-heal 1-5
                                            container of pudding- heal 8
                                            dog- +1 max hp
                                            handheld game system- -1 def
                                            pair of scissors- 1-10 damage
                                            toothpick- +1 hp
                                            incense holder- - both players spd
                                            cookie jar- open for 1-5 cookies
                                            cookies-heal 1-3 health
                                            spool of ribbon- -speed 5-20
                                            chair- chair
                                            pillow- sleep-- -30 spd go back to max health
                                            wishbone- one player gets a wish
                                            bag-get 1-5 items (random)
                                            umbrella- nothing
                                            hamster- deal 3-7 damage but they heal 1-5 health
                                            cat- deals 5 damage to both players
                                            dictionary- increase max mana by 1
                                            candle- use 3 mana to light it once you light it you gain +1 to spdbon
                                            marble- chance to make the enemy slip
                                            nail clippers- -1 atk +1 looking nice
                                            feather duster- clean up the place
                                            pool stick- 50/50 to do 1 damage or nothing
                                            spool of string- chance to knit a sweater
                                            sweater- +1 drip
                                            glasses- +1 max mana
                                            shopping bag- -all your mana for 5 items
                                            game cd- throw for 1-3 damage if you have handheld consol you can input one code 
                                            lace-thats some weird fabric -10000 aura
                                            picture frame- you think back to better times +1 mana
                                            toilet- you become very skibidi do 5 damge
                                            tennis ball- 3 damage but they enemy gets the ball afterward
                                            drawer-chance to get an item or throw for 4 damage
                                            rubber stamp- -1 spd
                                            pocket watch- +1spd bon +3spd
                                            lotion- does nothing or -1 spd if you have tissues AYO
                                            tissues- +1 health
                                            statuette- deal 3 damage chance to split and deal an extra 3 damage
                                            beaded bracelet- throw with a chance to exsplode dealing 10 damage to everyone
                                            game cartidge- PUT IT BACKKKK set health to 1
                                            bottle of lotion- gain 1-10 lotions
                                            thread- chance to gain 2def
                                            shell- it crumbles into dust
                                            glass- throw to deal 2 damage but they gain 1-3 broken glass
                                            stop sign- both players reset to 0 spd 2spd bon
                                            safty pin- reset both player to max health
                                            sheet of paper- write down enemy weaknesses -enemy defense
                                            mirror- you mirror your enemys health
                                            poisun mechanic-damage every turn
                                            plastic vampire teeth- heal 5 damage 5
                                            """
                                    print("Player 1 used gain a random item")
                                    s()
                                    P1MP = P1MP - magic_option
                                    bestitem=191
                                    itemspin=random.randint(1,bestitem)
                                    print("You rolled a " + str(itemspin) + " ")
                                    s()
                                    if itemspin >= 1 and itemspin<= 20:
                                        print("Player 1 Conjured a rusty spoon")
                                        s()
                                        print("what a waste of a turn")
                                        s()
                                        p1spoons=p1spoons+1
                                    elif itemspin >= 21 and itemspin<= 40:
                                        print("You Conjured Throwing knives")
                                        s()
                                        p1knives=p1knives+3
                                    elif itemspin >= 41 and itemspin<= 60:
                                        print("Player 1 Conjured a healing potion")
                                        s()
                                        p1pots=p1pots+1
                                    elif itemspin >=61 and itemspin<=80:
                                        arrow=random.randint(2,4)
                                        if p1bows>=1:
                                            print("Player 1 conjured " + str(arrow) + " arrows")
                                        elif p1bows==0:
                                            print("player 1 conjured a bow and arrow")
                                            s()
                                            p1bows = p1bows + 1
                                            p1arrows=p1arrows+1
                                        else:
                                            print("ERROR")
                                    elif itemspin >=81 and itemspin <=90:
                                        print("Player 1 Conjured a fancy hat")
                                        s()
                                        p1hats=p1hats+1
                                    elif itemspin >= 91 and itemspin<= 110:
                                        print("Player 1 Conjured a mana potion")
                                        s()
                                        p1mpots=p1mpots+1
                                    elif itemspin >= 111 and itemspin<= 130:
                                        print("Player 1 Conjured a sheild")
                                        s()
                                        p1sheilds=p1sheilds+1
                                    elif itemspin >= 131 and itemspin<= 150:
                                        print("Player 1 Conjured a pair of new sneakers")
                                        s()
                                        p1shoes=p1shoes+1
                                    elif itemspin >= 151 and itemspin<= 170:
                                        print("Player 1 Conjured a...")
                                        s()
                                        print("a avocado")
                                        s()
                                        p1avocado=p1avocado+1
                                    elif itemspin >= 171 and itemspin<= 190:
                                        print("Player 1 Conjured a can of whipped cream")
                                        s()                                        
                                        p1creams=p1creams+1
                                    elif itemspin == bestitem:
                                        print("Player 1 Conjured a...")
                                        s()
                                        s()
                                        s()
                                        s()
                                        s()
                                        print("wait what..")
                                        s()
                                        s()
                                        print("how... why!?!!?")
                                        s()
                                        print("why is the in the game (sigh)")
                                        s()
                                        s()
                                        print("i don't get paid enough for this")
                                        s()
                                        print("Player 1 Conjured a Glock-19")
                                        s()
                                        s()
                                        print("...This was not supposed to happen")
                                        s()
                                        print("")
                                        p1GLOCK19s=p1GLOCK19s+1
                                    else:
                                        print("THIS SHOULDN'T BE POSSIBLE HOW DID I MESS UP THIS BADLY")
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    print("")
                                    print("Player 1 gained " + str(P1MPBON) + " MP back")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    print("Player 1 has " + str(P1MP) + " MP left")
                                    s()
                                else:
                                    print("somthing went wrong please try again")
                                    s()
                            else:
                                print("try again")
                                s()
                        elif option == 4:        
                                print("Are you SURE you want to run away??")
                                s()
                                print("1: Yes")
                                s()
                                print("2: No")
                                s()
                                yesorno=int(input("select an answer: "))
                                s()
                                if yesorno==1:
                                    print("you forfiet the game and run away")
                                    s()
                                    print("Player 2 wins")
                                    s()
                                    crash=1
                                    while crash==1:
                                        escape=input(": ")
                                        if escape=="DEVUNLOCK":
                                            crash=2
                                            print("unlocked")
                                elif yesorno==2:
                                    print("")
                                else:
                                    print("")
                        elif option == 3:
                            glocks=0
                            print("Player 1 has " + str(p1pots) + " Healing Potions left")
                            s()
                            print("Player 1 has " + str(p1spoons) + " Rusty spoons left")
                            s()
                            if p1GLOCK19s>=1:
                                print("THEY HAVE A GUNNN!!!!!!!!")
                                s()
                                glocks=1
                            print("Player 1 has " + str(p1knives) + " Knives left")
                            s()
                            if p1bows==1:
                                print("Player 1 has a bow and has " + str(p1arrows) + " arrows left")
                                s()
                            elif p1bows==0:
                                print("player 1 doesnt have a bow and has " + str(p1arrows) + " arrows left")
                            print("player 1 has " + str(p1hats) + " Fancy hats left")    
                            print("Player 1 has " + str(p1mpots) + " Mana potions left")
                            s()
                            print("player 1 had " + str(p1sheilds) + " sheilds left")
                            s()
                            print("player 1 has " + str(p1shoes) + " pairs of sneaker left")
                            s()
                            print("player 1 has " + str(p1avocado) + " avocado's left")
                            s()
                            print("player 1 has " + str(p1pits) + " Pits left")
                            s()
                            print("player 1 has " + str(p1creams) + " Cans of whipped cream left")
                            s()





                            print("")
                            print("1: Use healing potion")
                            s()
                            print("2: Throw a rusty spoon")
                            s()
                            print("3: Throw a throwing knife")
                            s()
                            print("4: shoot an arrow")
                            s()
                            print("5: Use a mana potion")
                            s()
                            print("6: use the sheild")
                            s()
                            print("7: wear a fancy hat")
                            s()
                            print("8: wear sneakers")
                            s()
                            print("9: eat avocado")
                            s()
                            print("10: throw pit")
                            s()
                            print("11: eat whipped cream")
                            print("0: cancel")
                            if glocks==1:
                                print("100000: Shoot")
                                s()
                            s()
                            itemchoice=int(input("What would you like to do?: "))
                            s()
                            if itemchoice==1 and p1pots >= 1:
                                print("Player 1 Heals 5 health")
                                s()
                                P1HP=P1HP+5
                                if P1MAXHP<=P1HP:
                                    P1HP=P1MAXHP
                                print("Player 1 has " + str(P1HP) + " HP")
                                s()
                                p1pots=p1pots-1
                            elif itemchoice==3 and p1knives>=1:
                                print("Player 1 threw a knife")
                                s()
                                knifedamage=random.randint(1,5)
                                P2HP=P2HP-knifedamage
                                print("Player 1 did " + str(knifedamage) + " Damage to Player 2")
                                s()
                                print("Player 2 has " + str(P2HP) + " HP left")
                                s()
                                p1knives=p1knives-1
                            elif itemchoice==2 and p1spoons>=1:
                                print("Player 1 threw a Spoon")
                                s()
                                spooncrit=random.randint(1,100)
                                if spooncrit>=1 and spooncrit<=70:
                                    print("the spoon gave Player 2 a small cut and did 1 damage")
                                    s()
                                    P2HP=P2HP-1
                                    print("Player 2 has " + str(P2HP) + " HP left")
                                    s()
                                elif spooncrit>=71 and spooncrit<=99:
                                    spoondamage=random.randint(2,10)
                                    print("the spoon gave Player 2 a cut and did " + str(spoondamage) + " Damge to Player 2")
                                    s()
                                    P2HP=P2HP-spoondamage
                                    print("Player 2 Has " + str(P2HP) + " HP left")
                                    s()
                                elif spooncrit==100:
                                    print("Player 1 threw the spoon and cut Player 2")
                                    s()
                                    print("Player 2 got tetanites and died")
                                    s()
                                    P2HP=0
                                else:
                                    print("ERROR ERROR")
                                p1spoons=p1spoons-1
                            elif itemchoice==100000 and p1GLOCK19s>=1:
                                print("player 2 was shot and died")
                                P2HP=0
                                print("stop gun voilence")
                            elif itemchoice==0:
                                print("")
                            elif itemchoice==4 and p1bows==1 and p1arrows>=1:
                                arrowdamage=random.randint(2,5)
                                P2HP=P2HP-arrowdamage
                                print("You shot an arrow at player 2 doing " + str(arrowdamage) + " damage to Player 2, Player 2 has " + str(P2HP) + " HP left")
                                p1arrows=p1arrows-1
                                bbreak=random.randint(1,50)
                                if bbreak==50:
                                    p1bows=0
                                    print("your bow broke")
                            elif itemchoice==5 and p1mpots >= 1:
                                print("Player 1 regains 5 mana")
                                s()
                                P1MP=P1MP+5
                                if P1MAXMP<=P1MP:
                                    P1MP=P1MAXMP
                                print("Player 1 has " + str(P1MP) + " MP")
                                s()
                                p1mpots=p1mpots-1
                            elif itemchoice==6 and p1sheilds >= 1:
                                print("Player 1 sheilds themself and gains 2 def")
                                s()
                                P1DEF=P1DEF+2
                                p1sheilds=p1sheilds-1
                            elif itemchoice==7 and p1hats >= 1:
                                print("Player 1 wears the fancy hat and their max health goes up by 5 and they regain all missing health")
                                s()
                                P1MAXHP=P1MAXHP+5
                                P1HP=P1MAXHP
                                print("Player 1 has " + str(P1HP) + " HP")
                                s()
                                p1hats=p1hats-1
                            elif itemchoice==8 and p1shoes >= 1:
                                print("Player 1 wears the pair of sneaker and their Speed goes up by 5 and increase Speed bon by 1")
                                s()
                                P1SPD=P1SPD+5
                                P1SPDBON=P1SPDBON+.5
                                s()
                                p1shoes=p1shoes-1
                            elif itemchoice==9 and p1avocado >= 1:
                                print("Player 1 Heals 3 health")
                                s()
                                P1HP=P1HP+3
                                if P1MAXHP<=P1HP:
                                    P1HP=P1MAXHP
                                print("Player 1 has " + str(P1HP) + " HP")
                                s()
                                p1pits=p1pits+1
                                p1avocado=p1avocado-1
                            elif itemchoice==10 and p1pits>=1:
                                print("Player 1 threw a pit")
                                s()
                                knifedamage=random.randint(1,3)
                                P2HP=P2HP-knifedamage
                                print("Player 1 did " + str(knifedamage) + " Damage to Player 2")
                                s()
                                print("Player 2 has " + str(P2HP) + " HP left")
                                s()
                                p1pits=p1pits-1
                            elif itemchoice==11 and p1cream >= 1:
                                c02pois=random.randit(1-10)
                                if c02pois==10:
                                    print("player 1 died to carbon dioxide poisening")
                                    P1HP=0
                                    break
                                elif c02pois!=10:
                                    print("Player 1 Heals 5 health")
                                    s()
                                    P1HP=P1HP+3
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    print("Player 1 has " + str(P1HP) + " HP")
                                    s()
                                    p1creams=p1creams-1
                            else:
                                print("you either didnt have the item or you typed in a unavalible number either way your an idiot")
                                s()

                        elif option==5:
                            print("You pass you're turn")
                            turn = 2
                            P2SPD = P2SPD + P2SPDBON
                            P1MP = P1MP + P1MPBON
                            print("")
                            print("Player 1 gained " + str(P1MPBON) + " MP back")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            print("Player 1 has " + str(P1MP) + " MP left")
                            s()
                        else:
                            print("please try again")
                            s()
                elif P1SPD < P2SPD:
                    print("player 2's turn")
                    s()
                    print("player 2 has "+ str(P2MP) +" MP left")
                    s()
                    print("do one of the following")
                    s()
                    print("1: Attack")
                    s()
                    print("2: Magic")
                    s()
                    print("3: Use an item")
                    s()
                    print("4: Run Away")
                    s()
                    print("5: pass turn")
                    while turn == 1:
                        option=int(input("what would player 2 like to do?: "))
                        print("")
                        s()
                        critnumber=random.randint(rollp2,20)
                        if option == 1 and critnumber==20:
                            print("")
                            print("Player 2 used Attack")
                            s()
                            print("Player 2 Rolled a ",critnumber)
                            s()
                            print("Its a Criticle hit!!!")
                            s()
                            TOTDMG= (critnumber+(P2ATK*2))-P1DEF
                            if TOTDMG < 0:
                                TOTDMG=0
                            print("Player 2 did " + str(TOTDMG) + " Damage to Player 1")
                            s()
                            P1HP = P1HP-TOTDMG
                            print("player 1 has " + str(P1HP) + " HP Left")
                            s()
                            P1SPD = P1SPD + P1SPDBON
                            if rolladp2==2:
                                rolladp2=1
                                rollp2=1
                            if dmgp2 >= 2:
                                P2ATK=P2ATK-DMGBUFFP2
                                dmgp2=dmgp2-1
                            turn=2
                            roundnumber=roundnumber+1
                            P2MP = P2MP + P2MPBON
                            print("")
                            print("Player 2 gained " + str(P2MPBON) + " MP back")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            print("Player 2 has " + str(P2MP) + " MP left")
                            s()
                        elif option == 1 and critnumber<20 and critnumber>=2:
                            print("Player 2 used Attack")
                            s()
                            print("Player 2 Rolled a ", critnumber)
                            s()
                            TOTDMG= (critnumber+P2ATK)-P2DEF
                            if TOTDMG < 0:
                                TOTDMG=0
                            print("Player 2 did " + str(TOTDMG) + " Damage to Player 1")
                            s()
                            P1HP = P1HP-TOTDMG
                            print("Player 1 has " + str(P1HP) + " HP left")
                            s()
                            P1SPD = P1SPD + P1SPDBON
                            if rolladp2==2:
                                rolladp2=1
                                rollp2=1
                            if dmgp2 >= 2:
                                P2ATK=P2ATK-DMGBUFFP2
                                dmgp2 = dmgp2 - 1
                            turn=2
                            roundnumber=roundnumber+1
                            P2MP = P2MP + P2MPBON
                            print("")
                            print("Player 2 gained " + str(P2MPBON) + " MP back")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            print("Player 2 has " + str(P2MP) + " MP left")
                            s()
                        elif option == 1 and critnumber==1:
                            print("Player 2 used Attack")
                            s()
                            print("Player 2 Rolled a 1")
                            s()
                            print("Player 2 missed")
                            s()
                            print("Player 2 did 0 Damage to Player 1")
                            s()
                            print("Player 1 has " + str(P1HP) + " HP left")
                            s()
                            P1SPD = P1SPD + P1SPDBON
                            if dmgp2 >= 2:
                                P2ATK==P2ATK-DMGBUFFP2
                                dmgp2=dmgp2-1
                            turn=2
                            roundnumber=roundnumber+1
                            P2MP = P2MP + P2MPBON
                            print("")
                            print("Player 2 gained "+ str(P2MPBON) + " MP back")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            print("Player 2 has " + str(P2MP) + " MP left")
                            s()
                        elif option == 2:
                            print("Please do one of the following")
                            s()
                            print("0: Cancel")
                            s()
                            print("1: Gain +1 DEF")
                            s()
                            print("2: Gain an item")
                            s()
                            print("3: Better Roll Next Turn-3MP")
                            s()
                            print("4: Heal 20 percent of max health-4MP")
                            s()
                            print("5: FireBall-5MP")
                            s()
                            print("6: Damage boost for every MP you have-2MP")
                            s()
                            magic_option=int(input("What would you like to do?: "))
                            print("")
                            s()
                            if P2MP < magic_option:
                                print("You don't have enough Mana")
                            elif P2MP >= magic_option:
                                if magic_option == 1:
                                    P2DEF=P2DEF+1
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    print("")
                                    print("Player 2 gained " + str(P2MPBON) + " MP back")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    print("Player 2 has " + str(P2MP) + " MP left")
                                    s()
                                elif magic_option==6:
                                    print("Player 2 used Damage boost")
                                    s()
                                    P2MP = P2MP - magic_option
                                    DMGBUFFP2=P2ATKBON+P2MP
                                    P2MP=0
                                    dmgp2 = dmgp2+1
                                    P2ATK=DMGBUFFP2 + P2ATK
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    print("")
                                    print("Player 2 gained " + str(P2MPBON) + " MP back")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    print("Player 2 has " + str(P2MP) + " MP left")
                                    s()
                                elif magic_option==3:
                                    print("Player 2 used Advantage")
                                    rolladp2=2
                                    rollp2=10
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    print("")
                                    print("Player 2 gained " + str(P2MPBON) + " MP back")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    print("Player 2 has " + str(P2MP) + " MP left")
                                    s()
                                    turn = 2
                                elif magic_option==5:
                                    print("Player 2 used fireball")
                                    s()
                                    fireballdmg = random.randint(12,18)
                                    print("Player 2 did " + str(fireballdmg) + " Damage to Player 1")
                                    s()
                                    P1HP=P1HP-fireballdmg
                                    print("Player 1 has " + str(P1HP) + " HP left")
                                    s()
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    print("")
                                    print("Player 2 gained " + str(P2MPBON) + " MP back")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    print("Player 2 has " + str(P2MP) + " MP left")
                                    s()
                                elif magic_option==4:
                                    print("Player 2 used heal")
                                    s()
                                    P2HP = P2HP + (P2MAXHP/5)
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    print("")
                                    print("Player 2 gained " + str(P2MPBON) + " MP back")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    print("Player 2 has " + str(P2MP) + " MP left")
                                    s()
                                    if P2MAXHP < P2HP:
                                        P2HP = P2MAXHP
                                elif magic_option==0:
                                    print("")
                                elif magic_option==2:
                                    print("Player 2 used gain a random item")
                                    s()
                                    P2MP = P2MP - magic_option
                                    itemspin=random.randint(1,100)
                                    print("You rolled a " + str(itemspin) + " ")
                                    s()
                                    if itemspin >= 1 and itemspin<= 5:
                                        print("Player 2 Conjured a rusty spoon")
                                        s()
                                        print("what a waste of a turn")
                                        s()
                                        p2spoons=p2spoons+1
                                    elif itemspin >= 6 and itemspin<= 49:
                                        print("You Conjured Throwing knives")
                                        s()
                                        p2knives=p2knives+3
                                    elif itemspin >= 50 and itemspin<= 99:
                                        print("Player 2 Conjured a healing potion")
                                        s()
                                        p2pots=p2pots+1
                                    
                                    elif itemspin == 100:
                                        print("Player 2 Conjured a...")
                                        s()
                                        s()
                                        s()
                                        s()
                                        s()
                                        print("wait what..")
                                        s()
                                        s()
                                        print("how... why!?!!?")
                                        s()
                                        print("why is the in the game (sigh)")
                                        s()
                                        s()
                                        print("i don't get paid enough for this")
                                        s()
                                        print("Player 2 Conjured a Glock-19")
                                        s()
                                        s()
                                        print("...This was not supposed to happen")
                                        s()
                                        print("")
                                        p2GLOCK19s=p2GLOCK19s+1
                                    else:
                                        print("THIS SHOULDN'T BE POSSIBLE HOW DID I MESS UP THIS BADLY")
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    print("")
                                    print("Player 2 gained " + str(P1MPBON) + " MP back")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    print("Player 2 has " + str(P2MP) + " MP left")
                                    s()
                                else:
                                    print("somthing went wrong please try again")
                                    s()
                            else:
                                print("try again")
                                s()
                        elif option == 4:        
                                print("Are you SURE you want to run away??")
                                s()
                                print("1: Yes")
                                s()
                                print("2: No")
                                s()
                                yesorno=int(input("select an answer: "))
                                s()
                                if yesorno==1:
                                    print("you forfiet the game and run away")
                                    s()
                                    print("Player 1 wins")
                                    crash=1
                                    while crash==1:
                                        escape=input(": ")
                                        if escape=="DEVUNLOCK":
                                            crash=2
                                            print("unlocked")
                                elif yesorno==2:
                                    print("")
                                else:
                                    print("")
                        elif option == 3:
                            pots=0
                            spoons=0
                            glocks=0
                            knives=0
                            if p2pots >= 1:
                                print("Player 2 has " + str(p2pots) + " Healing Potions left")
                                pots=1
                                s()
                            if p2spoons >=1:
                                spoons=1
                                print("Player 2 has " + str(p2spoons) + " Rusty spoons left")
                            if p2knives >1:
                                knives=1
                                print("Player 1 has " + str(p2knives) + " Knives left")
                            if p2GLOCK19s >=1:
                                print("THEY HAVE A GUNNN!!!!!!!!")
                                glocks=1
                            if pots==1:
                                print("1: Heal 5 Health")
                                s()
                            if spoons == 1:
                                print("2: Throw a Spoon")
                                s()
                            if glocks==1:
                                print("10: Shoot")
                                s()
                            if knives==1:
                                print("3: Throw a knife")
                            print("0: cancel")
                            s()
                            itemchoice=int(input("What would you like to do?: "))
                            s()
                            if itemchoice==1 and pots>=1:
                                print("Player 2 Heals 5 health")
                                s()
                                P2HP=P2HP+5
                                if P2MAXHP<=P2HP:
                                    P2HP=P2MAXHP
                                print("Player 2 has " + str(P2HP) + " HP")
                                s()
                                p2pots=p2pots-1
                            elif itemchoice==3 and knives>=1:
                                print("Player 2 threw a knife")
                                s()
                                knifedamage=random.randint(1,5)
                                P1HP=P1HP-knifedamage
                                print("Player 2 did " + str(knifedamage) + " Damage to Player 1")
                                s()
                                print("Player 1 has " + str(P1HP) + " HP left")
                                s()
                                p2knives=p2knives-1
                            elif itemchoice==2 and spoons>=1:
                                print("Player 2 threw a Spoon")
                                s()
                                spooncrit=random.randint(1,100)
                                if spooncrit>=1 and spooncrit<=70:
                                    print("the spoon gave Player 1 a small cut and did 1 damage")
                                    s()
                                    P1HP=P1HP-1
                                    print("Player 1 has " + str(P1HP) + " HP left")
                                    s()
                                elif spooncrit>=71 and spooncrit<=99:
                                    spoondamage=random.randint(2,10)
                                    print("the spoon gave Player 1 a cut and did " + str(spoondamage) + " Damge to Player 1")
                                    s()
                                    P1HP=P1HP-spoondamage
                                    print("Player 1 Has " + str(P1HP) + " HP left")
                                    s()
                                elif spooncrit==100:
                                    print("Player 2 threw the spoon and cut Player 1")
                                    s()
                                    print("Player 1 got tetanites and died")
                                    s()
                                    P2HP=0
                                elif itemchoice==0:
                                    print("")
                                else:
                                    print("please choose a valid number")
                            elif itemchoice==10 and glocks>=1:
                                print("player 1 was shot and died")
                                P1HP=0
                                print("stop gun voilence")
                            else:
                                print("Please use a valid number")
                        elif option==5:
                            print("You pass you're turn")
                            turn = 2
                            P1SPD = P1SPD + P1SPDBON
                            P2MP = P2MP + P2MPBON
                            print("")
                            print("Player 2 gained " + str(P2MPBON) + " MP back")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            print("Player 2 has " + str(P2MP) + " MP left")
                            s()
                        else:
                            print("please try again")
                            s()
                elif P1SPD == P2SPD:
                    print("you have the same speed")
                    s()
                    print("choosing a random player to go")
                    s()
                    a= random.randint(1,2)
                    if a==1:
                        P1SPD=P1SPD+1
                    else:
                        P2SPD=P2SPD+1
                else:
                    print("UH OH")
            print("")
            print("Player 1 HP left ",P1HP)
            s()
            print("Player 2 HP left ",P2HP)
        print("winner winner chicken dinner")
        s()
        print("")
        print("")
        print("")
        print("Play again?")
        s()
        print("1: Yes")
        s()
        print("2: No")
        s()
        playagain=int(input("Play again?: "))
print("OvO")
