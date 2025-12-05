
import unittest
from Linksaves.LinuxSaveDTO import LinuxSaveDTO
from Linksaves.BaseLocations import BaseLocations
from Linksaves.Game import dicttype
from pathlib import Path
import json

testdatapath = Path(__file__).parent.joinpath("test_LinuxSaveDTO.json")
baselocationdatapath = Path(__file__).parent.parent.joinpath("Linksaves/baselocationdata.json")

testdata: dicttype
baselocationdata: dict[str,str]

with open(testdatapath, "r") as f:
    testdata = json.load(f)

with open(baselocationdatapath, "r") as f:
    baselocationdata = json.load(f)

class test_LinuxSaveDTO(unittest.TestCase):
    def test_init(self):
        if isinstance(testdata["linuxLocations"], dict):
            dto = LinuxSaveDTO(testdata["linuxLocations"], BaseLocations())
            print(dto.LocalLocation)

if __name__ == "__main__":
    unittest.main()