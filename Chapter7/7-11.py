def is_linked_list_a_palindrome(L: ListNode) -> bool:
    def reverse_list(head):
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    slow, fast = L, L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    head, reverse_head = L, reverse_list(slow)
    while head and reverse_head:
        if head.data != reverse_head.data:
            return False
        head, reverse_head = head.next, reverse_head.next
    return True

