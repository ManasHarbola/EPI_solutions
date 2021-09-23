def remove_kth_last(L, k):
    ptr1, ptr2 = L, L
    for i in range(k - 1):
        ptr2 = ptr2.next
    while ptr2:
        ptr1, ptr2 = ptr1.next, ptr2.next
    ptr1.next = ptr1.next.next
