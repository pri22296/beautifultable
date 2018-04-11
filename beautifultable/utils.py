"""Module containing some utility methods"""


def convert_to_numeric(item, precision):
    """
    Helper method to convert a string to float or int if possible.

    If the conversion is not possible, it simply returns the string.
    """
    try:
        num = int(item)
    except ValueError:
        try:
            num = float(item)
        except ValueError:
            return item
        else:
            return round(num, precision)
    except TypeError:
        return item
    else:
        return num


def raise_suppressed(exp):
    exp.__cause__ = None
    raise exp
