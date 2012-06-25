class VelvetH:
    def __init__(self, OutputDirectory = None, HashLength = None, FileFormat='fasta', ReadType = None, FileName = None):
        self.SetOutputDirectory(OutputDirectory)
        self.SetHashLength(HashLength)
        self.SetFileFormat(FileFormat)
        self.SetReadType(ReadType)
        self.SetFileName(FileName)
        
    def SetOutputDirectory(self,OutputDirectory):
        self.OutputDirectory = OutputDirectory
    def SetHashLength(self,HashLength):
        self.HashLength = HashLength
    def SetFileFormat(self,FileFormat):
        self.FileFormat = FileFormat
    def SetReadType(self,ReadType):
        self.ReadType = ReadType
    def SetFileName(self, FileName):
        self.FileName = FileName
        
    def GetOutputDirectory(self,OutputDirectory):
        return self.OutputDirectory
    def GetHashLength(self,HashLength):
        return self.HashLength
    def GetFileFormat(self,FileFormat):
        return self.FileFormat
    def GetReadType(self,ReadType):
        return self.ReadType
    def GetFileName(self, FileName):
        return self.FileName