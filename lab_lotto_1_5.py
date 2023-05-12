#+++++++Moritz Holzerbauer++++++++++
#++++++++Lotto_Laborübung+++++++++++
#++++++++++12.05.2023+++++++++++++++

import random #Lib einfügen

b = 0 #variable vergeben
zahl =[]


int_t = int(input("Bitte geben Sie ein, wie viele Tipps sie abgeben möchten: ")) #Anzahl der tipps

if int_t <=5: 
    while b <int_t:
        x = random.randint(1,45)#random zahl zwischen 1 und 45
        if x in zahl: #wenn x in in zahl schon vorhanden vorgang wiederholen
            b = b  
        else:
            zahl.append(x)
            b+=1

    print("Ihre zufälligen Zahlen sind: ", zahl)

else:
    print("Maximal 5 Tipps!")