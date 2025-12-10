import os
import shutil

class Link:
    def __init__(self, gamename: str, localdest: str, remotepath: str):
        """Checks and creates symlink"""
        self._remotetarget=remotepath
        self._localdest=localdest
        self._gamename = gamename
        self._linkresult = ""
        self._skipped = False
        self._successfullylinked = False
        self._symlinkcorrected = False
        self._symlinkalreadyexists = False

        if len(self._remotetarget) <= 4: 
            print(f"Remote path given for link is blank. Skipping {self._gamename}.")
            self._skipped = True
            return
        if not os.path.exists(self._remotetarget):
            print(f"Remote target isn't valid for {self._gamename}. Skipping")
            self._skipped = True
            return
        if os.path.exists(self._localdest):
            if (os.path.islink(self._localdest)):
                self.CheckLink()
            else:
                print(f"Copying Existing Files, Removing Directory and Creating Link for {self._gamename}")
                self.CopyExistingFiles()
                self.RemoveFolder(self._localdest)
                os.symlink(self._remotetarget, self._localdest)
        else:
            print(f"No directory or path exists for {self._gamename}. Creating symlink.")
            if os.path.islink(self._localdest):
                os.remove(self._localdest)
            os.makedirs(self._localdest, exist_ok=True)
            os.rmdir(self._localdest)
            os.symlink(self._remotetarget, self._localdest)
            
        self._successfullylinked = True
    
    def RemoveFolder(self, folderpath: str):
        """Recursive function for removing a folder and all items in it"""
        if os.path.isfile(folderpath):
            os.remove(folderpath)
            return
        if os.path.islink(folderpath):
            os.remove(folderpath)
            return
        if len(os.listdir(folderpath)) > 0:
            for f in os.listdir(folderpath):
                self.RemoveFolder(os.path.join(folderpath, f))
            os.rmdir(folderpath)
        else:
            os.rmdir(folderpath)

    def CheckLink(self):
        """Checks linkpath destination and replaces it if it doesn't match
        remotetarget"""
        if (os.readlink(self._localdest) == self._remotetarget):
            print(f"Link exists for {self._gamename} and is correct.")
            self._symlinkalreadyexists = True
            self._skipped = True
        else:
            print(f"Replacing link for {self._gamename} with correct symlink")
            os.remove(self._localdest)
            os.symlink(self._remotetarget, self._localdest)
            self._symlinkcorrected = True
        self._successfullylinked = True

    def CopyExistingFiles(self):
        """Copys files from existing folder to link destination."""
        files: list[str] = os.listdir(self._localdest)
        for f in files:
            shutil.copy(os.path.join(self._localdest, f), self._remotetarget)

    @property
    def SuccessfullyLinked(self) -> bool:
        return self._successfullylinked
    
    @property
    def SymlinkAlreadyExists(self) -> bool:
        return self._symlinkalreadyexists
    
    @property
    def Skipped(self) -> bool:
        return self._skipped
    
    @property
    def SymlinkCorrected(self) -> bool:
        return self._symlinkcorrected