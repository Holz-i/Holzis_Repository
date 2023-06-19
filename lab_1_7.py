def summe(a, b):
    return a + b

def differenz(a, b):
    return a - b

def main():
    try:
        zahl1 = float(input("Zahl 1: "))
        zahl2 = float(input("Zahl 2: "))
        
        ergebnis_summe = summe(zahl1, zahl2)
        ergebnis_differenz = differenz(zahl1, zahl2)
        
        print("Summe:", ergebnis_summe)
        print("Differenz:", ergebnis_differenz)
        
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")

main()