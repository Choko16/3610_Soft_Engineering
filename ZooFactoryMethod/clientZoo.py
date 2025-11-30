from Toronto_ZooClass import Toronto_Zoo
from Calgary_ZooClass import Calgary_Zoo


def run_demo():
    print("=== Visiting Toronto Zoo ===")
    tz = Toronto_Zoo()
    tz.startVisit()

    print("\n=== Visiting Calgary Zoo ===")
    cz = Calgary_Zoo()
    cz.startVisit()


if __name__ == "__main__":
    run_demo()
