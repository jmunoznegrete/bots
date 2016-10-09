from TimeS import SerieEscalar, TimeSerie, TP
from iAverages import iSMA, iPM
from complexindicator import EscalarIndicator, VectorIndicator

class iAO(EscalarIndicator):

    def doParams(self, params, offset):
        sma5 = iSMA([self.serie[0].List(), ], 'sma5', (5,), self.offset)
        sma34 = iSMA([self.serie[0].List(), ], 'sma34', (34,), self.offset)
        ## anado '+1' a NumMindData ya que empieza a calcular MT4
        ## en ese indice
        self.NumMinData = sma34.MinData() + self.offset + 1
        self.ListaIntermedios=[sma5, sma34]

    def doSpecific(self):
        pass

    def doCalc(self, cursor):
        if cursor == 1:
            cursor = 0


        Valor = \
            self.ListaIntermedios[0][cursor] \
            - self.ListaIntermedios[1][cursor]

        return Valor

class iAC(EscalarIndicator):

    def doParams(self, params, offset):
        ao = self.serie[0]
        smaao5 = iSMA([self.serie[0].List(), ], 'smaiAO', (5,), self.offset)
        self.NumMinData = smaao5.MinData() + ao.MinData()+ self.offset 
        self.ListaIntermedios=[ao, smaao5]

    def doSpecific(self):
        pass

    def doCalc(self, cursor):
        if cursor == 1:
            cursor = 0

        Valor = \
            self.ListaIntermedios[0][cursor] \
            - self.ListaIntermedios[1][cursor]

        return Valor


class iBW(VectorIndicator):
    def BuildIndicator(self):
        pm = iPM([self.price.SHigh(), self.price.SLow()], 'PM', (0,), 0)
        ao = iAO([pm, ], 'AO', (0,), 0)
        ac = iAC([ao, ], 'AC', (0,), 0)
        self.ListaIndicadores = [pm, ao, ac]

