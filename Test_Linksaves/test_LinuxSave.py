
import unittest
from Linksaves.LinuxSave import LinuxSave
from Linksaves.Game import dicttype
from pathlib import Path
import json

testdatapath = Path(__file__).parent.joinpath("test_LinuxSave.json")
baselocationdatapath = Path(__file__).parent.parent.joinpath("Linksaves/baselocationdata.json")

testdata: dicttype
baselocationdata: dict[str,str]

with open(testdatapath, "r") as f:
    testdata = json.load(f)

with open(baselocationdatapath, "r") as f:
    baselocationdata = json.load(f)

class test_LinuxSaveDTO(unittest.TestCase):
    def test_testdata(self):
        """
        Ensures data types for testdata are what is expected.
        
        :param self: Description
        """
        self.assertIsInstance(testdata["linuxLocations"], list)
        self.assertIsInstance(testdata["linuxLocations"][0], dict)
        
        loc0: dict[str,str]
        if(isinstance(testdata["linuxLocations"][0], dict)):
            loc0: dict[str,str] = testdata["linuxLocations"][0]

        self.assertIsNotNone(loc0)
        self.assertIsInstance(loc0, dict)
        self.assertIsInstance(loc0["isFile"], bool)

    def test_init(self):
        """
        Test object initialization and values of initiallized attributes/properties.
        
        :param self: Description
        """
        
        dto: LinuxSave
        if isinstance(testdata["linuxLocations"], list):
            dto: LinuxSave = LinuxSave(testdata["linuxLocations"][0])

        print(dto.GsmLocation)

if __name__ == "__main__":
    unittest.main()