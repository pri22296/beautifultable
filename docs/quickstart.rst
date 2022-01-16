*************************************************************************
Quickstart
*************************************************************************

=========================================================================
Building the Table
=========================================================================

Building a table is very easy. :class:`.BeautifulTable` provides two views
``rows`` and ``columns``. You can use them to modify their respective properties.

Let's create our first table and add some rows.

.. code:: python

   >>> from beautifultable import BeautifulTable
   >>> table = BeautifulTable()
   >>> table.rows.append(["Jacob", 1, "boy"])
   >>> table.rows.append(["Isabella", 1, "girl"])
   >>> table.rows.append(["Ethan", 2, "boy"])
   >>> table.rows.append(["Sophia", 2, "girl"])
   >>> table.rows.append(["Michael", 3, "boy"])
   >>> table.columns.header = ["name", "rank", "gender"]
   >>> table.rows.header = ["S1", "S2", "S3", "S4", "S5"]
   >>> print(table)
   +----+----------+------+--------+
   |    |   name   | rank | gender |
   +----+----------+------+--------+
   | S1 |  Jacob   |  1   |  boy   |
   +----+----------+------+--------+
   | S2 | Isabella |  1   |  girl  |
   +----+----------+------+--------+
   | S3 |  Ethan   |  2   |  boy   |
   +----+----------+------+--------+
   | S4 |  Sophia  |  2   |  girl  |
   +----+----------+------+--------+
   | S5 | Michael  |  3   |  boy   |
   +----+----------+------+--------+

BeautifulTable initializes the shape lazily. Here when you appended the first row,
the number of columns was set to 3. Further rows had to be of length 3. If you had
set the columns and/or row headers beforehand as follows, the table shape would already be
set to (5, 3). Hence you would just set the rows directly using their indices or keys.

.. code:: python

   >>> from beautifultable import BeautifulTable
   >>> table = BeautifulTable()
   >>> table.columns.header = ["name", "rank", "gender"]
   >>> table.rows.header = ["S1", "S2", "S3", "S4", "S5"]
   >>> table.rows[0] = ["Jacob", 1, "boy"]
   >>> table.rows[1] = ["Isabella", 1, "girl"]
   >>> table.rows[2] = ["Ethan", 2, "boy"]
   >>> table.rows[3] = ["Sophia", 2, "girl"]
   >>> table.rows[4]  =["Michael", 3, "boy"]
   >>> print(table)
   +----+----------+------+--------+
   |    |   name   | rank | gender |
   +----+----------+------+--------+
   | S1 |  Jacob   |  1   |  boy   |
   +----+----------+------+--------+
   | S2 | Isabella |  1   |  girl  |
   +----+----------+------+--------+
   | S3 |  Ethan   |  2   |  boy   |
   +----+----------+------+--------+
   | S4 |  Sophia  |  2   |  girl  |
   +----+----------+------+--------+
   | S5 | Michael  |  3   |  boy   |
   +----+----------+------+--------+


So, We created our first table. Let's add a new column.

.. code:: python

   >>> table.columns.append(["2010", "2012", "2008", "2010", "2011"], header="year")
   >>> print(table)
   +----+----------+------+--------+------+
   |    |   name   | rank | gender | year |
   +----+----------+------+--------+------+
   | S1 |  Jacob   |  1   |  boy   | 2010 |
   +----+----------+------+--------+------+
   | S2 | Isabella |  1   |  girl  | 2012 |
   +----+----------+------+--------+------+
   | S3 |  Ethan   |  2   |  boy   | 2008 |
   +----+----------+------+--------+------+
   | S4 |  Sophia  |  2   |  girl  | 2010 |
   +----+----------+------+--------+------+
   | S5 | Michael  |  3   |  boy   | 2011 |
   +----+----------+------+--------+------+

You can also build a :class:`.BeautifulTable` using slicing. Slicing creates a
new table with it's own copy of data. But it retains the properties
of the original object. You can slice both rows or columns.

.. code:: python

   >>> new_table = table.rows[:3]
   >>> print(new_table)
   +----+----------+------+--------+------+
   |    |   name   | rank | gender | year |
   +----+----------+------+--------+------+
   | S1 |  Jacob   |  1   |  boy   | 2010 |
   +----+----------+------+--------+------+
   | S2 | Isabella |  1   |  girl  | 2012 |
   +----+----------+------+--------+------+
   | S3 |  Ethan   |  2   |  boy   | 2008 |
   +----+----------+------+--------+------+


