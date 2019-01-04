import sys


PY3 = sys.version_info[0] == 3

if PY3:
    to_unicode = str
    basestring = (str, bytes)
    from itertools import zip_longest
    from collections.abc import Iterable
else:                                                  # pragma: no cover
    basestring = basestring
    to_unicode = unicode                               # noqa: F821
    from itertools import izip_longest as zip_longest  # noqa: F401
    from collections import Iterable                   # noqa: F401
