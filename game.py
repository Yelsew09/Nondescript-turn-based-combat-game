p1score=0
p2score=0
import random
import time
import sys, time
def q(str):
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(.02)
def s():
    time.sleep(.15)
game=1
while game==1:    
    q("\n")
    playagain=0
    q("Welcome to dungeons and damage\n")
    s()
    q("or the more commonly used name HELL\n")
    q("\n")
    s()
    q("1: Start\n")
    s()
    q("2: book\n")
    s()
    q("3: options\n")
    s()
    q("4: Exit\n")
    s()
    start=int(input("What would you like to do?: "))
    s()
    if start==1:
        q("1: PVP\n")
        s()
        q("2: PVC\n")
        s()
        q("3: Story\n")
        s()
        q("0: Back\n")
        s()
        start=int(input("what would you like to play: \n"))
        s()
        if start==1:
            playagain=1
        elif start==2:
            playagain=2
        elif start==3:
            q("1: solo\n")
            s()
            q("2: coop\n")
            s()
            q("0: back\n")
            start=int(input("What would you like to do?: \n"))
            if start==1:
                playagain=3
            elif start==2:
                playagain=4
            elif start==0:
                q("\n")
            else:
                q("wrong\n")
        elif start==0:
            q("\n")
        else:
            q("error\n")
    elif start==2:
        q("What would you like to know about?\n")
        s()
        q("1: How to play?\n")
        s()
        q("2: Characters\n")
        s()
        q("3: Attack System\n")
        s()
        q("4: Magic System\n")
        s()
        q("5: Item system\n")
        s()
        q("6: Other features\n")
        s()
        q("0: Back\n")
        s()
        q("\n")
        info=int(input("What would you like to do?: \n"))
        s()
        if info==1:
            q("You will start by selecting your charcters, once you have picked your charcter you will fight you can attack use magic use items forfiet or pass your turn when someone runs out of health the other player wins.\n")
            s()
            placeholder=input("Are you done reading\n")
            s()
        elif info==2:
            q("what would you like to know about the characters?\n")
            s()
            q("1: Stats\n")
            s()
            q("2: Backstories\n")
            s()
            q("0: Back\n")
            s()
            info=int(input("What would you like to do?: \n"))
            s()
            if info==1:
                q("Which Charcter's stats would you like to see\n")
                s()
                q("1: General\n")
                s()
                q("2: Knight\n")
                s()
                q("3: Peashooter\n")
                s()
                q("4: Mage\n")
                s()
                q("5: Rouge\n")
                s()
                q("6: Skele\n")
                s()
                q("7: Bard\n")
                s()
                q("8: Barbarain\n")
                s()
                q("9: Random system\n")
                s()
                q("0: Back\n")
                s()
                info=int(input("What would you like to know about?: \n"))
                if info==1: 
                    q("Every Charcter has 10 stats most are hidden the stats are\n")
                    q("1: HP\n")
                    q("2: MAXHP\n")
                    q("3: ATK\n")
                    q("4: ATKBON\n")
                    q("5: DEF\n")
                    q("6: MP\n")
                    q("7: MAXMP\n")
                    q("8: MPBON\n")
                    q("9: SPD\n")
                    q("10: SPDBON\n")
                    q("0: back\n")
                    info=int(input("What would you like to know about\n"))
                    if info==1:
                        q("A players Health\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==2:
                        q("A player max health\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==3:
                        q("How much damage they do per attack\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==4:
                        q("how much their attack is boosted with damage boost\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==5:
                        q("how much damage is reduced when being hit\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==6:
                        q("How much mana you have\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==7:
                        q("Your max amount of mana\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==8:
                        q("how much mana you gain back every turn\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==9:
                        q("to determin who goes first at the start of the game\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==10:
                        q("how much speed you gain every turn\n")
                        placeholder=input("Are you done reading\n")
                        s()
                    elif info==0:
                        q("\n")
                    else:
                        q("error\n")
                elif info==2:
                        q("Knights HP is 42\n")
                        q("knights max hp is 42\n")
                        q("the knight has an atk of 12\n")
                        q("the knights atk bon is 2\n")
                        q("the knights DEF is 14\n")
                        q("the knights MP is 4\n")
                        q("the knights max mp is 4\n")
                        q("the knights mp bon is 1\n")
                        q("the knights speed is 3\n")
                        q("the knights SPDBON is 2\n")
                        placeholder=input("Are you done reading\n")
                elif info==3:
                        q("peashooters HP is 35\n")
                        q("Peashooters max hp is 35\n")
                        q("Peashooters has an atk of 10\n")
                        q("Peashooters atk bon is 2\n")
                        q("Peashooters DEF is 14\n")
                        q("Peashooters MP is 5\n")
                        q("Peashooters max mp is 5\n")
                        q("Peashooters mp bon is 1\n")
                        q("Peashooters speed is 6\n")
                        q("Peashooters SPDBON is 2\n")
                        placeholder=input("Are you done reading\n")
                else:
                    q("coming soon\n")
            elif info==2:
                q("Which Charcter's would you like to know about\n")
                s()
                q("1: General\n")
                s()
                q("2: Knight\n")
                s()
                q("3: Peashooter\n")
                s()
                q("4: Mage\n")
                s()
                q("5: Rouge\n")
                s()
                q("6: Skele\n")
                s()
                q("7: Bard\n")
                s()
                q("8: Barbarain\n")
                s()
                q("0: Back\n")
                s()
                info=int(input("What would you like to know about?: \n"))
                if info==1:
                    q("They were taken to fight for all eternity they will never age eventually they will be numb to the pain of fighting day after day\n")
                    placeholder=input("Are you done reading\n")
                    s()
                elif info==2:
                    q("on his way to save a princess he was dragged into the arena to fight he weilds his sword with as much coarage as he can muster\n")
                    placeholder=input("Are you done reading\n")
                    s()
                elif info==3:
                    q("right before he was eaten by a zombie he was brought to the arena to fight a difrent enemy\n")
                    placeholder=input("Are you done reading\n")
                    s()
                elif info==4:
                    q("he was chilling in his tower when he was taken into the arena he holds his wand high and his hat higher\n")
                    placeholder=input("Are you done reading\n")
                    s()
                elif info==5:
                    q("after stealing from some children the rouge ran home but before they could put away their earnings they slipped into the void to never be seen again forced to fight in the arena for all eternity\n")
                    placeholder=input("Are you done reading\n")
                    s()
                elif info==6:
                    q("he was taking a nap in his grave but when he awoke he was no longer in his tomb he was in the arena\n")
                    placeholder=input("Are you done reading\n")
                    s()
                elif info==7:
                    q("after playing some music for the townsfolk they taken in the cover of the night into the arena\n")
                    placeholder=input("Are you done reading\n")
                    s()
                elif info==8:
                    q("he willingly went into the arena for he loved the thrill of the fight\n")
                    placeholder=input("Are you done reading\n")
                    s()
                    q("\n")
                else:
                    q("error\n")
            elif info==0:
                q("\n")
            else:
                q("try again\n")
                s()
        elif info==3:
            q("what would you like to know about attacking?\n")
            s()
            q("1: Damage system\n")
            s()
            q("2: Crit system\n")
            s()
            q("3: Damage boost\n")
            s()
            q("4: Advantage\n")
            s()
            q("0: Back\n")
            s()
            info=int(input("What would you like to do?: \n"))
            s()

        elif info==4:
            q("what would you like to know about magic?\n")
            s()
            q("1: MP system\n")
            s()
            q("2: Gain defense\n")
            s()
            q("3: Gain an item\n")
            s()
            q("4: Advantage\n")
            s()
            q("5: Heal\n")
            s()
            q("6: Fireball\n")
            s()
            q("7: Damage Boost\n")
            s()
            q("0: Back\n")
            s()
            info=int(input("What would you like to do?: \n"))
            s()
        elif info==5:
            q("What would you like to know about items?\n")
            s()
            q("1: item chances\n")
            s()
            q("2: Heal potion\n")
            s()
            q("3: Knives\n")
            s()
            q("4: Rusty spoon\n")
            s()
            q("0: Back\n")
            s()
            info=int(input("What would you like to do?: \n"))
            s()
        elif info==6:
            q("What would you like to know about other features\n")
            s()
            q("1: Healing\n")
            s()
            q("2: Speed\n")
            s()
            q("3: coming soon\n")
            s()
            q("0: Back\n")
            s()
            info=int(input("What would you like to do?: \n"))
            s()
        elif info==0:
            q("\n")
        else:
            q("ERROR\n")
    elif start==3:
        q("1: cheats\n")
        s()
        q("0: back\n")
        s()
        start=int(input("What would you like to do?: \n"))
        s()
        if start==1:
            q("1: On\n")
            s()
            q("2: Off\n")
            s()
            cheats=int(input("What do you want to do?\n"))
            s()
            if cheats==1:
                playagain=5
            elif cheats==2:
                playagain=0
        elif start==0:
            q("\n")
        else:
            q("1 or 0 next time\n")
    elif start==4:
        q("\n")
        s()
        playagain=0
        game=2
    while playagain==1:
        s()
        q("\n")
        s()
        q("Please select a class, player 1.\n")
        s()
        q("1: Knight\n")
        s()
        q("2: Peashooter\n")
        s()
        q("3: Mage\n")
        s()
        q("4: Rouge\n")
        s()
        q("5: Skele\n")
        s()
        q("6: Bard\n")
        s()
        q("7: Barbarain\n")
        s()
        q("8: Random\n")
        #Player 1 selects a class
        cc=1
        rc=1
        allcorrect=1
        while allcorrect==1:
            while cc==1:
                player1class = int(input("Choose a class from the list above (please choose a number): \n"))
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
                        P1SPD = 7
                        P1SPDBON = 2
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
                        P1MPBON = 3
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
                        P1MPBON = .5
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
                        q("Please give a valid number.\n")
                        cc=1
                        rc=1
                        s()
                q("1: Yes\n")
                s()
                q("2: No\n")
                s()
                yesorno = int(input("You have chosen " + str(player1class) + ". Is this correct?: \n"))
                s()
                if yesorno == 1:
                    q("Player 1 has chosen the " + str(player1class) + " class.\n")
                    s()
                    q("\n")
                    s()
                    allcorrect=2
                elif yesorno == 2:
                    q("repick your charcter.\n")
                    s()
                    cc=1
                    rc=1
                else:
                    q("Something went wrong please try again\n")
                    s()
                    cc=1
        cc=1
        rc=1
        allcorrect=1
        #Player 2 selects a class
        while allcorrect==1:
            while cc==1:
                q("Please select a classs, player 2\n")
                s()
                rc=1
                player2class = int(input("Choose 1 from the list above (please choose a number): \n"))
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
                        q("you have chosen random\n")
                        player2class=random.randint(1,7)
                        cc=2
                    else:
                        q("Next time put in a valid number \n")
                        s()
                q("1: Yes\n")
                s()
                q("2: No\n")
                s()
                yesorno = int(input("you have chosen " + str(player2class) + ". Is this correct?: \n"))
                s()
                if yesorno == 1:
                    q("Player 2 has chosen the " + str(player2class) + " class.\n")
                    s()
                    q("\n")
                    allcorrect=2
                elif yesorno == 2:
                    q("repick your charcter.\n")
                    s()
                    cc=1
                    rc=1
                else:
                    q("please try again\n")
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
            p1webs=0
            p2webs=0
            p1bandanas=0
            p2bandanas=0
            p1dictionarys=0
            p2dictionarys=0
            p1elmos=0
            p2elmos=0
            p1popbags=0
            p2popbags=0
            p1pop=0
            p2pop=0
        q("Player 1 HP " + str(P1HP) + "\n")
        s()
        q("Player 2 HP " + str(P2HP) + "\n")
        s()
        q("\n")
        q("Player 1 Speed " + str(P1SPD) + "\n")
        s()
        q("Player 2 Speed " + str(P2SPD) + "\n")
        s()
        while roundnumber < 100:
            turn=1
            q("Round " + str(roundnumber) + " \n")
            s()
            if P1HP <= 0:
                q("Player 2 wins the game\n")
                s()
                winner=player2class
                p2score=p2score+1
                break
            elif P2HP <= 0:
                q("Player 1 wins the game\n")
                s()
                winner=player1class
                p1score=p1score+1
                break
            else:
                q("\n")
                if P1SPD > P2SPD:
                    q("player 1's turn\n")
                    s()
                    q("player 1 has "+ str(P1MP) +" MP left\n")
                    s()
                    q("do one of the following\n")
                    s()
                    q("1: Attack\n")
                    s()
                    q("2: Magic\n")
                    s()
                    q("3: Use an item\n")
                    s()
                    q("4: Run Away\n")
                    s()
                    q("5: pass turn\n")
                    while turn == 1:
                        option=int(input("what would player 1 like to do?: \n"))
                        q("\n")
                        s()
                        critnumber=random.randint(rollp1,20)
                        if option == 1 and critnumber==20:
                            q("\n")
                            q("Player 1 used Attack\n")
                            s()
                            q("Player 1 Rolled a ",critnumber)
                            s()
                            q("Its a Criticle hit!!!\n")
                            s()
                            TOTDMG = (critnumber+(P1ATK*2))-P2DEF
                            if TOTDMG < 0:
                                TOTDMG = 0
                            q("Player 1 did " + str(TOTDMG) + " Damage to Player 2\n")
                            s()
                            P2HP = P2HP-TOTDMG
                            q("player 2 has " + str(P2HP) + " HP Left\n")
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
                            q("\n")
                            q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber<20 and critnumber>=2:
                            q("Player 1 used Attack\n")
                            s()
                            q("Player 1 Rolled a ",critnumber)
                            s()
                            TOTDMG = (critnumber+(P1ATK))-P2DEF
                            if TOTDMG < 0:
                                TOTDMG = 0
                            q("Player 1 did " + str(TOTDMG) + " Damage to Player 2\n")
                            s()
                            P2HP = P2HP-TOTDMG
                            q("Player 2 has " + str(P2HP) + " HP left\n")
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
                            q("\n")
                            q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber == 1:
                            q("Player 1 used Attack\n")
                            s()
                            q("Player 1 Rolled a 1\n")
                            s()
                            q("Player 1 missed\n")
                            s()
                            q("Player 1 did 0 Damage to Player 2\n")
                            s()
                            q("Player 2 has " + str(P2HP) + " HP left\n")
                            s()
                            P2SPD = P2SPD + P2SPDBON
                            if dmgp1 >= 2:
                                P1ATK=P1ATK-DMGBUFFP1
                                dmgp1 = dmgp1-1
                            turn=2
                            roundnumber=roundnumber+1
                            P1MP = P1MP + P1MPBON
                            q("\n")
                            q("Player 1 gained "+ str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        elif option == 2:
                            q("Please do one of the following\n")
                            s()
                            q("0: Cancel\n")
                            s()
                            q("1: Gain +1 DEF\n")
                            s()
                            q("2: Gain an item\n")
                            s()
                            q("3: Better Roll Next Turn-3MP\n")
                            s()
                            q("4: Heal 20 percent of max health-4MP\n")
                            s()
                            q("5: FireBall-5MP\n")
                            s()
                            q("6: Damage boost for every MP you have-2MP\n")
                            s()
                            magic_option=int(input("What would you like to do?: \n"))
                            q("\n")
                            s()
                            if P1MP < magic_option:
                                q("you dont have enough Mana\n")
                                s()
                            elif P1MP >= magic_option:
                                if magic_option == 1:
                                    P1DEF=P1DEF+1
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                elif magic_option==6:
                                    q("Player 1 used Damage boost\n")
                                    s()
                                    P1MP = P1MP - magic_option
                                    DMGBUFFP1=P1ATKBON+P1MP
                                    P1MP=0
                                    dmgp1 = dmgp1+1
                                    P1ATK=DMGBUFFP1 + P1ATK
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                elif magic_option==3:
                                    q("Player 1 used Advantage\n")
                                    rolladp1=2
                                    rollp1=10
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                    turn = 2
                                elif magic_option==5:
                                    q("Player 1 used fireball\n")
                                    s()
                                    fireballdmg = random.randint(12,18)
                                    q("Player 1 did " + str(fireballdmg) + " Damage to Player 2\n")
                                    s()
                                    P2HP=P2HP-fireballdmg
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                elif magic_option==4:
                                    q("Player 1 used heal\n")
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
                                    q("\n")
                                elif magic_option==2:
                                    """
                                            pair of tongs- steal an item from enemy:
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
                                    q("Player 1 used gain a random item\n")
                                    s()
                                    P1MP = P1MP - magic_option
                                    bestitem=291
                                    itemspin=random.randint(1,bestitem)
                                    q("You rolled a " + str(itemspin) + " \n")
                                    s()
                                    if itemspin >= 1 and itemspin<= 20:
                                        q("Player 1 Conjured a rusty spoon\n")
                                        s()
                                        q("what a waste of a turn\n")
                                        s()
                                        p1spoons=p1spoons+1
                                    elif itemspin >= 21 and itemspin<= 40:
                                        q("You Conjured Throwing knives\n")
                                        s()
                                        p1knives=p1knives+3
                                    elif itemspin >= 41 and itemspin<= 60:
                                        q("Player 1 Conjured a healing potion\n")
                                        s()
                                        p1pots=p1pots+1
                                    elif itemspin >=61 and itemspin<=80:
                                        arrow=random.randint(2,4)
                                        if p1bows>=1:
                                            q("Player 1 conjured " + str(arrow) + " arrows\n")
                                        elif p1bows==0:
                                            q("player 1 conjured a bow and arrow\n")
                                            s()
                                            p1bows = p1bows + 1
                                            p1arrows=p1arrows+1
                                        else:
                                            q("ERROR\n")
                                    elif itemspin >=81 and itemspin <=90:
                                        q("Player 1 Conjured a fancy hat\n")
                                        s()
                                        p1hats=p1hats+1
                                    elif itemspin >= 91 and itemspin<= 110:
                                        q("Player 1 Conjured a mana potion\n")
                                        s()
                                        p1mpots=p1mpots+1
                                    elif itemspin >= 111 and itemspin<= 130:
                                        q("Player 1 Conjured a sheild\n")
                                        s()
                                        p1sheilds=p1sheilds+1
                                    elif itemspin >= 131 and itemspin<= 150:
                                        q("Player 1 Conjured a pair of new sneakers\n")
                                        s()
                                        p1shoes=p1shoes+1
                                    elif itemspin >= 151 and itemspin<= 170:
                                        q("Player 1 Conjured a...\n")
                                        s()
                                        q("a avocado\n")
                                        s()
                                        p1avocado=p1avocado+1
                                    elif itemspin >= 171 and itemspin<= 190:
                                        q("Player 1 Conjured a can of whipped cream\n")
                                        s()                                        
                                        p1creams=p1creams+1
                                    elif itemspin >= 191 and itemspin<= 210:
                                        q("Player 1 Conjured a spiderweb\n")
                                        s()                                        
                                        p1webs=p1webs+1
                                    elif itemspin >= 211 and itemspin<= 230:
                                        q("Player 1 Conjured a dictionary\n")
                                        s()                                        
                                        p1dictionarys=p1dictionarys+1
                                    elif itemspin >= 231 and itemspin<= 250:
                                        q("Player 1 Conjured a bandana\n")
                                        s()                                        
                                        p1bandanas=p1bandanas+1 
                                    elif itemspin >= 251 and itemspin<= 270:
                                        q("Player 1 Conjured a elmo\n")
                                        s()
                                        p1elmos=p1elmos+1
                                    elif itemspin >= 271 and itemspin<= 290:
                                        q("Player 1 Conjured a bag of popcorn\n")
                                        s()                                        
                                        p1popbags=p1popbags+1
                                    elif itemspin == bestitem:
                                        q("Player 1 Conjured a...\n")
                                        s()
                                        s()
                                        s()
                                        s()
                                        s()
                                        q("wait what..\n")
                                        s()
                                        s()
                                        q("how... why!?!!?\n")
                                        s()
                                        q("why is the in the game (sigh)\n")
                                        s()
                                        s()
                                        q("i don't get paid enough for this\n")
                                        s()
                                        q("Player 1 Conjured a Glock-19\n")
                                        s()
                                        s()
                                        q("...This was not supposed to happen\n")
                                        s()
                                        q("\n")
                                        p1GLOCK19s=p1GLOCK19s+1
                                    else:
                                        q("THIS SHOULDN'T BE POSSIBLE HOW DID I MESS UP THIS BADLY\n")
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                else:
                                    q("somthing went wrong please try again\n")
                                    s()
                            else:
                                q("try again\n")
                                s()
                        elif option == 4:        
                                q("Are you SURE you want to run away??\n")
                                s()
                                q("1: Yes\n")
                                s()
                                q("2: No\n")
                                s()
                                yesorno=int(input("select an answer: \n"))
                                s()
                                if yesorno==1:
                                    q("you forfiet the game and run away\n")
                                    s()
                                    q("Player 2 wins\n")
                                    s()
                                    P1HP=0
                                    break
                                elif yesorno==2:
                                    q("\n")
                                else:
                                    q("\n")
                        elif option == 3:
                            glocks=0
                            q("Player 1 has " + str(p1pots) + " Healing Potions left\n")
                            s()
                            q("Player 1 has " + str(p1spoons) + " Rusty spoons left\n")
                            s()
                            if p1GLOCK19s>=1:
                                q("THEY HAVE A GUNNN!!!!!!!!\n")
                                s()
                                glocks=1
                            q("Player 1 has " + str(p1knives) + " Knives left\n")
                            s()
                            if p1bows==1:
                                q("Player 1 has a bow and has " + str(p1arrows) + " arrows left\n")
                                s()
                            elif p1bows==0:
                                q("player 1 doesnt have a bow and has " + str(p1arrows) + " arrows left\n")
                            q("player 1 has " + str(p1hats) + " Fancy hats left\n")   
                            s()
                            q("Player 1 has " + str(p1mpots) + " Mana potions left\n")
                            s()
                            q("player 1 had " + str(p1sheilds) + " sheilds left\n")
                            s()
                            q("player 1 has " + str(p1shoes) + " pairs of sneaker left\n")
                            s()
                            q("player 1 has " + str(p1avocado) + " avocado's left\n")
                            s()
                            q("player 1 has " + str(p1pits) + " Pits left\n")
                            s()
                            q("player 1 has " + str(p1creams) + " Cans of whipped cream left\n")
                            s()
                            q("player 1 has " + str(p1webs) + " webs of the spider left\n")
                            s()
                            q("player 1 has " + str(p1dictionarys) + " dictionarys left\n")
                            s()
                            q("player 1 has " + str(p1elmos) + " talking elmos left\n")
                            s()
                            q("Player 1 has " + str(p1popbags) + " popcorn bags left\n")
                            s()
                            q("player 1 has " + str(p1pop) + " peices of popcorn left\n")



                            q("\n")
                            q("1: Use healing potion\n")
                            s()
                            q("2: Throw a rusty spoon\n")
                            s()
                            q("3: Throw a throwing knife\n")
                            s()
                            q("4: shoot an arrow\n")
                            s()
                            q("5: Use a mana potion\n")
                            s()
                            q("6: use the sheild\n")
                            s()
                            q("7: wear a fancy hat\n")
                            s()
                            q("8: wear sneakers\n")
                            s()
                            q("9: eat avocado\n")
                            s()
                            q("10: throw pit\n")
                            s()
                            q("11: eat whipped cream\n")
                            s()
                            q("12: shoot web\n")
                            s()
                            q("13: wear bandana\n")
                            s()
                            q("14: read the dictionary\n")
                            s()
                            q("15: use elmo\n")
                            s()
                            q("16: pop the pocorn bag\n")
                            s()
                            q("17: eat popcorn\n")
                            s()
                            q("0: cancel\n")
                            if glocks==1:
                                q("100000: Shoot\n")
                                s()
                            itemss=1
                            firsttime=1
                            while itemss>=1:
                                if firsttime==2:
                                    glocks=0
                                    q("Player 1 has " + str(p1pots) + " Healing Potions left\n")
                                    s()
                                    q("Player 1 has " + str(p1spoons) + " Rusty spoons left\n")
                                    s()
                                    if p1GLOCK19s>=1:
                                        q("THEY HAVE A GUNNN!!!!!!!!\n")
                                        s()
                                        glocks=1
                                    q("Player 1 has " + str(p1knives) + " Knives left\n")
                                    s()
                                    if p1bows==1:
                                        q("Player 1 has a bow and has " + str(p1arrows) + " arrows left\n")
                                        s()
                                    elif p1bows==0:
                                        q("player 1 doesnt have a bow and has " + str(p1arrows) + " arrows left\n")
                                    q("player 1 has " + str(p1hats) + " Fancy hats left\n")   
                                    s()
                                    q("Player 1 has " + str(p1mpots) + " Mana potions left\n")
                                    s()
                                    q("player 1 had " + str(p1sheilds) + " sheilds left\n")
                                    s()
                                    q("player 1 has " + str(p1shoes) + " pairs of sneaker left\n")
                                    s()
                                    q("player 1 has " + str(p1avocado) + " avocado's left\n")
                                    s()
                                    q("player 1 has " + str(p1pits) + " Pits left\n")
                                    s()
                                    q("player 1 has " + str(p1creams) + " Cans of whipped cream left\n")
                                    s()
                                    q("player 1 has " + str(p1webs) + " webs of the spider left\n")
                                    s()
                                    q("player 1 has " + str(p1dictionarys) + " dictionarys left\n")
                                    s()
                                    q("player 1 has " + str(p1elmos) + " talking elmos left\n")
                                    s()
                                    q("Player 1 has " + str(p1popbags) + " popcorn bags left\n")
                                    s()
                                    q("player 1 has " + str(p1pop) + " peices of popcorn left\n")
                                s()
                                itemchoice=int(input("What would you like to do?: \n"))
                                s()
                                if itemchoice==1 and p1pots >= 1:
                                    q("Player 1 Heals 5 health\n")
                                    s()
                                    P1HP=P1HP+5
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1pots=p1pots-1
                                elif itemchoice==3 and p1knives>=1:
                                    q("Player 1 threw a knife\n")
                                    s()
                                    knifedamage=random.randint(1,5)
                                    P2HP=P2HP-knifedamage
                                    q("Player 1 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    p1knives=p1knives-1
                                elif itemchoice==2 and p1spoons>=1:
                                    q("Player 1 threw a Spoon\n")
                                    s()
                                    spooncrit=random.randint(1,100)
                                    if spooncrit>=1 and spooncrit<=70:
                                        q("the spoon gave Player 2 a small cut and did 1 damage\n")
                                        s()
                                        P2HP=P2HP-1
                                        q("Player 2 has " + str(P2HP) + " HP left\n")
                                        s()
                                    elif spooncrit>=71 and spooncrit<=99:
                                        spoondamage=random.randint(2,10)
                                        q("the spoon gave Player 2 a cut and did " + str(spoondamage) + " Damge to Player 2\n")
                                        s()
                                        P2HP=P2HP-spoondamage
                                        q("Player 2 Has " + str(P2HP) + " HP left\n")
                                        s()
                                    elif spooncrit==100:
                                        q("Player 1 threw the spoon and cut Player 2\n")
                                        s()
                                        q("Player 2 got tetanites and died\n")
                                        s()
                                        P2HP=0
                                    else:
                                        q("ERROR ERROR\n")
                                    p1spoons=p1spoons-1
                                elif itemchoice==100000 and p1GLOCK19s>=1:
                                    q("player 2 was shot and died\n")
                                    P2HP=0
                                    q("stop gun voilence\n")
                                elif itemchoice==0:
                                    q("\n")
                                    itemss=0
                                elif itemchoice==4 and p1bows==1 and p1arrows>=1:
                                    arrowdamage=random.randint(2,5)
                                    P2HP=P2HP-arrowdamage
                                    q("You shot an arrow at player 2 doing " + str(arrowdamage) + " damage to Player 2, Player 2 has " + str(P2HP) + " HP left\n")
                                    p1arrows=p1arrows-1
                                    bbreak=random.randint(1,50)
                                    if bbreak==50:
                                        p1bows=0
                                        q("your bow broke\n")
                                elif itemchoice==5 and p1mpots >= 1:
                                    q("Player 1 regains 5 mana\n")
                                    s()
                                    P1MP=P1MP+5
                                    if P1MAXMP<=P1MP:
                                        P1MP=P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP\n")
                                    s()
                                    p1mpots=p1mpots-1
                                elif itemchoice==6 and p1sheilds >= 1:
                                    q("Player 1 sheilds themself and gains 2 def\n")
                                    s()
                                    P1DEF=P1DEF+2
                                    p1sheilds=p1sheilds-1
                                elif itemchoice==7 and p1hats >= 1:
                                    q("Player 1 wears the fancy hat and their max health goes up by 5 and they regain all missing health\n")
                                    s()
                                    P1MAXHP=P1MAXHP+5
                                    P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1hats=p1hats-1
                                elif itemchoice==8 and p1shoes >= 1:
                                    q("Player 1 wears the pair of sneaker and their Speed goes up by 5 and increase Speed bon by 1\n")
                                    s()
                                    P1SPD=P1SPD+5
                                    P1SPDBON=P1SPDBON+.5
                                    s()
                                    p1shoes=p1shoes-1
                                elif itemchoice==9 and p1avocado >= 1:
                                    q("Player 1 Heals 3 health\n")
                                    s()
                                    P1HP=P1HP+3
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1pits=p1pits+1
                                    p1avocado=p1avocado-1
                                elif itemchoice==10 and p1pits>=1:
                                    q("Player 1 threw a pit\n")
                                    s()
                                    knifedamage=random.randint(1,3)
                                    P2HP=P2HP-knifedamage
                                    q("Player 1 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    p1pits=p1pits-1
                                elif itemchoice==11 and p1creams >= 1:
                                    c02pois=random.randint(1,10)
                                    if c02pois==10:
                                        q("player 1 died to carbon dioxide poisening\n")
                                        P1HP=0
                                        break
                                    elif c02pois!=10:
                                        q("Player 1 Heals 5 health and gains 1 Speed\n")
                                        s()
                                        P1HP=P1HP+5
                                        if P1MAXHP<=P1HP:
                                            P1HP=P1MAXHP
                                        q("Player 1 has " + str(P1HP) + " HP\n")
                                        s()
                                        P1SPD=P1SPD+1
                                        p1creams=p1creams-1
                                elif itemchoice==12 and p1webs >= 1:
                                    q("Player 1 shoots a web and slows down player 2\n")
                                    s()
                                    webslow=random.randint(1,8)
                                    P2SPD=P2SPD-webslow
                                    q("player 2 is " + str(webslow) + " speed slower now\n")
                                    s()
                                    p1webs=p1webs-1
                                elif itemchoice==13 and p1bandanas >= 1:
                                    q("Player 1 wears the drippy bandana and gains 1 defense and player 2's atk goes down by 1\n")
                                    s()
                                    P1DEF=P1DEF+1
                                    P2ATK=P2ATK-1
                                    p1bandanas=p1bandanas-1
                                elif itemchoice==14 and p1dictionarys >= 1:
                                    q("Player 1 reads a dictionary and understands a bit more. +1 to max mp\n")
                                    s()
                                    P1MAXMP=P1MAXMP+1
                                    p1dictionarys=p1dictionarys-1
                                elif itemchoice==15 and p1elmos >= 1:
                                    q("Player 1 uses talking elmo\n")
                                    s()
                                    P2MAXMP=P2MAXMP-1
                                    q("player 2 lost 1 max health due to the mental damage\n")
                                    s()
                                    p1elmos=p1elmos-1
                                elif itemchoice==16 and p1popbags >= 1 and P1MP>=3:
                                    q("Player 1 uses 3 mana to heat up some popcorn\n")
                                    s()
                                    P1MP=P1MP-3
                                    popcorn=random.randint(1,20)
                                    p1pop=p1pop+popcorn
                                    p1popbags=p1popbags-1
                                elif itemchoice==16 and p1popbags >=1 and P1MP<3:
                                    q("you dont enough mana to pop this bag\n")
                                    s()
                                elif itemchoice==17 and p1pop >= 1:
                                    eat=int(input("how many peices of popcorn would you like to eat?\n"))
                                    popcorn=random.randint(1,2)
                                    popcorn=popcorn*eat
                                    q("Player 1 Heals " + str(popcorn) + " health\n")
                                    s()
                                    P1HP=P1HP+popcorn
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1pop=p1pop-eat
                                else:
                                    q("you either didnt have the item or you typed in a unavalible number either way your an idiot\n")
                                    s()
                                firsttime=firsttime+1

                        elif option==5:
                            q("You pass you're turn\n")
                            turn = 2
                            P2SPD = P2SPD + P2SPDBON
                            P1MP = P1MP + P1MPBON
                            q("\n")
                            q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        else:
                            q("please try again\n")
                            s()
                elif P1SPD < P2SPD:
                    q("player 2's turn\n")
                    s()
                    q("player 2 has "+ str(P2MP) +" MP left\n")
                    s()
                    q("do one of the following\n")
                    s()
                    q("1: Attack\n")
                    s()
                    q("2: Magic\n")
                    s()
                    q("3: Use an item\n")
                    s()
                    q("4: Run Away\n")
                    s()
                    q("5: pass turn\n")
                    while turn == 1:
                        option=int(input("what would player 2 like to do?: \n"))
                        q("\n")
                        s()
                        critnumber=random.randint(rollp2,20)
                        if option == 1 and critnumber==20:
                            q("\n")
                            q("Player 2 used Attack\n")
                            s()
                            q("Player 2 Rolled a ",critnumber)
                            s()
                            q("Its a Criticle hit!!!\n")
                            s()
                            TOTDMG= (critnumber+(P2ATK*2))-P1DEF
                            if TOTDMG < 0:
                                TOTDMG=0
                            q("Player 2 did " + str(TOTDMG) + " Damage to Player 1\n")
                            s()
                            P1HP = P1HP-TOTDMG
                            q("player 1 has " + str(P1HP) + " HP Left\n")
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
                            q("\n")
                            q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber<20 and critnumber>=2:
                            q("Player 2 used Attack\n")
                            s()
                            q("Player 2 Rolled a "+str(critnumber)+"\n")
                            s()
                            TOTDMG= (critnumber+P2ATK)-P1DEF
                            if TOTDMG < 0:
                                TOTDMG=0
                            q("Player 2 did " + str(TOTDMG) + " Damage to Player 1\n")
                            s()
                            P1HP = P1HP-TOTDMG
                            q("Player 1 has " + str(P1HP) + " HP left\n")
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
                            q("\n")
                            q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber==1:
                            q("Player 2 used Attack\n")
                            s()
                            q("Player 2 Rolled a 1\n")
                            s()
                            q("Player 2 missed\n")
                            s()
                            q("Player 2 did 0 Damage to Player 1\n")
                            s()
                            q("Player 1 has " + str(P1HP) + " HP left\n")
                            s()
                            P1SPD = P1SPD + P1SPDBON
                            if dmgp2 >= 2:
                                P2ATK==P2ATK-DMGBUFFP2
                                dmgp2=dmgp2-1
                            turn=2
                            roundnumber=roundnumber+1
                            P2MP = P2MP + P2MPBON
                            q("\n")
                            q("Player 2 gained "+ str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        elif option == 2:
                            q("Please do one of the following\n")
                            s()
                            q("0: Cancel\n")
                            s()
                            q("1: Gain +1 DEF\n")
                            s()
                            q("2: Gain an item\n")
                            s()
                            q("3: Better Roll Next Turn-3MP\n")
                            s()
                            q("4: Heal 20 percent of max health-4MP\n")
                            s()
                            q("5: FireBall-5MP\n")
                            s()
                            q("6: Damage boost for every MP you have-2MP\n")
                            s()
                            magic_option=int(input("What would you like to do?: \n"))
                            q("\n")
                            s()
                            if P2MP < magic_option:
                                q("You don't have enough Mana\n")
                            elif P2MP >= magic_option:
                                if magic_option == 1:
                                    P2DEF=P2DEF+1
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                elif magic_option==6:
                                    q("Player 2 used Damage boost\n")
                                    s()
                                    P2MP = P2MP - magic_option
                                    DMGBUFFP2=P2ATKBON+P2MP
                                    P2MP=0
                                    dmgp2 = dmgp2+1
                                    P2ATK=DMGBUFFP2 + P2ATK
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                elif magic_option==3:
                                    q("Player 2 used Advantage\n")
                                    rolladp2=2
                                    rollp2=10
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                    turn = 2
                                elif magic_option==5:
                                    q("Player 2 used fireball\n")
                                    s()
                                    fireballdmg = random.randint(12,18)
                                    q("Player 2 did " + str(fireballdmg) + " Damage to Player 1\n")
                                    s()
                                    P1HP=P1HP-fireballdmg
                                    q("Player 1 has " + str(P1HP) + " HP left\n")
                                    s()
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                elif magic_option==4:
                                    q("Player 2 used heal\n")
                                    s()
                                    P2HP = P2HP + (P2MAXHP/5)
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                    if P2MAXHP < P2HP:
                                        P2HP = P2MAXHP
                                elif magic_option==0:
                                    q("\n")
                                elif magic_option==2:
                                    q("Player 2 used gain a random item\n")
                                    s()
                                    P2MP = P2MP - magic_option
                                    bestitem=291
                                    itemspin=random.randint(1,bestitem)
                                    q("You rolled a " + str(itemspin) + " \n")
                                    s()
                                    if itemspin >= 1 and itemspin<= 20:
                                        q("Player 2 Conjured a rusty spoon\n")
                                        s()
                                        q("what a waste of a turn\n")
                                        s()
                                        p2spoons=p2spoons+1
                                    elif itemspin >= 21 and itemspin<= 40:
                                        q("You Conjured Throwing knives\n")
                                        s()
                                        p2knives=p2knives+3
                                    elif itemspin >= 41 and itemspin<= 60:
                                        q("Player 2 Conjured a healing potion\n")
                                        s()
                                        p2pots=p2pots+1
                                    elif itemspin >=61 and itemspin<=80:
                                        arrow=random.randint(2,4)
                                        if p2bows>=1:
                                            q("Player 2 conjured " + str(arrow) + " arrows\n")
                                        elif p2bows==0:
                                            q("player 2 conjured a bow and arrow\n")
                                            s()
                                            p2bows = p2bows + 1
                                            p2arrows=p2arrows+1
                                        else:
                                            q("ERROR\n")
                                    elif itemspin >=81 and itemspin <=90:
                                        q("Player 2 Conjured a fancy hat\n")
                                        s()
                                        p2hats=p2hats+1
                                    elif itemspin >= 91 and itemspin<= 110:
                                        q("Player 2 Conjured a mana potion\n")
                                        s()
                                        p2mpots=p2mpots+1
                                    elif itemspin >= 111 and itemspin<= 130:
                                        q("Player 2 Conjured a sheild\n")
                                        s()
                                        p2sheilds=p2sheilds+1
                                    elif itemspin >= 131 and itemspin<= 150:
                                        q("Player 2 Conjured a pair of new sneakers\n")
                                        s()
                                        p2shoes=p2shoes+1
                                    elif itemspin >= 151 and itemspin<= 170:
                                        q("Player 2 Conjured a...\n")
                                        s()
                                        q("a avocado\n")
                                        s()
                                        p2avocado=p2avocado+1
                                    elif itemspin >= 171 and itemspin<= 190:
                                        q("Player 2 Conjured a can of whipped cream\n")
                                        s()                                        
                                        p2creams=p2creams+1
                                    elif itemspin >= 191 and itemspin<= 210:
                                        q("Player 2 Conjured a spiderweb\n")
                                        s()                                        
                                        p2webs=p2webs+1
                                    elif itemspin >= 211 and itemspin<= 230:
                                        q("Player 2 Conjured a dictionary\n")
                                        s()                                        
                                        p2dictionarys=p2dictionarys+1
                                    elif itemspin >= 231 and itemspin<= 250:
                                        q("Player 2 Conjured a bandana\n")
                                        s()                                        
                                        p2bandanas=p2bandanas+1 
                                    elif itemspin >= 251 and itemspin<= 270:
                                        q("Player 2 Conjured a elmo\n")
                                        s()
                                        p2elmos=p2elmos+1
                                    elif itemspin >= 271 and itemspin<= 290:
                                        q("Player 2 Conjured a bag of popcorn\n")
                                        s()                                        
                                        p2popbags=p2popbags+1
                                    elif itemspin == bestitem:
                                        q("Player 2 Conjured a...\n")
                                        s()
                                        s()
                                        s()
                                        s()
                                        s()
                                        q("wait what..\n")
                                        s()
                                        s()
                                        q("how... why!?!!?\n")
                                        s()
                                        q("why is the in the game (sigh)\n")
                                        s()
                                        s()
                                        q("i don't get paid enough for this\n")
                                        s()
                                        q("Player 1 Conjured a Glock-19\n")
                                        s()
                                        s()
                                        q("...This was not supposed to happen\n")
                                        s()
                                        q("\n")
                                        p2GLOCK19s=p2GLOCK19s+1
                                    else:
                                        q("THIS SHOULDN'T BE POSSIBLE HOW DID I MESS UP THIS BADLY\n")
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                else:
                                    q("somthing went wrong please try again\n")
                                    s()
                            else:
                                q("try again\n")
                                s()
                        elif option == 4:        
                                q("Are you SURE you want to run away??\n")
                                s()
                                q("1: Yes\n")
                                s()
                                q("2: No\n")
                                s()
                                yesorno=int(input("select an answer: \n"))
                                s()
                                if yesorno==1:
                                    q("you forfiet the game and run away\n")
                                    s()
                                    q("Player 1 wins\n")
                                    crash=1
                                    while crash==1:
                                        escape=input(": \n")
                                        if escape=="DEVUNLOCK":
                                            crash=2
                                            q("unlocked\n")
                                elif yesorno==2:
                                    q("\n")
                                else:
                                    q("\n")
                        elif option == 3:
                            glocks=0
                            q("Player 2 has " + str(p2pots) + " Healing Potions left\n")
                            s()
                            q("Player 2 has " + str(p2spoons) + " Rusty spoons left\n")
                            s()
                            if p2GLOCK19s>=1:
                                q("THEY HAVE A GUNNN!!!!!!!!\n")
                                s()
                                glocks=1
                            q("Player 2 has " + str(p1knives) + " Knives left\n")
                            s()
                            if p2bows==1:
                                q("Player 2 has a bow and has " + str(p2arrows) + " arrows left\n")
                                s()
                            elif p2bows==0:
                                q("player 2 doesnt have a bow and has " + str(p2arrows) + " arrows left\n")
                            q("player 2 has " + str(p2hats) + " Fancy hats left\n")   
                            s()
                            q("Player 2 has " + str(p2mpots) + " Mana potions left\n")
                            s()
                            q("player 2 had " + str(p2sheilds) + " sheilds left\n")
                            s()
                            q("player 2 has " + str(p2shoes) + " pairs of sneaker left\n")
                            s()
                            q("player 2 has " + str(p2avocado) + " avocado's left\n")
                            s()
                            q("player 2 has " + str(p2pits) + " Pits left\n")
                            s()
                            q("player 2 has " + str(p2creams) + " Cans of whipped cream left\n")
                            s()
                            q("player 2 has " + str(p2webs) + " webs of the spider left\n")
                            s()
                            q("player 2 has " + str(p2dictionarys) + " dictionarys left\n")
                            s()
                            q("player 2 has " + str(p2elmos) + " talking elmos left\n")
                            s()
                            q("Player 2 has " + str(p2popbags) + " popcorn bags left\n")
                            s()
                            q("player 2 has " + str(p2pop) + " peices of popcorn left\n")



                            q("\n")
                            q("1: Use healing potion\n")
                            s()
                            q("2: Throw a rusty spoon\n")
                            s()
                            q("3: Throw a throwing knife\n")
                            s()
                            q("4: shoot an arrow\n")
                            s()
                            q("5: Use a mana potion\n")
                            s()
                            q("6: use the sheild\n")
                            s()
                            q("7: wear a fancy hat\n")
                            s()
                            q("8: wear sneakers\n")
                            s()
                            q("9: eat avocado\n")
                            s()
                            q("10: throw pit\n")
                            s()
                            q("11: eat whipped cream\n")
                            s()
                            q("12: shoot web\n")
                            s()
                            q("13: wear bandana\n")
                            s()
                            q("14: read the dictionary\n")
                            s()
                            q("15: use elmo\n")
                            s()
                            q("16: pop the pocorn bag\n")
                            s()
                            q("17: eat popcorn\n")
                            s()
                            q("0: cancel\n")
                            if glocks==1:
                                q("100000: Shoot\n")
                                s()
                            firsttime=1
                            itemss=1
                            while itemss==1:
                                if firsttime>2:
                                    glocks=0
                                    q("Player 2 has " + str(p2pots) + " Healing Potions left\n")
                                    s()
                                    q("Player 2 has " + str(p2spoons) + " Rusty spoons left\n")
                                    s()
                                    if p2GLOCK19s>=1:
                                        q("THEY HAVE A GUNNN!!!!!!!!\n")
                                        s()
                                        glocks=1
                                    q("Player 2 has " + str(p1knives) + " Knives left\n")
                                    s()
                                    if p2bows==1:
                                        q("Player 2 has a bow and has " + str(p2arrows) + " arrows left\n")
                                        s()
                                    elif p2bows==0:
                                        q("player 2 doesnt have a bow and has " + str(p2arrows) + " arrows left\n")
                                    q("player 2 has " + str(p2hats) + " Fancy hats left\n")   
                                    s()
                                    q("Player 2 has " + str(p2mpots) + " Mana potions left\n")
                                    s()
                                    q("player 2 had " + str(p2sheilds) + " sheilds left\n")
                                    s()
                                    q("player 2 has " + str(p2shoes) + " pairs of sneaker left\n")
                                    s()
                                    q("player 2 has " + str(p2avocado) + " avocado's left\n")
                                    s()
                                    q("player 2 has " + str(p2pits) + " Pits left\n")
                                    s()
                                    q("player 2 has " + str(p2creams) + " Cans of whipped cream left\n")
                                    s()
                                    q("player 2 has " + str(p2webs) + " webs of the spider left\n")
                                    s()
                                    q("player 2 has " + str(p2dictionarys) + " dictionarys left\n")
                                    s()
                                    q("player 2 has " + str(p2elmos) + " talking elmos left\n")
                                    s()
                                    q("Player 2 has " + str(p2popbags) + " popcorn bags left\n")
                                    s()
                                    q("player 2 has " + str(p2pop) + " peices of popcorn left\n")
                                s()
                                itemchoice=int(input("What would you like to do?: \n"))
                                s()
                                if itemchoice==1 and p2pots >= 1:
                                    q("Player 2 Heals 5 health\n")
                                    s()
                                    P2HP=P2HP+5
                                    if P2MAXHP<=P2HP:
                                        P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2pots=p2pots-2
                                elif itemchoice==3 and p2knives>=1:
                                    q("Player 2 threw a knife\n")
                                    s()
                                    knifedamage=random.randint(1,5)
                                    P2HP=P2HP-knifedamage
                                    q("Player 2 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P1HP) + " HP left\n")
                                    s()
                                    p2knives=p2knives-1
                                elif itemchoice==2 and p2spoons>=1:
                                    q("Player 2 threw a Spoon\n")
                                    s()
                                    spooncrit=random.randint(1,100)
                                    if spooncrit>=1 and spooncrit<=70:
                                        q("the spoon gave Player 1 a small cut and did 1 damage\n")
                                        s()
                                        P1HP=P1HP-1
                                        q("Player 1 has " + str(P1HP) + " HP left\n")
                                        s()
                                    elif spooncrit>=71 and spooncrit<=99:
                                        spoondamage=random.randint(2,10)
                                        q("the spoon gave Player 1 a cut and did " + str(spoondamage) + " Damge to Player 1\n")
                                        s()
                                        P1HP=P1HP-spoondamage
                                        q("Player 1 Has " + str(P1HP) + " HP left\n")
                                        s()
                                    elif spooncrit==100:
                                        q("Player 2 threw the spoon and cut Player 1\n")
                                        s()
                                        q("Player 1 got tetanites and died\n")
                                        s()
                                        P1HP=0
                                    else:
                                        q("ERROR ERROR\n")
                                    p2spoons=p2spoons-1
                                elif itemchoice==100000 and p2GLOCK19s>=1:
                                    q("player 1 was shot and died\n")
                                    P1HP=0
                                    q("stop gun voilence\n")
                                elif itemchoice==0:
                                    q("\n")
                                    itemss=0
                                elif itemchoice==4 and p2bows==1 and p2arrows>=1:
                                    arrowdamage=random.randint(2,5)
                                    P1HP=P1HP-arrowdamage
                                    q("You shot an arrow at player 1 doing " + str(arrowdamage) + " damage to Player 1, Player 1 has " + str(P1HP) + " HP left\n")
                                    p2arrows=p2arrows-1
                                    bbreak=random.randint(1,50)
                                    if bbreak==50:
                                        p2bows=0
                                        q("your bow broke\n")
                                elif itemchoice==5 and p2mpots >= 1:
                                    q("Player 2 regains 5 mana\n")
                                    s()
                                    P2MP=P2MP+5
                                    if P2MAXMP<=P2MP:
                                        P2MP=P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP\n")
                                    s()
                                    p2mpots=p2mpots-1
                                elif itemchoice==6 and p2sheilds >= 1:
                                    q("Player 2 sheilds themself and gains 2 def\n")
                                    s()
                                    P2DEF=P2DEF+2
                                    p2sheilds=p2sheilds-1
                                elif itemchoice==7 and p2hats >= 1:
                                    q("Player 2 wears the fancy hat and their max health goes up by 5 and they regain all missing health\n")
                                    s()
                                    P2MAXHP=P2MAXHP+5
                                    P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2hats=p2hats-1
                                elif itemchoice==8 and p2shoes >= 1:
                                    q("Player 2 wears the pair of sneaker and their Speed goes up by 5 and increase Speed bon by 1\n")
                                    s()
                                    P2SPD=P2SPD+5
                                    P2SPDBON=P2SPDBON+.5
                                    s()
                                    p2shoes=p2shoes-1
                                elif itemchoice==9 and p2avocado >= 1:
                                    q("Player 2 Heals 3 health\n")
                                    s()
                                    P2HP=P2HP+3
                                    if P2MAXHP<=P2HP:
                                        P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2pits=p2pits+1
                                    p2avocado=p2avocado-1
                                elif itemchoice==10 and p2pits>=1:
                                    q("Player 2 threw a pit\n")
                                    s()
                                    knifedamage=random.randint(1,3)
                                    P2HP=P2HP-knifedamage
                                    q("Player 2 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    p2pits=p2pits-1
                                elif itemchoice==11 and p2creams >= 1:
                                    c02pois=random.randint(1,10)
                                    if c02pois==10:
                                        q("player 1 died to carbon dioxide poisening\n")
                                        P1HP=0
                                        break
                                    elif c02pois!=10:
                                        q("Player 2 Heals 5 health and gains 1 Speed\n")
                                        s()
                                        P2HP=P2HP+5
                                        if P2MAXHP<=P2HP:
                                            P2HP=P2MAXHP
                                        q("Player 2 has " + str(P2HP) + " HP\n")
                                        s()
                                        P2SPD=P2SPD+1
                                        p2creams=p2creams-1
                                elif itemchoice==12 and p2webs >= 1:
                                    q("Player 2 shoots a web and slows down player 1\n")
                                    s()
                                    webslow=random.randint(1,8)
                                    P1SPD=P1SPD-webslow
                                    q("player 1 is " + str(webslow) + " speed slower now\n")
                                    s()
                                    p2webs=p2webs-1
                                elif itemchoice==13 and p1bandanas >= 1:
                                    q("Player 2 wears the drippy bandana and gains 1 defense and player 1's atk goes down by 1\n")
                                    s()
                                    P2DEF=P2DEF+1
                                    P1ATK=P1ATK-1
                                    p2bandanas=p2bandanas-1
                                elif itemchoice==14 and p2dictionarys >= 1:
                                    q("Player 2 reads a dictionary and understands a bit more. +1 to max mp\n")
                                    s()
                                    P2MAXMP=P2MAXMP+1
                                    p2dictionarys=p2dictionarys-1
                                elif itemchoice==15 and p2elmos >= 1:
                                    q("Player 2 uses talking elmo\n")
                                    s()
                                    P1MAXMP=P1MAXMP-1
                                    q("player 1 lost 1 max health due to the mental damage\n")
                                    s()
                                    p2elmos=p2elmos-1
                                elif itemchoice==16 and p2popbags >= 1 and P2MP>=3:
                                    q("Player 2 uses 3 mana to heat up some popcorn\n")
                                    s()
                                    P2MP=P2MP-3
                                    popcorn=random.randint(1,20)
                                    p2pop=p2pop+popcorn
                                    p2popbags=p2popbags-1
                                elif itemchoice==16 and p2popbags >=1 and P2MP<3:
                                    q("you dont enough mana to pop this bag\n")
                                    s()
                                elif itemchoice==17 and p2pop >= 1:
                                    eat=int(input("how many peices of popcorn would you like to eat?\n"))
                                    popcorn=random.randint(1,2)
                                    popcorn=popcorn*eat
                                    q("Player 2 Heals " + str(popcorn) + " health\n")
                                    s()
                                    P2HP=P2HP+popcorn
                                    if P2MAXHP<=P2HP:
                                        P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2pop=p2pop-eat
                                else:
                                    q("you either didnt have the item or you typed in a unavalible number either way your an idiot\n")
                                    s()
                                firsttime=firsttime+1,

                        elif option==5:
                            q("You pass you're turn\n")
                            turn = 2
                            P1SPD = P1SPD + P1SPDBON
                            P2MP = P2MP + P2MPBON
                            q("\n")
                            q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        else:
                            q("please try again\n")
                            s()
                elif P1SPD == P2SPD:
                    q("you have the same speed\n")
                    s()
                    q("choosing a random player to go\n")
                    s()
                    a= random.randint(1,2)
                    if a==1:
                        P1SPD=P1SPD+1
                    else:
                        P2SPD=P2SPD+1
                else:
                    q("UH OH\n")
            q("\n")
            q("Player 1 HP left " + str(P1HP) + "\n")
            s()
            q("Player 2 HP left " + str(P2HP)+"\n")
        q("winner winner chicken dinner\n")
        q("\n")
        s()
        q("\n")
        q("score " + str(p1score) + " to " + str(p2score))
        q("\n")
        q("\n")
        q("Play again?\n")
        s()
        q("1: Yes\n")
        s()
        q("0: No\n")
        s()
        playagain=int(input("Play again?: \n"))
    while playagain==2:
        s()
        q("You Are playing agaisnt a bot\n")
        s()
        q("Please select a class, player 1.\n")
        s()
        q("1: Knight\n")
        s()
        q("2: Peashooter\n")
        s()
        q("3: Mage\n")
        s()
        q("4: Rouge\n")
        s()
        q("5: Skele\n")
        s()
        q("6: Bard\n")
        s()
        q("7: Barbarain\n")
        s()
        q("8: Random\n")
        #Player 1 selects a class
        cc=1
        rc=1
        allcorrect=1
        while allcorrect==1:
            while cc==1:
                player1class = int(input("Choose a class from the list above (please choose a number): \n"))
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
                        P1SPD = 7
                        P1SPDBON = 2
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
                        P1MPBON = 3
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
                        P1MPBON = .5
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
                        q("Please give a valid number.\n")
                        cc=1
                        rc=1
                        s()
                q("1: Yes\n")
                s()
                q("2: No\n")
                s()
                yesorno = int(input("You have chosen " + str(player1class) + ". Is this correct?: \n"))
                s()
                if yesorno == 1:
                    q("Player 1 has chosen the " + str(player1class) + " class.\n")
                    s()
                    q("\n")
                    s()
                    allcorrect=2
                elif yesorno == 2:
                    q("repick your charcter.\n")
                    s()
                    cc=1
                    rc=1
                else:
                    q("Something went wrong please try again\n")
                    s()
                    cc=1
        cc=1
        rc=1
        allcorrect=1
        #Player 2 selects a class
        while allcorrect==1:
            while cc==1:
                q("Computer is choosing their class\n")
                s()
                rc=1
                player2class = random.randint(1,7)
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
                        P2MPBON= 1
                        P2SPD= 4
                        P2SPDBON = 2
                        cc=2
                        rc=2
                q("Player 2 has chosen the " + str(player2class) + " class.\n")
                s()
                q("\n")
                allcorrect=2
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
            p1webs=0
            p2webs=0
            p1bandanas=0
            p2bandanas=0
            p1dictionarys=0
            p2dictionarys=0
            p1elmos=0
            p2elmos=0
            p1popbags=0
            p2popbags=0
            p1pop=0
            p2pop=0
        q("Player 1 HP ",P1HP)
        s()
        q("Player 2 HP ",P2HP)
        s()
        q("\n")
        #round start
        q("Player 1 Speed ",P1SPD)
        s()
        q("Player 2 Speed ",P2SPD )
        s()
        while roundnumber < 100:
            turn=1
            q("Round " + str(roundnumber) + " \n")
            s()
            if P1HP <= 0:
                q("Player 2 wins the game\n")
                s()
                winner=player2class
                p2score=p2score+1
                break
            elif P2HP <= 0:
                q("Player 1 wins the game\n")
                s()
                winner=player1class
                p1score=p1score+1
                break
            else:
                q("\n")
                if P1SPD > P2SPD:
                    q("player 1's turn\n")
                    s()
                    q("player 1 has "+ str(P1MP) +" MP left\n")
                    s()
                    q("do one of the following\n")
                    s()
                    q("1: Attack\n")
                    s()
                    q("2: Magic\n")
                    s()
                    q("3: Use an item\n")
                    s()
                    q("4: Run Away\n")
                    s()
                    q("5: pass turn\n")
                    while turn == 1:
                        option=int(input("what would player 1 like to do?: \n"))
                        q("\n")
                        s()
                        critnumber=random.randint(rollp1,20)
                        if option == 1 and critnumber==20:
                            q("\n")
                            q("Player 1 used Attack\n")
                            s()
                            q("Player 1 Rolled a ",critnumber)
                            s()
                            q("Its a Criticle hit!!!\n")
                            s()
                            TOTDMG = (critnumber+(P1ATK*2))-P2DEF
                            if TOTDMG < 0:
                                TOTDMG = 0
                            q("Player 1 did " + str(TOTDMG) + " Damage to Player 2\n")
                            s()
                            P2HP = P2HP-TOTDMG
                            q("player 2 has " + str(P2HP) + " HP Left\n")
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
                            q("\n")
                            q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber<20 and critnumber>=2:
                            q("Player 1 used Attack\n")
                            s()
                            q("Player 1 Rolled a ",critnumber)
                            s()
                            TOTDMG = (critnumber+(P1ATK))-P2DEF
                            if TOTDMG < 0:
                                TOTDMG = 0
                            q("Player 1 did " + str(TOTDMG) + " Damage to Player 2\n")
                            s()
                            P2HP = P2HP-TOTDMG
                            q("Player 2 has " + str(P2HP) + " HP left\n")
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
                            q("\n")
                            q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber == 1:
                            q("Player 1 used Attack\n")
                            s()
                            q("Player 1 Rolled a 1\n")
                            s()
                            q("Player 1 missed\n")
                            s()
                            q("Player 1 did 0 Damage to Player 2\n")
                            s()
                            q("Player 2 has " + str(P2HP) + " HP left\n")
                            s()
                            P2SPD = P2SPD + P2SPDBON
                            if dmgp1 >= 2:
                                P1ATK=P1ATK-DMGBUFFP1
                                dmgp1 = dmgp1-1
                            turn=2
                            roundnumber=roundnumber+1
                            P1MP = P1MP + P1MPBON
                            q("\n")
                            q("Player 1 gained "+ str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        elif option == 2:
                            q("Please do one of the following\n")
                            s()
                            q("0: Cancel\n")
                            s()
                            q("1: Gain +3 DEF\n")
                            s()
                            q("2: Gain an item\n")
                            s()
                            q("3: Better Roll Next Turn-3MP\n")
                            s()
                            q("4: Heal 20 percent of max health-4MP\n")
                            s()
                            q("5: FireBall-5MP\n")
                            s()
                            q("6: Damage boost for every MP you have-2MP\n")
                            s()
                            magic_option=int(input("What would you like to do?: \n"))
                            q("\n")
                            s()
                            if P1MP < magic_option:
                                q("you dont have enough Mana\n")
                                s()
                            elif P1MP >= magic_option:
                                if magic_option == 1:
                                    P1DEF=P1DEF+1
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                elif magic_option==6:
                                    q("Player 1 used Damage boost\n")
                                    s()
                                    P1MP = P1MP - magic_option
                                    DMGBUFFP1=P1ATKBON+P1MP
                                    P1MP=0
                                    dmgp1 = dmgp1+1
                                    P1ATK=DMGBUFFP1 + P1ATK
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                elif magic_option==3:
                                    q("Player 1 used Advantage\n")
                                    rolladp1=2
                                    rollp1=10
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                    turn = 2
                                elif magic_option==5:
                                    q("Player 1 used fireball\n")
                                    s()
                                    fireballdmg = random.randint(12,18)
                                    q("Player 1 did " + str(fireballdmg) + " Damage to Player 2\n")
                                    s()
                                    P2HP=P2HP-fireballdmg
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                elif magic_option==4:
                                    q("Player 1 used heal\n")
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
                                    q("\n")
                                elif magic_option==2:
                                    """
                                            pair of tongs- steal an item from enemy:
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
                                    q("Player 1 used gain a random item\n")
                                    s()
                                    P1MP = P1MP - magic_option
                                    bestitem=291
                                    itemspin=random.randint(1,bestitem)
                                    q("You rolled a " + str(itemspin) + " \n")
                                    s()
                                    if itemspin >= 1 and itemspin<= 20:
                                        q("Player 1 Conjured a rusty spoon\n")
                                        s()
                                        q("what a waste of a turn\n")
                                        s()
                                        p1spoons=p1spoons+1
                                    elif itemspin >= 21 and itemspin<= 40:
                                        q("You Conjured Throwing knives\n")
                                        s()
                                        p1knives=p1knives+3
                                    elif itemspin >= 41 and itemspin<= 60:
                                        q("Player 1 Conjured a healing potion\n")
                                        s()
                                        p1pots=p1pots+1
                                    elif itemspin >=61 and itemspin<=80:
                                        arrow=random.randint(2,4)
                                        if p1bows>=1:
                                            q("Player 1 conjured " + str(arrow) + " arrows\n")
                                        elif p1bows==0:
                                            q("player 1 conjured a bow and arrow\n")
                                            s()
                                            p1bows = p1bows + 1
                                            p1arrows=p1arrows+1
                                        else:
                                            q("ERROR\n")
                                    elif itemspin >=81 and itemspin <=90:
                                        q("Player 1 Conjured a fancy hat\n")
                                        s()
                                        p1hats=p1hats+1
                                    elif itemspin >= 91 and itemspin<= 110:
                                        q("Player 1 Conjured a mana potion\n")
                                        s()
                                        p1mpots=p1mpots+1
                                    elif itemspin >= 111 and itemspin<= 130:
                                        q("Player 1 Conjured a sheild\n")
                                        s()
                                        p1sheilds=p1sheilds+1
                                    elif itemspin >= 131 and itemspin<= 150:
                                        q("Player 1 Conjured a pair of new sneakers\n")
                                        s()
                                        p1shoes=p1shoes+1
                                    elif itemspin >= 151 and itemspin<= 170:
                                        q("Player 1 Conjured a...\n")
                                        s()
                                        q("a avocado\n")
                                        s()
                                        p1avocado=p1avocado+1
                                    elif itemspin >= 171 and itemspin<= 190:
                                        q("Player 1 Conjured a can of whipped cream\n")
                                        s()                                        
                                        p1creams=p1creams+1
                                    elif itemspin >= 191 and itemspin<= 210:
                                        q("Player 1 Conjured a spiderweb\n")
                                        s()                                        
                                        p1webs=p1webs+1
                                    elif itemspin >= 211 and itemspin<= 230:
                                        q("Player 1 Conjured a dictionary\n")
                                        s()                                        
                                        p1dictionarys=p1dictionarys+1
                                    elif itemspin >= 231 and itemspin<= 250:
                                        q("Player 1 Conjured a bandana\n")
                                        s()                                        
                                        p1bandanas=p1bandanas+1 
                                    elif itemspin >= 251 and itemspin<= 270:
                                        q("Player 1 Conjured a elmo\n")
                                        s()
                                        p1elmos=p1elmos+1
                                    elif itemspin >= 271 and itemspin<= 290:
                                        q("Player 1 Conjured a bag of popcorn\n")
                                        s()                                        
                                        p1popbags=p1popbags+1
                                    elif itemspin == bestitem:
                                        q("Player 1 Conjured a...\n")
                                        s()
                                        s()
                                        s()
                                        s()
                                        s()
                                        q("wait what..\n")
                                        s()
                                        s()
                                        q("how... why!?!!?\n")
                                        s()
                                        q("why is the in the game (sigh)\n")
                                        s()
                                        s()
                                        q("i don't get paid enough for this\n")
                                        s()
                                        q("Player 1 Conjured a Glock-19\n")
                                        s()
                                        s()
                                        q("...This was not supposed to happen\n")
                                        s()
                                        q("\n")
                                        p1GLOCK19s=p1GLOCK19s+1
                                    else:
                                        q("THIS SHOULDN'T BE POSSIBLE HOW DID I MESS UP THIS BADLY\n")
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                else:
                                    q("somthing went wrong please try again\n")
                                    s()
                            else:
                                q("try again\n")
                                s()
                        elif option == 4:        
                                q("Are you SURE you want to run away??\n")
                                s()
                                q("1: Yes\n")
                                s()
                                q("2: No\n")
                                s()
                                yesorno=int(input("select an answer: \n"))
                                s()
                                if yesorno==1:
                                    q("you forfiet the game and run away\n")
                                    s()
                                    q("Player 2 wins\n")
                                    s()
                                    P1HP=0
                                    break
                                elif yesorno==2:
                                    q("\n")
                                else:
                                    q("\n")
                        elif option == 3:
                            glocks=0
                            q("Player 1 has " + str(p1pots) + " Healing Potions left\n")
                            s()
                            q("Player 1 has " + str(p1spoons) + " Rusty spoons left\n")
                            s()
                            if p1GLOCK19s>=1:
                                q("THEY HAVE A GUNNN!!!!!!!!\n")
                                s()
                                glocks=1
                            q("Player 1 has " + str(p1knives) + " Knives left\n")
                            s()
                            if p1bows==1:
                                q("Player 1 has a bow and has " + str(p1arrows) + " arrows left\n")
                                s()
                            elif p1bows==0:
                                q("player 1 doesnt have a bow and has " + str(p1arrows) + " arrows left\n")
                            q("player 1 has " + str(p1hats) + " Fancy hats left\n")   
                            s()
                            q("Player 1 has " + str(p1mpots) + " Mana potions left\n")
                            s()
                            q("player 1 had " + str(p1sheilds) + " sheilds left\n")
                            s()
                            q("player 1 has " + str(p1shoes) + " pairs of sneaker left\n")
                            s()
                            q("player 1 has " + str(p1avocado) + " avocado's left\n")
                            s()
                            q("player 1 has " + str(p1pits) + " Pits left\n")
                            s()
                            q("player 1 has " + str(p1creams) + " Cans of whipped cream left\n")
                            s()
                            q("player 1 has " + str(p1webs) + " webs of the spider left\n")
                            s()
                            q("player 1 has " + str(p1dictionarys) + " dictionarys left\n")
                            s()
                            q("player 1 has " + str(p1elmos) + " talking elmos left\n")
                            s()
                            q("Player 1 has " + str(p1popbags) + " popcorn bags left\n")
                            s()
                            q("player 1 has " + str(p1pop) + " peices of popcorn left\n")



                            q("\n")
                            q("1: Use healing potion\n")
                            s()
                            q("2: Throw a rusty spoon\n")
                            s()
                            q("3: Throw a throwing knife\n")
                            s()
                            q("4: shoot an arrow\n")
                            s()
                            q("5: Use a mana potion\n")
                            s()
                            q("6: use the sheild\n")
                            s()
                            q("7: wear a fancy hat\n")
                            s()
                            q("8: wear sneakers\n")
                            s()
                            q("9: eat avocado\n")
                            s()
                            q("10: throw pit\n")
                            s()
                            q("11: eat whipped cream\n")
                            s()
                            q("12: shoot web\n")
                            s()
                            q("13: wear bandana\n")
                            s()
                            q("14: read the dictionary\n")
                            s()
                            q("15: use elmo\n")
                            s()
                            q("16: pop the pocorn bag\n")
                            s()
                            q("17: eat popcorn\n")
                            s()
                            q("0: cancel\n")
                            if glocks==1:
                                q("100000: Shoot\n")
                                s()
                            itemss=1
                            firsttime=1
                            while itemss>=1:
                                if firsttime==2:
                                    glocks=0
                                    q("Player 1 has " + str(p1pots) + " Healing Potions left\n")
                                    s()
                                    q("Player 1 has " + str(p1spoons) + " Rusty spoons left\n")
                                    s()
                                    if p1GLOCK19s>=1:
                                        q("THEY HAVE A GUNNN!!!!!!!!\n")
                                        s()
                                        glocks=1
                                    q("Player 1 has " + str(p1knives) + " Knives left\n")
                                    s()
                                    if p1bows==1:
                                        q("Player 1 has a bow and has " + str(p1arrows) + " arrows left\n")
                                        s()
                                    elif p1bows==0:
                                        q("player 1 doesnt have a bow and has " + str(p1arrows) + " arrows left\n")
                                    q("player 1 has " + str(p1hats) + " Fancy hats left\n")   
                                    s()
                                    q("Player 1 has " + str(p1mpots) + " Mana potions left\n")
                                    s()
                                    q("player 1 had " + str(p1sheilds) + " sheilds left\n")
                                    s()
                                    q("player 1 has " + str(p1shoes) + " pairs of sneaker left\n")
                                    s()
                                    q("player 1 has " + str(p1avocado) + " avocado's left\n")
                                    s()
                                    q("player 1 has " + str(p1pits) + " Pits left\n")
                                    s()
                                    q("player 1 has " + str(p1creams) + " Cans of whipped cream left\n")
                                    s()
                                    q("player 1 has " + str(p1webs) + " webs of the spider left\n")
                                    s()
                                    q("player 1 has " + str(p1dictionarys) + " dictionarys left\n")
                                    s()
                                    q("player 1 has " + str(p1elmos) + " talking elmos left\n")
                                    s()
                                    q("Player 1 has " + str(p1popbags) + " popcorn bags left\n")
                                    s()
                                    q("player 1 has " + str(p1pop) + " peices of popcorn left\n")
                                s()
                                itemchoice=int(input("What would you like to do?: \n"))
                                s()
                                if itemchoice==1 and p1pots >= 1:
                                    q("Player 1 Heals 5 health\n")
                                    s()
                                    P1HP=P1HP+5
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1pots=p1pots-1
                                elif itemchoice==3 and p1knives>=1:
                                    q("Player 1 threw a knife\n")
                                    s()
                                    knifedamage=random.randint(1,5)
                                    P2HP=P2HP-knifedamage
                                    q("Player 1 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    p1knives=p1knives-1
                                elif itemchoice==2 and p1spoons>=1:
                                    q("Player 1 threw a Spoon\n")
                                    s()
                                    spooncrit=random.randint(1,100)
                                    if spooncrit>=1 and spooncrit<=70:
                                        q("the spoon gave Player 2 a small cut and did 1 damage\n")
                                        s()
                                        P2HP=P2HP-1
                                        q("Player 2 has " + str(P2HP) + " HP left\n")
                                        s()
                                    elif spooncrit>=71 and spooncrit<=99:
                                        spoondamage=random.randint(2,10)
                                        q("the spoon gave Player 2 a cut and did " + str(spoondamage) + " Damge to Player 2\n")
                                        s()
                                        P2HP=P2HP-spoondamage
                                        q("Player 2 Has " + str(P2HP) + " HP left\n")
                                        s()
                                    elif spooncrit==100:
                                        q("Player 1 threw the spoon and cut Player 2\n")
                                        s()
                                        q("Player 2 got tetanites and died\n")
                                        s()
                                        P2HP=0
                                    else:
                                        q("ERROR ERROR\n")
                                    p1spoons=p1spoons-1
                                elif itemchoice==100000 and p1GLOCK19s>=1:
                                    q("player 2 was shot and died\n")
                                    P2HP=0
                                    q("stop gun voilence\n")
                                elif itemchoice==0:
                                    q("\n")
                                    itemss=0
                                elif itemchoice==4 and p1bows==1 and p1arrows>=1:
                                    arrowdamage=random.randint(2,5)
                                    P2HP=P2HP-arrowdamage
                                    q("You shot an arrow at player 2 doing " + str(arrowdamage) + " damage to Player 2, Player 2 has " + str(P2HP) + " HP left\n")
                                    p1arrows=p1arrows-1
                                    bbreak=random.randint(1,50)
                                    if bbreak==50:
                                        p1bows=0
                                        q("your bow broke\n")
                                elif itemchoice==5 and p1mpots >= 1:
                                    q("Player 1 regains 5 mana\n")
                                    s()
                                    P1MP=P1MP+5
                                    if P1MAXMP<=P1MP:
                                        P1MP=P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP\n")
                                    s()
                                    p1mpots=p1mpots-1
                                elif itemchoice==6 and p1sheilds >= 1:
                                    q("Player 1 sheilds themself and gains 2 def\n")
                                    s()
                                    P1DEF=P1DEF+2
                                    p1sheilds=p1sheilds-1
                                elif itemchoice==7 and p1hats >= 1:
                                    q("Player 1 wears the fancy hat and their max health goes up by 5 and they regain all missing health\n")
                                    s()
                                    P1MAXHP=P1MAXHP+5
                                    P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1hats=p1hats-1
                                elif itemchoice==8 and p1shoes >= 1:
                                    q("Player 1 wears the pair of sneaker and their Speed goes up by 5 and increase Speed bon by 1\n")
                                    s()
                                    P1SPD=P1SPD+5
                                    P1SPDBON=P1SPDBON+.5
                                    s()
                                    p1shoes=p1shoes-1
                                elif itemchoice==9 and p1avocado >= 1:
                                    q("Player 1 Heals 3 health\n")
                                    s()
                                    P1HP=P1HP+3
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1pits=p1pits+1
                                    p1avocado=p1avocado-1
                                elif itemchoice==10 and p1pits>=1:
                                    q("Player 1 threw a pit\n")
                                    s()
                                    knifedamage=random.randint(1,3)
                                    P2HP=P2HP-knifedamage
                                    q("Player 1 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    p1pits=p1pits-1
                                elif itemchoice==11 and p1creams >= 1:
                                    c02pois=random.randint(1,10)
                                    if c02pois==10:
                                        q("player 1 died to carbon dioxide poisening\n")
                                        P1HP=0
                                        break
                                    elif c02pois!=10:
                                        q("Player 1 Heals 5 health and gains 1 Speed\n")
                                        s()
                                        P1HP=P1HP+5
                                        if P1MAXHP<=P1HP:
                                            P1HP=P1MAXHP
                                        q("Player 1 has " + str(P1HP) + " HP\n")
                                        s()
                                        P1SPD=P1SPD+1
                                        p1creams=p1creams-1
                                elif itemchoice==12 and p1webs >= 1:
                                    q("Player 1 shoots a web and slows down player 2\n")
                                    s()
                                    webslow=random.randint(1,8)
                                    P2SPD=P2SPD-webslow
                                    q("player 2 is " + str(webslow) + " speed slower now\n")
                                    s()
                                    p1webs=p1webs-1
                                elif itemchoice==13 and p1bandanas >= 1:
                                    q("Player 1 wears the drippy bandana and gains 1 defense and player 2's atk goes down by 1\n")
                                    s()
                                    P1DEF=P1DEF+1
                                    P2ATK=P2ATK-1
                                    p1bandanas=p1bandanas-1
                                elif itemchoice==14 and p1dictionarys >= 1:
                                    q("Player 1 reads a dictionary and understands a bit more. +1 to max mp\n")
                                    s()
                                    P1MAXMP=P1MAXMP+1
                                    p1dictionarys=p1dictionarys-1
                                elif itemchoice==15 and p1elmos >= 1:
                                    q("Player 1 uses talking elmo\n")
                                    s()
                                    P2MAXMP=P2MAXMP-1
                                    q("player 2 lost 1 max health due to the mental damage\n")
                                    s()
                                    p1elmos=p1elmos-1
                                elif itemchoice==16 and p1popbags >= 1 and P1MP>=3:
                                    q("Player 1 uses 3 mana to heat up some popcorn\n")
                                    s()
                                    P1MP=P1MP-3
                                    popcorn=random.randint(1,20)
                                    p1pop=p1pop+popcorn
                                    p1popbags=p1popbags-1
                                elif itemchoice==16 and p1popbags >=1 and P1MP<3:
                                    q("you dont enough mana to pop this bag\n")
                                    s()
                                elif itemchoice==17 and p1pop >= 1:
                                    eat=int(input("how many peices of popcorn would you like to eat?\n"))
                                    popcorn=random.randint(1,2)
                                    popcorn=popcorn*eat
                                    q("Player 1 Heals " + str(popcorn) + " health\n")
                                    s()
                                    P1HP=P1HP+popcorn
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1pop=p1pop-eat
                                else:
                                    q("you either didnt have the item or you typed in a unavalible number either way your an idiot\n")
                                    s()
                                firsttime=firsttime+1

                        elif option==5:
                            q("You pass you're turn\n")
                            turn = 2
                            P2SPD = P2SPD + P2SPDBON
                            P1MP = P1MP + P1MPBON
                            q("\n")
                            q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        else:
                            q("please try again\n")
                            s()
                elif P1SPD < P2SPD:
                    q("player 2's turn\n")
                    s()
                    q("player 2 has "+ str(P2MP) +" MP left\n")
                    while turn == 1:
                        option=random.randint(1,2)
                        q("\n")
                        s()
                        critnumber=random.randint(rollp2,20)
                        if option == 1 and critnumber==20:
                            q("\n")
                            q("Player 2 used Attack\n")
                            s()
                            q("Player 2 Rolled a ",critnumber)
                            s()
                            q("Its a Criticle hit!!!\n")
                            s()
                            TOTDMG= (critnumber+(P2ATK*2))-P1DEF
                            if TOTDMG < 0:
                                TOTDMG=0
                            q("Player 2 did " + str(TOTDMG) + " Damage to Player 1\n")
                            s()
                            P1HP = P1HP-TOTDMG
                            q("player 1 has " + str(P1HP) + " HP Left\n")
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
                            q("\n")
                            q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber<20 and critnumber>=2:
                            q("Player 2 used Attack\n")
                            s()
                            q("Player 2 Rolled a ", critnumber)
                            s()
                            TOTDMG= (critnumber+P2ATK)-P1DEF
                            if TOTDMG < 0:
                                TOTDMG=0
                            q("Player 2 did " + str(TOTDMG) + " Damage to Player 1\n")
                            s()
                            P1HP = P1HP-TOTDMG
                            q("Player 1 has " + str(P1HP) + " HP left\n")
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
                            q("\n")
                            q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber==1:
                            q("Player 2 used Attack\n")
                            s()
                            q("Player 2 Rolled a 1\n")
                            s()
                            q("Player 2 missed\n")
                            s()
                            q("Player 2 did 0 Damage to Player 1\n")
                            s()
                            q("Player 1 has " + str(P1HP) + " HP left\n")
                            s()
                            P1SPD = P1SPD + P1SPDBON
                            if dmgp2 >= 2:
                                P2ATK==P2ATK-DMGBUFFP2
                                dmgp2=dmgp2-1
                            turn=2
                            roundnumber=roundnumber+1
                            P2MP = P2MP + P2MPBON
                            q("\n")
                            q("Player 2 gained "+ str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        elif option == 2:
                            pcmp=P2MP
                            if pcmp>6:
                                pcmp=6
                            if pcmp<1:
                                pcmp=0
                            magic_option=random.randint(1,pcmp)
                            q("\n")
                            q("The bot used option " + str(magic_option) + " \n")
                            s()
                            if P2MP < magic_option:
                                q("You don't have enough Mana\n")
                            
                            elif P2MP >= magic_option:
                                if magic_option == 1:
                                    P2DEF=P2DEF+1
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                elif magic_option==6:
                                    q("Player 2 used Damage boost\n")
                                    s()
                                    P2MP = P2MP - magic_option
                                    DMGBUFFP2=P2ATKBON+P2MP
                                    P2MP=0
                                    dmgp2 = dmgp2+1
                                    P2ATK=DMGBUFFP2 + P2ATK
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                elif magic_option==3:
                                    q("Player 2 used Advantage\n")
                                    rolladp2=2
                                    rollp2=10
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                    turn = 2
                                elif magic_option==5:
                                    q("Player 2 used fireball\n")
                                    s()
                                    fireballdmg = random.randint(12,18)
                                    q("Player 2 did " + str(fireballdmg) + " Damage to Player 1\n")
                                    s()
                                    P1HP=P1HP-fireballdmg
                                    q("Player 1 has " + str(P1HP) + " HP left\n")
                                    s()
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                elif magic_option==4:
                                    q("Player 2 used heal\n")
                                    s()
                                    P2HP = P2HP + (P2MAXHP/5)
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                    if P2MAXHP < P2HP:
                                        P2HP = P2MAXHP
                                elif magic_option==0:
                                    q("\n")
                                elif magic_option==2:
                                    q("Player 2 used gain a random item\n")
                                    s()
                                    P2MP = P2MP - magic_option
                                    bestitem=291
                                    itemspin=random.randint(1,bestitem)
                                    q("You rolled a " + str(itemspin) + " \n")
                                    s()
                                    if itemspin >= 1 and itemspin<= 20:
                                        q("Player 2 Conjured a rusty spoon\n")
                                        s()
                                        q("what a waste of a turn\n")
                                        s()
                                        p2spoons=p2spoons+1
                                    elif itemspin >= 21 and itemspin<= 40:
                                        q("You Conjured Throwing knives\n")
                                        s()
                                        p2knives=p2knives+3
                                    elif itemspin >= 41 and itemspin<= 60:
                                        q("Player 2 Conjured a healing potion\n")
                                        s()
                                        p2pots=p2pots+1
                                    elif itemspin >=61 and itemspin<=80:
                                        arrow=random.randint(2,4)
                                        if p2bows>=1:
                                            q("Player 2 conjured " + str(arrow) + " arrows\n")
                                        elif p2bows==0:
                                            q("player 2 conjured a bow and arrow\n")
                                            s()
                                            p2bows = p2bows + 1
                                            p2arrows=p2arrows+1
                                        else:
                                            q("ERROR\n")
                                    elif itemspin >=81 and itemspin <=90:
                                        q("Player 2 Conjured a fancy hat\n")
                                        s()
                                        p2hats=p2hats+1
                                    elif itemspin >= 91 and itemspin<= 110:
                                        q("Player 2 Conjured a mana potion\n")
                                        s()
                                        p2mpots=p2mpots+1
                                    elif itemspin >= 111 and itemspin<= 130:
                                        q("Player 2 Conjured a sheild\n")
                                        s()
                                        p2sheilds=p2sheilds+1
                                    elif itemspin >= 131 and itemspin<= 150:
                                        q("Player 2 Conjured a pair of new sneakers\n")
                                        s()
                                        p2shoes=p2shoes+1
                                    elif itemspin >= 151 and itemspin<= 170:
                                        q("Player 2 Conjured a...\n")
                                        s()
                                        q("a avocado\n")
                                        s()
                                        p2avocado=p2avocado+1
                                    elif itemspin >= 171 and itemspin<= 190:
                                        q("Player 2 Conjured a can of whipped cream\n")
                                        s()                                        
                                        p2creams=p2creams+1
                                    elif itemspin >= 191 and itemspin<= 210:
                                        q("Player 2 Conjured a spiderweb\n")
                                        s()                                        
                                        p2webs=p2webs+1
                                    elif itemspin >= 211 and itemspin<= 230:
                                        q("Player 2 Conjured a dictionary\n")
                                        s()                                        
                                        p2dictionarys=p2dictionarys+1
                                    elif itemspin >= 231 and itemspin<= 250:
                                        q("Player 2 Conjured a bandana\n")
                                        s()                                        
                                        p2bandanas=p2bandanas+1 
                                    elif itemspin >= 251 and itemspin<= 270:
                                        q("Player 2 Conjured a elmo\n")
                                        s()
                                        p2elmos=p2elmos+1
                                    elif itemspin >= 271 and itemspin<= 290:
                                        q("Player 2 Conjured a bag of popcorn\n")
                                        s()                                        
                                        p2popbags=p2popbags+1
                                    elif itemspin == bestitem:
                                        q("Player 2 Conjured a...\n")
                                        s()
                                        s()
                                        s()
                                        s()
                                        s()
                                        q("wait what..\n")
                                        s()
                                        s()
                                        q("how... why!?!!?\n")
                                        s()
                                        q("why is the in the game (sigh)\n")
                                        s()
                                        s()
                                        q("i don't get paid enough for this\n")
                                        s()
                                        q("Player 1 Conjured a Glock-19\n")
                                        s()
                                        s()
                                        q("...This was not supposed to happen\n")
                                        s()
                                        q("\n")
                                        p2GLOCK19s=p2GLOCK19s+1
                                    else:
                                        q("THIS SHOULDN'T BE POSSIBLE HOW DID I MESS UP THIS BADLY\n")
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                else:
                                    q("somthing went wrong please try again\n")
                                    s()
                            else:
                                q("try again\n")
                                s()
                        elif option == 4:        
                                q("Are you SURE you want to run away??\n")
                                s()
                                q("1: Yes\n")
                                s()
                                q("2: No\n")
                                s()
                                yesorno=int(input("select an answer: \n"))
                                s()
                                if yesorno==1:
                                    q("you forfiet the game and run away\n")
                                    s()
                                    q("Player 1 wins\n")
                                    crash=1
                                    while crash==1:
                                        escape=input(": \n")
                                        if escape=="DEVUNLOCK":
                                            crash=2
                                            q("unlocked\n")
                                elif yesorno==2:
                                    q("\n")
                                else:
                                    q("\n")
                        elif option == 3:
                            glocks=0
                            q("Player 2 has " + str(p2pots) + " Healing Potions left\n")
                            s()
                            q("Player 2 has " + str(p2spoons) + " Rusty spoons left\n")
                            s()
                            if p2GLOCK19s>=1:
                                q("THEY HAVE A GUNNN!!!!!!!!\n")
                                s()
                                glocks=1
                            q("Player 2 has " + str(p1knives) + " Knives left\n")
                            s()
                            if p2bows==1:
                                q("Player 2 has a bow and has " + str(p2arrows) + " arrows left\n")
                                s()
                            elif p2bows==0:
                                q("player 2 doesnt have a bow and has " + str(p2arrows) + " arrows left\n")
                            q("player 2 has " + str(p2hats) + " Fancy hats left\n")   
                            s()
                            q("Player 2 has " + str(p2mpots) + " Mana potions left\n")
                            s()
                            q("player 2 had " + str(p2sheilds) + " sheilds left\n")
                            s()
                            q("player 2 has " + str(p2shoes) + " pairs of sneaker left\n")
                            s()
                            q("player 2 has " + str(p2avocado) + " avocado's left\n")
                            s()
                            q("player 2 has " + str(p2pits) + " Pits left\n")
                            s()
                            q("player 2 has " + str(p2creams) + " Cans of whipped cream left\n")
                            s()
                            q("player 2 has " + str(p2webs) + " webs of the spider left\n")
                            s()
                            q("player 2 has " + str(p2dictionarys) + " dictionarys left\n")
                            s()
                            q("player 2 has " + str(p2elmos) + " talking elmos left\n")
                            s()
                            q("Player 2 has " + str(p2popbags) + " popcorn bags left\n")
                            s()
                            q("player 2 has " + str(p2pop) + " peices of popcorn left\n")



                            q("\n")
                            q("1: Use healing potion\n")
                            s()
                            q("2: Throw a rusty spoon\n")
                            s()
                            q("3: Throw a throwing knife\n")
                            s()
                            q("4: shoot an arrow\n")
                            s()
                            q("5: Use a mana potion\n")
                            s()
                            q("6: use the sheild\n")
                            s()
                            q("7: wear a fancy hat\n")
                            s()
                            q("8: wear sneakers\n")
                            s()
                            q("9: eat avocado\n")
                            s()
                            q("10: throw pit\n")
                            s()
                            q("11: eat whipped cream\n")
                            s()
                            q("12: shoot web\n")
                            s()
                            q("13: wear bandana\n")
                            s()
                            q("14: read the dictionary\n")
                            s()
                            q("15: use elmo\n")
                            s()
                            q("16: pop the pocorn bag\n")
                            s()
                            q("17: eat popcorn\n")
                            s()
                            q("0: cancel\n")
                            if glocks==1:
                                q("100000: Shoot\n")
                                s()
                            firsttime=1
                            itemss=1
                            while itemss==1:
                                if firsttime>2:
                                    glocks=0
                                    q("Player 2 has " + str(p2pots) + " Healing Potions left\n")
                                    s()
                                    q("Player 2 has " + str(p2spoons) + " Rusty spoons left\n")
                                    s()
                                    if p2GLOCK19s>=1:
                                        q("THEY HAVE A GUNNN!!!!!!!!\n")
                                        s()
                                        glocks=1
                                    q("Player 2 has " + str(p1knives) + " Knives left\n")
                                    s()
                                    if p2bows==1:
                                        q("Player 2 has a bow and has " + str(p2arrows) + " arrows left\n")
                                        s()
                                    elif p2bows==0:
                                        q("player 2 doesnt have a bow and has " + str(p2arrows) + " arrows left\n")
                                    q("player 2 has " + str(p2hats) + " Fancy hats left\n")   
                                    s()
                                    q("Player 2 has " + str(p2mpots) + " Mana potions left\n")
                                    s()
                                    q("player 2 had " + str(p2sheilds) + " sheilds left\n")
                                    s()
                                    q("player 2 has " + str(p2shoes) + " pairs of sneaker left\n")
                                    s()
                                    q("player 2 has " + str(p2avocado) + " avocado's left\n")
                                    s()
                                    q("player 2 has " + str(p2pits) + " Pits left\n")
                                    s()
                                    q("player 2 has " + str(p2creams) + " Cans of whipped cream left\n")
                                    s()
                                    q("player 2 has " + str(p2webs) + " webs of the spider left\n")
                                    s()
                                    q("player 2 has " + str(p2dictionarys) + " dictionarys left\n")
                                    s()
                                    q("player 2 has " + str(p2elmos) + " talking elmos left\n")
                                    s()
                                    q("Player 2 has " + str(p2popbags) + " popcorn bags left\n")
                                    s()
                                    q("player 2 has " + str(p2pop) + " peices of popcorn left\n")
                                s()
                                itemchoice=int(input("What would you like to do?: \n"))
                                s()
                                if itemchoice==1 and p2pots >= 1:
                                    q("Player 2 Heals 5 health\n")
                                    s()
                                    P2HP=P2HP+5
                                    if P2MAXHP<=P2HP:
                                        P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2pots=p2pots-2
                                elif itemchoice==3 and p2knives>=1:
                                    q("Player 2 threw a knife\n")
                                    s()
                                    knifedamage=random.randint(1,5)
                                    P2HP=P2HP-knifedamage
                                    q("Player 2 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P1HP) + " HP left\n")
                                    s()
                                    p2knives=p2knives-1
                                elif itemchoice==2 and p2spoons>=1:
                                    q("Player 2 threw a Spoon\n")
                                    s()
                                    spooncrit=random.randint(1,100)
                                    if spooncrit>=1 and spooncrit<=70:
                                        q("the spoon gave Player 1 a small cut and did 1 damage\n")
                                        s()
                                        P1HP=P1HP-1
                                        q("Player 1 has " + str(P1HP) + " HP left\n")
                                        s()
                                    elif spooncrit>=71 and spooncrit<=99:
                                        spoondamage=random.randint(2,10)
                                        q("the spoon gave Player 1 a cut and did " + str(spoondamage) + " Damge to Player 1\n")
                                        s()
                                        P1HP=P1HP-spoondamage
                                        q("Player 1 Has " + str(P1HP) + " HP left\n")
                                        s()
                                    elif spooncrit==100:
                                        q("Player 2 threw the spoon and cut Player 1\n")
                                        s()
                                        q("Player 1 got tetanites and died\n")
                                        s()
                                        P1HP=0
                                    else:
                                        q("ERROR ERROR\n")
                                    p2spoons=p2spoons-1
                                elif itemchoice==100000 and p2GLOCK19s>=1:
                                    q("player 1 was shot and died\n")
                                    P1HP=0
                                    q("stop gun voilence\n")
                                elif itemchoice==0:
                                    q("\n")
                                    itemss=0
                                elif itemchoice==4 and p2bows==1 and p2arrows>=1:
                                    arrowdamage=random.randint(2,5)
                                    P1HP=P1HP-arrowdamage
                                    q("You shot an arrow at player 1 doing " + str(arrowdamage) + " damage to Player 1, Player 1 has " + str(P1HP) + " HP left\n")
                                    p2arrows=p2arrows-1
                                    bbreak=random.randint(1,50)
                                    if bbreak==50:
                                        p2bows=0
                                        q("your bow broke\n")
                                elif itemchoice==5 and p2mpots >= 1:
                                    q("Player 2 regains 5 mana\n")
                                    s()
                                    P2MP=P2MP+5
                                    if P2MAXMP<=P2MP:
                                        P2MP=P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP\n")
                                    s()
                                    p2mpots=p2mpots-1
                                elif itemchoice==6 and p2sheilds >= 1:
                                    q("Player 2 sheilds themself and gains 2 def\n")
                                    s()
                                    P2DEF=P2DEF+2
                                    p2sheilds=p2sheilds-1
                                elif itemchoice==7 and p2hats >= 1:
                                    q("Player 2 wears the fancy hat and their max health goes up by 5 and they regain all missing health\n")
                                    s()
                                    P2MAXHP=P2MAXHP+5
                                    P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2hats=p2hats-1
                                elif itemchoice==8 and p2shoes >= 1:
                                    q("Player 2 wears the pair of sneaker and their Speed goes up by 5 and increase Speed bon by 1\n")
                                    s()
                                    P2SPD=P2SPD+5
                                    P2SPDBON=P2SPDBON+.5
                                    s()
                                    p2shoes=p2shoes-1
                                elif itemchoice==9 and p2avocado >= 1:
                                    q("Player 2 Heals 3 health\n")
                                    s()
                                    P2HP=P2HP+3
                                    if P2MAXHP<=P2HP:
                                        P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2pits=p2pits+1
                                    p2avocado=p2avocado-1
                                elif itemchoice==10 and p2pits>=1:
                                    q("Player 2 threw a pit\n")
                                    s()
                                    knifedamage=random.randint(1,3)
                                    P2HP=P2HP-knifedamage
                                    q("Player 2 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    p2pits=p2pits-1
                                elif itemchoice==11 and p2creams >= 1:
                                    c02pois=random.randint(1,10)
                                    if c02pois==10:
                                        q("player 1 died to carbon dioxide poisening\n")
                                        P1HP=0
                                        break
                                    elif c02pois!=10:
                                        q("Player 2 Heals 5 health and gains 1 Speed\n")
                                        s()
                                        P2HP=P2HP+5
                                        if P2MAXHP<=P2HP:
                                            P2HP=P2MAXHP
                                        q("Player 2 has " + str(P2HP) + " HP\n")
                                        s()
                                        P2SPD=P2SPD+1
                                        p2creams=p2creams-1
                                elif itemchoice==12 and p2webs >= 1:
                                    q("Player 2 shoots a web and slows down player 1\n")
                                    s()
                                    webslow=random.randint(1,8)
                                    P1SPD=P1SPD-webslow
                                    q("player 1 is " + str(webslow) + " speed slower now\n")
                                    s()
                                    p2webs=p2webs-1
                                elif itemchoice==13 and p1bandanas >= 1:
                                    q("Player 2 wears the drippy bandana and gains 1 defense and player 1's atk goes down by 1\n")
                                    s()
                                    P2DEF=P2DEF+1
                                    P1ATK=P1ATK-1
                                    p2bandanas=p2bandanas-1
                                elif itemchoice==14 and p2dictionarys >= 1:
                                    q("Player 2 reads a dictionary and understands a bit more. +1 to max mp\n")
                                    s()
                                    P2MAXMP=P2MAXMP+1
                                    p2dictionarys=p2dictionarys-1
                                elif itemchoice==15 and p2elmos >= 1:
                                    q("Player 2 uses talking elmo\n")
                                    s()
                                    P1MAXMP=P1MAXMP-1
                                    q("player 1 lost 1 max health due to the mental damage\n")
                                    s()
                                    p2elmos=p2elmos-1
                                elif itemchoice==16 and p2popbags >= 1 and P2MP>=3:
                                    q("Player 2 uses 3 mana to heat up some popcorn\n")
                                    s()
                                    P2MP=P2MP-3
                                    popcorn=random.randint(1,20)
                                    p2pop=p2pop+popcorn
                                    p2popbags=p2popbags-1
                                elif itemchoice==16 and p2popbags >=1 and P2MP<3:
                                    q("you dont enough mana to pop this bag\n")
                                    s()
                                elif itemchoice==17 and p2pop >= 1:
                                    eat=int(input("how many peices of popcorn would you like to eat?\n"))
                                    popcorn=random.randint(1,2)
                                    popcorn=popcorn*eat
                                    q("Player 2 Heals " + str(popcorn) + " health\n")
                                    s()
                                    P2HP=P2HP+popcorn
                                    if P2MAXHP<=P2HP:
                                        P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2pop=p2pop-eat
                                else:
                                    q("you either didnt have the item or you typed in a unavalible number either way your an idiot\n")
                                    s()
                                firsttime=firsttime+1,

                        elif option==5:
                            q("You pass you're turn\n")
                            turn = 2
                            P1SPD = P1SPD + P1SPDBON
                            P2MP = P2MP + P2MPBON
                            q("\n")
                            q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        else:
                            q("please try again\n")
                            s()
                elif P1SPD == P2SPD:
                    q("you have the same speed\n")
                    s()
                    q("choosing a random player to go\n")
                    s()
                    a= random.randint(1,2)
                    if a==1:
                        P1SPD=P1SPD+1
                    else:
                        P2SPD=P2SPD+1
                else:
                    q("UH OH\n")
            q("\n")
            q("Player 1 HP left ",P1HP)
            s()
            q("Player 2 HP left ",P2HP)
        q("winner winner chicken dinner\n")
        q("\n")
        s()
        q("\n")
        q("score " + str(p1score) + " to " + str(p2score))
        q("\n")
        q("\n")
        q("Play again?\n")
        s()
        q("1: Yes\n")
        s()
        q("0: No\n")
        s()
        playagain=int(input("Play again?: \n"))
    while playagain==3:
        s()
        q("\n")
        s()
        q("Please select a class, player 1.\n")
        s()
        q("1: Knight\n")
        s()
        q("2: Peashooter\n")
        s()
        q("3: Mage\n")
        s()
        q("4: Rouge\n")
        s()
        q("5: Skele\n")
        s()
        q("6: Bard\n")
        s()
        q("7: Barbarain\n")
        s()
        q("8: Random\n")
        #Player 1 selects a class
        cc=1
        rc=1
        allcorrect=1
        while allcorrect==1:
            while cc==1:
                player1class = int(input("Choose a class from the list above (please choose a number): \n"))
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
                        P1SPD = 7
                        P1SPDBON = 2
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
                        P1MPBON = 3
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
                        P1MPBON = .5
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
                        q("Please give a valid number.\n")
                        cc=1
                        rc=1
                        s()
                q("1: Yes\n")
                s()
                q("2: No\n")
                s()
                yesorno = int(input("You have chosen " + str(player1class) + ". Is this correct?: \n"))
                s()
                if yesorno == 1:
                    q("Player 1 has chosen the " + str(player1class) + " class.\n")
                    s()
                    q("\n")
                    s()
                    allcorrect=2
                elif yesorno == 2:
                    q("repick your charcter.\n")
                    s()
                    cc=1
                    rc=1
                else:
                    q("Something went wrong please try again\n")
                    s()
                    cc=1
        cc=1
        rc=1
        allcorrect=1
        #Player 2 selects a class
        while allcorrect==1:
            while cc==1:
                q("Please select a classs, player 2\n")
                s()
                rc=1
                player2class = int(input("Choose 1 from the list above (please choose a number): \n"))
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
                        q("you have chosen random\n")
                        player2class=random.randint(1,7)
                        cc=2
                    else:
                        q("Next time put in a valid number \n")
                        s()
                q("1: Yes\n")
                s()
                q("2: No\n")
                s()
                yesorno = int(input("you have chosen " + str(player2class) + ". Is this correct?: \n"))
                s()
                if yesorno == 1:
                    q("Player 2 has chosen the " + str(player2class) + " class.\n")
                    s()
                    q("\n")
                    allcorrect=2
                elif yesorno == 2:
                    q("repick your charcter.\n")
                    s()
                    cc=1
                    rc=1
                else:
                    q("please try again\n")
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
            p1webs=0
            p2webs=0
            p1bandanas=0
            p2bandanas=0
            p1dictionarys=0
            p2dictionarys=0
            p1elmos=0
            p2elmos=0
            p1popbags=0
            p2popbags=0
            p1pop=0
            p2pop=0
        q("Player 1 HP ",P1HP)
        s()
        q("Player 2 HP ",P2HP)
        s()
        q("\n")
        #round start
        q("Player 1 Speed ",P1SPD)
        s()
        q("Player 2 Speed ",P2SPD )
        s()
        q("efuifbwwwo\n")
        while roundnumber < 100:
            turn=1
            q("Round " + str(roundnumber) + " \n")
            s()
            if P1HP <= 0:
                q("Player 2 wins the game\n")
                s()
                winner=player2class
                p2score=p2score+1
                break
            elif P2HP <= 0:
                q("Player 1 wins the game\n")
                s()
                winner=player1class
                p1score=p1score+1
                break
            else:
                q("\n")
                if P1SPD > P2SPD:
                    q("player 1's turn\n")
                    s()
                    q("player 1 has "+ str(P1MP) +" MP left\n")
                    s()
                    q("do one of the following\n")
                    s()
                    q("1: Attack\n")
                    s()
                    q("2: Magic\n")
                    s()
                    q("3: Use an item\n")
                    s()
                    q("4: Run Away\n")
                    s()
                    q("5: pass turn\n")
                    while turn == 1:
                        option=int(input("what would player 1 like to do?: \n"))
                        q("\n")
                        s()
                        critnumber=random.randint(rollp1,20)
                        if option == 1 and critnumber==20:
                            q("\n")
                            q("Player 1 used Attack\n")
                            s()
                            q("Player 1 Rolled a ",critnumber)
                            s()
                            q("Its a Criticle hit!!!\n")
                            s()
                            TOTDMG = (critnumber+(P1ATK*2))-P2DEF
                            if TOTDMG < 0:
                                TOTDMG = 0
                            q("Player 1 did " + str(TOTDMG) + " Damage to Player 2\n")
                            s()
                            P2HP = P2HP-TOTDMG
                            q("player 2 has " + str(P2HP) + " HP Left\n")
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
                            q("\n")
                            q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber<20 and critnumber>=2:
                            q("Player 1 used Attack\n")
                            s()
                            q("Player 1 Rolled a ",critnumber)
                            s()
                            TOTDMG = (critnumber+(P1ATK))-P2DEF
                            if TOTDMG < 0:
                                TOTDMG = 0
                            q("Player 1 did " + str(TOTDMG) + " Damage to Player 2\n")
                            s()
                            P2HP = P2HP-TOTDMG
                            q("Player 2 has " + str(P2HP) + " HP left\n")
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
                            q("\n")
                            q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber == 1:
                            q("Player 1 used Attack\n")
                            s()
                            q("Player 1 Rolled a 1\n")
                            s()
                            q("Player 1 missed\n")
                            s()
                            q("Player 1 did 0 Damage to Player 2\n")
                            s()
                            q("Player 2 has " + str(P2HP) + " HP left\n")
                            s()
                            P2SPD = P2SPD + P2SPDBON
                            if dmgp1 >= 2:
                                P1ATK=P1ATK-DMGBUFFP1
                                dmgp1 = dmgp1-1
                            turn=2
                            roundnumber=roundnumber+1
                            P1MP = P1MP + P1MPBON
                            q("\n")
                            q("Player 1 gained "+ str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        elif option == 2:
                            q("Please do one of the following\n")
                            s()
                            q("0: Cancel\n")
                            s()
                            q("1: Gain +1 DEF\n")
                            s()
                            q("2: Gain an item\n")
                            s()
                            q("3: Better Roll Next Turn-3MP\n")
                            s()
                            q("4: Heal 20 percent of max health-4MP\n")
                            s()
                            q("5: FireBall-5MP\n")
                            s()
                            q("6: Damage boost for every MP you have-2MP\n")
                            s()
                            magic_option=int(input("What would you like to do?: \n"))
                            q("\n")
                            s()
                            if P1MP < magic_option:
                                q("you dont have enough Mana\n")
                                s()
                            elif P1MP >= magic_option:
                                if magic_option == 1:
                                    P1DEF=P1DEF+1
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                elif magic_option==6:
                                    q("Player 1 used Damage boost\n")
                                    s()
                                    P1MP = P1MP - magic_option
                                    DMGBUFFP1=P1ATKBON+P1MP
                                    P1MP=0
                                    dmgp1 = dmgp1+1
                                    P1ATK=DMGBUFFP1 + P1ATK
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                elif magic_option==3:
                                    q("Player 1 used Advantage\n")
                                    rolladp1=2
                                    rollp1=10
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                    turn = 2
                                elif magic_option==5:
                                    q("Player 1 used fireball\n")
                                    s()
                                    fireballdmg = random.randint(12,18)
                                    q("Player 1 did " + str(fireballdmg) + " Damage to Player 2\n")
                                    s()
                                    P2HP=P2HP-fireballdmg
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    P1MP = P1MP - magic_option
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                elif magic_option==4:
                                    q("Player 1 used heal\n")
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
                                    q("\n")
                                elif magic_option==2:
                                    q("Player 1 used gain a random item\n")
                                    s()
                                    P1MP = P1MP - magic_option
                                    bestitem=291
                                    itemspin=random.randint(1,bestitem)
                                    q("You rolled a " + str(itemspin) + " \n")
                                    s()
                                    if itemspin >= 1 and itemspin<= 20:
                                        q("Player 1 Conjured a rusty spoon\n")
                                        s()
                                        q("what a waste of a turn\n")
                                        s()
                                        p1spoons=p1spoons+1
                                    elif itemspin >= 21 and itemspin<= 40:
                                        q("You Conjured Throwing knives\n")
                                        s()
                                        p1knives=p1knives+3
                                    elif itemspin >= 41 and itemspin<= 60:
                                        q("Player 1 Conjured a healing potion\n")
                                        s()
                                        p1pots=p1pots+1
                                    elif itemspin >=61 and itemspin<=80:
                                        arrow=random.randint(2,4)
                                        if p1bows>=1:
                                            q("Player 1 conjured " + str(arrow) + " arrows\n")
                                        elif p1bows==0:
                                            q("player 1 conjured a bow and arrow\n")
                                            s()
                                            p1bows = p1bows + 1
                                            p1arrows=p1arrows+1
                                        else:
                                            q("ERROR\n")
                                    elif itemspin >=81 and itemspin <=90:
                                        q("Player 1 Conjured a fancy hat\n")
                                        s()
                                        p1hats=p1hats+1
                                    elif itemspin >= 91 and itemspin<= 110:
                                        q("Player 1 Conjured a mana potion\n")
                                        s()
                                        p1mpots=p1mpots+1
                                    elif itemspin >= 111 and itemspin<= 130:
                                        q("Player 1 Conjured a sheild\n")
                                        s()
                                        p1sheilds=p1sheilds+1
                                    elif itemspin >= 131 and itemspin<= 150:
                                        q("Player 1 Conjured a pair of new sneakers\n")
                                        s()
                                        p1shoes=p1shoes+1
                                    elif itemspin >= 151 and itemspin<= 170:
                                        q("Player 1 Conjured a...\n")
                                        s()
                                        q("a avocado\n")
                                        s()
                                        p1avocado=p1avocado+1
                                    elif itemspin >= 171 and itemspin<= 190:
                                        q("Player 1 Conjured a can of whipped cream\n")
                                        s()                                        
                                        p1creams=p1creams+1
                                    elif itemspin >= 191 and itemspin<= 210:
                                        q("Player 1 Conjured a spiderweb\n")
                                        s()                                        
                                        p1webs=p1webs+1
                                    elif itemspin >= 211 and itemspin<= 230:
                                        q("Player 1 Conjured a dictionary\n")
                                        s()                                        
                                        p1dictionarys=p1dictionarys+1
                                    elif itemspin >= 231 and itemspin<= 250:
                                        q("Player 1 Conjured a bandana\n")
                                        s()                                        
                                        p1bandanas=p1bandanas+1 
                                    elif itemspin >= 251 and itemspin<= 270:
                                        q("Player 1 Conjured a elmo\n")
                                        s()
                                        p1elmos=p1elmos+1
                                    elif itemspin >= 271 and itemspin<= 290:
                                        q("Player 1 Conjured a bag of popcorn\n")
                                        s()                                        
                                        p1popbags=p1popbags+1
                                    elif itemspin == bestitem:
                                        q("Player 1 Conjured a...\n")
                                        s()
                                        s()
                                        s()
                                        s()
                                        s()
                                        q("wait what..\n")
                                        s()
                                        s()
                                        q("how... why!?!!?\n")
                                        s()
                                        q("why is the in the game (sigh)\n")
                                        s()
                                        s()
                                        q("i don't get paid enough for this\n")
                                        s()
                                        q("Player 1 Conjured a Glock-19\n")
                                        s()
                                        s()
                                        q("...This was not supposed to happen\n")
                                        s()
                                        q("\n")
                                        p1GLOCK19s=p1GLOCK19s+1
                                    else:
                                        q("THIS SHOULDN'T BE POSSIBLE HOW DID I MESS UP THIS BADLY\n")
                                    turn = 2
                                    P2SPD = P2SPD + P2SPDBON
                                    P1MP = P1MP + P1MPBON
                                    q("\n")
                                    q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                                    s()
                                    if P1MAXMP < P1MP:
                                        P1MP = P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP left\n")
                                    s()
                                else:
                                    q("somthing went wrong please try again\n")
                                    s()
                            else:
                                q("try again\n")
                                s()
                        elif option == 4:        
                                q("Are you SURE you want to run away??\n")
                                s()
                                q("1: Yes\n")
                                s()
                                q("2: No\n")
                                s()
                                yesorno=int(input("select an answer: \n"))
                                s()
                                if yesorno==1:
                                    q("you forfiet the game and run away\n")
                                    s()
                                    q("Player 2 wins\n")
                                    s()
                                    P1HP=0
                                    break
                                elif yesorno==2:
                                    q("\n")
                                else:
                                    q("\n")
                        elif option == 3:
                            glocks=0
                            q("Player 1 has " + str(p1pots) + " Healing Potions left\n")
                            s()
                            q("Player 1 has " + str(p1spoons) + " Rusty spoons left\n")
                            s()
                            if p1GLOCK19s>=1:
                                q("THEY HAVE A GUNNN!!!!!!!!\n")
                                s()
                                glocks=1
                            q("Player 1 has " + str(p1knives) + " Knives left\n")
                            s()
                            if p1bows==1:
                                q("Player 1 has a bow and has " + str(p1arrows) + " arrows left\n")
                                s()
                            elif p1bows==0:
                                q("player 1 doesnt have a bow and has " + str(p1arrows) + " arrows left\n")
                            q("player 1 has " + str(p1hats) + " Fancy hats left\n")   
                            s()
                            q("Player 1 has " + str(p1mpots) + " Mana potions left\n")
                            s()
                            q("player 1 had " + str(p1sheilds) + " sheilds left\n")
                            s()
                            q("player 1 has " + str(p1shoes) + " pairs of sneaker left\n")
                            s()
                            q("player 1 has " + str(p1avocado) + " avocado's left\n")
                            s()
                            q("player 1 has " + str(p1pits) + " Pits left\n")
                            s()
                            q("player 1 has " + str(p1creams) + " Cans of whipped cream left\n")
                            s()
                            q("player 1 has " + str(p1webs) + " webs of the spider left\n")
                            s()
                            q("player 1 has " + str(p1dictionarys) + " dictionarys left\n")
                            s()
                            q("player 1 has " + str(p1elmos) + " talking elmos left\n")
                            s()
                            q("Player 1 has " + str(p1popbags) + " popcorn bags left\n")
                            s()
                            q("player 1 has " + str(p1pop) + " peices of popcorn left\n")



                            q("\n")
                            q("1: Use healing potion\n")
                            s()
                            q("2: Throw a rusty spoon\n")
                            s()
                            q("3: Throw a throwing knife\n")
                            s()
                            q("4: shoot an arrow\n")
                            s()
                            q("5: Use a mana potion\n")
                            s()
                            q("6: use the sheild\n")
                            s()
                            q("7: wear a fancy hat\n")
                            s()
                            q("8: wear sneakers\n")
                            s()
                            q("9: eat avocado\n")
                            s()
                            q("10: throw pit\n")
                            s()
                            q("11: eat whipped cream\n")
                            s()
                            q("12: shoot web\n")
                            s()
                            q("13: wear bandana\n")
                            s()
                            q("14: read the dictionary\n")
                            s()
                            q("15: use elmo\n")
                            s()
                            q("16: pop the pocorn bag\n")
                            s()
                            q("17: eat popcorn\n")
                            s()
                            q("0: cancel\n")
                            if glocks==1:
                                q("100000: Shoot\n")
                                s()
                            itemss=1
                            firsttime=1
                            while itemss>=1:
                                if firsttime==2:
                                    glocks=0
                                    q("Player 1 has " + str(p1pots) + " Healing Potions left\n")
                                    s()
                                    q("Player 1 has " + str(p1spoons) + " Rusty spoons left\n")
                                    s()
                                    if p1GLOCK19s>=1:
                                        q("THEY HAVE A GUNNN!!!!!!!!\n")
                                        s()
                                        glocks=1
                                    q("Player 1 has " + str(p1knives) + " Knives left\n")
                                    s()
                                    if p1bows==1:
                                        q("Player 1 has a bow and has " + str(p1arrows) + " arrows left\n")
                                        s()
                                    elif p1bows==0:
                                        q("player 1 doesnt have a bow and has " + str(p1arrows) + " arrows left\n")
                                    q("player 1 has " + str(p1hats) + " Fancy hats left\n")   
                                    s()
                                    q("Player 1 has " + str(p1mpots) + " Mana potions left\n")
                                    s()
                                    q("player 1 had " + str(p1sheilds) + " sheilds left\n")
                                    s()
                                    q("player 1 has " + str(p1shoes) + " pairs of sneaker left\n")
                                    s()
                                    q("player 1 has " + str(p1avocado) + " avocado's left\n")
                                    s()
                                    q("player 1 has " + str(p1pits) + " Pits left\n")
                                    s()
                                    q("player 1 has " + str(p1creams) + " Cans of whipped cream left\n")
                                    s()
                                    q("player 1 has " + str(p1webs) + " webs of the spider left\n")
                                    s()
                                    q("player 1 has " + str(p1dictionarys) + " dictionarys left\n")
                                    s()
                                    q("player 1 has " + str(p1elmos) + " talking elmos left\n")
                                    s()
                                    q("Player 1 has " + str(p1popbags) + " popcorn bags left\n")
                                    s()
                                    q("player 1 has " + str(p1pop) + " peices of popcorn left\n")
                                s()
                                itemchoice=int(input("What would you like to do?: \n"))
                                s()
                                if itemchoice==1 and p1pots >= 1:
                                    q("Player 1 Heals 5 health\n")
                                    s()
                                    P1HP=P1HP+5
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1pots=p1pots-1
                                elif itemchoice==3 and p1knives>=1:
                                    q("Player 1 threw a knife\n")
                                    s()
                                    knifedamage=random.randint(1,5)
                                    P2HP=P2HP-knifedamage
                                    q("Player 1 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    p1knives=p1knives-1
                                elif itemchoice==2 and p1spoons>=1:
                                    q("Player 1 threw a Spoon\n")
                                    s()
                                    spooncrit=random.randint(1,100)
                                    if spooncrit>=1 and spooncrit<=70:
                                        q("the spoon gave Player 2 a small cut and did 1 damage\n")
                                        s()
                                        P2HP=P2HP-1
                                        q("Player 2 has " + str(P2HP) + " HP left\n")
                                        s()
                                    elif spooncrit>=71 and spooncrit<=99:
                                        spoondamage=random.randint(2,10)
                                        q("the spoon gave Player 2 a cut and did " + str(spoondamage) + " Damge to Player 2\n")
                                        s()
                                        P2HP=P2HP-spoondamage
                                        q("Player 2 Has " + str(P2HP) + " HP left\n")
                                        s()
                                    elif spooncrit==100:
                                        q("Player 1 threw the spoon and cut Player 2\n")
                                        s()
                                        q("Player 2 got tetanites and died\n")
                                        s()
                                        P2HP=0
                                    else:
                                        q("ERROR ERROR\n")
                                    p1spoons=p1spoons-1
                                elif itemchoice==100000 and p1GLOCK19s>=1:
                                    q("player 2 was shot and died\n")
                                    P2HP=0
                                    q("stop gun voilence\n")
                                elif itemchoice==0:
                                    q("\n")
                                    itemss=0
                                elif itemchoice==4 and p1bows==1 and p1arrows>=1:
                                    arrowdamage=random.randint(2,5)
                                    P2HP=P2HP-arrowdamage
                                    q("You shot an arrow at player 2 doing " + str(arrowdamage) + " damage to Player 2, Player 2 has " + str(P2HP) + " HP left\n")
                                    p1arrows=p1arrows-1
                                    bbreak=random.randint(1,50)
                                    if bbreak==50:
                                        p1bows=0
                                        q("your bow broke\n")
                                elif itemchoice==5 and p1mpots >= 1:
                                    q("Player 1 regains 5 mana\n")
                                    s()
                                    P1MP=P1MP+5
                                    if P1MAXMP<=P1MP:
                                        P1MP=P1MAXMP
                                    q("Player 1 has " + str(P1MP) + " MP\n")
                                    s()
                                    p1mpots=p1mpots-1
                                elif itemchoice==6 and p1sheilds >= 1:
                                    q("Player 1 sheilds themself and gains 2 def\n")
                                    s()
                                    P1DEF=P1DEF+2
                                    p1sheilds=p1sheilds-1
                                elif itemchoice==7 and p1hats >= 1:
                                    q("Player 1 wears the fancy hat and their max health goes up by 5 and they regain all missing health\n")
                                    s()
                                    P1MAXHP=P1MAXHP+5
                                    P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1hats=p1hats-1
                                elif itemchoice==8 and p1shoes >= 1:
                                    q("Player 1 wears the pair of sneaker and their Speed goes up by 5 and increase Speed bon by 1\n")
                                    s()
                                    P1SPD=P1SPD+5
                                    P1SPDBON=P1SPDBON+.5
                                    s()
                                    p1shoes=p1shoes-1
                                elif itemchoice==9 and p1avocado >= 1:
                                    q("Player 1 Heals 3 health\n")
                                    s()
                                    P1HP=P1HP+3
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1pits=p1pits+1
                                    p1avocado=p1avocado-1
                                elif itemchoice==10 and p1pits>=1:
                                    q("Player 1 threw a pit\n")
                                    s()
                                    knifedamage=random.randint(1,3)
                                    P2HP=P2HP-knifedamage
                                    q("Player 1 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    p1pits=p1pits-1
                                elif itemchoice==11 and p1creams >= 1:
                                    c02pois=random.randint(1,10)
                                    if c02pois==10:
                                        q("player 1 died to carbon dioxide poisening\n")
                                        P1HP=0
                                        break
                                    elif c02pois!=10:
                                        q("Player 1 Heals 5 health and gains 1 Speed\n")
                                        s()
                                        P1HP=P1HP+5
                                        if P1MAXHP<=P1HP:
                                            P1HP=P1MAXHP
                                        q("Player 1 has " + str(P1HP) + " HP\n")
                                        s()
                                        P1SPD=P1SPD+1
                                        p1creams=p1creams-1
                                elif itemchoice==12 and p1webs >= 1:
                                    q("Player 1 shoots a web and slows down player 2\n")
                                    s()
                                    webslow=random.randint(1,8)
                                    P2SPD=P2SPD-webslow
                                    q("player 2 is " + str(webslow) + " speed slower now\n")
                                    s()
                                    p1webs=p1webs-1
                                elif itemchoice==13 and p1bandanas >= 1:
                                    q("Player 1 wears the drippy bandana and gains 1 defense and player 2's atk goes down by 1\n")
                                    s()
                                    P1DEF=P1DEF+1
                                    P2ATK=P2ATK-1
                                    p1bandanas=p1bandanas-1
                                elif itemchoice==14 and p1dictionarys >= 1:
                                    q("Player 1 reads a dictionary and understands a bit more. +1 to max mp\n")
                                    s()
                                    P1MAXMP=P1MAXMP+1
                                    p1dictionarys=p1dictionarys-1
                                elif itemchoice==15 and p1elmos >= 1:
                                    q("Player 1 uses talking elmo\n")
                                    s()
                                    P2MAXMP=P2MAXMP-1
                                    q("player 2 lost 1 max health due to the mental damage\n")
                                    s()
                                    p1elmos=p1elmos-1
                                elif itemchoice==16 and p1popbags >= 1 and P1MP>=3:
                                    q("Player 1 uses 3 mana to heat up some popcorn\n")
                                    s()
                                    P1MP=P1MP-3
                                    popcorn=random.randint(1,20)
                                    p1pop=p1pop+popcorn
                                    p1popbags=p1popbags-1
                                elif itemchoice==16 and p1popbags >=1 and P1MP<3:
                                    q("you dont enough mana to pop this bag\n")
                                    s()
                                elif itemchoice==17 and p1pop >= 1:
                                    eat=int(input("how many peices of popcorn would you like to eat?\n"))
                                    popcorn=random.randint(1,2)
                                    popcorn=popcorn*eat
                                    q("Player 1 Heals " + str(popcorn) + " health\n")
                                    s()
                                    P1HP=P1HP+popcorn
                                    if P1MAXHP<=P1HP:
                                        P1HP=P1MAXHP
                                    q("Player 1 has " + str(P1HP) + " HP\n")
                                    s()
                                    p1pop=p1pop-eat
                                else:
                                    q("you either didnt have the item or you typed in a unavalible number either way your an idiot\n")
                                    s()
                                firsttime=firsttime+1

                        elif option==5:
                            q("You pass you're turn\n")
                            turn = 2
                            P2SPD = P2SPD + P2SPDBON
                            P1MP = P1MP + P1MPBON
                            q("\n")
                            q("Player 1 gained " + str(P1MPBON) + " MP back\n")
                            s()
                            if P1MAXMP < P1MP:
                                P1MP = P1MAXMP
                            q("Player 1 has " + str(P1MP) + " MP left\n")
                            s()
                        else:
                            q("please try again\n")
                            s()
                elif P1SPD < P2SPD:
                    q("player 2's turn\n")
                    s()
                    q("player 2 has "+ str(P2MP) +" MP left\n")
                    s()
                    q("do one of the following\n")
                    s()
                    q("1: Attack\n")
                    s()
                    q("2: Magic\n")
                    s()
                    q("3: Use an item\n")
                    s()
                    q("4: Run Away\n")
                    s()
                    q("5: pass turn\n")
                    while turn == 1:
                        option=int(input("what would player 2 like to do?: \n"))
                        q("\n")
                        s()
                        critnumber=random.randint(rollp2,20)
                        if option == 1 and critnumber==20:
                            q("\n")
                            q("Player 2 used Attack\n")
                            s()
                            q("Player 2 Rolled a ",critnumber)
                            s()
                            q("Its a Criticle hit!!!\n")
                            s()
                            TOTDMG= (critnumber+(P2ATK*2))-P1DEF
                            if TOTDMG < 0:
                                TOTDMG=0
                            q("Player 2 did " + str(TOTDMG) + " Damage to Player 1\n")
                            s()
                            P1HP = P1HP-TOTDMG
                            q("player 1 has " + str(P1HP) + " HP Left\n")
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
                            q("\n")
                            q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber<20 and critnumber>=2:
                            q("Player 2 used Attack\n")
                            s()
                            q("Player 2 Rolled a ", critnumber)
                            s()
                            TOTDMG= (critnumber+P2ATK)-P1DEF
                            if TOTDMG < 0:
                                TOTDMG=0
                            q("Player 2 did " + str(TOTDMG) + " Damage to Player 1\n")
                            s()
                            P1HP = P1HP-TOTDMG
                            q("Player 1 has " + str(P1HP) + " HP left\n")
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
                            q("\n")
                            q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        elif option == 1 and critnumber==1:
                            q("Player 2 used Attack\n")
                            s()
                            q("Player 2 Rolled a 1\n")
                            s()
                            q("Player 2 missed\n")
                            s()
                            q("Player 2 did 0 Damage to Player 1\n")
                            s()
                            q("Player 1 has " + str(P1HP) + " HP left\n")
                            s()
                            P1SPD = P1SPD + P1SPDBON
                            if dmgp2 >= 2:
                                P2ATK==P2ATK-DMGBUFFP2
                                dmgp2=dmgp2-1
                            turn=2
                            roundnumber=roundnumber+1
                            P2MP = P2MP + P2MPBON
                            q("\n")
                            q("Player 2 gained "+ str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        elif option == 2:
                            q("Please do one of the following\n")
                            s()
                            q("0: Cancel\n")
                            s()
                            q("1: Gain +1 DEF\n")
                            s()
                            q("2: Gain an item\n")
                            s()
                            q("3: Better Roll Next Turn-3MP\n")
                            s()
                            q("4: Heal 20 percent of max health-4MP\n")
                            s()
                            q("5: FireBall-5MP\n")
                            s()
                            q("6: Damage boost for every MP you have-2MP\n")
                            s()
                            magic_option=int(input("What would you like to do?: \n"))
                            q("\n")
                            s()
                            if P2MP < magic_option:
                                q("You don't have enough Mana\n")
                            elif P2MP >= magic_option:
                                if magic_option == 1:
                                    P2DEF=P2DEF+1
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                elif magic_option==6:
                                    q("Player 2 used Damage boost\n")
                                    s()
                                    P2MP = P2MP - magic_option
                                    DMGBUFFP2=P2ATKBON+P2MP
                                    P2MP=0
                                    dmgp2 = dmgp2+1
                                    P2ATK=DMGBUFFP2 + P2ATK
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                elif magic_option==3:
                                    q("Player 2 used Advantage\n")
                                    rolladp2=2
                                    rollp2=10
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                    turn = 2
                                elif magic_option==5:
                                    q("Player 2 used fireball\n")
                                    s()
                                    fireballdmg = random.randint(12,18)
                                    q("Player 2 did " + str(fireballdmg) + " Damage to Player 1\n")
                                    s()
                                    P1HP=P1HP-fireballdmg
                                    q("Player 1 has " + str(P1HP) + " HP left\n")
                                    s()
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                elif magic_option==4:
                                    q("Player 2 used heal\n")
                                    s()
                                    P2HP = P2HP + (P2MAXHP/5)
                                    P2MP = P2MP - magic_option
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                    if P2MAXHP < P2HP:
                                        P2HP = P2MAXHP
                                elif magic_option==0:
                                    q("\n")
                                elif magic_option==2:
                                    q("Player 2 used gain a random item\n")
                                    s()
                                    P2MP = P2MP - magic_option
                                    bestitem=291
                                    itemspin=random.randint(1,bestitem)
                                    q("You rolled a " + str(itemspin) + " \n")
                                    s()
                                    if itemspin >= 1 and itemspin<= 20:
                                        q("Player 2 Conjured a rusty spoon\n")
                                        s()
                                        q("what a waste of a turn\n")
                                        s()
                                        p2spoons=p2spoons+1
                                    elif itemspin >= 21 and itemspin<= 40:
                                        q("You Conjured Throwing knives\n")
                                        s()
                                        p2knives=p2knives+3
                                    elif itemspin >= 41 and itemspin<= 60:
                                        q("Player 2 Conjured a healing potion\n")
                                        s()
                                        p2pots=p2pots+1
                                    elif itemspin >=61 and itemspin<=80:
                                        arrow=random.randint(2,4)
                                        if p2bows>=1:
                                            q("Player 2 conjured " + str(arrow) + " arrows\n")
                                        elif p2bows==0:
                                            q("player 2 conjured a bow and arrow\n")
                                            s()
                                            p2bows = p2bows + 1
                                            p2arrows=p2arrows+1
                                        else:
                                            q("ERROR\n")
                                    elif itemspin >=81 and itemspin <=90:
                                        q("Player 2 Conjured a fancy hat\n")
                                        s()
                                        p2hats=p2hats+1
                                    elif itemspin >= 91 and itemspin<= 110:
                                        q("Player 2 Conjured a mana potion\n")
                                        s()
                                        p2mpots=p2mpots+1
                                    elif itemspin >= 111 and itemspin<= 130:
                                        q("Player 2 Conjured a sheild\n")
                                        s()
                                        p2sheilds=p2sheilds+1
                                    elif itemspin >= 131 and itemspin<= 150:
                                        q("Player 2 Conjured a pair of new sneakers\n")
                                        s()
                                        p2shoes=p2shoes+1
                                    elif itemspin >= 151 and itemspin<= 170:
                                        q("Player 2 Conjured a...\n")
                                        s()
                                        q("a avocado\n")
                                        s()
                                        p2avocado=p2avocado+1
                                    elif itemspin >= 171 and itemspin<= 190:
                                        q("Player 2 Conjured a can of whipped cream\n")
                                        s()                                        
                                        p2creams=p2creams+1
                                    elif itemspin >= 191 and itemspin<= 210:
                                        q("Player 2 Conjured a spiderweb\n")
                                        s()                                        
                                        p2webs=p2webs+1
                                    elif itemspin >= 211 and itemspin<= 230:
                                        q("Player 2 Conjured a dictionary\n")
                                        s()                                        
                                        p2dictionarys=p2dictionarys+1
                                    elif itemspin >= 231 and itemspin<= 250:
                                        q("Player 2 Conjured a bandana\n")
                                        s()                                        
                                        p2bandanas=p2bandanas+1 
                                    elif itemspin >= 251 and itemspin<= 270:
                                        q("Player 2 Conjured a elmo\n")
                                        s()
                                        p2elmos=p2elmos+1
                                    elif itemspin >= 271 and itemspin<= 290:
                                        q("Player 2 Conjured a bag of popcorn\n")
                                        s()                                        
                                        p2popbags=p2popbags+1
                                    elif itemspin == bestitem:
                                        q("Player 2 Conjured a...\n")
                                        s()
                                        s()
                                        s()
                                        s()
                                        s()
                                        q("wait what..\n")
                                        s()
                                        s()
                                        q("how... why!?!!?\n")
                                        s()
                                        q("why is the in the game (sigh)\n")
                                        s()
                                        s()
                                        q("i don't get paid enough for this\n")
                                        s()
                                        q("Player 1 Conjured a Glock-19\n")
                                        s()
                                        s()
                                        q("...This was not supposed to happen\n")
                                        s()
                                        q("\n")
                                        p2GLOCK19s=p2GLOCK19s+1
                                    else:
                                        q("THIS SHOULDN'T BE POSSIBLE HOW DID I MESS UP THIS BADLY\n")
                                    turn = 2
                                    P1SPD = P1SPD + P1SPDBON
                                    P2MP = P2MP + P2MPBON
                                    q("\n")
                                    q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                                    s()
                                    if P2MAXMP < P2MP:
                                        P2MP = P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP left\n")
                                    s()
                                else:
                                    q("somthing went wrong please try again\n")
                                    s()
                            else:
                                q("try again\n")
                                s()
                        elif option == 4:        
                                q("Are you SURE you want to run away??\n")
                                s()
                                q("1: Yes\n")
                                s()
                                q("2: No\n")
                                s()
                                yesorno=int(input("select an answer: \n"))
                                s()
                                if yesorno==1:
                                    q("you forfiet the game and run away\n")
                                    s()
                                    q("Player 1 wins\n")
                                    crash=1
                                    while crash==1:
                                        escape=input(": \n")
                                        if escape=="DEVUNLOCK":
                                            crash=2
                                            q("unlocked\n")
                                elif yesorno==2:
                                    q("\n")
                                else:
                                    q("\n")
                        elif option == 3:
                            glocks=0
                            q("Player 2 has " + str(p2pots) + " Healing Potions left\n")
                            s()
                            q("Player 2 has " + str(p2spoons) + " Rusty spoons left\n")
                            s()
                            if p2GLOCK19s>=1:
                                q("THEY HAVE A GUNNN!!!!!!!!\n")
                                s()
                                glocks=1
                            q("Player 2 has " + str(p1knives) + " Knives left\n")
                            s()
                            if p2bows==1:
                                q("Player 2 has a bow and has " + str(p2arrows) + " arrows left\n")
                                s()
                            elif p2bows==0:
                                q("player 2 doesnt have a bow and has " + str(p2arrows) + " arrows left\n")
                            q("player 2 has " + str(p2hats) + " Fancy hats left\n")   
                            s()
                            q("Player 2 has " + str(p2mpots) + " Mana potions left\n")
                            s()
                            q("player 2 had " + str(p2sheilds) + " sheilds left\n")
                            s()
                            q("player 2 has " + str(p2shoes) + " pairs of sneaker left\n")
                            s()
                            q("player 2 has " + str(p2avocado) + " avocado's left\n")
                            s()
                            q("player 2 has " + str(p2pits) + " Pits left\n")
                            s()
                            q("player 2 has " + str(p2creams) + " Cans of whipped cream left\n")
                            s()
                            q("player 2 has " + str(p2webs) + " webs of the spider left\n")
                            s()
                            q("player 2 has " + str(p2dictionarys) + " dictionarys left\n")
                            s()
                            q("player 2 has " + str(p2elmos) + " talking elmos left\n")
                            s()
                            q("Player 2 has " + str(p2popbags) + " popcorn bags left\n")
                            s()
                            q("player 2 has " + str(p2pop) + " peices of popcorn left\n")



                            q("\n")
                            q("1: Use healing potion\n")
                            s()
                            q("2: Throw a rusty spoon\n")
                            s()
                            q("3: Throw a throwing knife\n")
                            s()
                            q("4: shoot an arrow\n")
                            s()
                            q("5: Use a mana potion\n")
                            s()
                            q("6: use the sheild\n")
                            s()
                            q("7: wear a fancy hat\n")
                            s()
                            q("8: wear sneakers\n")
                            s()
                            q("9: eat avocado\n")
                            s()
                            q("10: throw pit\n")
                            s()
                            q("11: eat whipped cream\n")
                            s()
                            q("12: shoot web\n")
                            s()
                            q("13: wear bandana\n")
                            s()
                            q("14: read the dictionary\n")
                            s()
                            q("15: use elmo\n")
                            s()
                            q("16: pop the pocorn bag\n")
                            s()
                            q("17: eat popcorn\n")
                            s()
                            q("0: cancel\n")
                            if glocks==1:
                                q("100000: Shoot\n")
                                s()
                            firsttime=1
                            itemss=1
                            while itemss==1:
                                if firsttime>2:
                                    glocks=0
                                    q("Player 2 has " + str(p2pots) + " Healing Potions left\n")
                                    s()
                                    q("Player 2 has " + str(p2spoons) + " Rusty spoons left\n")
                                    s()
                                    if p2GLOCK19s>=1:
                                        q("THEY HAVE A GUNNN!!!!!!!!\n")
                                        s()
                                        glocks=1
                                    q("Player 2 has " + str(p1knives) + " Knives left\n")
                                    s()
                                    if p2bows==1:
                                        q("Player 2 has a bow and has " + str(p2arrows) + " arrows left\n")
                                        s()
                                    elif p2bows==0:
                                        q("player 2 doesnt have a bow and has " + str(p2arrows) + " arrows left\n")
                                    q("player 2 has " + str(p2hats) + " Fancy hats left\n")   
                                    s()
                                    q("Player 2 has " + str(p2mpots) + " Mana potions left\n")
                                    s()
                                    q("player 2 had " + str(p2sheilds) + " sheilds left\n")
                                    s()
                                    q("player 2 has " + str(p2shoes) + " pairs of sneaker left\n")
                                    s()
                                    q("player 2 has " + str(p2avocado) + " avocado's left\n")
                                    s()
                                    q("player 2 has " + str(p2pits) + " Pits left\n")
                                    s()
                                    q("player 2 has " + str(p2creams) + " Cans of whipped cream left\n")
                                    s()
                                    q("player 2 has " + str(p2webs) + " webs of the spider left\n")
                                    s()
                                    q("player 2 has " + str(p2dictionarys) + " dictionarys left\n")
                                    s()
                                    q("player 2 has " + str(p2elmos) + " talking elmos left\n")
                                    s()
                                    q("Player 2 has " + str(p2popbags) + " popcorn bags left\n")
                                    s()
                                    q("player 2 has " + str(p2pop) + " peices of popcorn left\n")
                                s()
                                itemchoice=int(input("What would you like to do?: \n"))
                                s()
                                if itemchoice==1 and p2pots >= 1:
                                    q("Player 2 Heals 5 health\n")
                                    s()
                                    P2HP=P2HP+5
                                    if P2MAXHP<=P2HP:
                                        P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2pots=p2pots-2
                                elif itemchoice==3 and p2knives>=1:
                                    q("Player 2 threw a knife\n")
                                    s()
                                    knifedamage=random.randint(1,5)
                                    P2HP=P2HP-knifedamage
                                    q("Player 2 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P1HP) + " HP left\n")
                                    s()
                                    p2knives=p2knives-1
                                elif itemchoice==2 and p2spoons>=1:
                                    q("Player 2 threw a Spoon\n")
                                    s()
                                    spooncrit=random.randint(1,100)
                                    if spooncrit>=1 and spooncrit<=70:
                                        q("the spoon gave Player 1 a small cut and did 1 damage\n")
                                        s()
                                        P1HP=P1HP-1
                                        q("Player 1 has " + str(P1HP) + " HP left\n")
                                        s()
                                    elif spooncrit>=71 and spooncrit<=99:
                                        spoondamage=random.randint(2,10)
                                        q("the spoon gave Player 1 a cut and did " + str(spoondamage) + " Damge to Player 1\n")
                                        s()
                                        P1HP=P1HP-spoondamage
                                        q("Player 1 Has " + str(P1HP) + " HP left\n")
                                        s()
                                    elif spooncrit==100:
                                        q("Player 2 threw the spoon and cut Player 1\n")
                                        s()
                                        q("Player 1 got tetanites and died\n")
                                        s()
                                        P1HP=0
                                    else:
                                        q("ERROR ERROR\n")
                                    p2spoons=p2spoons-1
                                elif itemchoice==100000 and p2GLOCK19s>=1:
                                    q("player 1 was shot and died\n")
                                    P1HP=0
                                    q("stop gun voilence\n")
                                elif itemchoice==0:
                                    q("\n")
                                    itemss=0
                                elif itemchoice==4 and p2bows==1 and p2arrows>=1:
                                    arrowdamage=random.randint(2,5)
                                    P1HP=P1HP-arrowdamage
                                    q("You shot an arrow at player 1 doing " + str(arrowdamage) + " damage to Player 1, Player 1 has " + str(P1HP) + " HP left\n")
                                    p2arrows=p2arrows-1
                                    bbreak=random.randint(1,50)
                                    if bbreak==50:
                                        p2bows=0
                                        q("your bow broke\n")
                                elif itemchoice==5 and p2mpots >= 1:
                                    q("Player 2 regains 5 mana\n")
                                    s()
                                    P2MP=P2MP+5
                                    if P2MAXMP<=P2MP:
                                        P2MP=P2MAXMP
                                    q("Player 2 has " + str(P2MP) + " MP\n")
                                    s()
                                    p2mpots=p2mpots-1
                                elif itemchoice==6 and p2sheilds >= 1:
                                    q("Player 2 sheilds themself and gains 2 def\n")
                                    s()
                                    P2DEF=P2DEF+2
                                    p2sheilds=p2sheilds-1
                                elif itemchoice==7 and p2hats >= 1:
                                    q("Player 2 wears the fancy hat and their max health goes up by 5 and they regain all missing health\n")
                                    s()
                                    P2MAXHP=P2MAXHP+5
                                    P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2hats=p2hats-1
                                elif itemchoice==8 and p2shoes >= 1:
                                    q("Player 2 wears the pair of sneaker and their Speed goes up by 5 and increase Speed bon by 1\n")
                                    s()
                                    P2SPD=P2SPD+5
                                    P2SPDBON=P2SPDBON+.5
                                    s()
                                    p2shoes=p2shoes-1
                                elif itemchoice==9 and p2avocado >= 1:
                                    q("Player 2 Heals 3 health\n")
                                    s()
                                    P2HP=P2HP+3
                                    if P2MAXHP<=P2HP:
                                        P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2pits=p2pits+1
                                    p2avocado=p2avocado-1
                                elif itemchoice==10 and p2pits>=1:
                                    q("Player 2 threw a pit\n")
                                    s()
                                    knifedamage=random.randint(1,3)
                                    P2HP=P2HP-knifedamage
                                    q("Player 2 did " + str(knifedamage) + " Damage to Player 2\n")
                                    s()
                                    q("Player 2 has " + str(P2HP) + " HP left\n")
                                    s()
                                    p2pits=p2pits-1
                                elif itemchoice==11 and p2creams >= 1:
                                    c02pois=random.randint(1,10)
                                    if c02pois==10:
                                        q("player 1 died to carbon dioxide poisening\n")
                                        P1HP=0
                                        break
                                    elif c02pois!=10:
                                        q("Player 2 Heals 5 health and gains 1 Speed\n")
                                        s()
                                        P2HP=P2HP+5
                                        if P2MAXHP<=P2HP:
                                            P2HP=P2MAXHP
                                        q("Player 2 has " + str(P2HP) + " HP\n")
                                        s()
                                        P2SPD=P2SPD+1
                                        p2creams=p2creams-1
                                elif itemchoice==12 and p2webs >= 1:
                                    q("Player 2 shoots a web and slows down player 1\n")
                                    s()
                                    webslow=random.randint(1,8)
                                    P1SPD=P1SPD-webslow
                                    q("player 1 is " + str(webslow) + " speed slower now\n")
                                    s()
                                    p2webs=p2webs-1
                                elif itemchoice==13 and p1bandanas >= 1:
                                    q("Player 2 wears the drippy bandana and gains 1 defense and player 1's atk goes down by 1\n")
                                    s()
                                    P2DEF=P2DEF+1
                                    P1ATK=P1ATK-1
                                    p2bandanas=p2bandanas-1
                                elif itemchoice==14 and p2dictionarys >= 1:
                                    q("Player 2 reads a dictionary and understands a bit more. +1 to max mp\n")
                                    s()
                                    P2MAXMP=P2MAXMP+1
                                    p2dictionarys=p2dictionarys-1
                                elif itemchoice==15 and p2elmos >= 1:
                                    q("Player 2 uses talking elmo\n")
                                    s()
                                    P1MAXMP=P1MAXMP-1
                                    q("player 1 lost 1 max health due to the mental damage\n")
                                    s()
                                    p2elmos=p2elmos-1
                                elif itemchoice==16 and p2popbags >= 1 and P2MP>=3:
                                    q("Player 2 uses 3 mana to heat up some popcorn\n")
                                    s()
                                    P2MP=P2MP-3
                                    popcorn=random.randint(1,20)
                                    p2pop=p2pop+popcorn
                                    p2popbags=p2popbags-1
                                elif itemchoice==16 and p2popbags >=1 and P2MP<3:
                                    q("you dont enough mana to pop this bag\n")
                                    s()
                                elif itemchoice==17 and p2pop >= 1:
                                    eat=int(input("how many peices of popcorn would you like to eat?\n"))
                                    popcorn=random.randint(1,2)
                                    popcorn=popcorn*eat
                                    q("Player 2 Heals " + str(popcorn) + " health\n")
                                    s()
                                    P2HP=P2HP+popcorn
                                    if P2MAXHP<=P2HP:
                                        P2HP=P2MAXHP
                                    q("Player 2 has " + str(P2HP) + " HP\n")
                                    s()
                                    p2pop=p2pop-eat
                                else:
                                    q("you either didnt have the item or you typed in a unavalible number either way your an idiot\n")
                                    s()
                                firsttime=firsttime+1,

                        elif option==5:
                            q("You pass you're turn\n")
                            turn = 2
                            P1SPD = P1SPD + P1SPDBON
                            P2MP = P2MP + P2MPBON
                            q("\n")
                            q("Player 2 gained " + str(P2MPBON) + " MP back\n")
                            s()
                            if P2MAXMP < P2MP:
                                P2MP = P2MAXMP
                            q("Player 2 has " + str(P2MP) + " MP left\n")
                            s()
                        else:
                            q("please try again\n")
                            s()
                elif P1SPD == P2SPD:
                    q("you have the same speed\n")
                    s()
                    q("choosing a random player to go\n")
                    s()
                    a= random.randint(1,2)
                    if a==1:
                        P1SPD=P1SPD+1
                    else:
                        P2SPD=P2SPD+1
                else:
                    q("UH OH\n")
            q("\n")
            q("Player 1 HP left ",P1HP)
            s()
            q("Player 2 HP left ",P2HP)
        q("winner winner chicken dinner\n")
        q("\n")
        s()
        q("\n")
        q("score " + str(p1score) + " to " + str(p2score))
        q("\n")
        q("\n")
        q("Play again?\n")
        s()
        q("1: Yes\n")
        s()
        q("0: No\n")
        s()
        playagain=int(input("Play again?: \n"))
    while playagain==4:
        q("2\n")
    while playagain==5:
        q("Don't cheat\n")
q("OvO\n")