.. code:: python

   >>> new_table = table.columns[:3]
   >>> print(new_table)
   +----+----------+------+--------+
   |    |   name   | rank | gender |
   +----+----------+------+--------+
   | S1 |  Jacob   |  1   |  boy   |
   +----+----------+------+--------+
   | S2 | Isabella |  1   |  girl  |
   +----+----------+------+--------+
   | S3 |  Ethan   |  2   |  boy   |
   +----+----------+------+--------+
   | S4 |  Sophia  |  2   |  girl  |
   +----+----------+------+--------+
   | S5 | Michael  |  3   |  boy   |
   +----+----------+------+--------+

As you can see how easy it is to create a Table with **beautifultable**.
Now lets move on to see some common use cases. For details, please refer the API Documentation.


=========================================================================
Accessing Rows
=========================================================================

You can access a row using it's index or it's header. It returns a **BTRowData** object.

.. code:: python

   >>> print(list(table.rows[3]))
   ['Sophia', 2, 'girl', '2010']

To access a particular field of a row, you can again use the index, or the header
of the required column.

.. code:: python

   >>> print(table.rows[3][2])
   girl
   >>> print(table.rows[3]['gender'])
   girl


=========================================================================
Accessing Columns
=========================================================================

You can access a column using it's index or it's header. It returns a **BTColumnData** object.

.. code:: python

   >>> print(list(table.columns['name']))
   ['Jacob', 'Isabella', 'Ethan', 'Sophia', 'Michael']

To access a particular field of a column, you can again use the index, or the header
of the required row.

.. code:: python

   >>> print(table.columns[2][3])
   girl
   >>> print(table.columns[2]['S4'])
   girl

=========================================================================
Counting Rows and Columns
=========================================================================

You can get the number of columns or rows in the table by using the
``len`` function. You can also use the :attr:`.BeautifulTable.shape`
attribute.

.. code:: python

   >>> print(len(table.columns))
   3
   >>> print(len(table.rows))
   5
   >>> print(table.shape)
   (5,3)

=========================================================================
Inserting Rows and Columns
=========================================================================

BeautifulTable provides 2 methods, :meth:`.BTRowCollection.insert` and
:meth:`.BTColumnCollection.insert` for this purpose.

.. code:: python

   >>> table.rows.insert(3, ['Gary', 2, 'boy', 2009], header='S6')
   >>> table.columns.insert(2, [78, 67, 82, 56, 86, 74], header='marks')
   >>> print(table)
   +----+----------+------+-------+--------+------+
   |    |   name   | rank | marks | gender | year |
   +----+----------+------+-------+--------+------+
   | S1 |  Jacob   |  1   |  78   |  boy   | 2010 |
   +----+----------+------+-------+--------+------+
   | S2 | Isabella |  1   |  67   |  girl  | 2012 |
   +----+----------+------+-------+--------+------+
   | S3 |  Ethan   |  2   |  82   |  boy   | 2008 |
   +----+----------+------+-------+--------+------+
   | S6 |   Gary   |  2   |  56   |  boy   | 2009 |
   +----+----------+------+-------+--------+------+
   | S4 |  Sophia  |  2   |  86   |  girl  | 2010 |
   +----+----------+------+-------+--------+------+
   | S5 | Michael  |  3   |  74   |  boy   | 2011 |
   +----+----------+------+-------+--------+------+


=========================================================================
Removing Rows and Columns
=========================================================================

Removing a row or column is very easy. Just delete it using ``del``
statement.

.. code:: python

   >>> del table.rows[3]
   >>> del table.columns['year']
   >>> print(table)
   +----+----------+------+-------+--------+
   |    |   name   | rank | marks | gender |
   +----+----------+------+-------+--------+
   | S1 |  Jacob   |  1   |  78   |  boy   |
   +----+----------+------+-------+--------+
   | S2 | Isabella |  1   |  67   |  girl  |
   +----+----------+------+-------+--------+
   | S3 |  Ethan   |  2   |  82   |  boy   |
   +----+----------+------+-------+--------+
   | S4 |  Sophia  |  2   |  86   |  girl  |
   +----+----------+------+-------+--------+
   | S5 | Michael  |  3   |  74   |  boy   |
   +----+----------+------+-------+--------+

