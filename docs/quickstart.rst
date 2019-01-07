*************************************************************************
Quickstart
*************************************************************************

=========================================================================
Building the Table
=========================================================================

Building a table is very easy. You can append rows and columns
in the table. Let's create our first :class:`~.BeautifulTable`.

.. code:: python

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

We created our first table. Let's add some more data to it.
But this time we will add a new column.

.. code:: python

   >>> table.append_column("year", ["2010", "2012", "2008", "2010", "2011"])
   >>> print(table)
   +----------+------+--------+------+
   |   name   | rank | gender | year |
   +----------+------+--------+------+
   |  Jacob   |  1   |  boy   | 2010 |
   +----------+------+--------+------+
   | Isabella |  1   |  girl  | 2012 |
   +----------+------+--------+------+
   |  Ethan   |  2   |  boy   | 2008 |
   +----------+------+--------+------+
   |  Sophia  |  2   |  girl  | 2010 |
   +----------+------+--------+------+
   | Michael  |  3   |  boy   | 2011 |
   +----------+------+--------+------+

You can also build a :class:`~.BeautifulTable` using slicing. Slicing creates a
new table with it's own copy of data. But it retains the properties
of the original object.

.. code:: python

   >>> new_table = table[:3]
   >>> print(new_table)
   +----------+------+--------+------+
   |   name   | rank | gender | year |
   +----------+------+--------+------+
   |  Jacob   |  1   |  boy   | 2010 |
   +----------+------+--------+------+
   | Isabella |  1   |  girl  | 2012 |
   +----------+------+--------+------+
   |  Ethan   |  2   |  boy   | 2008 |
   +----------+------+--------+------+

As you can see how easy it is to create a Table with **beautifultable**.
Now lets move on to see some common use cases. Note that not all
features are described here. See the API Documentation to get a
detailed look at all the features.


=========================================================================
Accessing Rows
=========================================================================

You can access a row using it's index. It works just like a python
list. It returns a **RowData** object.

.. code:: python

   >>> print(list(table[3]))
   ['Sophia', 2, 'girl', '2010']

To access a particular field of a row, you can use the index, or the header.

.. code:: python

   >>> print(table[3][2])
   girl
   >>> print(table[3]['gender'])
   girl


=========================================================================
Accessing Columns
=========================================================================

Columns can be accessed using their header names or their index.
But since name of headers can be duplicated, There are methods
provided to access columns using their index. If columns are accessed
using their names, and if more than one column exists with that name
as it's header, then the first column found would be returned.

It should be noted here that the returned column is not a list. It is
an iterator.

.. code:: python

   >>> print(list(table['name']))
   ['Jacob', 'Isabella', 'Ethan', 'Sophia', 'Michael']

=========================================================================
Counting Rows and Columns
=========================================================================

You can get the number of columns in the table by accessing the
:attr:`~.BeautifulTable.column_count` property.

.. code:: python

   >>> print(table.column_count)
   3

To get the number of rows, you can just use the ``len`` function.

.. code:: python

   >>> print(len(table))
   5

=========================================================================
Inserting Rows and Columns
=========================================================================

BeautifulTable provides 2 methods, :meth:`~.BeautifulTable.insert_row` and
:meth:`~.BeautifulTable.insert_column` for this purpose.

.. code:: python

   >>> table.insert_row(3, ['Gary', 2, 'boy', 2009])
   >>> table.insert_column(2, 'marks', [78, 67, 82, 56, 86, 74])
   >>> print(table)
   +----------+------+-------+--------+------+
   |   name   | rank | marks | gender | year |
   +----------+------+-------+--------+------+
   |  Jacob   |  1   |  78   |  boy   | 2010 |
   +----------+------+-------+--------+------+
   | Isabella |  1   |  67   |  girl  | 2012 |
   +----------+------+-------+--------+------+
   |  Ethan   |  2   |  82   |  boy   | 2008 |
   +----------+------+-------+--------+------+
   |   Gary   |  2   |  56   |  boy   | 2009 |
   +----------+------+-------+--------+------+
   |  Sophia  |  2   |  86   |  girl  | 2010 |
   +----------+------+-------+--------+------+
   | Michael  |  3   |  74   |  boy   | 2011 |
   +----------+------+-------+--------+------+


=========================================================================
Removing Rows and Columns
=========================================================================

Removing a row or column is very easy. Just delete it using ``del``
statement.

