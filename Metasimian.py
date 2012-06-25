from MetaSimErrorModelConfig import MetaSimErrorModelConfig
from MetaSimSimulatorConfig import MetaSimSimulatorConfig
from MetaSimPrimaryConfig import MetaSimPrimaryConfig
from subprocess import call
import datetime
import os
import multiprocessing
class Metasimian:
    def __init__(self,PrimaryConf = None
                 ,SimulatorConf = None):
        self.Curpath = os.path.abspath(os.curdir)
        self.Curpath += '/'
        self.Primary = PrimaryConf()
        self.Simulator = SimulatorConf()
        self.ErrorModel = MetaSimErrorModelConfig(self.Primary)
    def SetPrimary(self,**kwargs):
        self.Primary = MetaSimPrimaryConfig(**kwargs)
    def SetErrorModel(self,**kwargs):
        self.ErrorModel = MetaSimErrorModelConfig(**kwargs) 
        
    
