def overlapping_lists(l0, l1):
    if l0 is None or l1 is None:
        return None
    curr0, curr1 = l0, l1
    sz0, sz1 = 0, 0
    while curr0:
        curr0 = curr0.next
        sz0 += 1
    while curr1:
        curr1 = curr1.next
        sz1 += 1
    curr0, curr1 = l0, l1
    while sz0 > sz1:
        curr0 = curr0.next
        sz0 -= 1
    while sz1 > sz0:
        curr1 = curr1.next
        sz1 -= 1
    while curr0 != curr1:
        curr0 = curr0.next
        curr1 = curr1.next
    return curr0