You can also use the helper methods :meth:`.BTRowCollection.pop`,
:meth:`.BTColumnCollection.pop` to do the same thing. Both these
methods take the index or header of the row/column to be removed.

Therefore the following 2 snippets are equivalent.

.. code:: python

   >>> table.columns.pop('marks')

.. code:: python

   >>> table.columns.pop(2)


=========================================================================
Updating data in the Table
=========================================================================

Let's change the name in the 4th row to ``'Sophie'``.

.. code:: python

   >>> table.rows[3][0] = 'Sophie' # index of 4th row is 3
   >>> print(list(table.rows[3]))
   ['Sophie', 2, 86, 'girl']

You could have done the same thing using the header.

.. code:: python

   >>> table.rows[3]['name'] = 'Sophie'


Or, you can also change the entire row, or even multiple rows
using slicing.

.. code:: python

   >>> table.rows[3] = ['Sophie', 2, 56, 'girl']


You can also update existing columns as shown below.

.. code:: python

   >>> table.columns['marks'] = [75, 46, 89, 56, 82]
   >>> print(table)
   +----+----------+------+-------+--------+
   |    |   name   | rank | marks | gender |
   +----+----------+------+-------+--------+
   | S1 |  Jacob   |  1   |  75   |  boy   |
   +----+----------+------+-------+--------+
   | S2 | Isabella |  1   |  46   |  girl  |
   +----+----------+------+-------+--------+
   | S3 |  Ethan   |  2   |  89   |  boy   |
   +----+----------+------+-------+--------+
   | S4 |  Sophie  |  2   |  56   |  girl  |
   +----+----------+------+-------+--------+
   | S5 | Michael  |  3   |  82   |  boy   |
   +----+----------+------+-------+--------+

The methods :meth:`.BTRowCollection.update` and :meth:`.BTColumnCollection.update`
can be used to perform the operations discussed in this section.

Note that you can only update existing columns but can't create
a new column using this method. For that you need to use the
methods :meth:`.BTRowCollection.append`, :meth:`.BTRowCollection.insert`,
:meth:`.BTColumnCollection.append` or :meth:`.BTColumnCollection.insert`.


=========================================================================
Searching for rows or columns headers
=========================================================================

Cheking if a column header is in the table.

.. code:: python

   >>> 'rank' in table.columns.header
   True

Cheking if a row header is in the table.

.. code:: python

   >>> 'S2' in table.rows.header
   True

Cheking if a row is in table

.. code:: python

   >>> ["Ethan", 2, 89, "boy"] in table.rows
   True

Cheking if a column is in table

.. code:: python

   >>> ["Jacob", "Isabella", "Ethan", "Sophie", "Michael"] in table.columns
   True

=========================================================================
Sorting based on a Column
=========================================================================

You can also :meth:`.BTRowCollection.sort` the table based on a column
by specifying it's index or it's header.

.. code:: python

   >>> table.rows.sort('marks')
   >>> print(table)
   +----+----------+------+-------+--------+
   |    |   name   | rank | marks | gender |
   +----+----------+------+-------+--------+
   | S2 | Isabella |  1   |  46   |  girl  |
   +----+----------+------+-------+--------+
   | S4 |  Sophia  |  2   |  56   |  girl  |
   +----+----------+------+-------+--------+
   | S1 |  Jacob   |  1   |  75   |  boy   |
   +----+----------+------+-------+--------+
   | S5 | Michael  |  3   |  82   |  boy   |
   +----+----------+------+-------+--------+
   | S3 |  Ethan   |  2   |  89   |  boy   |
   +----+----------+------+-------+--------+

=========================================================================
Customizing the look of the Table
=========================================================================

-------------------------------------------------------------------------
Alignment
-------------------------------------------------------------------------

Let's change the way some columns are aligned in our table.

