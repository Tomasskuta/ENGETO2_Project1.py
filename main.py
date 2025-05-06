ukoly = []

def hlavni_menu():
    while True:
        print("\n")
        print("=================================")
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        print("=================================")
        volba_menu = int(input("Vyberte možnost (1-4): "))
        print("\n")
        if volba_menu in range(1,5):
            if volba_menu == 1:
                pridat_ukol()
            elif volba_menu == 2:
                zobrazit_ukoly()
            elif volba_menu == 3:
                odstranit_ukol()
            else:
                exit()
        else:
            print("Volba musí být v rozmezí 1-4! ")
            

def pridat_ukol():
    while True:
        nazev_ukol = input("Zadejte název úkolu: ")
        popis_ukol = input("Zadejte popis úkolu: ")
        if len(nazev_ukol) and len(popis_ukol) > 0:
            ukol = nazev_ukol + (" - ") + popis_ukol

            ukoly.append(ukol)
            print("Úkol " +"'"+nazev_ukol+"'" +" byl přidán.")
            hlavni_menu()
        else:
            print("Název a popis úkolu musí obsahovat text! ")

def zobrazit_ukoly():
    i = 1
    for ukol in ukoly:
        i = +i
        print("Seznam úkolu: ")
        print(str(i) + (". ") + ukol)
    
def odstranit_ukol():
    zobrazit_ukoly()
    print("\n")
    print("\n")
    vymaz_ukol = int(input("Zadejte číslo úkolu, který chcete odstranit: ")) - 1
    ukoly.pop(vymaz_ukol)


hlavni_menu()
