
while True:
    try:
        choice = int(input("Pour convertir des pouces en cm tapez 1 \nPour convertir des cm en pouces tapez 2 \n"))
        print
    except ValueError:
            print("Veuillez entrer un nombre valide")
            continue
    if choice > 2 or choice < 0:
        print("Vous avez le choix entre 1 et 2")
        continue
    elif choice == 1:
        pouces = float(input("Entrez le nombre de pouces à convertir en cm : "))
        cm = pouces * 2.54
        print(f"Vos {pouces} pouces font {cm} centimetres")
    else:
        cm = float(input("Entrez le nombre de centimetres à convertir en pouces : "))
        pouces = cm / 2.54
        print(f"Vos {cm} centimetres font {pouces} pouces")
    if input("Voulez-vous continuer ? (o/n) : ") == "n":
        break
    else:
        continue