.. code:: python

   >>> table.columns.alignment['name'] = BeautifulTable.ALIGN_LEFT
   >>> table.columns.alignment['gender'] = BeautifulTable.ALIGN_RIGHT
   >>> print(table)
   +----+----------+------+-------+--------+
   |    | name     | rank | marks | gender |
   +----+----------+------+-------+--------+
   | S2 | Isabella |  1   |  46   |   girl |
   +----+----------+------+-------+--------+
   | S4 | Sophia   |  2   |  56   |   girl |
   +----+----------+------+-------+--------+
   | S1 | Jacob    |  1   |  75   |    boy |
   +----+----------+------+-------+--------+
   | S5 | Michael  |  3   |  82   |    boy |
   +----+----------+------+-------+--------+
   | S3 | Ethan    |  2   |  89   |    boy |
   +----+----------+------+-------+--------+

You can also set all columns to a specific alignment

.. code:: python

   >>> table.columns.alignment = BeautifulTable.ALIGN_RIGHT
   >>> print(table)
   +----+----------+------+-------+--------+
   |    |     name | rank | marks | gender |
   +----+----------+------+-------+--------+
   | S2 | Isabella |    1 |    46 |   girl |
   +----+----------+------+-------+--------+
   | S4 |   Sophia |    2 |    56 |   girl |
   +----+----------+------+-------+--------+
   | S1 |    Jacob |    1 |    75 |    boy |
   +----+----------+------+-------+--------+
   | S5 |  Michael |    3 |    82 |    boy |
   +----+----------+------+-------+--------+
   | S3 |    Ethan |    2 |    89 |    boy |
   +----+----------+------+-------+--------+

Headers can have a different alignment that the column.

.. code:: python

   >>> table.columns.header.alignment= BeautifulTable.ALIGN_RIGHT
   >>> table.columns.alignment = BeautifulTable.ALIGN_LEFT
   >>> print(table)
   +----+----------+------+-------+--------+
   |    |     name | rank | marks | gender |
   +----+----------+------+-------+--------+
   | S2 | Isabella | 1    | 46    | girl   |
   +----+----------+------+-------+--------+
   | S4 | Sophia   | 2    | 56    | girl   |
   +----+----------+------+-------+--------+
   | S1 | Jacob    | 1    | 75    | boy    |
   +----+----------+------+-------+--------+
   | S5 | Michael  | 3    | 82    | boy    |
   +----+----------+------+-------+--------+
   | S3 | Ethan    | 2    | 89    | boy    |
   +----+----------+------+-------+--------+


-------------------------------------------------------------------------
Padding
-------------------------------------------------------------------------

You can change the padding for individual column similar to
the alignment.

.. code:: python

   >>> table.columns.padding_left['rank'] = 5
   >>> table.columns.padding_right['rank'] = 3
   >>> print(table)
   +----+----------+------------+--------+
   |    |   name   |     rank   | gender |
   +----+----------+------------+--------+
   | S1 |  Jacob   |      1     |  boy   |
   +----+----------+------------+--------+
   | S2 | Isabella |      1     |  girl  |
   +----+----------+------------+--------+
   | S3 |  Ethan   |      2     |  boy   |
   +----+----------+------------+--------+
   | S4 |  Sophia  |      2     |  girl  |
   +----+----------+------------+--------+
   | S5 | Michael  |      3     |  boy   |
   +----+----------+------------+--------+


You can use a helper attribute :attr:`.BTColumnCollection.padding` to
set the left and right padding to a common value.


-------------------------------------------------------------------------
Styling
-------------------------------------------------------------------------

**beautifultable** comes with several predefined styles for various use cases.
You can use the :meth:`.BeautifulTable.set_style` method to set the style
of the table. The following styles are available:

* **STYLE_DEFAULT**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_DEFAULT)
     >>> print(table)
     +----+----------+------+--------+
     |    |   name   | rank | gender |
     +----+----------+------+--------+
     | S1 |  Jacob   |  1   |  boy   |
     +----+----------+------+--------+
     | S2 | Isabella |  1   |  girl  |
     +----+----------+------+--------+
     | S3 |  Ethan   |  2   |  boy   |
     +----+----------+------+--------+
     | S4 |  Sophia  |  2   |  girl  |
     +----+----------+------+--------+
     | S5 | Michael  |  3   |  boy   |
     +----+----------+------+--------+

