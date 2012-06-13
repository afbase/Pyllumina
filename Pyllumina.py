from RedVelvet import RedVelvet
from Metasimian import Metasimian
import datetime
import os
class Pyllumina:
    def SetFastaFile(self,filename):
        filenameType = type(filename)
        if filenameType is str:
            #self.FastaFile = open(filename,'r')
            self.FastaFileName = filename
        elif filenameType is list:
            #self.FastaFile = [open(file,'r') for file in filename]
            self.FastaFileName = filename
        else:
            Logr.ErrorMsg('SetFastaFile() Error, filename is not a fasta file')
    def RunPyllumina(self):
        try:
            #first we need to check if all parameters are set or not
            if FastaFileName == None:
                Logr.ErrorMsg('No Fasta File Set')
            if 
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
        self.ErrorLog           = Logr.CreateLog('Error.Log')     
        self.OutputLog          = Logr.CreateLog('Output.Log')   
        self.InputLog           = Logr.CreateLog('Input.Log')
        Logr.ErrorLog           = self.ErrorLog
        Logr.InputLog           = self.InputLog
        Logr.OutputLog          = self.OutputLog
        self.Metasim            = Metasimian(ErrorLog,OutputLog,InputLog)
        self.Velvet             = RedVelvet(ErrorLog,OutputLog,InputLog)
        
        #self.FastaFile          = None
        self.FastaFileName      = None
        self.