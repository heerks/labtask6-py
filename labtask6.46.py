"""Program:01"""

# Count how many times each number occurs and store the result in a dictionary.
# Do not use count().

numbers = [2, 3, 2, 5, 3, 2, 5, 8]

result = {}

for num in numbers:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1

print(result)


"""Program:02"""

# Print every student who achieved the highest marks and their marks.
# Expected toppers: Sara and Ahmed.

marks = {
    'Ali': 85,
    'Sara': 95,
    'Ahmed': 95,
    'Noor': 78
}

highest = max(marks.values())

for name, mark in marks.items():
    if mark == highest:
        print(name, mark)


"""Program:03"""

# Create a dictionary where the original values become keys
# and the original keys become values.

data = {'a': 1, 'b': 2, 'c': 3}

result = {}

for key, value in data.items():
    result[value] = key

print(result)


"""Program:04"""

# Group words according to their first letter.
# Build the dictionary using loops and conditions.

words = ['apple', 'ant', 'banana', 'ball', 'cat']

result = {}

for word in words:
    first = word[0]

    if first in result:
        result[first].append(word)
    else:
        result[first] = [word]

print(result)