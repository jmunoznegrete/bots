import unittest
from  ..TimeS import Barra, TimeSerie, SerieEscalar, TP

def setUpModule():
    print "\nInit: Test TimeS.py"

def tearDownModule():
    print "\nFin: Test TimeS.py"


class BarraTest(unittest.TestCase):
    def setUp(self):
        self.bar = Barra(1.0, 2.0, 3.0, 4.0)
    def test_creacion_de_barra(self):
        self.assertAlmostEqual(self.bar.Value(0), 1.0)
    def test_contenido_barra(self):
        self.assertEqual(str(self.bar), '[1.0, 2.0, 3.0, 4.0]')

class SerieEscalarTest(unittest.TestCase):
    def setUp(self):
        self.serie = SerieEscalar(2)
    def test_creacion_de_serie_2_elementos_a_cero(self):
        self.assertEqual(str(self.serie), '[0.0, 0.0]')
    def test_creacion_de_anadir_un_elemento(self):
        self.serie.appendValue(1.3)
        self.assertEqual(str(self.serie), '[0.0, 0.0, 1.3]')
    def test_longitud_de_serie(self):
        self.serie.appendValue(1.3)
        self.assertEqual(self.serie.length(), 3)
    def test_igualdad_series(self):
        self.s1 = SerieEscalar(0)
        self.s2 = SerieEscalar(0)
        self.s1.appendValue(1)
        self.s1.appendValue(3)
        self.s1.appendValue(2)
        self.s2.appendValue(1)
        self.s2.appendValue(3)
        self.s2.appendValue(2)
        self.assertEqual(self.s1, self.s2)

class TimeSerieTest(unittest.TestCase):
    def setUp(self):
        V=[
            3.0, 4.0, 1.0, 2.0,
            1.0, 3.0, 1.0, 2.0,
            2.0, 2.0, 1.0, 1.0,
          ]

        self.gbpusd = TimeSerie(Barra(3.0, 4.0, 1.0, 2.0), 'D1')
        self.eurusd = TimeSerie(Barra(3.0, 4.0, 1.0, 2.0), 'D1')
        for i in range(len(V)/4):
            k = 4 * i
            self.eurusd.appendBarra(Barra(V[k], V[k+1], V[k+2], V[k+3]))

    def test_creacion_serie(self):
        self.assertEqual(self.eurusd.returnBarraL(0), [2.0, 2.0, 1.0, 1.0])

    def test_retorna_serie_open(self):
        self.assertEqual (
            str(self.eurusd.SerieValue(TP['OPEN'])), 
            str([2.0, 3.0, 3.0, 1.0])  
            )

    def test_longitud_TimeSerie(self):
        self.assertEqual(self.eurusd.length(), 4)

    def test_valor_de_high(self):
        self.assertAlmostEqual(self.eurusd.Value(1, TP['HIGH']), 4.0)

    def test_str_TimeSerie(self):
        self.assertEqual(str(self.gbpusd), '[3.0][4.0][1.0][2.0]')

