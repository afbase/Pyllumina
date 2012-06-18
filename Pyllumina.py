from MetaSimSimulatorConfig import MetaSimSimulatorConfig
from MetaSimPrimaryConfig import MetaSimPrimaryConfig
from Metasimian import Metasimian
from FastaSequence import *
class Pyllumina:
    def FastaFileInputChecker(self,Input):
        if len(Input) > 1:
            #break it up
    def __init__(self,Fasta_FileName,ExpCov,MinCutoff,ErrorModel,PairLength):
        self.FastaFileInput = fasta_read(Fasta_FileName)
        self.FastaFileInputChecker(self.FastaFileInput)#Make sure this checks how many sequences we have; if more than one break it up into several files for metasim to read
        self.FastaFileName = Fasta_FileName
        self.MetaSimPrimary = MetaSimPrimaryConfig()
        self.MetaSimPrimary.Model = ErrorModel
        self.MetaSimSimulator = MetaSimSimulatorConfig()
        self.MetaSym = Metasimian(self.MetaSimPrimary,self.MetaSimSimulator)
        #Expected Covereage -> Velvet
        #MinCutoff->Velvet
        #PairLength -> MetaSim->PrimaryConf