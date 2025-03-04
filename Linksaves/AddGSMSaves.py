import os

class AddGSMSaves:
    def __init__(self, filepath:str=""):
        self._gsminfopath = ""
        self.GSMInfoPath = filepath

    @property.setter
    def GSMInfoPath(self, path:str) -> str:
        if(os.path.isfile(path) & os.path.basename(path) == "$$ GSM_DATA $$"):
            self._gsminfopath = path
        elif("$$ GSM_DATA $$" in os.listdir(path)):
            self._gsminfopath = os.path.join(path, "$$ GSM_DATA $$")
        else:
            print("No GSM DATA can be found at this location.")
            print(path)

    @property
    def GSMInfoPath(self) -> str:
        return self._gsminfopath

    def GetPath(self, filepath) -> str:
        