import unittest

from ..basicindicator import BasicIndicator
from ..TimeS import TimeSerie, TP, Barra, SerieEscalar

class iMV(BasicIndicator):
    def doCalc(self, cursor):
        if cursor == 1:
            cursor=0
        return self.serie[0].Value(cursor)
    def doSpecific(self):
        pass

class iMV2(BasicIndicator):
    def doCalc(self, cursor):
        if cursor == 1:
            cursor=0
        return self.serie[0].Value(cursor)
    def doSpecific(self):
        pass

def setUpModule():
    print "\nInit: basicindicator.py"

def tearDownModule():
    pass


class BasicIndicatorTest(unittest.TestCase):
    def setUp(self):
        self.serie = SerieEscalar([7.0, 0.0, 0.0, 0.0, 5.0, 6.0])

    def test_falta_definir_doCalc(self):
        with self.assertRaises(NotImplementedError):
            ejemplo = BasicIndicator([self.serie,], 'EJEM')
            
    def test_falta_definir_doSpecific(self):
        with self.assertRaises(NotImplementedError):
            ejemplo = BasicIndicator([self.serie,], 'EJEM')
            
    def test_indicador_mismo_valor(self):
        self.mv = iMV([self.serie,], 'mv')
        self.assertEqual(str(self.mv), '[7.0, 0.0, 0.0, 0.0, 5.0, 6.0]')

    def test_update_despues_de_anadir_valor(self):
        self.mv = iMV([self.serie,], 'mv')
        self.serie.appendValue(9.0)
        self.mv.update()
        self.assertEqual(str(self.mv), '[9.0, 0.0, 0.0, 0.0, 5.0, 6.0, 7.0]')

    def test_devolver_valor_etiqueta_ToIndicator(self):
        self.mv = iMV([self.serie,], 'mv')
        self.assertEqual(self.mv.ToIndicator().keys(), ['mv',])
        
    def test_devolver_valor_indicador_ToIndicator(self):
        self.mv = iMV([self.serie,], 'mv')
        self.s = SerieEscalar(3)
        for num in [5.0, 6.0, 7.0]:
            self.s.appendValue(num)
            
        self.assertEqual(
            self.mv.ToIndicator()['mv'], self.s)

    def test_devolver_MinData(self):
        self.mv = iMV([self.serie,], 'mv', (5,))

        self.assertEqual(self.mv.MinData(), 5)
        
    def test_longitud_indicador(self):
        self.assertEqual(self.serie.length(), 6)

    def test_valor_de_indicador_en_posicion(self):
        self.mv = iMV([self.serie,], 'mv')
        self.assertEqual(self.mv[-2], 5.0)
