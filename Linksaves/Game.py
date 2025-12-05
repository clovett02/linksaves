
from Linksaves.BaseLocations import BaseLocations
from Linksaves.LinuxSaveDTO import LinuxSaveDTO
import requests

dicttype = dict[str, str | list[dict[str, str]]]

class Game:
    """Stores Game and Save data"""
    # def __init__(self, linuxsaves: list[LinuxSaveDTO], baselocationdata: BaseLocations) -> None:
    def __init__(self) -> None:
        # self._baselocations: BaseLocations = baselocationdata
        # self._LinuxLocations: list[LinuxSaveDTO] = linuxsaves
        # self._steamcompatpath = baselocationdata.SteamCompatPath
        # self._steamuserdatapath = baselocationdata.SteamUserDataPath
        self._baselocations: BaseLocations
        self._LinuxLocations: list[LinuxSaveDTO]
        self._id:str
        self._steamid:str
        self._name:str
        self._gsmname:str

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

    def SetDataFromAPIResponse(self, jsondata: dicttype):
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
                self._LinuxLocations.append(LinuxSaveDTO(r, self._baselocations)) 

    def LoadDataFromAPI(self, gameid: str):
        jsondata: dicttype = requests.get(f"http://thor.gamesaveapi/api/gamesave/byid/{gameid}").json()
        self.SetDataFromAPIResponse(jsondata)
    
