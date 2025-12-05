
import unittest
from Linksaves.Game import Game

testgame = Game()
testgame.LoadDataFromAPI("22")

class test_Game(unittest.TestCase):
    def test_SteamID(self):
        self.assertEqual("49520", testgame.SteamID)
    
    def test_Name(self):
        self.assertEqual("Borderlands 2", testgame.Name)
    
    def test_GsmName(self):
        self.assertEqual("Borderlands2", testgame.GSMName)
    

if __name__ == "__main__":
    unittest.main()