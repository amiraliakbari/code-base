
def binary_search(arr, x):
    a = 0
    b = len(arr)
    while b-a > 0:
        m = (a+b)/2
        if arr[m] == x: return m
        if arr[m] < x:
            a = m+1
            continue
        if arr[m] > x:
            b = m
            continue
    return -1


def test_binary_search():
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert binary_search(a, 1) == -1
    assert binary_search(a, 2) == 0
    assert binary_search(a, 3) == 1
    assert binary_search(a, 6) == -1
    assert binary_search(a, 7) == 3
    assert binary_search(a, 9) == -1
    assert binary_search(a, 11) == 4
    assert binary_search(a, 19) == 7
    assert binary_search(a, 20) == -1
    assert binary_search(a, 23) == 8
    assert binary_search(a, 25) == -1
    print "binary_search test successfull"

