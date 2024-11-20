"""
this project was made by emilio
"""

pa=1
from distutils.command.build_scripts import first_line_re
import sys, time, random
def q(str,anything):
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(.03)
    time.sleep(anything)
q("Welcome to the program this program does all sorts of things such as\n",.3)
while pa==1:
    q("1: Multiplication Table Generator\n",.1)
    q("2: Simple Password Authentication\n",.1)
    q("3: FizzBuzz Challenge\n",.1)
    q("4: Factorial Calculator\n",.1)
    q("5: Prime Number Checker\n",.1)
    q("6: Word or Sentence Reversal\n",.1)
    q("7: Countdown Timer\n",.1)
    q("8: Summing a Series of Numbers\n",.1)
    q("what would you like to do? ",0)
    pay=int(input(": "))
    if pay==1:
        q("You have chosen Multiplication Table Generator\n",.3)
        q("Put the number you want multibliction table of?",0)
        fir=int(input(": "))
        q("Put the number of how long the table is",0)
        sec=int(input(": "))
        sec=sec+1
        fer=fir
        for i in range(sec):
            qe=i+1
            q(str(qe) + " * " + str(fer) + " = ",.5)
            q(str(fir),.2)
            q("\n",0)
            fir=fir+fer
    elif pay==2:
        q("You have chosen Simple Password Authentication\n",.3)
        q("Please give your password",0)
        pas=input(": ")
        corpas=1
        while corpas==1:
            q("Restate your password",0)
            chec=input(": ")
            if chec==pas:
                q("Correct\n",.2)
                corpas=2
            elif chec!=pas:
                q("Wrong\n",.2)
            else:
                q("Their has been an error in the program",.2)
    elif pay==3:
        q("You have chosen FizzBuzz challenge\n",.3)
        q("The program picks a random number 1-100 if its a multible of 3 it says Fizz if its a multible of 5 it say Buzz if its a multible of both it says FizzBuzz\n",.2)
        wq=1
        while wq==1:    
            fb=random.randint(1,100)
            if fb % 3 == 0:
                q("Fizz",.2)
            if fb % 5 == 0:
                q("Buzz",.2)
            if fb % 5 !=0 and fb % 3 !=0:
                q(str(fb),.2)
            q("\n",0)
            q("1: Yes\n",.1)
            q("2: No\n",.1)
            q("would you like to continue the Fizz Buzz Challenge?",0)
            wq=int(input(": "))
    elif pay==4:
        q("You have chosen factorial calculator\n",.3)
        q("Insert a number",0)
        m=1
        r=int(input(": "))
        d=r
        while m==1:
            a=d-1
            d=d-1
            if a > 0:
                q(str(r) + " * " + str(a) + "\n",0)
                r=r*a
            else:
                q(str(r) + "\n",0)
                m=0
    elif pay==5:
        q("You have chosen prime number checker\n",.3)
        q("This feature of the program will probally never be added tbh i don't like prime numbers")
    elif pay==6:
        q("You have chosen Word or Sentence Reversal\n",.3)
        b=0
        v=0
        k=0
        o=1
        r=input(": ")
        z=r
        while k==0:
            for char in z:
                b=b+1
            if b<0:
                q("\n",0)
                break
            for char in z:
                v=v+1
                if v==b:
                    q(str(char),.1)
            v=0
            b=0-o
            o=o+1
    elif pay==7:
        q("You have chosen Countdown Timer\n",.3)
        q("This feature of the program will be added soon")
    elif pay==8:
        q("Summing a Series of Numbers\n",.1)
        q("Insert a number",0)  
    else:
        q("that was an invalid")
    q("1: Yes\n",.1)
    q("2: No\n",.1)
    q("Would you like to use this program again?",0)
    pa=int(input(": "))
