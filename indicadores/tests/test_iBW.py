import unittest
import os
from bot.loaders.loadPriceIndicator import loadPriceResult

from ..TimeS import TimeSerie, SerieEscalar, Barra
from ..iBW import iAO, iAC, iBW
from ..iAverages import iPM, iSMA, iEMA

class iBWTest(unittest.TestCase):

    def test_calculo_iAC_real(self):
        filename = os.path.dirname(__file__) + '//DBiBW.csv'
        ## loader = loadPriceResult(filename, numprices, timeframe, column )
        loader = loadPriceResult(filename, 50, 'D1', 5 )

        Precio = loader.Precio()
        resultado = loader.Result()
        ibw = iBW(Precio)

        self.assertEqual(ibw.ToIndicator()['AC'], resultado)

class iAOTest(unittest.TestCase):
    def test_calculo_iAO_real_from_iBW_class(self):
        filename = os.path.dirname(__file__) + '//DBiBW.csv'
        ## loader = loadPriceResult(filename, numprices, timeframe, column )
        loader = loadPriceResult(filename, 50, 'D1', 9 )

        Precio = loader.Precio()
        resultado = loader.Result()
        ibw = iBW(Precio)

        self.assertEqual(ibw.ToIndicator()['AO'], resultado)

    def test_calculo_iAO_real_from_iAO(self):
        filename = os.getcwd() + '//bot//indicadores//tests//DBiBW.csv'
        ## loader = loadPriceResult(filename, numprices, timeframe, column )
        loader = loadPriceResult(filename, 50, 'D1', 9 )

        Precio = loader.Precio()
        resultado = loader.Result()
        pm = iPM([Precio.SHigh(), Precio.SLow(),], 'PM', (0,), 0)
        ao = iAO([pm,], 'AO',(0,), 0)
        self.assertEqual(ao.ToIndicator()['AO'], resultado)

    def test_iAO_getitem_serie(self):
        filename = os.getcwd() + '//bot//indicadores//tests//DBiBW.csv'
        ## loader = loadPriceResult(filename, numprices, timeframe, column )
        loader = loadPriceResult(filename, 50, 'D1', 9 )

        Precio = loader.Precio()
        resultado = loader.Result()
        ibw = iBW(Precio)

        self.assertEqual(ibw['AO'], resultado)

    def test_iAO_getitem_valor(self):
        filename = os.getcwd() + '//bot//indicadores//tests//DBiBW.csv'
        ## loader = loadPriceResult(filename, numprices, timeframe, column )
        loader = loadPriceResult(filename, 50, 'D1', 9 )

        Precio = loader.Precio()
        resultado = loader.Result()
        ibw = iBW(Precio)

        self.assertAlmostEqual(0.003620588235,ibw['AO'][-2])

