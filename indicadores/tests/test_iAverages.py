import unittest

from ..TimeS import TimeSerie, Barra, TP
from ..iAverages import iSMA, iPM

def setUpModule():
    print "\nInit: Test iAverages.py"

def TearDownModule():
    print "\nFin: Test iAverages.py"

class iSMAtest(unittest.TestCase):
    def setUp(self):
        self.eurusd = TimeSerie(Barra(4.0, 7.0, 2.0, 3.0), 'D1')
        for i in range(5):
            self.eurusd.appendBarra(Barra(5.0+i, 7.0+i, 2.0+i, 3.0+i))

    def test_calculo_iSMA_3(self):
        sma3 = iSMA([self.eurusd.SClose(), ], 'SMA 3', (3,))
        self.assertEqual(
            str(sma3), 
            '[6.0, 0.0, 0.0, 3.3333333333333335, 4.0, 5.0]'
            )
        ###print '\nisma3'
        ###print self.eurusd.SClose()
        ###print sma3

    def test_calculo_iSMA_3_offset_1(self):
        sma3 = iSMA( [self.eurusd.SClose(), ], 'SMA 3', (3,), 1)
        ###print '\nisma3'
        ###print self.eurusd.SClose()
        ###print sma3
        self.assertEqual(
            str(sma3), 
            '[5.0, 0.0, 0.0, 0.0, 3.3333333333333335, 4.0]'
            )

    def test_calculo_iSMA_con_menos_datos_del_intervalo(self):
        sma3 = iSMA( [self.eurusd.SClose(), ], 'SMA 3', (7,), 0)
        self.assertEqual( str(sma3), '[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]')
        
    
class iPMtest(unittest.TestCase):
    def setUp(self):
        self.eurusd = TimeSerie(Barra(4.0, 7.0, 2.0, 3.0), 'D1')
        for i in range(5):
            self.eurusd.appendBarra(Barra(5.0+i, 7.0+i, 2.0+i, 3.0+i))

    def test_calculo_PM(self):
        pm = iPM ([self.eurusd.SHigh(), self.eurusd.SLow(),], 'PM', (0,), 0)
        ###print '\niPM, 0'
        ###print self.eurusd.SHigh()
        ###print self.eurusd.SLow()
        ###print pm
        self.assertEqual(str(pm), '[8.5, 4.5, 4.5, 5.5, 6.5, 7.5]')

    def test_calculo_PM_offset_no_nulo(self):
        pm = iPM ([self.eurusd.SHigh(), self.eurusd.SLow(),], 'PM', (0,), 1)
        ###print '\niPM, 3'
        ###print self.eurusd.SHigh()
        ###print self.eurusd.SLow()
        ###print pm
        self.assertEqual(str(pm), '[7.5, 0.0, 4.5, 4.5, 5.5, 6.5]')


