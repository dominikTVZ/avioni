import sqlite3
from korisnik import Korisnik

con = sqlite3.connect('Projekt.db')
cur = con.cursor()


vlasnik_ime = input(f'Unesite <ime> vlasnika: ')


vlasnik = Korisnik()
found = vlasnik.dohvatiKorisnika(vlasnik_ime, cur)
if not found:
    print('\nNema platitelja/osobe')
    exit(1)
vlasnik.ispis()
vlasnik.avion.ispis()

con.commit()
con.close()

