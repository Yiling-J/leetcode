from random import randint


def get_middle(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    need = 2 - (len(l1) + len(l2)) % 2
    mid1 = l1[len1 / 2] if len1 % 2 == 1 else (l1[len1 / 2 - 1] + l1[len1 / 2]) / 2.0
    mid2 = l2[len2 / 2] if len2 % 2 == 1 else (l2[len2 / 2 - 1] + l2[len2 / 2]) / 2.0
    if mid1 > mid2:
        left = l2[len(l2) / 2 + len(l2) % 2 - 1:]
        right = l1[:len(l1) / 2 + 1]
        q = 1 if len2 % 2 else 2
    elif mid1 < mid2:
        left = l1[len(l1) / 2 + len(l1) % 2 - 1:]
        right = l2[:len(l2) / 2 + 1]
        q = 1 if len1 % 2 else 2
    else:
        return mid1
    return get_same_distance(left, right, need, q)


def get_same_distance(left, right, need, q):
    lc = len(left)
    rc = len(right)
    while len(left) > 2 or len(right) > 2:
        print(left)
        print(right)
        if len(left) == 1:
            # need 2, reutn bigger 2 of left one and right last two
            if need == 1:
                return right[-1]
            else:
                all = [left[0], right[-1], right[-2]]
                all.sort()
                return all[1:]
        if len(right) == 1:
            # need 2, return smaller 2 of right and left first two
            if need == 1:
                return left[0]
            else:
                all = [right[0], left[0], left[1]]
                all.sort()
                return all[:2]
        l_length = len(left)
        r_length = len(right)
        n = min(l_length, r_length) / 2
        l_value = left[n]
        r_value = right[-n - 1]
        if l_value == r_value:
            print('---F---')
            print(l_value)
            return l_value if need == 1 else [l_value, l_value]
        if l_value > r_value:
            left = left[:n + 1]
            right = right[-n - 1:]
        else:
            left = left[n:]
            right = right[:-n]
    print('---F---')
    print(left)
    print(right)
    if len(left) == len(right) == 2:
        all = left + right
        all.sort()
        if need == 1:
            return all[q]
        else:
            return all[1:3]


def test():
    l1 = [randint(0, 50) for i in range(randint(2, 20))]
    l2 = [randint(0, 50) for i in range(randint(2, 20))]

    # fix length test
    l1 = [randint(0, 50) for i in range(3)]
    l2 = [randint(0, 50) for i in range(8)]

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
    print('===Guess===')
    print(r)
    print('===Merged===')
    all = l1 + l2
    all.sort()
    print(all)
    l = len(all)
    if l % 2: 
        t = all[l/2]
    else:
        t = [all[l/2-1], all[l/2]]
    print(t)
    return r == t

for i in range(1000):
    print(i)
    result = test()
    if not result:
        break