* **STYLE_NONE**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_NONE)
     >>> print(table)
           name    rank  gender
     S1   Jacob     1     boy
     S2  Isabella   1     girl
     S3   Ethan     2     boy
     S4   Sophia    2     girl
     S5  Michael    3     boy

* **STYLE_DOTTED**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_DOTTED)
     >>> print(table)
     .................................
     :    :   name   : rank : gender :
     .................................
     : S1 :  Jacob   :  1   :  boy   :
     : S2 : Isabella :  1   :  girl  :
     : S3 :  Ethan   :  2   :  boy   :
     : S4 :  Sophia  :  2   :  girl  :
     : S5 : Michael  :  3   :  boy   :
     .................................

* **STYLE_SEPARATED**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_SEPARATED)
     >>> print(table)
     +====+==========+======+========+
     |    |   name   | rank | gender |
     +====+==========+======+========+
     | S1 |  Jacob   |  1   |  boy   |
     +----+----------+------+--------+
     | S2 | Isabella |  1   |  girl  |
     +----+----------+------+--------+
     | S3 |  Ethan   |  2   |  boy   |
     +----+----------+------+--------+
     | S4 |  Sophia  |  2   |  girl  |
     +----+----------+------+--------+
     | S5 | Michael  |  3   |  boy   |
     +----+----------+------+--------+

* **STYLE_COMPACT**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_COMPACT)
     >>> print(table)
             name     rank   gender
     ---- ---------- ------ --------
     S1    Jacob      1      boy
     S2   Isabella    1      girl
     S3    Ethan      2      boy
     S4    Sophia     2      girl
     S5   Michael     3      boy

* **STYLE_MYSQL**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_MYSQL)
     >>> print(table)  # Yes, the default style is same as this style
     +----+----------+------+--------+
     |    |   name   | rank | gender |
     +----+----------+------+--------+
     | S1 |  Jacob   |  1   |  boy   |
     +----+----------+------+--------+
     | S2 | Isabella |  1   |  girl  |
     +----+----------+------+--------+
     | S3 |  Ethan   |  2   |  boy   |
     +----+----------+------+--------+
     | S4 |  Sophia  |  2   |  girl  |
     +----+----------+------+--------+
     | S5 | Michael  |  3   |  boy   |
     +----+----------+------+--------+

* **STYLE_MARKDOWN**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_MARKDOWN)
     >>> print(table)  # Markdown alignment not supported currently
     |    |   name   | rank | gender |
     |----|----------|------|--------|
     | S1 |  Jacob   |  1   |  boy   |
     | S2 | Isabella |  1   |  girl  |
     | S3 |  Ethan   |  2   |  boy   |
     | S4 |  Sophia  |  2   |  girl  |
     | S5 | Michael  |  3   |  boy   |

* **STYLE_RST**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_RST)
     >>> print(table)
     ==== ========== ====== ========
             name     rank   gender
     ==== ========== ====== ========
     S1    Jacob      1      boy
     S2   Isabella    1      girl
     S3    Ethan      2      boy
     S4    Sophia     2      girl
     S5   Michael     3      boy
     ==== ========== ====== ========

* **STYLE_BOX**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_BOX)
     >>> print(table)
     ┌────┬──────────┬──────┬────────┐
     │    │   name   │ rank │ gender │
     ├────┼──────────┼──────┼────────┤
     │ S1 │  Jacob   │  1   │  boy   │
     ├────┼──────────┼──────┼────────┤
     │ S2 │ Isabella │  1   │  girl  │
     ├────┼──────────┼──────┼────────┤
     │ S3 │  Ethan   │  2   │  boy   │
     ├────┼──────────┼──────┼────────┤
     │ S4 │  Sophia  │  2   │  girl  │
     ├────┼──────────┼──────┼────────┤
     │ S5 │ Michael  │  3   │  boy   │
     └────┴──────────┴──────┴────────┘

* **STYLE_BOX_DOUBLED**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
     >>> print(table)
     ╔════╦══════════╦══════╦════════╗
     ║    ║   name   ║ rank ║ gender ║
     ╠════╬══════════╬══════╬════════╣
     ║ S1 ║  Jacob   ║  1   ║  boy   ║
     ╠════╬══════════╬══════╬════════╣
     ║ S2 ║ Isabella ║  1   ║  girl  ║
     ╠════╬══════════╬══════╬════════╣
     ║ S3 ║  Ethan   ║  2   ║  boy   ║
     ╠════╬══════════╬══════╬════════╣
     ║ S4 ║  Sophia  ║  2   ║  girl  ║
     ╠════╬══════════╬══════╬════════╣
     ║ S5 ║ Michael  ║  3   ║  boy   ║
     ╚════╩══════════╩══════╩════════╝

