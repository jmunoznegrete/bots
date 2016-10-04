from TimeS import SerieEscalar, TimeSerie, TP
from iAverages import iSMA, iPM
from complexindicator import EscalarIndicator, VectorIndicator

class iAO(EscalarIndicator):

    def doParams(self, params, offset):
        sma9 = iSMA([self.serie[0], ], 'sma9', (0,), self.offset)
        sma34 = iSMA([self.serie[0], ], 'sma34', (0,), self.offset)
        self.NumMinData = sma34.MinData() + self.offset + 1
        self.ListaIntermedios=[ipm, sma9, sma34]

    def doSpecific():
        pass

    def doCalc(cursor):
        if cursor == 1:
            cursor = 0

        self.lista[cursor] = \
            self.ListaIntermedios[0].Value(cursor) \
            - self.ListaIntermedios[1].Value(cursor)

class iAC(EscalarIndicator):

    def doParams(self, params, offset):
        ao = iAO([self.serie[0], ], 'iAO', (0,), self.offset)
        smaao5 = iSMA([self.serie[0], ], 'smaiAO', (5,), self.offset)
        self.NumMinData = smaaao5.MinData() + self.offset + 1
        self.ListaIntermedios=[ao, smaao5]

    def doSpecific():
        pass

    def doCalc(cursor):
        if cursor == 1:
            cursor = 0

        self.lista[cursor] = \
            self.ListaIntermedios[0].Value(cursor) \
            - self.ListaIntermedios[1].Value(cursor)


class iBW(VectorIndicator):
    def BuildIndicator():
        pm = iPM([self.price.SHigh(), self.price.SLow()], 'PM', (0,), 0)
        ao = iAO([pm, ], 'AO', (0,), 0)
        ac = iAC([ao, ], 'AC', (0,), 0)
        self.ListaIndicadores = [pm, ao, ac]

