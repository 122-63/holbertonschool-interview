def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file.
    """

    minOpe = 0
    div = 2
    while isinstance(n, int) and n > 1:
        while n % div:
            div += 1
        minOpe += div
        n = int(n / div)
    return minOpe
