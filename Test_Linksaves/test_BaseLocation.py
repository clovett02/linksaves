
import unittest
from pathlib import Path
import json
from Linksaves.BaseLocations import BaseLocations
import os

testdata: dict[str,str]
pathtotestdata = Path(__file__).parent.parent.joinpath("Linksaves/baselocationdata.json")

with open(pathtotestdata, "r") as f:
    testdata = json.load(f)

testobj = BaseLocations()

class test_BaseLocation(unittest.TestCase):
    def test_SteamCompatPath(self):
        self.assertEqual(testdata["steamcompatpath"], testobj.SteamCompatPath)

    def test_SteamUserDataPath(self):
        self.assertEqual(testdata["steamuserdatapath"], testobj.SteamUserDataPath)

    def test_BaseRemotePath(self):
        self.assertEqual(testdata["baseremotepath"], testobj.BaseRemotePath)

    def test_UserDir(self):
        self.assertEqual(os.path.expanduser("~"), testobj.UserDir)

if __name__ == "__main__":
    unittest.main()