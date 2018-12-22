import sys


PY3 = sys.version_info[0] == 3

if PY3:
    str = str
    from itertools import zip_longest
    from collections.abc import Iterable
else:
    str = unicode
    from itertools import izip_longest as zip_longest
    from collections import Iterable
