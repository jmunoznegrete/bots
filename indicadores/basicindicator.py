ActualizaTick = 1

from .TimeS import SerieEscalar, TimeSerie, TP

class BasicIndicator(object):
    """ Base Class to build simple Indicators
        serie: is a list of SerieEscalar used as input
        label: holds the acronym of the indicator
        params: is a tuple: the first element is used for moving averages
        offset: to slip the input serie"""
    def __init__(self, serie, label, params=(0,), offset=0):
        self.interval = params[0]
        self.offset = offset
        self.pending = True
        self.NumMinData = 0
        self.doParams(params, offset)
        self.doSpecific()
        self.serie = serie
        self.lista = SerieEscalar(self.NumMinData)
        self.label = label

        self.update()

    def update(self):
        ## The loop limits are set to consider new data arrival.
        ## This function is called any time a serie update is required
        ## When enough data is available the 0 value is set with 
        ## no data displacement in order to update its value under
        ## any tick arrival

        PrimerDato = (self.lista.length() + 1) - self.serie[0].length()
        LimiteDato = self.serie[0].length()
                            
        # cursor is to come along appended serie values
        for cursor in range(PrimerDato, 1):
            self.lista.appendValue(self.doCalc(cursor))

        if self.serie[0].length() >= self.interval + self.offset:
            self.lista.setCur(self.doCalc(ActualizaTick))

    def ToIndicator(self):
        return {self.label:self.lista}

    def List(self):
        return self.lista

    def doParams(self, params, offset):
        ## further review of how to handle self.offset and 
        ## self.interval is required
        ## It must be declared in any new indicator class derived from
        ## this
        self.interval = params[0]
        self.offset = offset
        self.pending = True
        self.NumMinData = self.interval + offset

    def doSpecific(self):
        raise NotImplementedError

    
    def doCalc(self, cursor):
        raise NotImplementedError

    def MinData(self):
        return self.NumMinData
    def length(self):
        return self.lista.length()
    def __getitem__(self, index):
        return self.lista.Value(index)
    def __str__(self):
        return str(self.lista)
