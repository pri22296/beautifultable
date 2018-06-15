"""Module containing some utility methods"""


def _convert_to_numeric(item):
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
            return num
    except TypeError:
        return item
    else:
        return num


def get_output_str(item, detect_numerics, precision, sign_value):
    """Returns the final string which should be displayed
    """
    if detect_numerics:
        item = _convert_to_numeric(item)
    if isinstance(item, float):
        item = round(item, precision)
    try:
        item = '{:{sign}}'.format(item, sign=sign_value)
    except (ValueError, TypeError):
        pass
    return str(item)


def raise_suppressed(exp):
    exp.__cause__ = None
    raise exp
