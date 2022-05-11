"""Module containing some utility methods"""


import contextlib
import warnings
import functools
from typing import Union

from .ansi import ANSIMultiByteString
from .compat import to_unicode


def to_numeric(item: Union[str, int, float]):
    """
    Helper method to convert a string to float or int if possible.

    If the conversion is not possible, it simply returns the string.
    """
    num_types = (int, float)
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


def ensure_type(value, *types, varname="value"):
    if not isinstance(value, types):
        expected_types_str = "/".join([t.__name__ for t in types])
        raise TypeError(
            f"Expected '{varname}' to be of type '{expected_types_str}', got '{type(value).__name__}'"
        )

    return value


def pre_process(item, detect_numerics, precision: int, sign_value: int):
    """Returns the final string which should be displayed"""
    if item is None:
        return ""
    if detect_numerics:
        item = to_numeric(item)
    if isinstance(item, float):
        item = round(item, precision)
    with contextlib.suppress(ValueError, TypeError):
        item = "{:{sign}}".format(item, sign=sign_value)
    return to_unicode(item)


def termwidth(item):
    """Returns the visible width of the string as shown on the terminal"""
    obj = ANSIMultiByteString(to_unicode(item))
    return obj.termwidth()


def textwrap(item, width):
    obj = ANSIMultiByteString(to_unicode(item))
    return obj.wrap(width)


def deprecation_message(
    old_name, deprecated_in, removed_in, extra_msg
):  # pragma: no cover
    return f"'{old_name}' has been deprecated in 'v{deprecated_in}' and will be removed in 'v{removed_in}'. {extra_msg}"


def deprecated(
    deprecated_in,
    removed_in,
    replacement=None,
    details=None,
):  # pragma: no cover
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwds):
            nonlocal details
            if not details:
                if replacement:
                    details = replacement.__qualname__
                    details = details.replace(
                        "BTColumns",
                        "BeautifulTable.columns",
                    )
                    details = details.replace(
                        "BTRows",
                        "BeautifulTable.rows",
                    )
                    details = details.replace(
                        "BTColumnHeader",
                        "BeautifulTable.columns.header",
                    )
                    details = details.replace(
                        "BTRowHeader",
                        "BeautifulTable.rows.header",
                    )
                    details = f"Use '{details}' instead."
                else:
                    details = ""
            message = deprecation_message(
                f.__qualname__,
                deprecated_in,
                removed_in,
                details,
            )
            if replacement:
                f.__doc__ = "{}\n\n{}".format(replacement.__doc__, message)
            warnings.warn(message, FutureWarning)
            return f(*args, **kwds)

        return wrapper

    return decorator


def deprecated_param(
    deprecated_in,
    removed_in,
    old_name,
    new_name=None,
    details=None,
):  # pragma: no cover
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            nonlocal details
            if not details:
                details = f"Use '{new_name}' instead." if new_name else ""
            message = deprecation_message(
                old_name,
                deprecated_in,
                removed_in,
                details,
            )
            if old_name in kwargs:
                warnings.warn(message, FutureWarning)
            return f(*args, **kwargs)

        return wrapper

    return decorator
