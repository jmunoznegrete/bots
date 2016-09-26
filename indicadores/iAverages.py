from basicindicator import BasicIndicator

class iSMA(BasicIndicator):
    """ SimpleMoving Average """
    def doCalc(self, cursor):
        media = 0.0
        for i in range(self.interval):
            media = media + self.serie[0].Value(cursor - i - self.offset)

        return media / float(self.interval)

    def doSpecific(self):
        pass


class iPM(BasicIndicator):
    """ Average Low - High in a bar"""
    def doCalc(self, cursor):
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
        self.NumMinData = self.NumMinData + 1


class iEMA(BasicIndicator):
    """ SimpleMoving Average """
    def doCalc(self, cursor):
        media = 0.0
        C = 2.0 / float(self.interval + 1)

        if self.pending:
            for i in range(self.interval):
                media = media + self.serie[0].Value(cursor - i - self.offset)
            media = media / self.interval
            ##if self.serie[0].length() > 
            ##  self.lista.length() + self.offset -1:
            self.pending = False
        else:
            media = \
                C * self.serie[0].Value(cursor - self.offset) \
                + (1.0 - C) * self.lista.Value(cursor - 1)
        return media 

    def doSpecific(self):
        self.pending = True

