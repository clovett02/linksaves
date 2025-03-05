import os

class GSMSave:

    """Gets and holds attributes from Game save manaager file."""
    def __init__(self, steamgameID:str="", filepath:str=""):
        self._gsminfopath = ""
        self._localsavepath = ""
        self._specialpath = ""
        self._shortpath = ""
        self._steamgameid = steamgameID
        self.GSMInfoPath = filepath
        self.GetPath()

    def GetPath(self) -> str:
        with open(self.GSMInfoPath) as f:
            for row in f:
                if "SpecialPath=" in row:
                    pathstart=row.index("=") + 1
                    self.SpecialPath = row[pathstart:]
                if "Path=" in row:
                    pathstart=row.index("=") + 1


    @property
    def SpecialPath(self) -> str:
        return self._specialpath
    
    @SpecialPath.setter
    def SpecialPath(self, pathstr):
        if "%DOCUMENTS%" in pathstr:
            self._specialpath = os.path.expanduser("~/.local/share/Steam/steamapps" +
                                    f"/compatdata/{self.SteamGameID}/pfx/drive_c/users" +
                                    "/steamuser/Documents")
        elif pathstr == r"":
            self._specialpath = os.path.expanduser("~/")

    @property
    def ShortPath(self) -> str:
        return self._shortpath

    @property
    def GSMInfoPath(self) -> str:
        """Path to Gamesaves Manager Info File including filename. The '$$ GSM_DATA $$' file."""
        return self._gsminfopath
    
    @GSMInfoPath.setter
    def GSMInfoPath(self, path:str):
        if(os.path.isfile(path) & (os.path.basename(path) == "$$ GSM_DATA $$")):
            self._gsminfopath = path
        elif("$$ GSM_DATA $$" in os.listdir(path)):
            self._gsminfopath = os.path.join(path, "$$ GSM_DATA $$")
        else:
            print("No GSM DATA can be found at this location.")
            print(path)

    @property
    def LocalSavePath(self) -> str:
        """The full path to the save directory on client PC"""
        return self._localsavepath

    @LocalSavePath.setter
    def LocalSavePath(self, path):
        pass

    @property
    def SteamCompatDir(self) -> str:
        return os.path.expanduser(r"~/.local/share/Steam/steamapps/compatdata")
    
    @property
    def SteamGameID(self) -> str:
        return self._steamgameid
