import random
import time
def s():
    time.sleep(.1)
print("Welcome to insert game title here")
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
print("5: Sans")
s()
print("6: Bard")
s()
print("7: Barbarain")
s()
#Player 1 selects a class
cc=1
allcorrect=1
while allcorrect==1:
    while cc==1:
        player1class = int(input("Choose a class from the list above (please choose a number): "))
        s()
        s()
        if player1class == 1:
            player1class = "Knight"
            P1HP = 42
            P1MAXHP = P1HP
            P1ATK = 12
            P1ATKBON = 2
            P1DEF = 14
            P1MP = 4
            P1MAXMP = P1MP
            P1MPBON = 1
            P1SPD = 3
            P1SPDBON = 2
            cc=2
        elif player1class == 2:
            player1class = "Peashooter"
            P1HP = 35
            P1MAXHP = P1HP
            P1ATK = 10
            P1ATKBON = 1
            P1DEF = 14
            P1MP = 5
            P1MAXMP = P1MP
            P1MPBON = 1
            P1SPD = 6
            P1SPDBON = 2
            cc=2
        elif player1class == 3:
            player1class = "Mage"
            P1HP = 29
            P1MAXHP = P1HP
            P1ATK = 7
            P1ATKBON = 2
            P1DEF = 10
            P1MP = 20
            P1MAXMP = P1MP
            P1MPBON = 5
            P1SPD = 2
            P1SPDBON = 2
            cc=2
        elif player1class == 4:
            player1class = "Rouge"
            P1HP = 31
            P1MAXHP = P1HP
            P1ATK = 13
            P1ATKBON = 4
            P1DEF = 14
            P1MP = 6
            P1MAXMP = P1MP
            P1MPBON = 1
            P1SPD = 7
            P1SPDBON = 3
            cc=2
        elif player1class == 5:
            player1class = "Sans"
            P1HP = 1
            P1MAXHP = P1HP
            P1ATK = 20
            P1ATKBON = 4
            P1DEF = 20
            P1MP = 15
            P1MAXMP = P1MP
            P1MPBON = 3
            P1SPD = 4
            P1SPDBON = 2
            cc=2
        elif player1class == 6:
            player1class = "Bard"
            P1HP = 37
            P1MAXHP = P1HP
            P1ATK = 7
            P1ATKBON = 1
            P1DEF = 13
            P1MP = 17
            P1MAXMP = P1MP
            P1MPBON = 4
            P1SPD = 5
            P1SPDBON = 2
            cc=2
        elif player1class == 7:
            player1class = "Barbarian"
            P1HP = 52
            P1MAXHP = P1HP
            P1ATK = 14
            P1ATKBON = 2
            P1DEF = 11
            P1MP = 2
            P1MAXMP = P1MP
            P1MPBON = .25
            P1SPD = 4
            P1SPDBON = 2
            cc=2
        else:
            print("Please give a valid number.")
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
    else:
        print("Something went wrong please try again")
        s()
        cc=1
cc=1
allcorrect=1
#Player 2 selects a class
while allcorrect==1:
    while cc==1:
        print("Please select a classs, player 2")
        s()
        player2class = int(input("Choose 1 from the list above (please choose a number): "))
        s()
        if player2class == 1:
            player2class = "Knight"
            P2HP = 42
            P2MAXHP = P2HP
            P2ATK = 12
            P2ATKBON = 2 
            P2DEF = 14
            P2MP = 4
            P2MAXMP = P2MP
            P2MPBON = 1
            P2SPD = 3
            P2SPDBON = 2
            cc=2
        elif player2class == 2:
            player2class = "Peashooter"
            P2HP = 35
            P2MAXHP = P2HP
            P2ATK = 10
            P2ATKBON = 1 
            P2DEF = 14
            P2MP = 5
            P2MAXMP = P2MP
            P2MPBON = 1
            P2SPD = 6
            P2SPDBON = 2
            cc=2
        elif player2class == 3:
            player2class = "Mage"
            P2HP = 29
            P2MAXHP = P2HP
            P2ATK = 7
            P2ATKBON = 2
            P2DEF = 10
            P2MP = 20
            P2MAXMP = P2MP
            P2MPBON = 5
            P2SPD = 2
            P2SPDBON = 2
            cc=2
        elif player2class == 4:
            player2class = "Rouge"
            P2HP = 31
            P2MAXHP = P2HP
            P2ATK = 13
            P2ATKBON = 4 
            P2DEF = 14
            P2MP = 6
            P2MAXMP = P2MP
            P2MPBON = 1
            P2SPD = 7
            P2SPDBON = 3
            cc=2
        elif player2class == 5:
            player2class = "Sans"
            P2HP = 1
            P2MAXHP = P2HP
            P2ATK = 20
            P2ATKBON = 4
            P2DEF = 20
            P2MP = 15
            P2MAXMP = P2MP
            P2MPBON = 3
            P2SPD = 4
            P2SPDBON = 2
            cc=2
        elif player2class == 6:
            player2class = "Bard"
            P2HP = 37
            P2MAXHP = P2HP
            P2ATK = 7
            P2ATKBON = 1
            P2DEF = 13
            P2MP = 17
            P2MAXMP = P2MP
            P2MPBON = 4
            P2SPD = 5
            P2SPDBON = 2
            cc=2
        elif player2class ==7:
            player2class = "Barbrian"
            P2HP= 52
            P2MAXHP = P2HP
            P2ATK= 14
            P2ATKBON= 2
            P2DEF= 11
            P2MP= 2
            P2MAXMP = P2MP
            P2MPBON= 0
            P2SPD= 4
            P2SPDBON = 2
            cc=2
        else:
            print("Please give a valid number.")
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
    else:
        print("please try again")
        s()
        cc=1
