class Move:
    winTable = [[0, -1, 1],
                [1, 0, -1],
                [-1, 1, 0]]

    def __init__(self, move):
        self.move = move

    def value(self) -> int | None:
        if self.move == 'X':
            return 1
        elif self.move == 'Y':
            return 2
        elif self.move == 'Z':
            return 3
        return None

    def wins(self, otherMove) -> int | None:
        otherValue = None
        if otherMove == 'A':
            otherValue = 1
        elif otherMove == 'B':
            otherValue = 2
        elif otherMove == 'C':
            otherValue = 3

        if self.winTable[self.value() - 1][otherValue - 1] == 1:
            return 6
        elif self.winTable[self.value() - 1][otherValue - 1] == 0:
            return 3
        elif self.winTable[self.value() - 1][otherValue - 1] == -1:
            return 0
        return None

    def calculateScore(self, otherMove):
        return self.wins(otherMove) + self.value()


turns = [line.rstrip('\n') for line in open('data/data.txt')]

total = 0
for turn in turns:
    enemy, you = turn.split(' ')
    yourMove = Move(you)
    total += yourMove.calculateScore(enemy)

print(total)
