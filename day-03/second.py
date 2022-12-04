rucksacks = [line.rstrip('\n') for line in open('data/data.txt')]
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getElementPriority(element: str) -> int:
    return alphabet.index(element) + 1


def findCommonElement(first, second, third) -> str:
    return ''.join(set(first).intersection(set(second)).intersection(set(third)))


total = 0
for index in range(len(rucksacks)):
    if index % 3 == 2:
        common = findCommonElement(rucksacks[index - 2], rucksacks[index - 1], rucksacks[index])
        total += getElementPriority(common)

print(total)
