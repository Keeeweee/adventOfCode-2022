class Move:
    winTable = [[0, 1, -1],
                [-1, 0, 1],
                [1, -1, 0]]

    def __init__(self, result):
        self.result = result

    def valueIndex(self) -> int | None:
        if self.result == 'X':
            return -1
        elif self.result == 'Y':
            return 0
        elif self.result == 'Z':
            return 1
        return None

    def value(self):
        if self.result == 'X':
            return 0
        elif self.result == 'Y':
            return 3
        elif self.result == 'Z':
            return 6
        return None

    def wins(self, otherMove) -> int | None:
        otherValue = None
        if otherMove == 'A':
            otherValue = 0
        elif otherMove == 'B':
            otherValue = 1
        elif otherMove == 'C':
            otherValue = 2

        return self.winTable[otherValue].index(self.valueIndex()) + 1


    def calculateScore(self, otherMove):
        return self.wins(otherMove) + self.value()


turns = [line.rstrip('\n') for line in open('data/data.txt')]

total = 0
for turn in turns:
    enemy, you = turn.split(' ')
    yourMove = Move(you)
    total += yourMove.calculateScore(enemy)

print(total)
