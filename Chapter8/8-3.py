def is_well_formed(s):
    stack = []
    left_mappings = {'[' : ']',
                     '(' : ')',
                     '{' : '}'}
    for c in s:
        if c in left_mappings:
            stack.append(c)
        elif len(stack) == 0:
            return False
        elif left_mappings[stack[-1]] == c:
            stack.pop()
        else:
            return False
    return len(stack) == 0

