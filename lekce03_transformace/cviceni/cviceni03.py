def gmean(values):
    n = len(values)
    result = 1.0

    for value in values:
        result *= value

    return result ** (1 / n)
