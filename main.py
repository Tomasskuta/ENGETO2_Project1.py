def hlavni_menu():
    volba_menu = input("Vyberte možnost (1-4):")
    if volba_menu == 1:
        pridat_ukol()
    elif volba_menu == 2:
        zobrazit_ukoly()
    elif volba_menu == 3:
        odstranit_ukol()
    else:
        exit()

def pridat_ukol():
    print("pridat")

def zobrazit_ukoly():
    print("zobrazit")
    
def odstranit_ukol():
    print("odstranit")


hlavni_menu()