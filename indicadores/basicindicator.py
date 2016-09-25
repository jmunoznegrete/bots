from TimeS import SerieEscalar, TimeSerie, TP

class BasicIndicator(object):
    """ Base Class to build simple Indicators
        serie: is a list of SerieEscalar used as input
        label: holds the acronym of the indicator
        params: is a tuple: the first element is used for moving averages
        offset: to slip the input serie"""
    def __init__(self, serie, label, params=(0,), offset=0):
        self.interval = params[0]
        self.offset = offset
        self.doParams(params)
        self.serie = serie
        self.lista = SerieEscalar(self.interval+self.offset)
        self.label = label

        self.update()

    def update(self):
        ## The loop limits are set to consider new data arrival.
        ## This function is called any time a serie update is required
        ## When enough data is available the 0 value is set with 
        ## no data displacement in order to update its value under
        ## any tick arrival

        PrimerDato = self.lista.length() 
        LimiteDato = self.serie[0].length()
                            
        for cursor in range(PrimerDato, LimiteDato):
            self.lista.appendValue(self.doCalc(cursor))

        if self.serie[0].length() >= self.interval + self.offset:
            self.lista.setCur(self.doCalc(0))

    def ToIndicator(self):
        return {self.label:self.lista}

    def doParams(self, params):
        ## further reviewof how to handle self.offset and 
        ## self.interval is required
        ## It must be declared in any new indicator class derived from
        ## this
        raise NotImplementedError

    def doCalc(self, cursor):
        raise NotImplementedError

    def __str__(self):
        return str(self.lista)
