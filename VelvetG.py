class VelvetG:
#    def __init__(self):
#        self.CoverageCutOff = None
#        self.MaxCoverage = None
#        self.MinContigLength = None
#        self.InsertLength = None
#        self.InsertLengthLong = None
#        self.ExpectedCoverage = None
    def __init__(self, CoverageCutOff = None, MaxCoverage = None, MinContigLength = None, InsertLength = None, InsertLengthLong = None, ExpectedCoverage = None ):
        self.SetCoverageCutOff(CoverageCutOff) 
        self.SetMaxCoverage(MaxCoverage)
        self.SetMinContigLength(MinContigLength)
        self.SetInsertLength(InsertLength)
        self.SetInsertLengthLong(InsertLengthLong)
        self.SetExpectedCoverage(ExpectedCoverage)
    def GetCoverageCutOff(self):
        return self.CoverageCutOff
    def GetMaxCoverage(self):
        return self.MaxCoverage
    def GetMinContigLength(self):
        return self.MinContigLength
    def GetInsertLength(self):
        return self.InsertLength
    def GetInsertLengthLong(self):
        return self.InsertLengthLong
    def GetExpectedCoverage(self):
        return self.ExpectedCoverage
    def SetCoverageCutOff(self,Coverage):
        self.CoverageCutOff = Coverage
    def SetMaxCoverage(self,Coverage):
        self.MaxCoverage = Coverage
    def SetMinContigLength(self,Contig):
        self.MinContigLength = Contig
    def SetInsertLength(self,Length):
        self.InsertLength = Length
    def SetInsertLengthLong(self,LongLength):
        self.InsertLengthLong = LongLength
    def SetExpectedCoverage(self,EC):
        self.ExpectedCoverage = EC 
    