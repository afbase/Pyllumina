from subprocess import call
import datetime
import os
class RedVelvet:
    #    InputLog = None
    #    OutputLog = None
    #    ErrorLog = None
    def GetTimeStamp(self):
        now = datetime.datetime.now()
        Time = [ now.year, now.month, now.day, now.hour, now.minute,now.second]
        return Time
    def MakeDirectory(self,ArgsIn):
        ArgsIn_Size = len(ArgsIn)
        Temp = ''
        for i in range(ArgsIn_Size):
            Temp = Temp + ArgsIn[i]
        call(['mkdir', Temp], stdin=self.InputLog, stdout=self.OutputLog, stderr=self.ErrorLog, shell=False)
        return 1
    def VelvetH_Call(self,ArgsIn):
        ArgsIn.insert(0,'velveth')
        call(ArgsIn, stdin=self.InputLog, stdout=self.OutputLog, stderr=self.ErrorLog, shell=False)
        return 1
    def VelvetG_Call(self,ArgsIn):
        ArgsIn.insert(0,'velvetg')
        call(ArgsIn, stdin=self.InputLog, stdout=self.OutputLog, stderr=self.ErrorLog, shell=False)
        return 1
    def SymbolicLink(self,source):
        Temp = ['ln', '-s', source]
        call(Temp, stdin=self.InputLog, stdout=self.OutputLog, stderr=self.ErrorLog, shell=False)
        return 1
    def CreateLog(self,FileName):
        TStr = [str(i) for i in self.INIT_TIME]
        TStr.append(FileName)
        TStr.insert(0, self.Curpath)
        FileName = ''.join(TStr)
        call(['touch',FileName])
        return open(FileName,'a')
    def N50Score(self, contigs):
        #Complete N50 assembly score code
        SigmaContigs = sum(contigs)
        HalfSigma = SigmaContigs/2
        contigs.sort()
        sums = [sum(contigs[len(contigs)-1:i]) for i in range(len(contigs)-1,-1,-1)]
        for i in range(len(sums)):
            if sums(i)>HalfSigma:
                N50 = contigs[i]
                break
        return N50
    def SetKMERRange(self,MinKMER,MaxKMER):
        KmerRange = [i for i in range(MinKMER,MaxKMER + 1,1)]
    def SetExpectedCoverageRange(self,MinExpectedCoverage, MaxExpectedCoverage):
        ExpectedCoverageRange = [i for i in range(MinExpectedCoverage,MaxExpectedCoverage + 1,1)]
    def SetCoverageCutoffRange(self,MinCoverageCutoffRange,MaxCoverageCutoffRange):
        CoverageCutoffRange = [i for i in range(MinCoverageCutoffRange,MaxCoverageCutoffRange + 1,1)]
    def SetMinContigLengthRange(self,MinMinContigLength, MaxMinContigLength):
        MinContigLengthRange = [i for i in range(MinMinContigLength, MaxMinContigLength + 1, 1)]
    def SetPairedEndRange(self,MinPairedEndRange,MaxPairedEndRange):
        PairedEndRange = [i for i in range(MinPairedEndRange,MaxPairedEndRange + 1, 1)]
    def __init__(self):
        self.Curpath = os.path.abspath(os.curdir)
        self.Curpath += '/'
        self.INIT_TIME = self.GetTimeStamp()            #INIT_TIME must come first
        self.ErrorLog = self.CreateLog('Error.Log')     
        self.OutputLog = self.CreateLog('Output.Log')   
        self.InputLog = self.CreateLog('Input.Log')     
        self.KmerRange = None                           
        self.ExpectedCoverageRange = None               
        self.CoverageCutoffRange = None                 
        self.MinContigLengthRange = None                
        self.PairedEndRange = None
