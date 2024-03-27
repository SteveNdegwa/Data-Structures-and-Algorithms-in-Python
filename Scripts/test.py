# letters_dict = {
#     0: [],
#     1: [],
#     2: ["a", "b", "c"],
#     3: ["d", "e", "f"],
#     4: ["g", "h", "i"],
#     5: ["j", "k", "l"],
#     6: ["m", "n", "o"],
#     7: ["p", "q", "r", "s"],
#     8: ["t", "u", "v"],
#     9: ["w", "x", "y", "z"],
# }
#
#
# def possible_combinations(arr):
#     num = arr[0]
#
#     if len(arr) == 1:
#         perms = []
#         for x, letter in enumerate(letters_dict[num]):
#             perms.append(letter)
#         return perms
#
#     perms = possible_combinations(arr[1:])
#     letters = letters_dict[num]
#     if not len(letters):
#         return perms
#
#     results = []
#     for x in range(len(letters)):
#         letter = letters[x]
#         for y in range(len(perms)):
#             # results.append(f'{letters[x]}{perms[y]}')
#             results.append("%s%s" % (letters[x], perms[y]))
#     return results
#
#
# print(possible_combinations([5, 5, 5, 5, 5]))

def river_sizes(arr):
    results = []
    explored = [[False for x in range(len(arr[j]))] for j in range(len(arr))]
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if not explored[x][y]:
                get_river_sizes(arr, explored, x, y, results)
    return results


def get_river_sizes(arr, explored, row, col, results):
    nodes_to_explore = [[row, col]]
    current_size = 0

    while len(nodes_to_explore):
        row = nodes_to_explore[0][0]
        col = nodes_to_explore[0][1]
        nodes_to_explore.pop(0)
        if explored[row][col]:
            continue
        if arr[row][col] == 0:
            explored[row][col] = True
            continue
        explored[row][col] = True
        current_size += 1
        neighbors = get_neighbors(arr, row, col)
        for neighbor in neighbors:
            nodes_to_explore.append(neighbor)
    if current_size > 0:
        results.append(current_size)


def get_neighbors(arr, row, col):
    neighbors_list = []
    if row != 0:
        neighbors_list.append([row - 1, col])
    if row != len(arr) - 1:
        neighbors_list.append([row + 1, col])
    if col != 0:
        neighbors_list.append([row, col - 1])
    if col != len(arr[row]) - 1:
        neighbors_list.append([row, col + 1])
    return neighbors_list


print(river_sizes([[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]))
