from random import randint


def get_middle(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    mid1 = l1[len1 / 2] if len1 % 2 == 1 else (l1[len1 / 2 - 1] + l1[len1 / 2]) / 2.0
    mid2 = l2[len2 / 2] if len2 % 2 == 1 else (l2[len2 / 2 - 1] + l2[len2 / 2]) / 2.0
    if mid1 > mid2:
        left = l2[len(l2) / 2 + len(l2) % 2 - 1:]
        right = l1[:len(l1) / 2 + 1]
    elif mid1 < mid2:
        left = l1[len(l1) / 2 + len(l1) % 2 - 1:]
        right = l2[:len(l2) / 2 + 1]
    else:
        return mid1
    return get_same_distance(left, right)


def get_same_distance(left, right):
    while len(left) > 2 or len(right) > 2:
        print(left)
        print(right)
        l_length = len(left)
        r_length = len(right)
        n = min(l_length, r_length) / 2
        l_value = left[n]
        r_value = right[-n - 1]
        if l_value == r_value:
            print('---F---')
            print(l_value)
            return l_value
        if l_value > r_value:
            left = left[:n + 1]
            right = right[-n - 1:]
        else:
            left = left[n:]
            right = right[:-n]
    print('---F---')
    print(left)
    print(right)

get_same_distance(left, right)

l1 = [randint(0, 50) for i in range(randint(2, 20))]
l2 = [randint(0, 50) for i in range(randint(2, 20))]

# fix length test
# l1 = [randint(0, 50) for i in range(2)]
# l2 = [randint(0, 50) for i in range(7)]

# error
# l1 = [2, 8]
# l2 = [4, 6, 15, 17, 22, 29, 33, 42, 42, 49]

l1.sort()
l2.sort()
print('===Origin===')
print(l1)
print(len(l1))
print('')
print(l2)
print(len(l2))
print('')


r = get_middle(l1, l2)
print('===Merged===')
all = l1 + l2
all.sort()
print(all)
l = len(all)
if l % 2: 
	print(all[l/2])
else:
	print(all[l/2-1], all[l/2])


"""
Case1:
===Origin===
[1, 2, 3, 9, 13, 14, 21, 21, 27, 30, 39]
[3, 5, 12, 16, 16, 22, 24, 28, 31, 33, 34, 38, 47, 48]

[14, 21, 21, 27, 30, 39]
[3, 5, 12, 16, 16, 22, 24, 28]
[14, 21, 21, 27]
[16, 22, 24, 28]
---F---
[-21-, 27]
[16, 22]
===Merged===
[1, 2, 3, 3, 5, 9, 12, 13, 14, 16, 16, 21, -21-, 22, 24, 27, 28, 30, 31, 33, 34, 38, 39, 47, 48]

Case2:
===Origin===
[3, 6, 8, 20, 22, 22, 23, 23, 29, 34, 36, 40]
[14, 14, 17, 19, 21, 27, 28, 29, 37, 43, 44]

[22, 23, 23, 29, 34, 36, 40]
[14, 14, 17, 19, 21, 27]
[22, 23, 23, 29]
[17, 19, 21, 27]
[22, 23, 23]
[19, 21, 27]
---F---
[22, -23-]
[21, 27]
===Merged===
[3, 6, 8, 14, 14, 17, 19, 20, 21, 22, 22, -23-, 23, 27, 28, 29, 29, 34, 36, 37, 40, 43, 44]

GUESS:
When need 1 number, for two original lists, if even one left, geet bigger of middle two, else, smaller of middle two
"""
