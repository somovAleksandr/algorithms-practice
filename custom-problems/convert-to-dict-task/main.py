def convert_to_dict(*args):
    """
    Converts passed arguments into a dictionary where each argument is both key and value.

    :param args: Variable length argument list.
    :return: Dictionary with each argument as key and value.
    """
    return {el: el for el in args}


if __name__ == "__main__":
    print(convert_to_dict(1, 2, 3))  # {1: 1, 2: 2, 3: 3}
    print(convert_to_dict('a', 'b', (1, 2), 42))  # {'a': 'a', 'b': 'b', (1, 2): (1, 2), 42: 42}