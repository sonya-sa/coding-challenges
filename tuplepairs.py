"""


    >>> tuplepairs([1,-1,2,-2,2,-2,3,4,3])
    [(1, -1), (2, -2)]

"""

def tuplepairs(lst):
    tup_lst = []
    check = 0

    # for i in range(len(lst)):
    #     if i == check:
    #         num = lst[i]
    #         if -num in lst:
    #             tup = (num, -num)
    #             lst.remove(num)
    #             lst.remove(-num)
    #             check += 1

    for num in sorted(lst, reverse=True):
        if -num in lst:
            tup_lst.append((num,-num))
            lst.remove(num)
            lst.remove(-num)

    for tup in tup_lst:
        if tup in tup_lst:
            tup_lst.remove(tup[0])

    return sorted(tup_lst)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n")