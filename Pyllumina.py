from MetaSimSimulatorConfig import MetaSimSimulatorConfig
from MetaSimPrimaryConfig import MetaSimPrimaryConfig
from Metasimian import Metasimian
from FastaSequence import *
class Pyllumina:
    """
    This class is designed to be the top-level class for all code.  The user should use only this class.
    """
    def FastaFileInputChecker(self,Input):
        """
        If Input is an array data structure, it returns 0, if Input is a string type, it returns 1
        """
        if type(Input) == list or type(Input) == tuple:
            return 0
        else:
            return 1 
    def SetSequenceLength(self,FSequence):
        """
        Input: FastaSequence object or FastaSequence array
        Output: Sequence Length int or int array
        """
        if type(Input) == list or type(Input) == tuple:
            self.SequenceLength = [len(i.seq) for i in FSequence]
        else:
            self.SequenceLength = len(FSequence.seq)
    def __init__(self,Fasta_FileName,ExpCov,KMER,ErrorModel):
        if self.FastaFileInputChecker(Fasta_FileName)==1:#Make sure this checks how many sequences we have; if more than one break it up into several files for metasim to read
            self.FastaSequence = fasta_read(Fasta_FileName)
        else:
            self.FastaSequence = [fasta_read(i) for i in Fasta_FileName]
        self.SetSequenceLength(self.FastaSequence)
        self.FastaFileName = Fasta_FileName
        self.ExpectedCoverage = ExpCov
        self.KmerLength = KMER
        self.MetaSimPrimary = MetaSimPrimaryConfig()
        self.MetaSimPrimary.Model = ErrorModel
        self.MetaSimSimulator = MetaSimSimulatorConfig()
        self.MetaSym = Metasimian(self.MetaSimPrimary,self.MetaSimSimulator)
        
        #Expected Covereage -> Velvet
        #MinCutoff->Velvet
        #PairLength -> MetaSim->PrimaryConf