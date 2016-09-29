import unittest

from ..TimeS import TimeSerie, Barra, TP, SerieEscalar
from ..iAverages import iSMA, iPM, iEMA

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

    def test_calculo_iSMA_3_offset_1(self):
        sma3 = iSMA( [self.eurusd.SClose(), ], 'SMA 3', (3,), 1)
        self.assertEqual(
            str(sma3), 
            '[5.0, 0.0, 0.0, 0.0, 3.3333333333333335, 4.0]'
            )

    def test_calculo_iSMA_con_menos_datos_del_intervalo(self):
        sma3 = iSMA( [self.eurusd.SClose(), ], 'SMA 3', (7,), 0)
        self.assertEqual( str(sma3), '[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]')
        
    
class iPMtest(unittest.TestCase):
    def setUp(self):
        self.eurusd = TimeSerie(Barra(4.0, 7.0, 2.0, 3.0), 'D1')
        for i in range(5):
            self.eurusd.appendBarra(Barra(5.0+i, 7.0+i, 2.0+i, 3.0+i))

    def test_calculo_PM(self):
        pm = iPM ([self.eurusd.SHigh(), self.eurusd.SLow(),], 'PM', (0,), 0)
        self.assertEqual(str(pm), '[8.5, 4.5, 4.5, 5.5, 6.5, 7.5]')

    def test_calculo_PM_offset_no_nulo(self):
        pm = iPM ([self.eurusd.SHigh(), self.eurusd.SLow(),], 'PM', (0,), 1)
        self.assertEqual(str(pm), '[7.5, 0.0, 4.5, 4.5, 5.5, 6.5]')


class iEMAtest(unittest.TestCase):
    ##def setUp(self):
    def test_calculo_primer_elemento_EMA_3(self):
        eurusdClose = SerieEscalar([5.0, 3.0, 4.0], Normalized=False)
        ema = iEMA ([eurusdClose,], 'EMA', (3,), 0)
        self.assertEqual(str(ema), '[4.0, 0.0, 0.0]')

    def test_calculo_segundo_y_tercer_elementos_EMA_3(self):
        eurusdClose = SerieEscalar([5.0, 3.0, 4.0, 5.0, 6.0], Normalized=False)
        ema = iEMA ([eurusdClose,], 'EMA', (3,), 0)
        self.assertEqual(str(ema), '[5.25, 0.0, 0.0, 4.0, 4.5]')

    def test_calculo_cuatro_elementos_EMA_3(self):
        eurusdClose = SerieEscalar([8.0, 5.0, 3.0, 4.0, 5.0, 6.0, 7.0])

        ema = iEMA ([eurusdClose,], 'EMA', (3,), 0)
        self.assertEqual(str(ema), '[7.0625, 0.0, 0.0, 4.0, 4.5, 5.25, 6.125]')

    def test_calculo_varios_elementos_EMA_4(self):
        serie = SerieEscalar([8.0, 5.0, 3.0, 4.0, 5.0, 6.0, 7.0])
        resultado = SerieEscalar([6.662, 0.0, 0.0, 0.0, 4.25, 4.95, 5.77])
        ema = iEMA([serie, ], 'EMA', (4,), 0)
        self.assertEqual(ema.ToIndicator()['EMA'], resultado)

    def test_calculo__EMA_4_desfase_1(self):
        serie = SerieEscalar([8.0, 5.0, 3.0, 4.0, 5.0, 6.0, 7.0])
        resultado = SerieEscalar([5.77, 0.0, 0.0, 0.0, 0.0, 4.25, 4.95])
        ema = iEMA([serie, ], 'EMA', (4,), 1)
        self.assertEqual(ema.ToIndicator()['EMA'], resultado)

    def test_calculo__EMA_4_desfase_2(self):
        serie = SerieEscalar([8.0, 5.0, 3.0, 4.0, 5.0, 6.0, 7.0])
        resultado = SerieEscalar([4.95, 0.0, 0.0, 0.0, 0.0, 0.0, 4.25])
        ema = iEMA([serie, ], 'EMA', (4,), 2)
        self.assertEqual(ema.ToIndicator()['EMA'], resultado)

