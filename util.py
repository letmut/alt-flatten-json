def check_if_numbers_are_consecutive(li: list):
    """
    Returns True if numbers in the list are consecutive

    :param list_: list of integers
    :return: Boolean
    """
    return all(True if second - first == 1 else False
                for first, second in zip(li[:-1], li[1:]))
