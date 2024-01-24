def fib(n):
    fib_list = [0, 1]

    i = 2
    while i < n:
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        i += 1

    return fib_list
# def fib(n):
#     if n < 2:
#         return n
#
#     return fib(n-1) + fib(n-2)

#

# print(fib(10))


def permutation(word):
    if len(word) == 1:
        return word
    perms = permutation(word[1:])
    char = word[0]
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result


print(permutation("abcdefghijklmnopqrstuvwxyz"))
