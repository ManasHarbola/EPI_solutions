def evaluate(expression):
    stack = []
    result = 0
    operations = {'+' : lambda a, b: b + a,
                  '-' : lambda a, b: b - a,
                  '*' : lambda a, b: b * a,
                  '/' : lambda a, b: int(b / a)}
    delimiter = ','
    for token in expression.split(delimiter):
        if token in operations:
            stack.append(operations[token](stack.pop(), stack.pop()))
        else:
            stack.append(int(token))

    return stack.pop()

