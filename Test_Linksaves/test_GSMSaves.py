import unittest
from Linksaves.GSMSave import GSMSave
import os

testpath=r"/media/Linked_Gamesaves/GameSave Manager; Sync & Link/BatmanArkhamAsylum(GOTYEdition)/122"
ArkhamAsylumID="35140"
DocumentsFolder=r"/pfx/drive_c/users/steamuser/Documents"
SteamCompatDir=os.path.expanduser(r"~/.local/share/Steam/steamapps/compatdata")

class test_GSMSaves(unittest.TestCase):
    def test_GSMInfoPath(self):
        AGS: GSMSave = GSMSave(ArkhamAsylumID, testpath)
        self.assertEqual(r"/media/Linked_Gamesaves/GameSave Manager; " + \
                         r"Sync & Link/BatmanArkhamAsylum(GOTYEdition)/122/$$ GSM_DATA $$",
                          AGS.GSMInfoPath)
        
    def test_SpecialPath(self):
        AGS: GSMSave = GSMSave(ArkhamAsylumID, testpath)
        self.assertEqual(f"{SteamCompatDir}/{ArkhamAsylumID}{DocumentsFolder}", AGS.SpecialPath)
        # print(AGS.SpecialPath)

if __name__ == "__main__":
    unittest.main()
