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
# from decimal import Decimal
#
# list1 = [
#     ['04/05/2023', 'Cr', 'Transfer', 'MPESA', 'Cr', 'From', ':', '254725360891,', 'Sender', ':', 'JOSEPH', 'OMANDI,',
#      'MPESA', 'TrnID', ':', 'RE48P9UNQ0', '(Trn', 'From', '1001', 'Br)', '04/05/2023', '0.00', '1,500.00',
#      '1,500.00Cr'],
#     ['17/05/2023', 'Cr', 'Cheque', 'POST', 'BANK', 'SACCO,', 'Drawee:POST', 'BANK', 'SACCO,', 'Bank:11,Clg', 'Br:45',
#      '9048', '17/05/2023', '0.00', '9,280.00']
# ]
#
# debit = Decimal()
# credit = Decimal()
#
# for line in list1:
#     try:
#         debit = Decimal(str(line[-3]).replace(",", ""))
#         credit = Decimal(str(line[-2]).replace(",", ""))
#         description = " ".join(line[1:-4])
#
#     except:
#         debit = Decimal(str(line[-2]).replace(",", ""))
#         credit = Decimal(str(line[-1]).replace(",", ""))
#         description = " ".join(line[1:-3])
#     print(debit, credit)
#     print(description)
import re

# word = "xyzXYZabcABC"
# small = {}
# capital = {}
# count = 0
#
# for x, letter in enumerate(word):
#     if letter.islower():
#         small[letter] = x
#     else:
#         if capital.get(letter) is not None:
#             pass
#         else:
#             capital[letter] = x
#
#
# for item in small.items():
#     if capital.get(item[0].upper()) is not None and item[1] < capital.get(item[0].upper()):
#         count += 1
#
#
# print(small)
# print(capital)
# print(count)


words_dictionary = {
    "one": 1,
    "two": 2,

}

string = "two+two+two"
# answer = int()
# previous_operand = ""
# for item in re.split(r'(\w+)', string):
#     if words_dictionary.get(item) is not None:
#         answer += int("%s%s" % (previous_operand, words_dictionary[item]))
#         previous_operand = ""
#     else:
#         previous_operand = item
# print(answer)


operand= "+"
sum=0


for word in re.split(r'(\w+)', string):
    if word in ("one", "two"):
        val = 1 if word == "one" else 2
        sum = sum + val if operand == "+" else sum - val
    else:

        if word == " " or word == "":
            continue
        else:
            operand=word
print(sum)

