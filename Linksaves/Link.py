import os
import shutil
from Linksaves.Save import Save

class Link:
    def __init__(self, save: Save):
        """Checks and creates symlink"""
        self._remotetarget=save.RemotePath
        self._localdest=save.LinuxPath
        self._save = save
        if len(self._save.RemotePath) <= 4: 
            print(f"Remote path given for link is blank. Skipping {self._save.Name}.")
            return
        if not os.path.exists(self._remotetarget):
            print(f"Remote target isn't valid for {self._save.Name}. Skipping")
            return
        if os.path.exists(self._localdest):
            if (os.path.islink(self._localdest)):
                self.CheckLink()
            else:
                print(f"Copying Existing Files, Removing Directory and Creating Link for {self._save.Name}")
                self.CopyExistingFiles()
                self.RemoveFolder(self._localdest)
                os.symlink(self._remotetarget, self._localdest)
        else:
            print(f"No directory or path exists for {self._save.Name}. Creating symlink.")
            if os.path.islink(self._localdest):
                os.remove(self._localdest)
            os.makedirs(self._localdest, exist_ok=True)
            os.rmdir(self._localdest)
            os.symlink(self._remotetarget, self._localdest)
    
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
            print(f"Link exists for {self._save.Name} and is correct.")
        else:
            print(f"Replacing link for {self._save.Name} with correct symlink")
            os.remove(self._localdest)
            os.symlink(self._remotetarget, self._localdest)

    def CopyExistingFiles(self):
        """Copys files from existing folder to link destination."""
        files: list[str] = os.listdir(self._localdest)
        for f in files:
            shutil.copy(os.path.join(self._localdest, f), self._remotetarget)
