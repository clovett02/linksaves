from typing import List
import os
import requests
import json

class Save:
    """Stores Save data"""
    def __init__(self, name:str, linuxpath:str="", windowspath:str="", gsmname:str="", gsmpath:str="",
                 steamcompatpath:str="", steamuserdatapath:str="", userdir:str="", baseremotepath:str=""):
        self._steamcompatpath=steamcompatpath
        self._steamuserdatapath=steamuserdatapath
        self._userdir=userdir
        self._name=name
        self._linuxpath=""
        self.LinuxPath=linuxpath
        self._windowspath=windowspath
        self._gsmname=gsmname
        self._gsmpath=gsmpath
        self._baseremotepath=baseremotepath
        

    @property
    def Name(self) -> str:
        """Friendly Name of Game"""
        return self._name
    
    @property
    def LinuxPath(self) -> str:
        """Path to Save Directory on Linux"""
        return self._linuxpath
    
    @LinuxPath.setter
    def LinuxPath(self, path:str):
        linuxpath: str = path.replace("$SteamCompatDir", self._steamcompatpath)
        linuxpath = linuxpath.replace("$SteamUserData", self._steamuserdatapath)
        linuxpath = linuxpath.replace("$UserDir", self._userdir)
        self._linuxpath = linuxpath
    
    @property
    def WindowsPath(self) -> str:
        """Path to Save Directory on Windows"""
        return self._windowspath
    
    @property
    def GSMName(self) -> str:
        """Name in Gamesave Manager Folder"""
        return self._gsmname
    
    @property
    def GSMPath(self) -> str:
        """Path to save within GSM folder from GSMName"""
        return self._gsmpath

    @property
    def RemotePath(self) -> str:
        return f"{self._baseremotepath}/{self.GSMName}{self.GSMPath}"
    
    def __str__(self):
        return f"""Game Name: {self.Name}\nLinux Path: {self.LinuxPath}\n""" + \
        f"""Windows Path: {self.WindowsPath}\nGSM Name: {self.GSMName}\nGSM Path: {self.GSMPath}\n""" + \
        f"""Remote Path: {self.RemotePath}"""
    

class Saves:
    UserDir: str = os.path.expanduser('~')
    SteamCompatDir: str = f"{UserDir}/.local/share/Steam/steamapps/compatdata"
    SteamUserdataDir: str = f"{UserDir}/.local/share/Steam/userdata/72532730"
    BaseRemotePath: str = "/media/Linked_Gamesaves/GameSave Manager; Sync & Link"
    def __init__(self, steamuserdatadir:str="", userdir:str="", 
                 baseremotepath:str=""):
        """"Stores save info from DB in Save objects"""
        self._saves: list[Save] = []
        self.ExecuteQuery()

    @property
    def Saves(self) -> list[Save]:
        return self._saves
    
    @Saves.setter
    def Saves(self, jsonlist: list[dict]):
        for row in jsonlist:
            self._saves.append(Save(
                name=row['gameName'],
                linuxpath=row['linux'],
                gsmname=row['gsmname'],
                gsmpath=row['gsmlocation'],
                steamcompatpath=self.SteamCompatDir,
                steamuserdatapath=self.SteamUserdataDir,
                userdir=self.UserDir,
                baseremotepath=self.BaseRemotePath

            ))
    
    def GetSaves(self) -> list[dict]:
        """Returns Saves as list of dictionary objects."""
        response = requests.get("http://thor.gamesaveapi/api/gamesave/all")
        return response.json()

    def ExecuteQuery(self):
        self.Saves = self.GetSaves()