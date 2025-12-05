from Linksaves.Games import Games
from Linksaves.Link import Link

if __name__ == "__main__":
    games = Games()
    for s in games.Saves:
        Link(s)