
import requests

class GameInstallSave:
    def __init__(self) -> None:
        pass

    def GetGameInstallSaves(self) -> list[dict[str,str]]:
        """Returns Saves as list of dictionary objects."""
        response = requests.get("http://thor.gamesaveapi/api/gamesave/all")
        return response.json()
        