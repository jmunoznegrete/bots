from TimeS import SerieEscalar, TimeSerie, TP

class EscalarIndicator(object):
    """ Base Class to build derivated Indicators
        serie: is a list of SerieEscalar used as input
        label: holds the indicator acronym
        params: is a tuple: the first element is used for moving averages
            useful for compatibility purposes when calculating MACD i.e.
        offset: to slip the input serie
        self.update() updates first the source indicators, then
        proceed with self update"""
    def __init__(self, serie, label, params=(0,), offset=0):
        self.interval = params[0]
        self.offset = offset
        self.pending = True
        self.NumMinData = 0
        self.serie = serie
        self.ListaIntermedios = []
        self.label = label
        self.doSpecific()
        self.doParams(params, offset)
        self.lista = SerieEscalar(self.NumMinData)


        self.update()

    def update(self):
        ## The loop limits are set to consider new data arrival.
        ## This function is called any time a serie update is required
        ## When enough data is available the 0 value is set with 
        ## no data displacement in order to update its value under
        ## any tick arrival

        for indicador in self.ListaIntermedios:
            indicador.update()

        PrimerDato = (self.lista.length() + 1) - self.serie[0].length()
        LimiteDato = self.serie[0].length()
                            
        # cursor is to come along appended serie values
        for cursor in range(PrimerDato, 1):
            self.lista.appendValue(self.doCalc(cursor))

        if self.serie[0].length() >= self.interval + self.offset:
            self.lista.setCur(self.doCalc(ActualizaTick))

    def ToIndicator(self):
        return {self.label:self.lista}

    def doParams(self, params, offset):
        ## further review of how to handle self.offset and 
        ## self.interval is required
        ## It must be declared in any new indicator class derived from
        ## this. i.e.
        ## self.interval = params[0]
        ## self.offset = offset
        ## self.pending = True
        ## self.NumMinData = self.interval + offset
        raise NotImplementedError

    def doSpecific(self):
        raise NotImplementedError

    
    def doCalc(self, cursor):
        raise NotImplementedError

    def MinData(self):
        return self.NumMinData
    def __str__(self):
        return str(self.lista)



class VectorIndicator(object):
    """ Class to group a set of escalar indicators
        i.e. MACD dictionary will contain three SerieEscalar:
        MACD, signal and Histogram
        Input Parameter: Price SerieEscalar
        self.BuildIndicator() builds a sorted list of indicators
        """
    def __init__(self, price):
        self.price = price
        self.ListaIndicadores = []
        self.ListaValues={}
        self.BuildIndicator()
        for indicador in self.ListaIndicadores:
            ListaValues.update(indicador.ToIndicator())

    def update(self):
        for indicador in self.ListaIndicadores:
            indicador.update()

    def Value(self):
        return self.ListaValues

    def BuildIndicator(self, price):
        raise NotImplemented
