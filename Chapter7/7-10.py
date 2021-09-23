def even_odd_merge(L):
    if L is None or L.next is None or L.next.next is None:
        return L
    
    even_head = ListNode()
    even_tail = even_head
    odd_head = ListNode()
    odd_tail = odd_head

    evenPtr, oddPtr = L, L.next
    while evenPtr and oddPtr:
        even_tail.next = evenPtr
        even_tail = even_tail.next

        odd_tail.next = oddPtr
        odd_tail = odd_tail.next

        evenPtr = oddPtr.next
        if evenPtr is None:
            break
        oddPtr = oddPtr.next.next

    #if evenPtr is None, we're done iterating
    #if oddPtr is None, we have to add one more even entry
    if oddPtr is None:
        even_tail.next = evenPtr
        even_tail = even_tail.next

    #connect even list to odd list
    even_tail = odd_head.next
    return even_head.next
