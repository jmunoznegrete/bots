from basicindicator import BasicIndicator

class iSMA(BasicIndicator):
    """ SimpleMoving Average """
    def doCalc(self, cursor):
        media = 0.0
        for i in range(self.interval):
            media = media + self.serie[0].Value(cursor - i - self.offset)

        return media / float(self.interval)

    def doParams(self, params):
        ## Nothing to do
        pass

class iPM(BasicIndicator):
    """ Average Low - High in a bar"""
    def doCalc(self, cursor):
        media = 0.0
        NumSeries = len(self.serie)
        for i in range(NumSeries):
            ## offset was previously incremented by one so 
            ## the precise value is "restablished" this way
            media = media + self.serie[i].Value(cursor - self.offset + 1) 
        media = media / float(NumSeries)
        return media

    def doParams(self, params):
        ## 1 additional element is required when initializing
        ## self.serie to prevent from wrong first element calculation
        self.offset = self.offset + 1