* **STYLE_BOX_ROUNDED**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
     >>> print(table)
     ╭────┬──────────┬──────┬────────╮
     │    │   name   │ rank │ gender │
     ├────┼──────────┼──────┼────────┤
     │ S1 │  Jacob   │  1   │  boy   │
     ├────┼──────────┼──────┼────────┤
     │ S2 │ Isabella │  1   │  girl  │
     ├────┼──────────┼──────┼────────┤
     │ S3 │  Ethan   │  2   │  boy   │
     ├────┼──────────┼──────┼────────┤
     │ S4 │  Sophia  │  2   │  girl  │
     ├────┼──────────┼──────┼────────┤
     │ S5 │ Michael  │  3   │  boy   │
     ╰────┴──────────┴──────┴────────╯

* **STYLE_GRID**

  .. code:: python

     >>> table.set_style(BeautifulTable.STYLE_GRID)
     >>> print(table)
     ╔════╤══════════╤══════╤════════╗
     ║    │   name   │ rank │ gender ║
     ╟────┼──────────┼──────┼────────╢
     ║ S1 │  Jacob   │  1   │  boy   ║
     ╟────┼──────────┼──────┼────────╢
     ║ S2 │ Isabella │  1   │  girl  ║
     ╟────┼──────────┼──────┼────────╢
     ║ S3 │  Ethan   │  2   │  boy   ║
     ╟────┼──────────┼──────┼────────╢
     ║ S4 │  Sophia  │  2   │  girl  ║
     ╟────┼──────────┼──────┼────────╢
     ║ S5 │ Michael  │  3   │  boy   ║
     ╚════╧══════════╧══════╧════════╝

For more finer customization, you can change what characters are used to draw
various parts of the table. Here we show you an example of how you can use
this feature. You can read the API Reference for more details.

.. code:: python

   >>> table.set_style(BeautifulTable.STYLE_NONE)  # clear all formatting
   >>> table.border.left = 'o'
   >>> table.border.right = 'o'
   >>> table.border.top = '<~>'
   >>> table.border.bottom = '='
   >>> table.columns.header.separator = '^'
   >>> table.columns.separator = ':'
   >>> table.rows.separator = '~'
   >>> print(table)
   <~><~><~><~><~><~><~><~><~><~><~>
   o    :   name   : rank : gender o
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   o S1 :  Jacob   :  1   :  boy   o
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   o S2 : Isabella :  1   :  girl  o
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   o S3 :  Ethan   :  2   :  boy   o
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   o S4 :  Sophia  :  2   :  girl  o
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   o S5 : Michael  :  3   :  boy   o
   =================================

As you can see, you can change quite a lot about your *BeautifulTable* instance.
For further sections, We switch the look of the table to *default* again.

-------------------------------------------------------------------------
Colored Tables
-------------------------------------------------------------------------

**beautifultable** comes with out of the box support for colored tables using
ansi escape sequences. You can also use any library which makes use of
these sequences to produce colored text output.

::

    python3 -m pip install termcolor

.. code:: python

   >>> from termcolor import colored
   >>> table.rows.append([colored("John", 'red'), 4, colored("boy", 'blue')])
   >>> print(table)

