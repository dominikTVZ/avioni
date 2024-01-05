from avion import Avion

class Korisnik:

    def __init__(self, avion=None):
        self.__korisnik_id =0
        self.__ime = ""
        self.__prezime = ""
        self.__avion = avion
        self.__select_korisnik_sql = '''SELECT id_korisnik, prezime from korisnik WHERE ime = ?;'''
        self.__insert_korisnik_sql =  ''' INSERT INTO korisnik (ime, prezime) VALUES(?, ?);'''



    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime= prezime

    @property
    def avion(self):
        return self.__avion

    @avion.setter
    def avion(self, avion):
        self.__avion = avion



    def ispis(self):
        print(f'{self.__ime}, {self.__prezime}')

    def dodajKorisnika(self, cur):
        korisnik_tapl = (self.ime, self.prezime)
        cur.execute(self.__insert_korisnik_sql, korisnik_tapl)
        return




    def dohvatiKorisnika(self, ime, cur):
        found = True
        vlasnik_ime = (ime, )
        res = cur.execute(self.__select_korisnik_sql, vlasnik_ime)
        redak = res.fetchone()

        if redak is None:
            found = None
        else:
            self.ime = ime
            self.__prezime = redak[1]
            korisnik_id = redak[0]
            self.avion = Avion(korisnik_id)
            found = self.avion.dohvatiAvion(cur)
        return found
