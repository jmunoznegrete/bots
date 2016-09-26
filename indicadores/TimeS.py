class OHPL(object):
    def __init__(self):
        self.OPEN = 0
        self.HIGH = 1
        self.LOW = 2
        self.CLOSE =3

TP = {'OPEN':0, 'HIGH':1, 'LOW': 2, 'CLOSE':3}
        
class Barra(object):
    """ Barra adds the values OHLC to the Price Serie"""
    def __init__(self, openP=0.0, highP=0.0, lowP=0.0, closeP=0.0):
        self.valor = [openP, highP, lowP, closeP]
        
    def Value(self, indice):
        return self.valor[indice]

    def __str__(self):
        return str(self.valor)


class TimeSerie(object):
    """ TimeSerie creates a list of four SerieEscalar to support
        OHLC value bars
        Element 0 holds the current value (last value) of the
        Serie to have same indexing type as mt4"""
    def __init__(self, barra, tipo):
        self.tipo = tipo
        self.price = [
            SerieEscalar(), SerieEscalar(),SerieEscalar(), SerieEscalar()
            ]
        self.addBarra(barra)
    def addBarra(self, barra):
        for i in range(4):
            self.price[i].appendValue(barra.Value(i))
    def SClose(self):
        return self.price[TP['CLOSE']]
    def SHigh(self):
        return self.price[TP['HIGH']]
    def SLow(self):
        return self.price[TP['LOW']]
    def SOpen(self):
        return self.price[TP['OPEN']]
    def SerieValue(self, tipo):
        return self.price[tipo]
    def returnBarraL(self, indice):
        return [
                self.price[0].Value(indice),
                self.price[1].Value(indice),
                self.price[2].Value(indice),
                self.price[3].Value(indice)
                ]
    def Value(self, indice, tipo):
        return self.price[tipo].Value(indice)
    def appendBarra(self, barra):
        for i in range(4):
            self.price[i].appendValue(self.price[i].Value(0))
            self.price[i].setCur(barra.Value(i))
    def length(self):
        return self.price[0].length()
    def __str__(self):
        cadena = str(self.price[0]) + str(self.price[1])
        cadena = cadena + str(self.price[2]) + str(self.price[3])
        return str(cadena)

class SerieEscalar(object):
    """ List of values initialized to a number of 0.0
        If a List of float is provided the SerieEscalar is initialized
        to taht value
        It is a general purpose List of scalars"""
    def __init__(self, Elements=0):
        if type(Elements) == int:
            self.Serie=[0.0 for i in range(Elements)]
        elif type(Elements) == list:
            self.Serie=Elements[:]
        else:
             raise TypeError
    def Value(self, indice):
        return self.Serie[indice]
    def appendValue(self, valor):
        self.Serie.append(valor)
    def length(self):
        return len(self.Serie)
    def setCur(self, valor):
        self.Serie[0] = valor
    def __eq__(self, s1):
        equal = True
        if s1.length() != self.length():
            return False
        for i in range(s1.length()):
            if abs(s1.Value(i) -  self.Value(i))> 0.00001:
                equal = False
                break
        return equal
            
    def __str__(self):
        return str(self.Serie)

