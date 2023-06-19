def summe(a, b):
    return a + b

def differenz(a, b):
    return a - b

def main():
    try:
        a = float(input("Zahl 1: "))
        b = float(input("Zahl 2: "))
        
        ergebnis_summe = summe(a, b)
        ergebnis_differenz = differenz(a, b)
        
        print("Summe:", ergebnis_summe)
        print("Differenz:", ergebnis_differenz)
        
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")

main()






