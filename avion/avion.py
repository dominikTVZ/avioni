class Avion:
    def __init__(self, avion_id = 0):
        self._mjesto_proizvodnje = ""
        self._naziv = ""
        self._brzina = 0
        self._raspon = 0
        self.__id = avion_id
        self.__select_avion_sql = '''SELECT mjesto_proizvodnje, naziv, brzina, raspon FROM avion WHERE id_avion = ?; '''

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
       print( f'Naziv: {self.naziv} \nMjesto proizvodnje:{self.mjesto_proizvodnje}\n Brzina:{self._brzina} \n Raspon: {self._raspon}')


    def dohvatiAvion(self, cur):
        found = True
        tapl = (self.id, )
        res = cur.execute(self.__select_avion_sql, tapl)
        redak = res.fetchone()
        if redak is None:
            found = False
        else:
            self.naziv = redak[0]
            self.mjesto_proizvodnje = redak[1]
            self.brzina = redak[2]
            self.raspon = redak[3]
        return found