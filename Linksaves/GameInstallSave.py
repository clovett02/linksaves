
import os
import subprocess
import requests

class GameInstallSave:
    def __init__(self) -> None:
        pass

    def GetGameInstallSaves(self) -> list[dict[str,str]]:
        """Returns Saves as list of dictionary objects."""
        response = requests.get("http://thor.gamesaveapi/api/gamesave/all")
        return response.json()
        
if __name__ == "__main__":
    command = "findmnt -o target -t ext4,zfs"
    # result = os.system(command)
    result = subprocess.check_output(command, shell=True, text=True)
    print(result)