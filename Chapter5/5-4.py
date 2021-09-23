def can_reach_end(lst):
    furthest = 0
    i = 0
    sz = len(lst)
    while furthest < sz - 1 and i < len(lst) and i <= furthest:
        furthest = max(furthest, i + lst[i])
        i += 1

    return furthest >= sz - 1
