from MetaSimErrorModelConfig import MetaSimErrorModelConfig

from subprocess import call
import datetime
import os

class Metasimian:
    def __init__(self,PrimaryConf,SimulatorConf):
        self.Curpath = os.path.abspath(os.curdir)
        self.Curpath += '/'
        self.Primary = PrimaryConf()
        self.Simulator = SimulatorConf()
        self.ErrorModel = MetaSimErrorModelConfig(self.Primary)
