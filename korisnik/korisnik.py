from avion import Avion

class Korisnik:

    def __init__(self, avion=None):
        self.__korisnik_id =0
        self.__ime = ""
        self.__prezime = ""
        self.__avion = avion
        self.__select_korisnik_sql = '''SELECT id_korisnik, prezime, avion_id from korisnik WHERE ime = ?;'''


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

    @property
    def brzina(self):
        return self.__brzina


    @brzina.setter
    def brzina(self, brzina):
        self.__brzina = brzina

    def ispis(self):
        print(f'{self.__ime}, {self.__prezime}')


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
            self.__korisnik_id = redak[0]
            avion_id = redak[2]
            self.avion = Avion(avion_id)
            found = self.avion.dohvatiAvion(cur)
        return found
