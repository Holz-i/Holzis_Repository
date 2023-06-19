while True:
    try:
        a = int(input("Zahl 1: "))  # int a
        break
    except ValueError:
        print("Nur Zahlen bitte")

while True:
    try:
        b = int(input("Zahl 2: "))  # int b
        if b != 0:
            break
        else:
            print("Die zweite Zahl darf nicht 0 sein.")
    except ValueError:
        print("Nur Zahlen bitte")

print("Sum a+b =", a + b)
print("Dif a-b =", a - b)
print("Dif b-a =", b - a)
print("Pro a*b =", a * b)

if a != 0 and b != 0:
    print("Quo a/b =", a / b)
    print("Quo b/a =", b / a)

while b == 0 or a == 0:
    print("DIV 0!")
    a = int(input("Neue Zahl 1 eingeben: "))
    b = int(input("Neue Zahl 2 eingeben: "))

if a != 0 and b != 0:
    print("Quo a/b =", a / b)
    print("Quo b/a =", b / a)