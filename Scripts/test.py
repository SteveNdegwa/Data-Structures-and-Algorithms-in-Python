from datetime import datetime


def river_sizes(arr):
    sizes = []
    start = datetime.now()
    explored = [[False for y in range(len(arr[x]))] for x in range(len(arr))]
    [get_river_sizes(arr, explored, sizes, x, y) for x in range(len(arr)) for y in range(len(arr[x])) if not explored[x][y]]
    end = datetime.now()
    print("processed in", (end - start))
    return sizes


def get_river_sizes(arr, explored, sizes, row, col):
    nodes_to_be_explored = [[row, col]]
    current_river_size = 0
    while nodes_to_be_explored:
        row = nodes_to_be_explored[0][0]
        col = nodes_to_be_explored[0][1]
        nodes_to_be_explored.pop(0)
        if explored[row][col]:
            continue
        explored[row][col] = True
        if arr[row][col] == 0:
            continue
        current_river_size += 1
        get_neighbours(arr, nodes_to_be_explored, row, col)
    return sizes.append(current_river_size) if current_river_size > 0 else None


def get_neighbours(arr, nodes_to_be_explored, row, col):
    nodes_to_be_explored.append([row - 1, col]) if row != 0 else None
    nodes_to_be_explored.append([row + 1, col]) if row != len(arr) - 1 else None
    nodes_to_be_explored.append([row, col - 1]) if col != 0 else None
    nodes_to_be_explored.append([row, col + 1]) if col != len(arr[row]) - 1 else None


# print(river_sizes([[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]))
# [2, 1, 5, 2, 2]


letters_dict = {
    0: [],
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}


def possible_combinations(arr):
    if not len(arr):
        return []
    if len(arr) == 1:
        return [letter for letter in letters_dict[arr[0]]]
    current_number = arr[0]
    perms = possible_combinations(arr[1:])
    if not perms:
        return [letter for letter in letters_dict[current_number]]
    if not letters_dict[current_number]:
        return perms
    results = list()
    [results.append("%s%s" % (letter, perm)) for perm in perms for letter in letters_dict[current_number]]
    return results


combs = possible_combinations([2, 4, 7, 9])
print(combs)
print(len(combs))

