ukoly = []

def hlavni_menu():
    while True:
        volba_menu = int(input("Vyberte možnost (1-4): "))
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
    nazev_ukol = input("Zadejte název úkolu: ")
    popis_ukol = input("Zadejte popis úkolu: ")
    ukol = nazev_ukol + (" - ") + popis_ukol

    ukoly.append(ukol)
    print("Úkol " +nazev_ukol +" byl přidán.")

def zobrazit_ukoly():
    i = 1
    for ukol in ukoly:
        i = +i
        print(str(i) + (". ") + ukol)
    
def odstranit_ukol():
    vymaz_ukol = int(input("Zadejte číslo úkolu, který chcete odstranit: ")) - 1
    
    ukoly.pop(vymaz_ukol)


hlavni_menu()
