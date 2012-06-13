from RedVelvet import RedVelvet
from Metasimian import Metasimian
class Pyllumina:
    def __init__(self):
        self.INIT_TIME = self.GetTimeStamp()            #INIT_TIME must come first
        self.Curpath = os.path.abspath(os.curdir)
        self.Curpath += '/'
        self.ErrorLog = self.CreateLog('Error.Log')     
        self.OutputLog = self.CreateLog('Output.Log')   
        self.InputLog = self.CreateLog('Input.Log') 
        self.Metasim = Metasimian(ErrorLog,OutputLog,InputLog)
        self.Velvet = RedVelvet(ErrorLog,OutputLog,InputLog)
