from MetaSimPrimaryConfig import MetaSimPrimaryConfig
class MetaSimErrorModelConfig:
    def __init__(   self,MetaSimPrimaryConf = MetaSimPrimaryConfig(),
                    ExpectedReadLength = None,
                    FlowCycleCount = None,
                    MatePairProb = None,
                    MatePairReadLength = None,
                    RemoveLinkerSeq = None,
                    MeanNegativeFlowSignal = None,
                    SigmaNegativeFlowSignal = None,
                    SignalSigmaWithRootMean = None,
                    GenerateSignalTrace = None,
                    ReadLengthDistribution = None,
                    Mean = None,
                    Sigma = None,
                    MatePairProb = None,
                    StartErrorRate = None,
                    EndErrorRate = None,
                    InsertErrorRate = None,
                    DeletionErrorRate = None,
                 ):
        Model454 = '454'
        ModelSanger = 'sanger'.upper()
        ModelIllumina = 'illumina'.upper()
        ModelEmpirical = 'empirical'.upper()
        self.Primary = MetaSimPrimaryConf
        if self.Primary.Model == Model454 or self.Primary.Model == ModelSanger:
            self.Model454Init(ExpectedReadLength, FlowCycleCount, MatePairProb, MatePairReadLength, RemoveLinkerSeq, MeanNegativeFlowSignal, SigmaNegativeFlowSignal, SignalSigmaWithRootMean, GenerateSignalTrace)
        elif self.Primary.Model == ModelEmpirical or self.Primary.Model == ModelIllumina:
            self.Mconf = None
        else:#Sanger
            self.ModelSangerInit(Mean, Sigma, MatePairProb, StartErrorRate, EndErrorRate, InsertErrorRate, DeletionErrorRate)
            
    def Model454Init(self,ExpectedReadLength, FlowCycleCount, MatePairProb, MatePairReadLength, RemoveLinkerSeq, MeanNegativeFlowSignal, SigmaNegativeFlowSignal, SignalSigmaWithRootMean, GenerateSignalTrace):
        self.SetExpectedReadLength( ExpectedReadLength )
        self.SetFlowCycleCount( FlowCycleCount )
        self.SetMatePairProb( MatePairProb )
        self.SetMatePairReadLength( MatePairReadLength )
        self.SetRemoveLinkerSeq( RemoveLinkerSeq )
        self.SetMeanNegativeFlowSignal( MeanNegativeFlowSignal )
        self.SetSigmaNegativeFlowSignal( SigmaNegativeFlowSignal )
        self.SetSignalSigmaWithRootMean( SignalSigmaWithRootMean )
        self.SetGenerateSignalTrace( GenerateSignalTrace )
        
    def ModelSangerInit(self, ReadLengthDistribution , Mean, Sigma, MatePairProb, StartErrorRate, EndErrorRate, InsertErrorRate, DeletionErrorRate):
        self.SetReadLengthDistribution( ReadLengthDistribution )
        self.SetMean( Mean )
        self.SetSigma( Sigma )
        self.SetMatePairProb( MatePairProb )
        self.SetStartErrorRate( StartErrorRate )
        self.SetEndErrorRate( EndErrorRate )
        self.SetInsertErrorRate( InsertErrorRate )
        self.SetDeletionErrorRate( DeletionErrorRate )
        
    def SetReadLengthDistribution(self,ReadLengthDistribution ):
        self.ReadLengthDistribution = ReadLengthDistribution
    def SetMean(self,Mean ):
        self.Mean = Mean
    def SetSigma(self,Sigma ):
        self.Sigma = Sigma
    def SetMatePairProb(self,MatePairProb ):
        self.MatePairProb = MatePairProb
    def SetStartErrorRate(self,StartErrorRate ):
        self.StartErrorRate = StartErrorRate
    def SetEndErrorRate(self,EndErrorRate ):
        self.EndErrorRate = EndErrorRate
    def SetInsertErrorRate(self,InsertErrorRate ):
        self.InsertErrorRate = InsertErrorRate
    def SetDeletionErrorRate(self,DeletionErrorRate ):
        self.DelectionErrorRate = DeletionErrorRate
    def SetExpectedReadLength(self,ExpectedReadLength ):
        self.ExpectedReadLength = ExpectedReadLength
    def SetFlowCycleCount(self,FlowCycleCount ):
        self.FlowCycleCount = FlowCycleCount
    def SetMatePairReadLength(self,MatePairReadLength ):
        self.MatePairReadLength = MatePairReadLength
    def SetRemoveLinkerSeq(self,RemoveLinkerSeq ):
        self.RemoveLinkerSeq = RemoveLinkerSeq
    def SetMeanNegativeFlowSignal(self,MeanNegativeFlowSignal ):
        self.MeanNegativeFlowSignal = MeanNegativeFlowSignal
    def SetSigmaNegativeFlowSignal(self,SigmaNegativeFlowSignal ):
        self.SigmaNegativeFlowSignal = SigmaNegativeFlowSignal
    def SetSignalSigmaWithRootMean(self,SignalSigmaWithRootMean ):
        self.SignalSigmaWithRootMean = SignalSigmaWithRootMean
    def SetGenerateSignalTrace(self,GenerateSignalTrace ):
        self.GenerateSignalTrace = GenerateSignalTrace
        
    def GetReadLengthDistribution(self):
        return self.ReadLengthDistribution
    def GetMean(self):
        return self.Mean
    def GetSigma(self):
        return self.Sigma
    def GetMatePairProb(self):
        return self.MatePairProb
    def GetStartErrorRate(self):
        return self.StartErrorRate
    def GetEndErrorRate(self):
        return self.EndErrorRate
    def GetInsertErrorRate(self):
        return self.InsertErrorRate
    def GetDeletionErrorRate(self):
        return self.DelectionErrorRate
    def GetExpectedReadLength(self):
        return self.ExpectedReadLength
    def GetFlowCycleCount(self):
        return self.FlowCycleCount
    def GetMatePairReadLength(self):
        return self.MatePairReadLength
    def GetRemoveLinkerSeq(self):
        return self.RemoveLinkerSeq
    def GetMeanNegativeFlowSignal(self):
        return self.MeanNegativeFlowSignal
    def GetSigmaNegativeFlowSignal(self):
        return self.SigmaNegativeFlowSignal
    def GetSignalSigmaWithRootMean(self):
        return self.SignalSigmaWithRootMean
    def GetGenerateSignalTrace(self):
        return self.GenerateSignalTrace