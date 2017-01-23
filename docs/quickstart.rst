************************************************************************* 
Quickstart
*************************************************************************

=========================================================================
Building the Table
=========================================================================

Building a table is very easy. You can append rows and columns
in the table. Let's create our first BeautifulTable.

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

We created our first BeautifulTable. Let's add some more data to it.
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

You can also build a BeautifulTable using slicing.
Slicing creates a new table with it's own copy of data.
But it retains the properties of the original object.

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

As you can see how easy it is to create a Table with BeautifulTable.
Now lets move on to see some common use cases. Note that not all
features are described here. See the API Documentation to get a
detailed look at all the features.


=========================================================================
Accessing Rows
=========================================================================

You can access a row using it's index. It works just like a python
list. It returns a ``Row`` object.

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


You can use a helper method `set_padding_widths` to set the left and right
padding to a common value.


-------------------------------------------------------------------------
ASCII Characters
-------------------------------------------------------------------------
You can customize what characters are used to draw various parts of the
table. Here we show you an example of how you can use this feature.
You can read the API Reference for more details.

.. code:: python

   >>> table.left_border_char = 'o'
   >>> table.right_border_char = 'o'
   >>> table.top_border_char = '<~>'
   >>> table.bottom_border_char = '='
   >>> table.header_seperator_char = '^'
   >>> table.row_seperator_char = ''
   >>> table.intersection_char = ''
   >>> table.column_seperator_char = ':'
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

=========================================================================
Inserting Rows and Columns
=========================================================================

BeautifulTable provides 2 methods, `insert_row` and `insert_column` for
this purpose.

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

Removing a row or column is very easy. Just delete it using `del`
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

You can also use the helper methods `pop_row`, `pop_column` to do the
same thing. Both these methods take the index of the row, or column to
be removed.

Instead of the index, you can also pass the header of the column to
`pop_column`. Therefore the following 2 snippets are equivalent.

.. code:: python

   >>> table.pop_column('marks')

.. code:: python

   >>> table.pop_column(2)


=========================================================================
Updating data in the Table
=========================================================================

Let's change the name in the 4th row to 'Sophie'.

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

The methods `update_row` and `update_column` can be used to
perform the operations discussed in this section.

Note that you can only update existing columns but can't create
a new column using this method. For that you need to use the
methods `append_column` or `insert_column`.


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

You can also sort the table based on a column by
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

You can do much more with BeautifulTable but this much should give you a
good start. Those of you who are interested to have more control can
read the API Documentation.
