class MetaSimPrimaryConfig:
    def __init__(self,PresetName = None, NumberOfReads = None, Model = 'illumina', DNACloneDist = None, Mean = None, Sigma = None):
        self.SetPresetName(PresetName)
        self.SetNumberOfReads(NumberOfReads)
        self.SetModel(Model)
        self.SetDNACloneDist(DNACloneDist)
        self.SetMean(Mean)
        self.SetSigma(Sigma)
    def SetPresetName(self, PreName):
        self.PresetName = PreName
    def SetNumberOfReads(self,Num):
        self.NumberOfReads = Num
    def SetModel(self,ModelName):
        self.Model = ModelName.upper()
    def SetDNACloneDist(self,Dist):
        self.DNACloneDist = Dist
    def SetMean(self,mu):
        self.Mean = mu
    def SetSigma(self,funnyApple):
        self.Sigma = funnyApple
    def GetPresetName(self):
        return self.PresetName
    def GetNumberOfReads(self):
        return self.NumberOfReads
    def GetModel(self):
        return self.Model
    def GetDNACloneDist(self):
        return self.DNACloneDist
    def GetMean(self):
        return self.Mean
    def GetSigma(self):
        return self.Sigma 
    