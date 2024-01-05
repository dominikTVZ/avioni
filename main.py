import sqlite3
from utilities import unos_intervala
from korisnik import Korisnik



con = sqlite3.connect('Novi.db')
cur = con.cursor()


running = True
while running:
    print('-' * 20)


    print('1. Ispis svih korisnika')
    print('2. Unesite ime korisnika i vidite njegove avione')
    print('3. Unesite novog korisnika')
    print('4. Zaustavi program')
    print('-' * 20)

    odabir = unos_intervala(1, 4)

    if odabir == 1:

        ispis_korisnika = ''' SELECT ime, prezime FROM korisnik;'''

        popis = cur.execute(ispis_korisnika).fetchall()

        for i, redak in enumerate(popis, start=1):
            print(f'{i}. {redak[0]} {redak[1]}')


    if odabir == 2 :
        vlasnik_ime = input(f'Unesite <ime> vlasnika: ')

        vlasnik = Korisnik()
        found = vlasnik.dohvatiKorisnika(vlasnik_ime, cur)
        if not found:
            print('\nNema vlasnika')
            exit(1)
        vlasnik.ispis()

        vlasnik.avion.ispis()

        con.commit()


    elif odabir == 3:

        korisnik_ime = input("Unesite ime korisnika: ")
        korisnik_prezime = input("Unesite prezime korisnika: ")
        korisnik = Korisnik()
        korisnik.ime = korisnik_ime
        korisnik.prezime = korisnik_prezime
        korisnik.dodajKorisnika(cur)
        con.commit()



    elif odabir == 4:
        running = False




