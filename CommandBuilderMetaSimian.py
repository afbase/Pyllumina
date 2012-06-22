from Metasimian import Metasimian
class CommandBuilderMetaSimian:
    def __init__(self,Metasim = Metasimian()):
        self.SetMetasim(Metasim)
    def SetMetasim(self,Metasim):
        self.Metasim = Metasim
    def GetMetasim(self):
        return self.Metasim
    #def BuildCommands(self):
    #    self.Metasim