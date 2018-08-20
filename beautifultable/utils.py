"""Module containing some utility methods"""

import re
import sys


PY3 = sys.version_info[0] == 3
ANSI_REGEX = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')


def _convert_to_numeric(item):
    """
    Helper method to convert a string to float or int if possible.

    If the conversion is not possible, it simply returns the string.
    """
    if PY3:
        num_types = (int, float)
    else:
        num_types = (int, long, float)
    # We don't wan't to perform any conversions if item is already a number
    if isinstance(item , num_types):
        return item

    # First try for an int conversion so that strings like "5" are converted
    # to 5 instead of 5.0 . This is safe as a direct int cast for a non integer
    # string raises a ValueError.
    try:
        num = int(str(item))
    except ValueError:
        try:
            num = float(str(item))
        except ValueError:
            return item
        else:
            return num
    except TypeError:
        return item
    else:
        return num


def get_output_str(item, detect_numerics, precision, sign_value):
    """Returns the final string which should be displayed"""
    if detect_numerics:
        item = _convert_to_numeric(item)
    if isinstance(item, float):
        item = round(item, precision)
    try:
        item = '{:{sign}}'.format(item, sign=sign_value)
    except (ValueError, TypeError):
        pass
    return str(item)


def ansilen(item):
    """Returns the length of the string after stripping ansi escape sequences"""
    return len(ANSI_REGEX.sub('', item))


def raise_suppressed(exp):
    exp.__cause__ = None
    raise exp
