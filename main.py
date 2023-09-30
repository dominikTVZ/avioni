import sqlite3
from korisnik import Korisnik

con = sqlite3.connect('Projekt.db')
cur = con.cursor()


vlasnik_string = input(f'Unesite <ime prezime> platitelja: ')
lista = vlasnik_string.split()

vlasnik = Korisnik()
found = vlasnik.dohvatiKorisnika(lista[0], lista[1], cur)
if not found:
    print('\nNema platitelja/osobe')
    exit(1)
vlasnik.ispis()
vlasnik.avion.ispis()

con.commit()
con.close()

