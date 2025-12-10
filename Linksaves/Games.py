import os
import requests
from Linksaves.Game import Game
from Linksaves.BaseLocations import BaseLocations
from pathlib import Path

dicttype = dict[str, str | list[dict[str, str]]]

class Games:
    def __init__(self, steamuserdatadir:str="", userdir:str="", 
                 baseremotepath:str=""):
        """"Stores Game info from DB in Game objects"""
        self._games: list[Game] = []
        self._baselocationdata = BaseLocations()
        self.ExecuteQuery()

    @property
    def Games(self) -> list[Game]:
        return self._games
    
    @Games.setter
    def Games(self, jsonlist: list[dicttype]):
        for row in jsonlist:
            g = Game()
            g.SetDataFromAPIResponse(row)
            self._games.append(g)
    
    def GetGames(self) -> list[dicttype]:
        """Returns Game objects as list of dictionary objects."""
        response = requests.get("http://thor.gamesaveapi/api/gamesave/all")
        return response.json()

    def ExecuteQuery(self):
        json = self.GetGames()
        self.Games = json

def GetSaves() -> list[dicttype]:
    """Returns Saves as list of dictionary objects."""
    response = requests.get("http://thor.gamesaveapi/api/gamesave/all")
    return response.json()
