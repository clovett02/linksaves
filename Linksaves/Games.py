import os
import requests
from Linksaves.Game import Game
from Linksaves.BaseLocations import BaseLocations

dicttype = dict[str, str | list[dict[str, str]]]


class Games:
    UserDir: str = os.path.expanduser('~')
    SteamCompatDir: str = f"{UserDir}/.local/share/Steam/steamapps/compatdata"
    SteamUserdataDir: str = f"{UserDir}/.local/share/Steam/userdata/72532730"
    BaseRemotePath: str = "/media/Linked_Gamesaves/GameSave Manager; Sync & Link"
    def __init__(self, steamuserdatadir:str="", userdir:str="", 
                 baseremotepath:str=""):
        """"Stores save info from DB in Save objects"""
        self._saves: list[Game] = []
        self._baselocationdata = BaseLocations()
        self.ExecuteQuery()

    @property
    def Saves(self) -> list[Game]:
        return self._saves
    
    @Saves.setter
    def Saves(self, jsonlist: list[dicttype]):
        for row in jsonlist:
            g = Game()
            g.SetDataFromAPIResponse(row)
            self._saves.append(g)
    
    def GetSaves(self) -> list[dicttype]:
        """Returns Saves as list of dictionary objects."""
        response = requests.get("http://thor.gamesaveapi/api/gamesave/all")
        return response.json()

    def ExecuteQuery(self):
        json = self.GetSaves()
        self.Saves = json