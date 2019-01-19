##########################################################################
beautifultable
##########################################################################

.. inclusion-marker-badges-start

.. image:: https://badge.fury.io/py/beautifultable.svg
    :target: https://badge.fury.io/py/beautifultable

.. image:: https://img.shields.io/pypi/pyversions/beautifultable.svg
    :target: https://pypi.python.org/pypi/beautifultable/

.. image:: https://codecov.io/gh/pri22296/beautifultable/branch/master/graphs/badge.svg
    :target: https://codecov.io/gh/pri22296/beautifultable/branch/master/

.. image:: https://api.codacy.com/project/badge/Grade/7a76eb35ad4e450eaf00339e98381511
    :target: https://www.codacy.com/app/pri22296/beautifultable?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pri22296/beautifultable&amp;utm_campaign=Badge_Grade

.. image:: https://travis-ci.org/pri22296/beautifultable.svg?branch=master
    :target: https://travis-ci.org/pri22296/beautifultable

.. image:: https://readthedocs.org/projects/beautifultable/badge/?version=latest
    :alt: Documentation Status
    :target: http://beautifultable.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/Donate-PayPal-yellow.svg
    :target: https://paypal.me/beautifultable

.. inclusion-marker-badges-end


.. inclusion-marker-introduction-start

**************************************************************************
Introduction
**************************************************************************

This Package provides BeautifulTable class for easily printing
tabular data in a visually appealing ASCII format to a terminal. 

Features included but not limited to:

* Full customization of the look and feel of the table
* Build the Table as you wish, By adding rows, or by columns or even
  mixing both these approaches.
* Full support for *colors* using ANSI sequences or any library of your
  choice. It just works.
* Plenty of predefined *styles* for multiple use cases and option to
  create custom ones.
* Support for *Unicode* characters.
  
.. inclusion-marker-introduction-end


 
.. inclusion-marker-links-start

**************************************************************************
Links
**************************************************************************

* `Documentation <http://beautifultable.readthedocs.io/en/latest/>`_

* `Source <https://github.com/pri22296/beautifultable>`_

* `API Reference <http://beautifultable.readthedocs.io/en/latest/source/beautifultable.html#module-beautifultable>`_


.. inclusion-marker-links-end



.. inclusion-marker-usage-start

**************************************************************************
Usage
**************************************************************************

Here is an example of how you can use beautifultable::

    >>> from beautifultable import BeautifulTable
    >>> table = BeautifulTable()
    >>> table.column_headers = ["name", "rank", "gender"]
    >>> table.append_row(["Jacob", 1, "boy"])
    >>> table.append_row(["Isabella", 1, "girl"])
    >>> table.append_row(["Ethan", 2, "boy"])
    >>> table.append_row(["Sophia", 2, "girl"])
    >>> table.append_row(["Michael", 3, "boy"])
    >>> print(table)
    +----------+------+--------+
    |   name   | rank | gender |
    +----------+------+--------+
    |  Jacob   |  1   |  boy   |
    +----------+------+--------+
    | Isabella |  1   |  girl  |
    +----------+------+--------+
    |  Ethan   |  2   |  boy   |
    +----------+------+--------+
    |  Sophia  |  2   |  girl  |
    +----------+------+--------+
    | Michael  |  3   |  boy   |
    +----------+------+--------+

You can learn more about beautifultable at this `Tutorial <http://beautifultable.readthedocs.io/en/latest/quickstart.html>`_

.. inclusion-marker-usage-end



.. inclusion-marker-install-start

**************************************************************************
Installation
**************************************************************************

::

    pip install beautifultable

.. inclusion-marker-install-end



.. inclusion-marker-changelog-start

**************************************************************************
Changelog
**************************************************************************

==========
v0.7.0
==========

* Added 4 new styles, **STYLE_BOX**, **STYLE_BOX_DOUBLED**, **STYLE_BOX_ROUNDED**,
  **STYLE_GRID**.
* Renamed **STYLE_RESTRUCTURED_TEXT** to **STYLE_RST**
* **wcwidth** is now an optional dependency
* Updated the algorithm for calculating width of columns(better division of space among columns)
* Added support for Paragraphs(using ``\n`` character)
* Added finer control for intersection characters using 12 new
  attributes ``intersect_{top|header|row|bottom}_{left|mid|right}``
* Added the ability to also accept bytestrings instead of unicode
* Deprecated attribute ``intersection_char``
* Deprecated methods ``get_top_border()``, ``get_bottom_border()``, ``get_header_separator()``,
  ``get_row_separator()``, ``auto_calculate_width()``
* Fixed an issue with **WEP_ELLIPSIS** and **WEP_STRIP** when using multibyte characters
* Fixed an issue where table would not be in proper form if ``column_width`` is too low

==========
v0.6.0
==========

* Added support for handling Multi byte strings
* Added support for colored strings using ANSI escape sequences
* Added constraint where all strings must be unicode
* Fixed an issue where sometimes width was calculated as higher than intended

==========
v0.5.3
==========

* Added support for handing color codes using ANSI escape sequences(experimental)
* Fixed collections ABCs deprecation warning

==========
v0.5.2
==========

* Added new style **STYLE_NONE**
* Fixed issue regarding improper conversion of non-string floats

==========
v0.5.1
==========

* Added ``detect_numerics`` boolean for toggling automatic numeric conversion

==========
v0.5.0
==========

* Added new property ``serialno_header``
* Deprecated methods with misspelled *"seperator"* in their name.
* Fixed an issue where table was corrupted when ``column_count`` was too high


==========
v0.4.0
==========

* Added predefined styles for easier customization
* Added *reverse* argument to ``sort()`` method
* Fixed *enum34* dependency for python versions prior to 3.4

==========
v0.3.0
==========

* Added property ``serialno`` for auto printing serial number
* Fixed an issue with ``sign_mode`` related to str conversion
* Fixed bugs related to python version prior to 3.3
* Fixed exception on **WEP_ELLIPSIS** and token length less than 3
* Fixed printing issues with empty table

==========
v0.2.0
==========

* Added python 2 support

==========
v0.1.3
==========

* Fixed minor issues

==========
v0.1.2
==========

* Added new property ``default_padding``
* Added new method ``update_row``
* Fixed an issue in ``auto_calculate_width()``

==========
v0.1.1
==========

* Initial release on PyPI


.. inclusion-marker-changelog-end


.. inclusion-marker-contribution-start

**************************************************************************
Contribute
**************************************************************************

If you have any suggestions or bug reports, Please create a Issue. Pull
Requests are always welcome.

.. inclusion-marker-contribution-end



.. inclusion-marker-license-start

**************************************************************************
License
**************************************************************************

This project is licensed under the MIT License - see the `LICENSE.txt <https://github.com/pri22296/beautifultable/blob/master/LICENSE.txt>`_ file for details.


.. inclusion-marker-license-end



.. inclusion-marker-donation-start

**************************************************************************
Donation
**************************************************************************

Love *beautifultable*? Consider supporting the development :)

.. image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
    :target: https://paypal.me/beautifultable


.. inclusion-marker-donation-end
