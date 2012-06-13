from RedVelvet import RedVelvet
from Metasimian import Metasimian
import datetime
import os
class Pyllumina:
    def GetTimeStamp(self):
        now = datetime.datetime.now()
        Time = [ now.year, now.month, now.day, now.hour, now.minute,now.second]
        return Time
    def CreateLog(self,FileName):
        TStr = [str(i) for i in self.INIT_TIME]
        TStr.append(FileName)
        TStr.insert(0, self.Curpath)
        FileName = ''.join(TStr)
        call(['touch',FileName])
        return open(FileName,'a')
    def SetFastaFile(self,filename):
        self.FastaFile = open(filename,'r')
    def __init__(self):
        self.INIT_TIME          = self.GetTimeStamp()            #INIT_TIME must come first
        self.Curpath            = os.path.abspath(os.curdir)
        self.Curpath            += '/'
        self.ErrorLog           = self.CreateLog('Error.Log')     
        self.OutputLog          = self.CreateLog('Output.Log')   
        self.InputLog           = self.CreateLog('Input.Log') 
        self.Metasim            = Metasimian(ErrorLog,OutputLog,InputLog)
        self.Velvet             = RedVelvet(ErrorLog,OutputLog,InputLog)
        self.FastaFile          = None