.. code:: python

   >>> del table[3]
   >>> del table['year']
   >>> print(table)
   +----------+------+-------+--------+
   |   name   | rank | marks | gender |
   +----------+------+-------+--------+
   |  Jacob   |  1   |  78   |  boy   |
   +----------+------+-------+--------+
   | Isabella |  1   |  67   |  girl  |
   +----------+------+-------+--------+
   |  Ethan   |  2   |  82   |  boy   |
   +----------+------+-------+--------+
   |  Sophia  |  2   |  86   |  girl  |
   +----------+------+-------+--------+
   | Michael  |  3   |  74   |  boy   |
   +----------+------+-------+--------+

You can also use the helper methods :meth:`~.BeautifulTable.pop_row`,
:meth:`~.BeautifulTable.pop_column` to do the same thing. Both these
methods take the index of the row, or column to be removed.

Instead of the index, you can also pass the header of the column to
:meth:`~.BeautifulTable.pop_column`. Therefore the following 2
snippets are equivalent.

.. code:: python

   >>> table.pop_column('marks')

.. code:: python

   >>> table.pop_column(2)


=========================================================================
Updating data in the Table
=========================================================================

Let's change the name in the 4th row to ``'Sophie'``.

.. code:: python

   >>> table[3][0] = 'Sophie' # index of 4th row is 3
   >>> print(table[3])
   ['Sophie', 2, 86, 'girl']

You could have done the same thing using the header.

.. code:: python

   >>> table[3]['name'] = 'Sophie'


Or, you can also change the entire row, or even multiple rows
using slicing.

.. code:: python

   >>> table[3] = ['Sophie', 2, 56, 'girl']


You can also update existing columns as shown below.

.. code:: python

   >>> table['marks'] = [75, 46, 89, 56, 82]
   >>> print(table)
   +----------+------+-------+--------+
   |   name   | rank | marks | gender |
   +----------+------+-------+--------+
   |  Jacob   |  1   |  75   |  boy   |
   +----------+------+-------+--------+
   | Isabella |  1   |  46   |  girl  |
   +----------+------+-------+--------+
   |  Ethan   |  2   |  89   |  boy   |
   +----------+------+-------+--------+
   |  Sophie  |  2   |  56   |  girl  |
   +----------+------+-------+--------+
   | Michael  |  3   |  82   |  boy   |
   +----------+------+-------+--------+

The methods :meth:`~.BeautifulTable.update_row` and
:meth:`~.BeautifulTable.update_column` can be used to perform the operations
discussed in this section.

Note that you can only update existing columns but can't create
a new column using this method. For that you need to use the
methods :meth:`~.BeautifulTable.append_column` or
:meth:`~.BeautifulTable.insert_column`.


=========================================================================
Searching for rows or columns headers
=========================================================================

Cheking if a header is in the table.

.. code:: python

   >>> 'rank' in table
   True

Cheking if a row is in table

.. code:: python

   >>> ["Ethan", 2, 89, "boy"] in table
   True


=========================================================================
Sorting
=========================================================================

You can also :meth:`~.BeautifulTable.sort` the table based on a column by
specifying it's index or it's header.

.. code:: python

   >>> table.sort('name')
   >>> print(table)
   +----------+------+-------+--------+
   |   name   | rank | marks | gender |
   +----------+------+-------+--------+
   |  Ethan   |  2   |  89   |  boy   |
   +----------+------+-------+--------+
   | Isabella |  1   |  46   |  girl  |
   +----------+------+-------+--------+
   |  Jacob   |  1   |  75   |  boy   |
   +----------+------+-------+--------+
   | Michael  |  3   |  82   |  boy   |
   +----------+------+-------+--------+
   |  Sophie  |  2   |  56   |  girl  |
   +----------+------+-------+--------+

=========================================================================
Customizing the look of the Table
=========================================================================

-------------------------------------------------------------------------
Alignment
-------------------------------------------------------------------------

Let's change the way some columns are aligned in our table.

.. code:: python

   >>> table.column_alignments['name'] = BeautifulTable.ALIGN_LEFT
   >>> table.column_alignments['gender'] = BeautifulTable.ALIGN_RIGHT
   >>> print(table)
   +----------+------+--------+------+
   | name     | rank | gender | year |
   +----------+------+--------+------+
   | Jacob    |  1   |    boy | 2010 |
   +----------+------+--------+------+
   | Isabella |  1   |   girl | 2012 |
   +----------+------+--------+------+
   | Ethan    |  2   |    boy | 2008 |
   +----------+------+--------+------+
   | Sophia   |  2   |   girl | 2010 |
   +----------+------+--------+------+
   | Michael  |  3   |    boy | 2011 |
   +----------+------+--------+------+


