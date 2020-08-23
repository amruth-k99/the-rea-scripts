import sys


def minimumMovements(pos=2, obst=[], ways=[], last=0):
    count = 0
    if not pos in obst:
        return 0
    if obst[0] == 1 and last == 2:
        return None
        return -1
        count = count + minimumMovements(1, obst.pop(0), [], pos)

    return count


def main():
    obst = [2, 1, 2]
    decimal = minimumMovements(2, obst)
    print("Min Moves: "+str(decimal))


if __name__ == "__main__":
    main()
    pass
