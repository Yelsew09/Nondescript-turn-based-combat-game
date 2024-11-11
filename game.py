import random, time, sys
def crash():
    q("Something went wrong. Crashing...")
    try:
        crash()
    except:
        crash()
def wait(temporal_distance):
    time.sleep(temporal_distance)
def confirm():
    confirm = input("")
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
def q(str):
    for char in str:
        q(char, end='')
        sys.stdout.flush()
        time.sleep(.02)
def boom():
    option = int(input(''))
    return option

q("Welcome to Dungeons and Damage.\n")
wait(1)
q("Not to be confused with Dungeons and Dragons.\n")
wait(1)
q("There are no dungeons here, but there is a lot of damage.\n")
wait(1)
q("Informally known as HELL.\n")
wait(1)
q("1: Play the game\n")
wait(.15)
q("2: Guide\n")
wait(.15)
q("3: Options\n")
wait(.15)


ac = 0
while ac == 0:
    q("What would you like to do? ")
    option = int(input(''))
    wait(.5)
    
    
    if option == 2:
        q("Guide coming soon")
    
    
    elif option == 3:
        q("Options coming soon")
    
    
    elif option == 1:
        gc = 0
        while gc == 0:
            q("1: Knight\n")
            wait(.15)
            q("2: Peashooter\n")
            wait(.15)
            q("3: Mage\n")
            wait(.15)
            q("4: Rouge\n")
            wait(.15)
            q("5: Skele\n")
            wait(.15)
            q("6: Bard\n")
            wait(.15)
            q("7: Barbarian\n")
            wait(.15)
            q("8: Random\n")
            cc = 0
            while cc == 0:
                q("Please select a class, Player 1\n")
                option = boom()
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
                        q("Please choose a valid option")
                ync = 0
                while ync == 0:
                    q("1: Yes\n")
                    wait(.15)
                    q("2: No\n")
                    wait(.15)
                    q("Player 1 has chosen the " + str(option) + " class, is this correct? ")
                