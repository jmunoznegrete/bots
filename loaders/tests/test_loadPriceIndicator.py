import unittest
import os

from bot.indicadores.TimeS import SerieEscalar, TimeSerie, Barra
from ..loadPriceIndicator import loadPriceResult

def setUpModule():
    print "\nInit: Test loadPriceIndicator.py"

class loadPriceResultTest(unittest.TestCase):
    def setUp(self):
        self.filename = os.path.dirname(__file__) + '//Muestra.csv'
    def test_not_enough_prices(self):
        with self.assertRaises(ValueError):
            loader = loadPriceResult(self.filename, 50, 'D1', 9)
    def test_column_index_too_big(self):
        with self.assertRaises(IndexError):
            loader = loadPriceResult(self.filename, 10, 'D1', 28)
    def test_last_column_extract_end_of_line(self):
        loader = loadPriceResult(self.filename, 10, 'D1', 12)
        self.assertEqual(5.0, loader.Result()[-9])
    def test_column_extract_correct_Result(self):
        loader = loadPriceResult(self.filename, 4, 'D1', 3)
        resultado = SerieEscalar([1.3911, 1.3892, 1.3878, 1.3897])
        self.assertEqual(resultado, loader.Result())
    def test_column_extract_correct_price(self):
        loader = loadPriceResult(self.filename, 4, 'D1', 3)
        Precio = loader.Precio()
        High=SerieEscalar([1.3911, 1.3892, 1.3878, 1.3897])
        self.assertEqual(High, Precio.SLow())
