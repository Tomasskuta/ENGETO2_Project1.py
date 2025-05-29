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
        try:
            volba_menu = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            print("Zadejte platné číslo mezi 1 a 4!")
            continue
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
    if not ukoly:
        print("Seznam úkolů je prázdný. Není co zobrazit.")
        return
    i = 1
    print("Seznam úkolu: ")
    for ukol in ukoly:
        print(str(i) + (". ") + ukol)
        i += 1
    
def odstranit_ukol():
    while True:
        if not ukoly:
            print("Seznam úkolů je prázdný. Není co odstraňovat.")
            return
        zobrazit_ukoly()
        print("\n")
        print("\n")
        vymaz_ukol = int(input("Zadejte číslo úkolu, který chcete odstranit: ")) - 1
        if vymaz_ukol + 1 <= len(ukoly):
            ukoly.pop(vymaz_ukol)
            print("Úkol "+"'"+str(vymaz_ukol+1)+"'"+" byl odstraněn.")
            hlavni_menu()
        else:
            print("Tento úkol neexistuje!")


hlavni_menu()
