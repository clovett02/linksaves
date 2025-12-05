
from Linksaves.BaseLocations import BaseLocations

class LinuxSaveDTO:

    def __init__(self, loc: dict[str,str], baselocationdata: BaseLocations) -> None:
        """
        Stores data for Linux Location. Used by Game object.
        
        :param self: Description
        :param loc: Description
        :type loc: dict[str, str]
        :param baselocationdata: Description
        :type baselocationdata: BaseLocations
        """
        self._LocalLocation = ""
        self.LocalLocation = loc["localLocation"]
        self._GsmLocation = loc["gsmlocation"]
        self._IsFile = loc["isFile"]
        self._IsFolder = loc["isFolder"]
        self._baselocationdata = baselocationdata

    
    @property
    def LocalLocation(self) -> str:
        """Path to Save Directory on Linux"""
        return self._LocalLocation
    
    @LocalLocation.setter
    def LocalLocation(self, path:str):
        localpath: str = path.replace("$SteamCompatDir", self._baselocationdata.SteamCompatPath)
        localpath = localpath.replace("$SteamUserData", self._baselocationdata.SteamUserDataPath)
        localpath = localpath.replace("$UserDir", self._baselocationdata.UserDir)
        self._LocalLocation = localpath

    @property
    def GsmLocation(self) -> str:
        return self._GsmLocation