import unittest
import Linksaves.AddGSMSaves as AddGSMSaves

testpath=r"/media/Linked_Gamesaves/GameSave Manager; Sync & Link/BatmanArkhamAsylum(GOTYEdition)/122"

class test_AddGSMSaves(unittest.TestCase):
    def test_GSMInfoPath():
        AGS = AddGSMSaves(testpath)

if __name__ == "__main__":
    unittest.main()
