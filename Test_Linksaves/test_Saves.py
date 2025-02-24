import unittest
from Linksaves.Save import Save, Saves

class test_Saves(unittest.TestCase):
    def test_SavesRetrieval(self):
        saves = Saves()
        self.assertGreater(len(saves.Saves), 3)


if __name__ == "__main__":
    unittest.main()