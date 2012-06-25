import multiprocessing
class MetaSimSimulatorConfig:
    def GetNumOfThreads(self):
        return self.NumOfThreads
    def GetGenerateFastaOutput(self):
        return self.GenerateFastaOutput
    def GetFastaOutputFileName(self):
        return self.FastaOutputFileName
    def GetCompressOutput(self):
        return self.CompressOutput
    def GetUniformSequenceWeights(self):
        return self.UniformSequenceWeights
    def GetMergeAllToOneTaxonProfile(self):
        return self.MergeAllToOneTaxonProfile
    
    def SetNumOfThreads(self,NumThreads):
        self.NumOfThreads = NumThreads
    def SetGenerateFastaOutput(self,GFO):
        self.GenerateFastaOutput = GFO
    def SetFastaOutputFileName(self, FileName):
        self.FastaOutputFileName = FileName
    def SetCompressOutput(self,CO):
        self.CompressOutput = CO
    def SetUniformSequenceWeights(self,USW):
        self.UniformSequenceWeights = USW
    def SetMergeAllToOneTaxonProfile(self,MATOTP):
        self.MergeAllToOneTaxonProfile = MATOTP
        
    def __init__(self,  NumOfThreads = multiprocessing.cpu_count(), GenerateFastaOutput = True, FastaOutputFileName = None, CompressOutput = False, UniformSequenceWeights = False, MergeAllToOneTaxonProfile = False):
        self.SetNumOfThreads(NumOfThreads)
        self.SetGenerateFastaOutput(GenerateFastaOutput)
        self.SetFastaOutputFileName(FastaOutputFileName)
        self.SetCompressOutput(CompressOutput)
        self.setUniformSequenceWeights(UniformSequenceWeights)
        self.SetMergeAllToOneTaxonProfile(MergeAllToOneTaxonProfile)