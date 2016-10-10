import unittest
from  ..TimeS import Barra, TimeSerie, SerieEscalar, TP, Tick

def setUpModule():
    print ("\nInit: Test TimeS.py")

def tearDownModule():
    pass


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
    def test_creacion_de_serie_no_normalizada(self):
        s1 = SerieEscalar([1,2,3], Normalized=False)
        self.assertEqual(s1, SerieEscalar([3, 1, 2]))
    def test_creacion_de_serie_con_lista_vacia(self):
        s1 = SerieEscalar(0)
        s2 = SerieEscalar([])
        self.assertEqual(s1, s2)
    def test_creacion_de_anadir_un_elemento(self):
        self.serie.appendValue(1.3)
        self.assertEqual(str(self.serie), '[1.3, 0.0, 0.0]')
    def test_longitud_de_serie(self):
        self.serie.appendValue(1.3)
        self.assertEqual(self.serie.length(), 3)

    ## test cases related to index_out_of_range
    def test_error_indice_positivo(self):
        with self.assertRaises(IndexError):
            x = self.serie.Value(3)
    def test_error_indice_negativo(self):
        with self.assertRaises(IndexError):
            x = self.serie.Value(-4)

    ## test cases related to __eq__ function
    def test_Almost_Equal_para_dos_SerieEscalar(self):
        self.serie.appendValue(1.30000004)
        self.assertEqual(self.serie, SerieEscalar([1.3, 0.0, 0.0]))
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
    def test_desigualdad_series(self):
        self.s1 = SerieEscalar([1, 2, 3])
        self.s2 = SerieEscalar([1, 2, ])
        self.assertNotEqual(self.s1, self.s2)
    def test_Not_Almost_Equal_para_dos_SerieEscalar(self):
        self.serie.appendValue(1.304)
        self.assertNotEqual(self.serie, SerieEscalar([1.3, 0.0, 0.0]))
    def test_devuelve_elemento_dado_el_indice_correcto(self):
        self.s1 = SerieEscalar([1.0, 2.0, 5.0, 7.0])
        self.assertEqual(self.s1[-2], 5.0)
    def test_devuelve_elemento_dado_el_indice_incorrecto(self):
        self.s1 = SerieEscalar([1.0, 2.0, 5.0, 7.0])
        with self.assertRaises(IndexError):
            x = self.s1[2]


class TimeSerieTest(unittest.TestCase):
    def setUp(self):
        V=[
            3.0, 4.0, 1.0, 2.0,
            1.0, 3.0, 1.0, 2.0,
            2.0, 2.0, 1.0, 1.0,
          ]

        self.gbpusd = TimeSerie('D1')
        self.eurusd = TimeSerie('D1')
        self.gbpusd.appendBarra(Barra(3.0, 4.0, 1.0, 2.0))
        self.eurusd.appendBarra(Barra(3.0, 4.0, 1.0, 2.0))
        for i in range(int(len(V)/4)):
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
        self.assertAlmostEqual(self.eurusd.Value(-1, TP['HIGH']), 3.0)

    def test_str_TimeSerie(self):
        self.assertEqual(str(self.gbpusd), '[3.0][4.0][1.0][2.0]')

    def test_llega_tick_entre_high_y_low(self):
        tick = Tick(2.0, 5, '02:02:2016', 'EURUSD')
        self.eurusd.setCur(tick)
        self.assertEqual(self.eurusd.Value(0, TP['CLOSE']), 2.0)
    def test_llega_tick_mayor_que_high(self):
        tick = Tick(8.0, 5, '02:02:2016', 'EURUSD')
        self.eurusd.setCur(tick)
        self.assertEqual(self.eurusd.Value(0, TP['HIGH']), 8.0)
    def test_llega_tick_menor_que_low(self):
        tick = Tick(8.0, 5, '02:02:2016', 'EURUSD')
        self.eurusd.setCur(tick)
        self.assertEqual(self.eurusd.Value(0, TP['HIGH']), 8.0)
