def BinarySearch(alist, item):
    first = 0 
    last = len(alist) - 1
    found = False 


    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] == "":
            found = False
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1



BinarySearch(["a", "b", "", "", "c", "", "d", ""], "a")

def sparse_search(lst, item, first_index=0, last_index=None):
    """
    >>> i = sparse_search(['', '', 'a', '', 'b', '', '', 'c', '', ''], 'a')
    >>> i = 2
    True
    """

    mid = (last_index + first_index) // 2

    if lst[mid] == '':
        left = mid -1 
        right = mid + 1

        while True:
            if left < first_index and right > last_index:
                return None
            elif right <= last_index and lst[right] != '':
                mid = right
                break
            elif left >= first_index and lst[left] != '':
                mid = left
                break

            right += 1
            left -= 1


    if lst[mid] == item:
        return mid
