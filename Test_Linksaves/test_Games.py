import unittest
from Linksaves.Games import Games

games: Games = Games()

class test_Games(unittest.TestCase):
    def test_Saves(self):
        self.assertGreater(len(games.Games), 5)

if __name__ == "__main__":
    unittest.main()