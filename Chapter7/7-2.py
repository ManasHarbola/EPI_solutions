def reverse_sublist(L, start, finish):
    #reverses a linked list of length n
    def reverse_list(L, n):
        prev_node = None
        next_node = None
        tail = L
        for i in range(n):
            next_node, L.next = L.next, prev_node
            prev_node, L = L, next_node
        return (prev_node, tail)
    
    if start == finish:
        return L
    
    before_start, start_head, after_finish = None, None, None
    head, curr = L, L
    idx = 1
    while idx <= finish:
        if idx == start - 1:
            before_start = curr
        elif idx == start:
            start_head = curr
        elif idx == finish:
            after_finish = curr.next
        curr = curr.next
        idx += 1
    
    sublist_head, sublist_tail = reverse_list(start_head, finish - start + 1)
    if before_start:
        before_start.next = sublist_head
    else:
        head = sublist_head
    sublist_tail.next = after_finish

    return head

