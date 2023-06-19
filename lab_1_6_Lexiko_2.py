deutsch = ["Haus", "Baum", "Auto", "Tisch", "Stuhl"]
englisch = ["house", "tree", "car", "table", "chair"]

while True:
    eingabe = input("Geben Sie ein deutsches Wort ein (oder 'exit' zum Beenden): ")

    index = -1  # Index zur Speicherung des gefundenen deutschen Worts

    for i in range(len(deutsch)):
        if deutsch[i] == eingabe:
            index = i
            break

    if index != -1:
        print("Englische Übersetzung:", englisch[index])
    else:
        print("Das eingegebene Wort ist nicht verfügbar.")

    if eingabe == "exit":
        print("Das Programm wird beendet.")
        break

