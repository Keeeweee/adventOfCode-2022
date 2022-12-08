rows = [line.rstrip('\n') for line in open('data/data.txt')]
columns = 9


def getRowElements(row):
    elements = []
    for i, element in enumerate(row):
        if i % 4 == 1:
            elements.append(element)
    return elements


def placeIntoColumns(columns, newElements):
    for index, element in enumerate(newElements):
        if element != ' ':
            columns[index].append(element)


def parseMove(row: str):
    row = row.replace("move ", '')
    row = row.replace("from ", '')
    row = row.replace("to ", '')
    row = row.strip()
    return [int(char) for char in row.split(' ')]


def getResult(space):
    result = ''
    for tower in space:
        result += tower[-1]
    return result


space = [[] for i in range(columns)]
initialising = True
for row in rows:
    if row == '':
        initialising = False
        for tower in space:
            tower.reverse()
        continue

    if initialising:
        rowElements = getRowElements(row)
        if rowElements[0] != '1':
            placeIntoColumns(space, rowElements)

    else:
        count, start, end = parseMove(row)
        moveElements = []
        for i in range(count):
            moveElements.append(space[start - 1].pop())
        moveElements.reverse()
        for i in range(count):
            space[end - 1].append(moveElements[i])

print(getResult(space))
