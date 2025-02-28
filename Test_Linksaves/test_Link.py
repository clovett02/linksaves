import unittest
import os
from Linksaves.Link import Link
from Linksaves.Save import Save
from typing import List

#path to this test folder
currentdir="/home/$USER/Repositories/General/ubuntu-desktop-24/Install/Test_Linksaves"
testdir=f"{currentdir}/TestDirectory"
testdir=os.path.expandvars(testdir)

locallinkfolder=f"{testdir}/Local"
remotedestination=f"{testdir}/Remote"

testgamename1="Test Game 1"
gsmname1="testgame1"
gsmpath1="/101/100"
testgameremotepath1=f"{remotedestination}/{gsmname1}{gsmpath1}"
testgamelocalpath1=f"{locallinkfolder}/{testgamename1}/Saves"
save1 = Save(testgamename1, linuxpath=testgamelocalpath1, gsmname=gsmname1, gsmpath=gsmpath1,
            baseremotepath=f"{remotedestination}")

testgamename2="Test Game 2"
gsmname2="testgame2"
gsmpath2="/202/200"
testgameremotepath2=f"{remotedestination}/{gsmname2}{gsmpath2}"
testgamelocalpath2=f"{locallinkfolder}/{testgamename2}/Saves"
save2 = Save(testgamename2, linuxpath=testgamelocalpath2, gsmname=gsmname2, gsmpath=gsmpath2,
            baseremotepath=f"{remotedestination}")



numofsaves=5
testgamenames: List[str] = [f"Test Game {i}" for i in range(numofsaves)]
gsmnames: List[str] = [f"TestGame{i}" for i in range(numofsaves)]
gsmpaths: List[str] = [f"/{i}0{i}/{i}00" for i in range(numofsaves)]
testgameremotepaths: List[str] = [f"{remotedestination}/{gsmnames[i]}{gsmpaths[i]}" for i in range(numofsaves)]
testgamelocalpaths: List[str] = [f"{locallinkfolder}/{testgamenames[i]}/Saves" for i in range(numofsaves)]

saves: List[Save] = [Save(testgamenames[i], linuxpath=testgamelocalpaths[i], gsmname=gsmnames[i], gsmpath=gsmpaths[i]) for i in range(numofsaves)]


class test_Link(unittest.TestCase):
    def setUp(self):
        os.makedirs(locallinkfolder, exist_ok=True)
        os.makedirs(remotedestination, exist_ok=True)
        return super().setUp()
    def test_Link(self):
        os.makedirs(f"{testgameremotepath1}", exist_ok=True)
        Link(save1)
        self.assertTrue(os.path.islink(testgamelocalpath1))
        self.assertEqual(testgameremotepath1, os.readlink(testgamelocalpath1))

    def test_ReplaceIncorrectLink(self):
        os.makedirs(f"{remotedestination}/testgame2/202/200")
        os.mkdir(f"{locallinkfolder}/Test Game 2")
        os.symlink(f"{remotedestination}/fakedestination", f"{locallinkfolder}/Test Game 2/Saves")
        Link(save2)

    def test_ReplaceDirectorywithLink(self):
        pass
    
    def test_ReplaceDirectorywithLinkWhenDirectoryIsNotEmpty(self):
        pass

    def test_SkipsWhenRemotePathDoesntExist(self):
        Link(saves[3])

    def test_SkipsWhenBaseRemotePathNotGiven(self):
        saves[4]._baseremotepath = ""
        Link(saves[4])

    def tearDown(self):
        def removefolder(folderpath):
            if os.path.isfile(folderpath):
                os.remove(folderpath)
                return
            if os.path.islink(folderpath):
                os.remove(folderpath)
                return
            if len(os.listdir(folderpath)) > 0:
                for f in os.listdir(folderpath):
                    removefolder(os.path.join(folderpath, f))
                os.rmdir(folderpath)
            else:
                os.rmdir(folderpath)
        removefolder(testdir)
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()
