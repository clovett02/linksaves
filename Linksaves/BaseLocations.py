
import os
from pathlib import Path
import json

class BaseLocations:
    def __init__(self) -> None:
        """Loads base location data from file"""
        self._steamcompatpath: str
        self._steamuserdatapath: str
        self._baseremotepath: str
        self._userdir = os.path.expanduser('~')
        self.LoadLocationData()

    @property
    def SteamCompatPath(self) -> str:
        return self._steamcompatpath
    
    @SteamCompatPath.setter
    def SteamCompatPath(self, p:str):
        self._steamcompatpath = p

    @property
    def SteamUserDataPath(self) -> str:
        return self._steamuserdatapath
    
    @SteamUserDataPath.setter
    def SteamUserDataPath(self, p:str):
        self._steamuserdatapath = p

    @property
    def BaseRemotePath(self) -> str:
        return self._baseremotepath

    @BaseRemotePath.setter
    def BaseRemotePath(self, p:str):
        self._baseremotepath = p

    @property
    def UserDir(self):
        return self._userdir

    def LoadLocationData(self):
        filepath = Path(__file__).parent.joinpath("baselocationdata.json")
        with open(filepath, "r") as f:
            jsondata: dict[str,str] = json.load(f)
            self.SteamCompatPath = jsondata["steamcompatpath"]
            self.SteamUserDataPath = jsondata["steamuserdatapath"]
            self.BaseRemotePath = jsondata["baseremotepath"]
