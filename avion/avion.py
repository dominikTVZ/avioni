class Avion:
    avioni = []
    def __init__(self, avion_id = 0):
        self._mjesto_proizvodnje = ""
        self._naziv = ""
        self._brzina = 0
        self._raspon = 0
        self.__id = avion_id
        self.__select_avion_sql = '''SELECT  naziv, mjesto_proizvodnje, brzina, raspon FROM avion WHERE korisnik_id= ?; '''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def naziv(self):
        return self._naziv

    @naziv.setter
    def naziv(self, naziv):
        self._naziv = naziv
    @property
    def mjesto_proizvodnje(self):
        return self._mjesto_proizvodnje

    @mjesto_proizvodnje.setter
    def mjesto_proizvodnje(self, mjesto_proizvodnje):
        self._mjesto_proizvodnje = mjesto_proizvodnje

    @property
    def brzina(self):
        return self._brzina

    @brzina.setter
    def brzina(self, brzina):
        self._brzina = brzina

    @property
    def raspon(self):
        return self._raspon

    @raspon.setter
    def raspon(self, raspon):
        self._raspon = raspon

    def ispis(self):
        for avion in self.avioni:
            print(f'Naziv aviona: {avion.naziv}')
            print(f'Mjesto proizvodnje: {avion.mjesto_proizvodnje}')
            print(f'Brzina: {avion.brzina} km/h')
            print(f'Raspon krila aviona: {avion.raspon} m')




    def dohvatiAvion(self, cur):
        found = True
        tapl = (self.id, )
        res = cur.execute(self.__select_avion_sql, tapl)
        redovi = res.fetchall()
        for redak in redovi:
            avion = Avion()  # Stvorite novu instancu aviona
            avion.naziv = redak[0]
            avion.mjesto_proizvodnje = redak[1]
            avion.brzina = redak[2]
            avion.raspon = redak[3]
            self.avioni.append(avion)  # Dodajte avion u listu aviona
        return found