winner=1
roundnumber = 1  
DMGBUFFP1=0
DMGBUFFP2=0
dmgp1=1
dmgp2=1
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
            print("3: Run Away")
            s()
            while turn == 1:
                option=int(input("what would player 1 like to do?: "))
                s()
                critnumber=random.randint(1,20)
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
                    if dmgp1==2:
                        P1ATK==P1ATK-P1ATKBON
                        dmgp1=1
                    turn=2
                    P2SPD = P2SPD + P2SPDBON
                    roundnumber=roundnumber + 1
                    P1MP = P1MP + P1MPBON
                    print("")
                    print("Player 1 gained " + str(P1MPBON) + " MP back")
                    s()
                    if P1MAXMP < P1MP:
                        P1MP = P1MAXMP
                    print("Player 1 has " + str(P1MP) + " MP left") 
                    s()
                elif option == 1 and not critnumber==20:
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
                    if dmgp1==2:
                        P1ATK==P1ATK-P1ATKBON
                    turn=2
                    P2SPD=P2SPD+P2SPDBON
                    roundnumber=roundnumber+1
                    P1MP = P1MP + P1MPBON
                    print("")
                    print("Player 1 gained " + str(P1MPBON) + " MP back")
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
                    print("1: Gain +1 perma defence")
                    s()
                    print("2: Damage boost for one turn-2MP")
                    s()
                    print("3: Gain advantage-3MP")
                    s()
                    print("4: Heal 20 percent of max health-4MP")
                    s()
                    print("5: FireBall-5MP")
                    s()
                    magic_option=int(input("What would you like to do?: "))
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
                        elif magic_option==2:
                            print("Player 1 used Damage boost")
                            s()
                            DMGBUFFP1=P1ATKBON
                            dmgp1 = 2
                            P1ATK=DMGBUFFP1 + P1ATK
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
                        elif magic_option==3:
                            print("this feature is coming soon try again")
                            s()
                            turn = 1
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
                        else:
                            print("somthing went wrong please try again")
                            s()
                    else:
                        print("try again")
                        s()
                elif option == 3:        
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
                            break
                        elif yesorno==2:
                            print("")
                        else:
                            print("")
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
            print("3: Run Away")
            s()
            while turn == 1:
                option=int(input("what would player 2 like to do?: "))
                s()
                critnumber=random.randint(1,20)
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
                    print("player 2 has " + str(P1HP) + " HP Left")
                    s()
                    P1SPD = P1SPD + P1SPDBON
                    if dmgp2==2:
                        P2ATK==P2ATK-P2ATKBON
                        dmgp2=1
                    turn=2
                    P1SPD = P1SPD + P1SPDBON
                    roundnumber=roundnumber+1
                    P2MP = P2MP + P2MPBON
                    print("")
                    print("Player 2 gained " + str(P2MPBON) + " MP back")
                    s()
                    if P2MAXMP < P2MP:
                        P2MP = P2MAXMP
                    print("Player 2 has " + str(P2MP) + " MP left") 
                    s()
                elif option == 1 and not critnumber==20:
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
                    print("Player 2 has " + str(P1HP) + " HP left")
                    s()
                    P1SPD = P1SPD + P1SPDBON
                    if dmgp2==2:
                        P2ATK==P2ATK-P2ATKBON
                    turn=2
                    P1SPD=P1SPD+P1SPDBON
                    roundnumber=roundnumber+1
                    P2MP = P2MP + P2MPBON
                    print("")
                    print("Player 2 gained " + str(P2MPBON) + " MP back")
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
                    print("1: Gain +1 perma defence")
                    s()
                    print("2: Damage boost for one turn-2MP")
                    s()
                    print("3: Gain advantage-3MP")
                    s()
                    print("4: Heal 20 percent of max health-4MP")
                    s()
                    print("5: FireBall-5MP")
                    s()
                    magic_option=int(input("What would you like to do?: "))
                    s()
                    if P2MP < magic_option:
                        print("you dont have enough Mana")
                        s()
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
                        elif magic_option==2:
                            print("Player 2 used Damage boost")
                            s()
                            DMGBUFFP2=P2ATKBON
                            dmgp2 = 2
                            P2ATK=DMGBUFFP2 + P2ATK
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
                        elif magic_option==3:
                            print("this feature is coming soon try again")
                            s()
                            turn = 1
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
                        else:
                            print("somthing went wrong please try again")
                            s()
                    else:
                        print("try again")
                        s()
                elif option == 3:        
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
                            break
                        elif yesorno==2:
                            print("")
                        else:
                            print("")
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
    print("")
    print("Player 1 HP left ",P1HP)
    s()
    print("Player 2 HP left ",P2HP)
print(winner," wins")
