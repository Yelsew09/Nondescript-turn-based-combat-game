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
#Player 1 selects a class
cc = 1
allcorrect = 1
while allcorrect == 1:
    while cc == 1:
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
            cc=2
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
            cc=2
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
            cc=2
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
            cc=2
        elif player1class == 5:
            player1class = "Sans"
            P1HP = 33
            P1MAXHP = P1HP
            P1ATK = 10
            P1ATKBON = 2
            P1DEF = 11
            P1MP = 15
            P1MPBON = 3
            P1MAXMP = P1MP
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
            P1MPBON = 4
            P1MAXMP = P1MP
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
            P1MPBON = .25
            P1MAXMP = P1MP
            P1SPD = 4
            P1SPDBON = 2
            cc=2
        else:
            print("Please give a valid number.")
    print("1: Yes")
    print("2: No")
    yesorno = int(input("You have chosen " + str(player1class) + ". Is this correct?: "))
    if yesorno == 1:
        print("Player 1 has chosen the " + str(player1class) + " class.")
        print("")
        ac=2
    elif yesorno == 2:
        print("repick your charcter.")
        cc=1
    else:
        print("Something went wrong please try again")
        cc=1
cc=1
allcorrect=1
#Player 2 selects a class
while allcorrect==1:
    while cc==1:
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
            cc=2
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
            cc=2
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
            cc=2
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
            cc=2
        elif player2class == 5:
            player2class = "Sans"
            P2HP = 33
            P2MAXHP = P2HP
            P2ATK = 10
            P2ATKBON = 2
            P2DEF = 11
            P2MP = 15
            P2MPBON = 3
            P2MAXMP = P2MP
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
            P2MPBON = 4
            P2MAXMP = P2MP
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
            P2MPBON= 0
            P2MAXMP = P2MP
            P2SPD= 4
            P2SPDBON = 2
            cc=2
        else:
            print("Please give a valid number.")
    print("1: Yes")
    print("2: No")
    yesorno = int(input("you have chosen " + str(player2class) + ". Is this correct?: "))
    if yesorno == 1:
        print("Player 2 has chosen the " + str(player2class) + " class.")
        print("")
        allcorrect=2
    elif yesorno == 2:
        print("repick your charcter.")
        cc=1
    else:
        print("please try again")
        cc=1
