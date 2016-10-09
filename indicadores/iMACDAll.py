from TimeS import SerieEscalar, TimeSerie, TP
from iAverages import iSMA, iPM, iEMA
from complexindicator import EscalarIndicator, VectorIndicator

class iMACD(EscalarIndicator):
    def doParams(self, params, offset):
        smaFast = iEMA(
            [self.serie[0], ], 'smaFast', 
            (self.params[0],), self.offset
            )
        smaSlow = iEMA(
            [self.serie[0], ], 'smaSlow', 
            (self.params[1],), self.offset
            )
        ## anado '+1' a NumMindData ya que empieza a calcular MT4
        ## en ese indice
        self.NumMinData = smaSlow.MinData() + self.offset + 1
        self.ListaIntermedios=[smaFast, smaSlow]

    def doSpecific(self):
        pass

    def doCalc(self, cursor):
        if cursor == 1:
            cursor = 0

        Valor = \
            self.ListaIntermedios[0][cursor] \
            - self.ListaIntermedios[1][cursor]

        return Valor

class iSignal(EscalarIndicator):

    def doParams(self, params, offset):
        emamacd = iSMA(
            [self.serie[0].List(), ], 'emaMACD', 
            (self.params[2],), self.offset
        )
        self.NumMinData = emamacd.MinData() + self.offset 
        self.ListaIntermedios=[emamacd]

    def doSpecific(self):
        pass

    def doCalc(self, cursor):
        if cursor == 1:
            cursor = 0

        Valor = self.ListaIntermedios[0][cursor]

        return Valor

class iHistogram(EscalarIndicator):
    def doParams(self, params, offset):
        self.NumMindata = self.offset + 1
        self.ListaIntermedios=[self.serie[0], self.serie[1]]
    def doSpecific(self):
        pass
    def doCalc(self, cursor):
        if cursor == 1:
            cursor = 0

        Valor = \
            self.ListaIntermedios[0][cursor] \
            - self.ListaIntermedios[1][cursor]

        return Valor

class iMACDSet(VectorIndicator):
    def BuildIndicator(self):
        imacd = iMACD([self.price.SClose(), ], 'MACD', self.params, 0)
        isignal = iSignal([imacd, ], 'SIG', self.params, 0)
        ihisto = iHistogram([imacd, isignal], 'HIST', (0,), 0)
        self.ListaIndicadores = [imacd, isignal, ihisto]

