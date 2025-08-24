def below_average(*args):
    """
    Returns a list of integers from the input that are less than the arithmetic average
    of the sum of all integers divided by the total number of arguments (including non-ints).

    This behavior is specific: only integers are summed, but average is calculated over len(args).

    Example:
        below_average(1, 2, 3, 4, 5) → average = 15/5 = 3.0 → [1, 2]
        below_average(1, 2, 'a', 4)   → sum(ints)=7, len=4 → avg=1.75 → [1]

    :param args: Variable number of arguments (only integers are summed)
    :return: List of integers less than the computed average
    """
    if not args:
        return []

    total_sum = 0
    for el in args:
        if type(el) == int:
            total_sum += el

    average = total_sum / len(args)

    result = []
    for el in args:
        if type(el) == int and el < average:
            result.append(el)

    return result