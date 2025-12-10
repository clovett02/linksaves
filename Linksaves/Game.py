
from Linksaves.BaseLocations import BaseLocations
from Linksaves.LinuxSave import LinuxSave
import requests
# from pathlib import Path

dicttype = dict[str, str | list[dict[str, str]]]

class Game:
    """Stores Game and Save data"""
    def __init__(self) -> None:
        self._baselocations: BaseLocations = BaseLocations()
        self._LinuxLocations: list[LinuxSave] = []
        self._id:str = ""
        self._steamid:str = ""
        self._name:str = ""
        self._gsmname:str = ""

    @property
    def SteamID(self) -> str:
        return self._steamid

    @property
    def Name(self) -> str:
        """Friendly Name of Game"""
        return self._name
    
    @property
    def GSMName(self) -> str:
        """Name in Gamesave Manager Folder"""
        return self._gsmname
    
    @property
    def LinuxLocations(self) -> list[LinuxSave]:
        return self._LinuxLocations
    
    def __str__(self):
        result = f"Game Name: {self.Name}\nGSM Name: {self.GSMName}\n"
        i=1
        for s in self._LinuxLocations:
            remotepath = self._baselocations.BaseRemotePath + f"/{self.GSMName}" + f"{s.GsmLocation}"
            result += f"LocalLocation {i}: {s.LocalLocation}\nRemotePath {i}: {remotepath}\nIsFolder {i}: {s._IsFolder}\n"
        return result
    
    def SetDataFromAPIResponse(self, jsondata: dicttype) -> None:
        if isinstance(jsondata["id"], str):
            self._id = jsondata["id"]
        if isinstance(jsondata["steamId"], str):
            self._steamid = jsondata["steamId"]
        if isinstance(jsondata["gameName"], str):
            self._name = jsondata["gameName"]
        if isinstance(jsondata["gsmname"], str):
            self._gsmname = jsondata["gsmname"]
        for r in jsondata["linuxLocations"]:
            if isinstance(r, dict):
                self._LinuxLocations.append(LinuxSave(r))

    def LoadDataFromAPI(self, gameid: str) -> None:
        jsondata: dicttype = requests.get(f"http://thor.gamesaveapi/api/gamesave/byid/{gameid}").json()
        self.SetDataFromAPIResponse(jsondata)
    
