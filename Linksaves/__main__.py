from Linksaves.Save import Saves
from Linksaves.Link import Link

if __name__ == "__main__":
    saves = Saves()
    for s in saves.Saves:
        Link(s)