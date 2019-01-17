"""Module containing some utility methods"""

import warnings


from .ansi import ANSIMultiByteString
from .compat import to_unicode, PY3
from .exceptions import BeautifulTableDeprecationWarning


def _convert_to_numeric(item):
    """
    Helper method to convert a string to float or int if possible.

    If the conversion is not possible, it simply returns the string.
    """
    if PY3:
        num_types = (int, float)
    else:                                 # pragma: no cover
        num_types = (int, long, float)    # noqa: F821
    # We don't wan't to perform any conversions if item is already a number
    if isinstance(item, num_types):
        return item

    # First try for an int conversion so that strings like "5" are converted
    # to 5 instead of 5.0 . This is safe as a direct int cast for a non integer
    # string raises a ValueError.
    try:
        num = int(to_unicode(item))
    except ValueError:
        try:
            num = float(to_unicode(item))
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
    return to_unicode(item)


def termwidth(item):
    """Returns the visible width of the string as shown on the terminal"""
    obj = ANSIMultiByteString(to_unicode(item))
    return obj.termwidth()


def textwrap(item, width):
    obj = ANSIMultiByteString(to_unicode(item))
    return obj.wrap(width)


def raise_suppressed(exp):
    exp.__cause__ = None
    raise exp


def deprecation(message):
    warnings.warn(message, BeautifulTableDeprecationWarning)
