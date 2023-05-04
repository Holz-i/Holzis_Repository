c=input("Geben Sie ihren Namen an: ") #Nur String eingabe (erklärung für sitznachbar) wert auf c überschreiben

a=int(input("Zahl 1: ")) #Eingabeauforderung und den Input (string) auf int definieren wert auf a überschreiben    

b=int(input("Zahl 2: ")) #Eingabeauforderung und den Input (string) auf int definieren wert auf b überschreiben  

print("Herzlich Wilkommen: "+ c) #Ausgabe auf den Monitor mit dem vorher eingetragenen Namen

if b == 0: #If Bedienung wird mit Einzug gestartet und beendet
    print("leider sind Ihre Zahlen falsch")
    print("!Geben Sie neue Zweite Zahl ungleich 0 ein!")
    a=int(input("Zahl 1: "))     
    b=int(input("Zahl 2: "))
    print(a+b)  
    print(a-b)  
    print(a/b)  
    print(a*b)
    
    
    
else:
    print(a+b)  #plus mit Ausgabe
    print(a-b)  #minus mit Ausgabe
    print(a/b)  #durch mit Ausgabe
    print(a*b)  #mal mit Ausgabe
    
print("Danke für die Nutzung meines Programmes, ich wünsche einen wunderschönen Tag!")

