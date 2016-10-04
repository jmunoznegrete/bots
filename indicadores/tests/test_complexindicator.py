import unittest
from ..complexindicator import EscalarIndicator, VectorIndicator
from ..iAverages import iPM, iSMA, iEMA

### To test these two superclasses PM and PM offset 1
### and SMA(3) and SMA(4) substration will be created.

class PMerror1(EscalarIndicator):
    def example(self):
        self.serie = serie
    def doCalc():
        pass
class PMerror2(EscalarIndicator):
    def example(self):
        self.serie = serie
    def doParams():
        pass
        
def setUpModule():
    print "\nInit: Test Complex Indicator Superclass"

def TearDownModule():
    print "\nFin: Test Complex Indicator Superclass"

class EscalarIndicatorTest(unittest.TestCase):
    ## Testing Errors when critial functions are not defined
    def test_doParams_specific_function(self):
        with self.assertRaises(NotImplementedError):
            pmdif = PMerror1([1,2],'PMdif',(0,))
    def test_doCalc_specific_function(self):
        with self.assertRaises(NotImplementedError):
            pmdif = PMerror2([1,2],'PMdif',(0,))

    def test_incompleted(self):
        """ We have just tested the existence of two functions.
        Remaining sentences of the class body need to be tested."""
        raise NotImplementedError, 'ESTE MODULO REQUIERE MAS TESTS'
            