winner=1
roundnumber = 1  
DMGBUFFP1=0
DMGBUFFP2=0
dmgp1 = 1
dmgp2 = 1
print("Player 1 HP ",P1HP)
print("Player 2 HP ",P2HP)
print("")
#round start
print("Player 1 Speed ",P1SPD)
print("Player 2 Speed ",P2SPD )
while roundnumber < 10:
    turn = 1
    print("Round " + str(roundnumber) + " ")
    if P1HP <= 0:
        print("Player 2 wins the game")
        winner=player2class
        break
    elif P2HP <= 0:
        print("Player 1 wins the game")
        winner=player2class
        break
    else:
        print("")
        if P1SPD > P2SPD:
            print("Player 1's turn")
            print("Player 1 has "+ str(P1MP) +" MP left")
            print("do one of the following")
            print("1: Attack")
            print("2: Magic")
            print("3: Run Away")
            while turn == 1:
                option=int(input("what would player 1 like to do?: "))
                critnumber=random.randint(1,20)
                if option == 1 and critnumber==20:
                    print("")
                    print("Player 1 used Attack")
                    print("Its a Criticle hit!!!")
                    print("Player 1 did " + str(P1ATK*2) + "Damage to Player 2")
                    P2HP = P2HP-(P1ATK*2)
                    print("player 2 has " + str(P2HP) + " HP Left")
                    P2SPD = P2SPD + P2SPDBON
                    if dmgp1==2:
                        P1ATK==P1ATK-P1ATKBON
                        dmgp1=1
                    turn=2
                    P2SPD = P2SPD + P2SPDBON
                    roundnumber=roundnumber+1
                elif option == 1 and not critnumber==20:
                    print("Player 1 used Attack")
                    print("Player 1 did " + str(P1ATK) + " Damage to Player 2")
                    P2HP = P2HP-P1ATK
                    print("Player 2 has " + str(P2HP) + " HP left")
                    P2SPD = P2SPD + P2SPDBON
                    if dmgp1==2:
                        P1ATK==P1ATK-P1ATKBON
                    turn=2
                    P2SPD=P2SPD+P2SPDBON
                    roundnumber=roundnumber+1
                elif option == 2:
                    print("Please do one of the following")
                    print("1: Damage boost for one turn-2MP")
                    print("2: Gain advantage-3MP")
                    print("3: FireBall-5MP")
                    print("4: Heal 20% of max health-4MP")
                    print("5: Cancel")
                    magic_option=int(input("What would you like to do?: "))
                    if magic_option==1:
                        print("Player 1 used Damage boost")
                        DMGBUFFP1=P1ATKBON
                        dmgp1=2
                        turn = 2
                        P1ATK=DMGBUFFP1 + P1ATK
                        P2SPD=P2SPD+P2SPDBON
                    elif magic_option==2:
                        print("this feature is coming soon try again")
                        turn = 1
                    elif magic_option==3:
                        print("fireball")
                        turn = 2
                        P2SPD = P2SPD + P2SPDBON
                    elif magic_option==4:
                        print("heal")
                        turn = 2
                        P2SPD = P2SPD + P2SPDBON
                    elif magic_option==5:
                        print("")
                    else:
                        print("somthing went wrong please try again")
                elif option == 3:        
                        print("Are you SURE you want to run away??")
                        print("1: Yes")
                        print("2: No")
                        yesorno=int(input("select an answer: "))
                        if yesorno==1:
                            print("you forfiet the game and run away")
                            print("Player 2 wins")
                            break
                        elif yesorno==2:
                            print("")
                        else:
                            print("")
                else:
                    print("please try again")
        elif P1SPD < P2SPD:
            print("player 2's turn")
            print("player 2 has "+ str(P2MP) +" MP left")
            print("do one of the following")
            print("1: Attack")
            print("2: Magic")
            print("3: Run Away")
            while turn == 1:
                option=int(input("what would player 2 like to do?: "))
                critnumber=random.randint(1,20)
                if option == 1 and critnumber==20:
                    print("")
                    print("Player 2 used Attack")
                    print("Its a Criticle hit!!!")
                    print("Player 2 did " + str(P2ATK*2) + "Damage to Player 1")
                    P1HP = P1HP-(P2ATK*2)
                    print("player 1 has " + str(P1HP) + " HP Left")
                    P1SPD = P1SPD + P1SPDBON
                    if dmgp2==2:
                        P2ATK==P2ATK-P2ATKBON
                        dmgp2=1
                    turn=2
                    P1SPD = P1SPD + P1SPDBON
                    roundnumber=roundnumber+1
                elif option == 1 and not critnumber==20:
                    print("Player 2 used Attack")
                    print("Player 2 did " + str(P2ATK) + " Damage to Player 1")
                    P1HP = P1HP-P2ATK
                    print("Player 1 has " + str(P1HP) + " HP left")
                    P1SPD = P1SPD + P1SPDBON
                    if dmgp2==2:
                        P2ATK==P2ATK-P2ATKBON
                    turn=2
                    P1SPD=P1SPD+P1SPDBON
                    roundnumber=roundnumber+1
                elif option == 2:
                    print("Please do one of the following")
                    print("1: Damage boost for one turn-2MP")
                    print("2: Gain advantage-3MP")
                    print("3: FireBall-5MP")
                    print("4: Heal 20% of max health-4MP")
                    print("5: Cancel")
                    magic_option=int(input("What would you like to do?: "))
                    if magic_option==1:
                        print("Player 2 used Damage boost")
                        DMGBUFFP2=P1ATKBON
                        dmgp2=2
                        turn = 2
                        P2ATK=DMGBUFFP2 + P2ATK
                        P1SPD=P1SPD+P1SPDBON
                    elif magic_option==2:
                        print("this feature is coming soon try again")
                        turn = 1
                    elif magic_option==3:
                        print("fireball")
                        turn = 2
                        P2SPD = P2SPD + P2SPDBON
                    elif magic_option==4:
                        print("heal")
                        turn = 2
                        P1SPD = P1SPD + P1SPDBON
                    elif magic_option==5:
                        print("")
                    else:
                        print("somthing went wrong please try again")
                elif option == 3:        
                        print("Are you SURE you want to run away??")
                        print("1: Yes")
                        print("2: No")
                        yesorno=int(input("select an answer: "))
                        if yesorno==1:
                            print("you forfiet the game and run away")
                            print("Player 1 wins")
                            break
                        elif yesorno==2:
                            print("")
                        else:
                            print("")
                else:
                    print("please try again")
        elif P1SPD == P2SPD:
            print("you have the same speed")
            print("choosing a random player to go")
            a= random.randint(1,2)
            if a==1:
                P1SPD=P1SPD+1
            else:
                P2SPD=P2SPD+1
    print("")
    print("Player 1 HP left ",P1HP)
    print("Player 2 HP left ",P2HP)
print(winner," wins")