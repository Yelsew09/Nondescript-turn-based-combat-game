cc = 0
            while cc == 0:
                
                if P1SPD > P2SPD:
                    if P1HP <= 0 and P2HP <= 0:
                        q("You somehow killed each other.\n",0)
                        wait(.15)
                        q("Congrats.\n",0)
                        wait(.5)
                        
                    elif P1HP <= 0:
                        q("Player 1 has " + str(P1HP) + " left.\n",0)
                        wait(.15)
                        q("This, unfortunatly, means he is dead and cannot continue on.\n",0)
                        wait(.15)
                        q("Player 2 wins!\n",0)
                        wait(.15)
                        q("1: Yes")
                        wait(.15)
                        q("2: No")
                        wait(.15)
                        q("Play again? ",0)
                        oc = 0
                        while oc == 0:
                            option = int(input(''))
                            if option == 1:
                                oc = 1
                                cc = 1
                                gc = 0
                                q("Restarting the program, please wait.\n",0)
                                wait(5)
                            elif option == 2:
                                oc = 1
                                gc = 1
                                cc = 1
                                wait(.5)
                            else:
                                q("Please give a valid option\n",0)
                    elif P2HP <= 0:
                        q("Player 2 has " + str(P2HP) + " left.\n",0)
                        wait(.15)
                        q("This, fortunately, means he is dead and cannot continue on.\n",0)
                        wait(.15)
                        q("Player 1 wins!!!\n",0)
                        wait(.15)
                        q("1: Yes\n",0)
                        wait(.15)
                        q("2: No\n",0)
                        wait(.15)
                        q("Play again?")
                        oc = 0
                        while oc == 0:
                            option = int(input(''))
                            if option == 1:
                                oc = 1
                                cc = 1
                                gc = 0
                                q("Restarting the program, please wait.\n",0)
                                wait(5)
                            elif option == 2:
                                oc = 1
                                gc = 1
                                cc = 1
                                wait(5)
                    else:
                        q("Player 1 has " + str(P1HP) + "/" + str(P1MAXHP) + "HP left, and " + str(P1MP) + "/" + str(P1MAXMP) + "MP left.\n",0)
                        wait(.15)
                        q("Player 2 has " + str(P2HP) + "/" + str(P2MAXHP) + "HP left, and " + str(P2MP) + "/" + str(P2MAXMP) + "MP left.\n",0)
                        wait(.15)
                        q("Player 1's turn.\n",0)
                        wait(.15)
                        oc = 0
                        while oc == 0:
                            q("1: Attack")
                            wait(.15)
                            q("2: Magic")
                            wait(.15)
                            q("3: Use an item\n",0)
                            wait(.15)
                            q("4: Pass turn\n",0)
                            wait(.15)
                            q("5: Run away (forfeit)\n",0)
                            wait(.15)
                            q("What would you like to do? ")
                            option = int(input(''))
                            wait(.5)
                            if option == 1:
                                critnumber = critnum(P1AD,1,20)
                                if critnumber == 20:
                                    q("IT'S A CRITICAL HIT!!!\n",0)
                                    wait(.15)
                                    q("Player 1 did " + str(P1ATK*2) + " damage to player 2\n",0)
                                    wait(.15)
                                    P2HP = P2HP - (P1ATK*2)
                                    q("Player 2 has " + str(P2HP) + "HP left\n",0)
                                    wait(.15)
                                elif critnumber + P1ATKBON >= P2DEF:
                                    q("Player 1 rolled a " + str(critnumber) + " landed a hit, doing " + str(P1ATK) + " damage to player 2.\n",0)
                                    wait(.15)
                                    P2HP = P2HP - P1ATK
                                    q("Player 2 has " + str(P2HP) + "HP left.\n",0)
                                    wait(.15)
                                elif critnumber + P1ATKBON < P2DEF:
                                    q("Player 1 rolled a " + str(critnumber) + ", missing their attack.\n",0)
                                else:
                                    explode()
                            elif option == 2:
                                q("1: Fireball - 5MP\n",0)
                                wait(.15)
                                q("2: Summon a random item - 2MP\n",0)
                                wait(.15)
                                q("3: Gain advantage on your next turn - 5MP\n",0)
                                wait(.15)
                                q("4: Impose disadvantage on your opponent's next attack - 5MP\n",0)
                                wait(.15)
                                q("5: Heal 20 percent of your max health - 5MP\n",0)
                                wait(.15)
                                q("6: Gain a damage boost on your next attack - Varies\n",0)
                                wait(.15)
                                q("Currently 7: Spell descriptions")
                                wait(.15)
                                q("0: Cancel\n",0)
                                wait(.15)
                                mc = 0
                                while mc == 0:
                                    q("What would you like to do? ")
                                    option = int(input(''))
                                    wait(.5)
                                    if option == 1:
                                        if P1MP < 5:
                                            q("You don't have enough MP to do that.\n",0)
                                            wait(.15)
                                        elif P1MP >= 5:
                                            critnumber = critnum(0,12,18)
                                            q("Player 1 did " + str(critnumber) + " damage to player 2.\n",0)
                                            wait(.15)
                                            P1MP = P1MP - 5
                                        else:
                                            explode()
                                    elif option == 2:
                                        critnumber = critnum(0,1,100)
                                        if critnumber >= 1 and critnumber <= 10:
                                            q("You conjured up a...\n",0)
                                            wait(.5)
                                            q("Rusty...",.5)
                                            wait(.6)
                                            q("Spoon?\n",0)
                                            P1SPOON = P1SPOON + 1
                                        elif critnumber >= 11 and critnumber <= 55:
                                            q("You conjured up a few throwing knives\n",0)
                                            wait(.25)
                                            P1KNIVES = P1KNIVES + 3
                                        elif critnumber >= 56 and critnumber <= 99:
                                            q("You got a healing potion!\n",0)
                                            wait(.2)
                                            P1POTS = P1POTS + 1
                                        elif critnumber == 100:
                                            if P1GLOCK == 0 and P2NARRATORS == 1:
                                                q("Ok, great. Now the OTHER guy has a gun.\n",.2)
                                                wait(.3)
                                                q("I'm leaving.\n",.2)
                                                wait(.5)
                                                P1NARRATORS = 1
                                            elif P1NARRATORS > 0:
                                                q("You did it again.\n",.4)
                                                wait(1)
                                                q("Landed a 1 in 100 chance to get a literal GUN.\n",.3)
                                                wait(1)
                                                q("That thing could've won you the game intstanly.\n",.1)
                                                wait(1)
                                                q("And you kept going.",.1)
                                                wait(.8)
                                                print(" ")
                                                q("WHY?!?!?\n",0)
                                                wait(1)
                                                q("Alright, I'm ending this here and now.\n",0)
                                                wait(1)
                                                q("God landed a destructive hit, doing " + str(999+P2HP) + " damage to player 2.\n",0)
                                                wait(.15)
                                                q("Player 2 has " + str(P2HP) + "HP left.\n",0)
                                                wait(.5)
                                            elif P1GLOCK == 0 and not P2NARRATORS == 1:
                                                q("You conjured up a...",0)
                                                wait(.2)
                                                q("GUN?!?!?!?\n",.01)
                                                wait(.2)
                                                q("Like, not even an old gun like a musket.\n",0)
                                                wait(.4)
                                                q("It's just a Glock-19\n",0)
                                                wait(5)
                                                q("I quit\n",0)
                                                wait(.5)
                                            else:
                                                explode()
                                        else:
                                            explode()
                                    elif option == 5:
                                        if P1MP < 4:
                                            q("You don't have enough MP for that.\n",0)
                                            wait(.5)
                                        else:
                                            q("You gained advantage on your next turn.\n",0)
                                            wait(.5)
                                            P1AD = 1
                                            P1ADTR = 2
                                            P1MP = P1MP - 5
                                            mc = 1
                                            oc = 1
                                    elif option == 4:
                                        if P1MP < 5:
                                            q("You don't have enough MP for that\n",0)
                                            wait(.5)
                                        else:
                                            if P2AD == 1:
                                                q("You got rid of your opponent's advantage.")
                                                wait(.5)
                                                P2AD = 0
                                                P2ADTR = 0
                                                mc = 1
                                                oc = 1
                                    elif option == 5:
                                        if P1MP < 5:
                                            q("You don't have enough MP for that.\n",0)
                                            wait(.15)
                                        else:
                                            HEAL = P1HP/5
                                            HEAL = round(HEAL,0)
                                            q("Player 1 healed " + str(HEAL) + "HP.\n",0)
                                            
                                            
                elif P2SPD > P1SPD:
                    q("Let player 2 go first, then player 1\n",0)
                    gc = 1
                    ac = 1
                    cc = 1
                elif P1SPD == P2SPD:
                    q("Since you both have the same speed, we are randomly determining who will go first.\n",0)
                    option = random.randint (1,2)
                    if option == 1:
                        P1SPD = P1SPD + 1
                        q("Player 1 is going first.\n",0)
                    elif option == 2:
                        P2SPD = P2SPD + 1
                        q("Player 2 is going first.\n",0)
                    else:
                        explode()
                else:
                    explode()