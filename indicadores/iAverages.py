from .basicindicator import BasicIndicator, ActualizaTick

class iSMA(BasicIndicator):
    """ SimpleMoving Average """
    def doCalc(self, cursor):
        if cursor == 1:
            cursor = 0
        media = 0.0
        for i in range(self.interval):
            media = media + self.serie[0].Value(cursor - i - self.offset)

        return media / float(self.interval)

    def doSpecific(self):
        self.NumMinData = self.NumMinData - 1


class iPM(BasicIndicator):
    """ Average Low - High in a bar"""
    def doCalc(self, cursor):
        if cursor == 1:
            cursor = 0
        media = 0.0
        NumSeries = len(self.serie)
        for i in range(NumSeries):
            ## offset was previously incremented by one so 
            ## the precise value is "restablished" this way
            media = media + self.serie[i].Value(cursor - self.offset) 
        media = media / float(NumSeries)
        return media

    def doSpecific(self):
        ## 1 additional element is required when initializing
        ## self.serie to prevent from wrong first element calculation
        pass
        ##self.NumMinData = self.NumMinData + 1


class iEMA(BasicIndicator):
    """ ExponentialMoving Average """
    ## This case is more complexe due to First calculation
    ## differs from next elements
    ## Special case come up if len(serie)  == Interval

    def doCalc(self, cursor):
        media = 0.0
        C = 2.0 / float(self.interval + 1)

        if self.pending:
            media = self.doFirstTime(cursor)
            self.pending = False
        else:
            if (self.lista.length() == self.NumMinData+1) \
                and cursor == ActualizaTick:
                cursor = 0
                media = self.doFirstTime(cursor)
            else:
                cursorlista=0
                if cursor == ActualizaTick:
                    cursor = 0
                    cursorlista=-1
                media = \
                    C * self.serie[0].Value(cursor - self.offset) \
                    + (1.0 - C) * self.lista.Value(cursorlista)
        return media 

    def doFirstTime(self, cursor):
        return self.serie[0][cursor - self.offset]
        media = 0.0
        for i in range(self.interval):
            media = media + self.serie[0].Value(cursor - i - self.offset)
        media = media / self.interval
        return media


    def doSpecific(self):
        self.NumMinData = self.offset
##        self.NumMinData = self.NumMinData - 1
        self.pending = True

