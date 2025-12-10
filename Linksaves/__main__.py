from Linksaves.Games import Games
from Linksaves.Link import Link
from BaseLocations import BaseLocations
from pathlib import Path

if __name__ == "__main__":
    games = Games()
    b = BaseLocations()
    for g in games.Games:
        for s in g.LinuxLocations:
            remotepath = Path(b.BaseRemotePath).joinpath(g.GSMName).joinpath(s.GsmLocation)
            Link(g.Name, s.LocalLocation, remotepath.name)