.. raw:: html

   <p style="font-family: monospace; background-color: #eeffcc;">
   +----+----------+------+--------+<br />
   |&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp; name&nbsp;&nbsp; | rank | gender |<br />
   +----+----------+------+--------+<br />
   | S1 |&nbsp; Jacob&nbsp;&nbsp; |&nbsp; 1 &nbsp; |&nbsp; boy&nbsp;&nbsp; |<br />
   +----+----------+------+--------+<br />
   | S2 | Isabella |&nbsp; 1&nbsp;&nbsp; |&nbsp; girl&nbsp; |<br />
   +----+----------+------+--------+<br />
   | S3 |&nbsp; Ethan&nbsp;&nbsp; |&nbsp; 2&nbsp;&nbsp; |&nbsp; boy&nbsp;&nbsp; |<br />
   +----+----------+------+--------+<br />
   | S4 |&nbsp; Sophia&nbsp; |&nbsp; 2&nbsp;&nbsp; |&nbsp; girl&nbsp; |<br />
   +----+----------+------+--------+<br />
   | S5 | Michael&nbsp; |&nbsp; 3&nbsp;&nbsp; |&nbsp; boy&nbsp;&nbsp; |<br />
   +----+----------+------+--------+<br />
   | S6 |&nbsp;&nbsp; <span style="color: #ff0000;">John</span>&nbsp;&nbsp; |&nbsp; 4&nbsp;&nbsp; |&nbsp; <span style="color: #0000ff;">boy</span>&nbsp;&nbsp; |<br />
   +----+----------+------+--------+
   </p>

You can also use these sequences for making texts bold, italics, etc.

-------------------------------------------------------------------------
Paragraphs
-------------------------------------------------------------------------

A cell can contain multiple paragraphs such that each one start from
a new line. **beautifultable** parses ``\n`` as a paragraph change.

.. code:: python

   >>> new_table = BeautifulTable(max_width=40)
   >>> new_table.columns.header = ["Heading 1", "Heading 2"]
   >>> new_table.rows.append(["first Line\nsecond Line", "single line"])
   >>> new_table.rows.append(["first Line\nsecond Line\nthird Line", "first Line\nsecond Line"])
   >>> new_table.rows.append(["single line", "this is a very long first line\nThis is a very long second line"])
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

You can even render a :class:`.BeautifulTable` instance inside another
table. To do that, just pass the table as any regular text and it just
works.

.. code:: python

   >>> # Setting up the inner table
   >>> subtable = BeautifulTable()
   >>> subtable.rows.append(["Jacob", 1, "boy"])
   >>> subtable.rows.append(["Isabella", 1, "girl"])
   >>> subtable.border.left = ''
   >>> subtable.border.right = ''
   >>> subtable.border.top = ''
   >>> subtable.border.right = ''
   >>>
   >>> # Setting up the outer table
   >>> table = BeautifulTable()
   >>> table.columns.header = ["Heading 1", "Heading 2"]
   >>> table.rows.append(["Sample text", "Another sample text"])
   >>> table.rows.append([subtable, "More sample text"])
   >>> table.columns.padding_left[0] = 0
   >>> table.columns.padding_right[0] = 0
   >>> print(table)
   +---------------------+---------------------+
   |      Heading 1      |      Heading 2      |
   +---------------------+---------------------+
   |     Sample text     | Another sample text |
   +---------------------+---------------------+
   |  Jacob   | 1 | boy  |  More sample text   |
   |----------+---+------|                     |
   | Isabella | 1 | girl |                     |
   +---------------------+---------------------+

=========================================================================
Streaming Tables
=========================================================================

There are situations where data retrieval is slow such as when data is
recieved over a network and you want to display the data as soon as
possible. In these cases, you can use streaming tables to render the table
with the help of a generator.

Streaming table do have their limitation. The width calculation routine
requires you to either set it manually or specify the column header or
add atleast 1 row. You also cannot have row headers for streaming tables.

.. code:: python

   >>> import time
   >>> def time_taking_process():
   ...     for i in range(5):
   ...         time.sleep(1)
   ...         yield [i, i**2]
   ...
   ...
   >>> table = BeautifulTable()
   >>> table.columns.header = ["Number", "It's Square"]
   >>> for line in table.stream(time_taking_process()):
   ...     print(line)
   ...
   +--------+-------------+
   | Number | It's Square |
   +--------+-------------+
   |   0    |      0      |
   +--------+-------------+
   |   1    |      1      |
   +--------+-------------+
   |   2    |      4      |
   +--------+-------------+
   |   3    |      9      |
   +--------+-------------+
   |   4    |     16      |
   +--------+-------------+

=========================================================================
Support for Multibyte Unicode characters
=========================================================================

**beautifultable** comes with built-in support for multibyte unicode such as
east-asian characters.

You can do much more with BeautifulTable but this much should give you a
good start. Those of you who are interested to have more control can
read the API Documentation.
