from subprocess import call
import datetime
import os
class Metasimian:
    def MetaSim_Call(self,ArgsIn):
        ArgsIn.insert(0,'metasim')
        call(ArgsIn, stdin=self.InputLog, stdout=self.OutputLog, stderr=self.ErrorLog, shell=False)
        return 1 
    def __init__(self):
        self.Curpath = os.path.abspath(os.curdir)
        self.Curpath += '/'
