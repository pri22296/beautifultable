"""Module containing some utility methods"""


def convert_to_numeric(item):
    """
    Helper method to convert a string to float or int if possible.

    If the conversion is not possible,it simply returns the string.
    """
    try:
        num = float(item)
        if num.is_integer():
            return int(num)
        return num
    except (ValueError, TypeError):
        return item