-------------------------------------------------------------------------
Padding
-------------------------------------------------------------------------

You can change the padding for individual column similar to
the alignment.

.. code:: python

   >>> table.left_padding_widths['rank'] = 5
   >>> table.right_padding_widths['rank'] = 3
   >>> print(table)
   +----------+------------+--------+------+
   | name     |     rank   | gender | year |
   +----------+------------+--------+------+
   | Jacob    |      1     |    boy | 2010 |
   +----------+------------+--------+------+
   | Isabella |      1     |   girl | 2012 |
   +----------+------------+--------+------+
   | Ethan    |      2     |    boy | 2008 |
   +----------+------------+--------+------+
   | Sophia   |      2     |   girl | 2010 |
   +----------+------------+--------+------+
   | Michael  |      3     |    boy | 2011 |
   +----------+------------+--------+------+


You can use a helper method :meth:`~.BeautifulTable.set_padding_widths` to
set the left and right padding to a common value.


-------------------------------------------------------------------------
Styling
-------------------------------------------------------------------------

**beautifultable** comes with several predefined styles for various use cases.
You can use the :meth:`~.BeautifulTable.set_style` method to set the style
of the table. The following styles are available:

* **STYLE_DEFAULT**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_DEFAULT)
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

* **STYLE_NONE**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_NONE)
     >>> print(table)
        name    rank  gender
       Jacob     1     boy
      Isabella   1     girl
       Ethan     2     boy
       Sophia    2     girl
      Michael    3     boy

* **STYLE_DOTTED**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_DOTTED)
     >>> print(table)
     ............................
     :   name   : rank : gender :
     ............................
     :  Jacob   :  1   :  boy   :
     : Isabella :  1   :  girl  :
     :  Ethan   :  2   :  boy   :
     :  Sophia  :  2   :  girl  :
     : Michael  :  3   :  boy   :
     ............................

* **STYLE_SEPARATED**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_SEPARATED)
     >>> print(table)
     +==========+======+========+
     |   name   | rank | gender |
     +==========+======+========+
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

* **STYLE_COMPACT**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_COMPACT)
     >>> print(table)
        name     rank   gender
     ---------- ------ --------
       Jacob      1      boy
      Isabella    1      girl
       Ethan      2      boy
       Sophia     2      girl
      Michael     3      boy

* **STYLE_MYSQL**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_MYSQL)
     >>> print(table)  # Yes, the default style is same as this style
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

* **STYLE_MARKDOWN**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_MARKDOWN)
     >>> print(table)  # Markdown alignment not supported currently
     |   name   | rank | gender |
     |----------|------|--------|
     |  Jacob   |  1   |  boy   |
     | Isabella |  1   |  girl  |
     |  Ethan   |  2   |  boy   |
     |  Sophia  |  2   |  girl  |
     | Michael  |  3   |  boy   |

* **STYLE_RESTRUCTURED_TEXT**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_RESTRUCTURED_TEXT)
     >>> print(table)
     ========== ====== ========
        name     rank   gender
     ========== ====== ========
       Jacob      1      boy
      Isabella    1      girl
       Ethan      2      boy
       Sophia     2      girl
      Michael     3      boy
     ========== ====== ========

For more finer customization, you can change what characters are used to draw
various parts of the table. Here we show you an example of how you can use
this feature. You can read the API Reference for more details.

.. code:: python

   >>> table.left_border_char = 'o'
   >>> table.right_border_char = 'o'
   >>> table.top_border_char = '<~>'
   >>> table.bottom_border_char = '='
   >>> table.header_separator_char = '^'
   >>> table.row_separator_char = ''
   >>> table.intersection_char = ''
   >>> table.column_separator_char = ':'
   >>> print(table)
   <~><~><~><~><~><~><~><~><~><~><~><~
   o name     : rank : gender : year o
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   o Jacob    :  1   :    boy : 2010 o
   o Isabella :  1   :   girl : 2012 o
   o Ethan    :  2   :    boy : 2008 o
   o Sophia   :  2   :   girl : 2010 o
   o Michael  :  3   :    boy : 2011 o
   ===================================

As you can see, you can change quite a lot about your *BeautifulTable* instance.
For further sections, We switch the look of the table to *default* again.

