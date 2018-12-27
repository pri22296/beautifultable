import sys


PY3 = sys.version_info[0] == 3

if PY3:
    #str = str
    to_unicode = str
    basestring = (str, bytes)
    from itertools import zip_longest
    from collections.abc import Iterable
else:
    basestring = basestring
    to_unicode = unicode
    from itertools import izip_longest as zip_longest
    from collections import Iterable
