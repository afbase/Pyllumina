from RedVelvet import RedVelvet
from Metasimian import Metasimian
from Logger import Logger
import datetime
import os
class Pyllumina:
    def SetReads(self,ReadNum):
        self.ReadSize = ReadNum
    def SetFastaFile(self,filename):
        filenameType = type(filename)
        if filenameType is str:
            #self.FastaFile = open(filename,'r')
            self.FastaFileName = filename
        elif filenameType is list:
            #self.FastaFile = [open(file,'r') for file in filename]
            self.FastaFileName = filename
        else:
            self.Logr.ErrorMsg('SetFastaFile() Error, filename is not a Fasta file')
    def CheckSettings(self):
        if self.FastaFileName == None:
            self.Logr.ErrorMsg('No Fasta File Set')
            return False
        if self.ReadSize == None:
            self.Logr.ErrorMsg('No ReadSize Set; please set the  number  of  reads  or  mate  pairs  generate')
            return False
        return True
    def RunPyllumina(self):
        try:
            #first we need to check if all parameters are set or not
            if self.CheckSettings()==True:
                continue
            else:
                self.Logr.ErrorMsg('RunPyllumina failed;  Settings were not set')
        finally:
            #Close files
            self.ErrorLog.close()
            self.OutputLog.close()
            self.InputLog.close()
    def __init__(self):
        self.INIT_TIME          = self.GetTimeStamp()            #INIT_TIME must come first
        self.Curpath            = os.path.abspath(os.curdir)
        self.Curpath            += '/'
        self.Logr               = Logger()
        self.ErrorLog           = self.Logr.CreateLog('Error.Log')     
        self.OutputLog          = self.Logr.CreateLog('Output.Log')   
        self.InputLog           = self.Logr.CreateLog('Input.Log')
        self.Logr.ErrorLog      = self.ErrorLog
        self.Logr.InputLog      = self.InputLog
        self.Logr.OutputLog     = self.OutputLog
        self.Metasim            = Metasimian(self.ErrorLog,self.OutputLog,self.InputLog)
        self.Velvet             = RedVelvet(self.ErrorLog,self.OutputLog,self.InputLog)
        #self.FastaFile          = None
        self.FastaFileName      = None
        self.ReadSize           = None
        self.MetaSimCommands    = []