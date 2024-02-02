#1
n=int(input())
for i in range(n):
    print(" /V\\n / V \\n / V V \\n /VV V VV\ ")
for j in range(1,9):
    for i in range(1,9):
        print(i,end="/V\\n / V \\n / V V \\n /VV V VV\ ")
    print()

#4
n= int(input("sisestage suur arv: "))
paaritu= 0 
veider= 0
for i in n: 
    if i % 2 == 0:
        paaritu += 1
    else:
        veider += 1
print(paaritu, veider)

#3
n = random.number(0,100)
print(n)
positivne=0
mitu=0
for i in range(n):
    randomNumber=random.number(-100,100)
    if randomNumber>0:
        positivne +=1
    mitu +=1
print("positivne: ", positivne)

#5
Summa=0
A=int(input("kirjutage number A: "))
B=int(input("kirjutage number B: "))
for i in range(A,B +1):
    Summa +=1
print(Summa)

while True:
    try:
        mitu=int(input("Mitu tk: "))
        if 1<=mitu<10:
            break
    except ValueError:
        print("Vale tuup")

for i in range(mitu):
    print(' /V\ '.center(10,' '),end="")
print()
for i in range(mitu):
    print(' / V \ '.center(10,' '),end="")
print()
for i in range(mitu):
    print(' / V V \ '.center(10,' '),end="")
print()
for i in range(mitu):
    print(' /VV V VV\ '.center(10,' '),end="")
print()

from curses.ascii import NAK
from lib2to3.pgen2.token import NAME
from random import *
from ssl import HAS_SSLv2, HAS_TLSv1
from webbrowser import MacOSX
sum_num=0
sum_km=0
for i in range(12):
    num=randint(1000,100000)
    km=randint(1,1000)
    sum_num+=num 
    sum_km+=km
    print(f"{i+1}. maakond. \nEnlanik: {num}. Pindala: {km}\n Kokku: {sum_num},{sum_km}")
vastus=sum_num/sum_km
print(f"Keskmine: {vastus:.3f}")

from random import *
while True:
    try:
        K=int(input("Mitu kotleti sul on? "))
        if K>0:break 
    except ValueError:
        print("Vale tuup")
while True:
    try:
        M=int(input("Mitu kotleti ühel pannil? "))
        if M>0:break 
    except ValueError:
        print("Vale tuup")
pann=0
while K>0:
    if K>=M:
        K-=M 
        pann+=1
    else:
        lisapann+=1
        print(f"Praetud: {lisapann} tk")
        break
print(f"Täispannid: {pann} ja veel om vaja {lisapann}")

N=25
kesk1=0
kesk2=0
for i in range(N):
    h1=randint(1,5)
    h2=randint(1,5)
    kesk1+=h1 
    kesk2+=h2 
kesk1/=N 
kesk2/=N 
print(f"Keskmine hinn 1 klassis on {kesk1}") 
print(f"Keskmine hinn 2 klassis on {kesk2}") 

