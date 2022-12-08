assignments = [line.rstrip('\n') for line in open('data/data.txt')]


class Interval:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

    def contains(self, other: "Interval") -> bool:
        return other.start <= self.start <= other.end or self.start <= other.end <= self.end

    def __repr__(self):
        return str((self.start, self.end))


count = 0
for assignment in assignments:
    first, second = assignment.split(',')

    firstInterval = Interval(*first.split('-'))
    secondInterval = Interval(*second.split('-'))
    if firstInterval.contains(secondInterval) or secondInterval.contains(firstInterval):
        count += 1

print(count)
