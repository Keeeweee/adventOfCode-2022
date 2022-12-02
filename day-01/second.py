calories = [line.rstrip('\n') for line in open('data/data.txt')]

elfCalories = []
currentElf = 0
for row in calories:
    if row == '':
        elfCalories.append(currentElf)
        currentElf = 0
    else:
        currentElf += int(row)

elfCalories.append(currentElf)

print(sum(sorted(elfCalories)[-3:]))