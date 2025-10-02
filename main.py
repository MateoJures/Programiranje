#Funkcija za učitavanje teksta iz datoteke 
def ucitaj_tekst(filepath):
    try:
        # KOd za otvaranje datoteke ide ovdje
        with open (filepath, 'r', encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Greška: Datoteka na putanji '{filepath}' nije pronađena")
        return None # Vratit ćemo 'ništa' ako datoteka ne postoji
      
      # Funkcija za proišćavanje teksta 
def ocisti_tekst(tekst):
#Kod za pročišćavanje teksta ide ovdje
    tekst = tekst.lower()
    interpunkcija = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')

    lista_rijeci = tekst.split()
    
    return lista_rijeci

 #Funkcija za brojanje frekvencije riječi u tekstu
def broj_frekcenciju(lista_rijeci):
    #1. kreiramo prazan riječnik koji će čuvati rezultate
    rjec_frekvencija = {}

    #2. prolazimo kroz svaku riječ u primljenoj listi
    for rijec in lista_rijeci:
        if rijec in lista_rijeci:
            srjecnik_frekvencija[rijec] += 1
        else:
            rjecnik_frekvencija[rijec] = 1

    return rjecnik_frekvencija

STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da', 'ali', 'bi', 'bio', 'bila', 'što', 'ga', 'mu', 'joj', 'ih']
      
def ukloni_stop_words(rjecnik_frekvenicja, stop_words_lista):
    ocisceni_rijecnik = {}
    for rijec, frekvencija in rjecnik_frekvencija.items():
        if rijec not in stop_words_lista:
            ocisceni[rijec] = frekvencija
    return ocisceni_rijecnik


if __name__=="__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)
    if ucitani_tekst:
        print("Učitani tekst je:")
        print(ucitani_tekst)
    else:
        print("Greška pri učitavanju datoteke.")

    ucitani_tekst = ocisti_tekst(ucitani_tekst)

    if ucitani_tekst:
        print("Očišćeni tekst je:")
        print(ucitani_tekst)
        print(ucitani_tekst._len_())
        broj_rijeci = broji_frekvenciju(ucitani_tekst)
    else:
        print("Greška pri čišćenju teksta.")

    #Novi dio - pozivamo novu funkciju
    print("Brojim frekvenciju riječi...")
    broj_rijeci = broj_frekvenciju(procisceni_tekst)
    print("Brojanje zavrseno")

    #Ispisujemo rezultat da vidim što smo dobili
    print("\n--- Rječnik frekvencija ---")
    print(broj_rijeci)
    print("----------------------")
else:
    print('program se prekida jer tekst nije pročišćen.')
    

    #faza 3: filtriranje i sortiranje
    ociscenje_frekvencije = ukloni_stop_words(broj_rijeci, STOP_WORDS)
    print("\n--- Očišćeni rječnik frekvencije ---")
    print(ociscenje_frekvencije)
    print("--------------------------")
