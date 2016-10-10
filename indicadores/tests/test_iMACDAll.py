import unittest
import os
from bot.loaders.loadPriceIndicator import loadPriceResult

from ..TimeS import TimeSerie, SerieEscalar, Barra
from ..iMACDAll import iMACDSet, iMACD, iSignal, iHistogram
from ..iAverages import iPM, iSMA, iEMA

def setUpModule():
    print("\nInit iMACD")

class iMACDSetTest(unittest.TestCase):

    def test_calculo_MACD_real(self):
        filename = os.path.dirname(__file__) + '//DBiMACD.csv'
        ## loader = loadPriceResult(filename, numprices, timeframe, column )
        loader = loadPriceResult(filename, 50, 'D1', 6 )

        Precio = loader.Precio()
        resultado = loader.Result()
        imacdset = iMACDSet(Precio, (12,26,9))

        self.assertEqual(imacdset['MACD'], resultado)

    def test_calculo_Signal(self):
        filename = os.path.dirname(__file__) + '//DBiMACD.csv'
        ## loader = loadPriceResult(filename, numprices, timeframe, column )
        loader = loadPriceResult(filename, 25, 'D1', 7 )

        Precio = loader.Precio()
        resultado = loader.Result()
        imacdset = iMACDSet(Precio, (12,26,9))

        self.assertEqual(imacdset['SIG'], resultado)

    def test_calculo_Histogram(self):
        filename = os.getcwd() + '//bot//indicadores//tests//DBiMACD.csv'
        ## loader = loadPriceResult(filename, numprices, timeframe, column )
        loader = loadPriceResult(filename, 25, 'D1', 8 )

        Precio = loader.Precio()
        resultado = loader.Result()
        imacdset = iMACDSet(Precio, (12,26,9))
        resultado = imacdset['HIST']
        self.assertEqual(imacdset['HIST'], resultado)

