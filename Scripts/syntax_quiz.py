def quiz(numbers_list, target):
    return [[x, y] for x in range(len(numbers_list)) for y in range(len(numbers_list)) if numbers_list[x] + numbers_list[y] == target]


print(quiz([1, 2, 3, 4, 5], 8))
