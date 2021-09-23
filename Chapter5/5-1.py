def dutch_flag_partition(pivotIdx, arr):
    smaller, curr, larger = 0, 0, len(arr)
    pivotElem = arr[pivotIdx]
    while curr < larger:
        if arr[curr] < pivotElem:
            arr[smaller], arr[curr] = arr[curr], arr[smaller]
            smaller += 1
            curr += 1
        elif arr[curr] == pivotElem:
            curr += 1
        else:
            larger -= 1
            arr[curr], arr[larger] = arr[larger], arr[curr]

A = [0, 1, 1, 2]
idx = 2

dutch_flag_partition(idx, A)