-------------------------------------------------------------------------
Colored Tables
-------------------------------------------------------------------------

**beautifultable** comes with out of the box support for colored tables using
ansi escape sequences. You can also use any library which makes use of
these sequences to produce colored text output.

.. code:: python

   >>> table.append_row([colored("John", 'red'), 4, colored("boy", 'blue')])
   >>> print(table)

.. raw:: html

   <p style="font-family: monospace; background-color: #eeffcc;">
   +----------+------+--------+<br />
   |&nbsp;&nbsp; name&nbsp;&nbsp; | rank | gender |<br />
   +----------+------+--------+<br />
   |&nbsp; Jacob&nbsp;&nbsp; |&nbsp; 1 &nbsp; |&nbsp; boy&nbsp;&nbsp; |<br />
   +----------+------+--------+<br />
   | Isabella |&nbsp; 1&nbsp;&nbsp; |&nbsp; girl&nbsp; |<br />
   +----------+------+--------+<br />
   |&nbsp; Ethan&nbsp;&nbsp; |&nbsp; 2&nbsp;&nbsp; |&nbsp; boy&nbsp;&nbsp; |<br />
   +----------+------+--------+<br />
   |&nbsp; Sophia&nbsp; |&nbsp; 2&nbsp;&nbsp; |&nbsp; girl&nbsp; |<br />
   +----------+------+--------+<br />
   | Michael&nbsp; |&nbsp; 3&nbsp;&nbsp; |&nbsp; boy&nbsp;&nbsp; |<br />
   +----------+------+--------+<br />
   |&nbsp;&nbsp; <span style="color: #ff0000;">John</span>&nbsp;&nbsp; |&nbsp; 4&nbsp;&nbsp; |&nbsp; <span style="color: #0000ff;">boy</span>&nbsp;&nbsp; |<br />
   +----------+------+--------+
   </p>

You can also use these sequences for making texts bold, italics, etc.

-------------------------------------------------------------------------
Paragraphs
-------------------------------------------------------------------------

A cell can contain multiple paragraphs such that each one start from
a new line. **beautifultable** parses ``\n`` as a paragraph change.

.. code:: python

   >>> new_table = BeautifulTable(max_width=40)
   >>> new_table.column_headers = ["Heading 1", "Heading 2"]
   >>> new_table.append_row(["first Line\nsecond Line", "single line"])
   >>> new_table.append_row(["first Line\nsecond Line\nthird Line", "first Line\nsecond Line"])
   >>> new_table.append_row(["single line", "this is a very long first line\nThis is a very long second line"])
   >>> print(new_table)
   +-------------+------------------------+
   |  Heading 1  |       Heading 2        |
   +-------------+------------------------+
   | first Line  |      single line       |
   | second Line |                        |
   +-------------+------------------------+
   | first Line  |       first Line       |
   | second Line |      second Line       |
   | third Line  |                        |
   +-------------+------------------------+
   | single line | this is a very long fi |
   |             |        rst line        |
   |             | This is a very long se |
   |             |       cond line        |
   +-------------+------------------------+

-------------------------------------------------------------------------
Subtables
-------------------------------------------------------------------------

You can even render a :class:`~.BeautifulTable` instance inside another
table. To do that, just pass the table as any regular text and it just
works.

.. code:: python

   >>> subtable = BeautifulTable()
   >>> subtable.column_headers = ["name", "rank", "gender"]
   >>> subtable.append_row(["Jacob", 1, "boy"])
   >>> subtable.append_row(["Isabella", 1, "girl"])
   >>> parent_table = BeautifulTable()
   >>> parent_table.column_headers = ["Heading 1", "Heading 2"]
   >>> parent_table.append_row(["Sample text", "Another sample text"])
   >>> parent_table.append_row([subtable, "More sample text"])
   >>> print(parent_table)
   +------------------------------+---------------------+
   |          Heading 1           |      Heading 2      |
   +------------------------------+---------------------+
   |         Sample text          | Another sample text |
   +------------------------------+---------------------+
   | +----------+------+--------+ |  More sample text   |
   | |   name   | rank | gender | |                     |
   | +----------+------+--------+ |                     |
   | |  Jacob   |  1   |  boy   | |                     |
   | +----------+------+--------+ |                     |
   | | Isabella |  1   |  girl  | |                     |
   | +----------+------+--------+ |                     |
   +------------------------------+---------------------+

You can do much more with BeautifulTable but this much should give you a
good start. Those of you who are interested to have more control can
read the API Documentation.
