from bot.indicadores.TimeS import SerieEscalar, TimeSerie, Barra

class loadPriceResult(object):
    """ Open a file to load a number prices and the indicator results
        included in column. 
    """
    def __init__ (self, filename, numprices, timeframe, column):
        self.filename = filename
        self.numprices = numprices
        self.column = column
        self.precio = TimeSerie(timeframe)
        self.result = SerieEscalar()
        self.loadData()
    def loadData(self):
        with open(self.filename, 'r') as f:
	        i=0
	        for line in f:
	            valores = line.split(',')
	            if i == 0:
	                i = i+1
	                continue
	            VOpen = float(valores[1])
	            VHigh = float(valores[2])
	            VLow = float(valores[3])
	            VClose = float(valores[4])
	            VTime = valores[0]
	            self.precio.appendBarra(Barra(VOpen, VHigh, VLow, VClose), VTime)
	            VResultado = float(valores[self.column])
	            self.result.appendValue(VResultado)
	            i = i + 1
	            if i > self.numprices:
	                break

        f.close()

        if i < self.numprices:
            raise ValueError('Not enough Price Values')

    def Precio(self):
        return self.precio

    def Result(self):
        return self.result

        
