def convert_to_numeric(item):
    """
    Helper method to convert a string to float or int if possible.

    If the conversion is not possible,it simply returns the string.
    """
    try:
        r = float(item)
        if r.is_integer():
            r = int(r)
        return r
    except (ValueError, TypeError):
        return item
