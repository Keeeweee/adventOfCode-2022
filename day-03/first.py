rucksacks = [line.rstrip('\n') for line in open('data/data.txt')]
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getElementPriority(element: str) -> int:
    return alphabet.index(element) + 1


total = 0
for element in rucksacks:
    first = set(element[:len(element)//2])
    second = set(element[len(element)//2:])
    common = ''.join(first.intersection(second))

    total += getElementPriority(common)

print(total)
