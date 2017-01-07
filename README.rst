##########################################################################
ASCII Table Library for Python 3
##########################################################################

**************************************************************************
Introduction
**************************************************************************

This Package provides BeautifulTable class for easily printing
tabular data in a visually appealing ASCII format to consoles. 

Features include:

* Full customization of the look and feel of the Table
* Build the Table as you wish, By adding Rows, or by columns or using
  both method together.

*************************************************************************  
Quickstart
*************************************************************************

-------------------------------------------------------------------------
Building the Table
-------------------------------------------------------------------------

Let's see BeautifulTable in action.
 
>>> from printer_tools import BeautifulTable
>>> table = BeautifulTable()
>>> table.set_column_headers(["name", "rank", "gender"])
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

As you can see how easy it is to create a Table with TablePrinter.
Now lets move on to see some common use cases. Note that not all features
are described here. See the API Documentation to get a detailed
look at all the features.

-------------------------------------------------------------------------
Accessing Rows
-------------------------------------------------------------------------

You can access a row using it's index. It works
just like a python list.

>>> print(table[3])
['Sophia', 2, 'girl', '2010']
>>> table[3][0] = 'Sophie'
>>> print(table[3])
['Sophie', 2, 'girl', '2010']
>>> del table[3]
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
| Michael  |  3   |  boy   | 2011 |
+----------+------+--------+------+

-------------------------------------------------------------------------
Accessing Columns
-------------------------------------------------------------------------

Columns can be accessed using their header names.
But since name of headers can be duplicated, There are
methods provided to access columns using their index.
If columns are accessed using their names, and if more than one column
exists with that name as it's header, then the first column
would be returned.

>>> print(list(table['name']))
['Jacob', 'Isabella', 'Ethan', 'Michael']
>>> table['3rd column'] = [0,2,4,8,10]
>>> print(table)

Note that adding a column like this, always creates a new column.
To modify an existing column, use methods like ... TODO
PLAN : Make setter only applicable for modifying. That should be a better design.

>>> del table['year']
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
| Michael  |  3   |  boy   |
+----------+------+--------+

-------------------------------------------------------------------------
Searching for rows and columns headers
-------------------------------------------------------------------------

Cheking if a header is in the table.

>>> 'rank' in table
True

Cheking if a row is in table

>>> ["Ethan", 2, "boy"] in table
True

-------------------------------------------------------------------------
Sorting
-------------------------------------------------------------------------

You can also sort the table based on a column by
specifeing it's index or it's header. <-PLAN

>>> table.sort('name')
>>> print(table)
+----------+------+--------+
|   name   | rank | gender |
+----------+------+--------+
|  Ethan   |  2   |  boy   |
+----------+------+--------+
| Isabella |  1   |  girl  |
+----------+------+--------+
|  Jacob   |  1   |  boy   |
+----------+------+--------+
| Michael  |  3   |  boy   |
+----------+------+--------+

-------------------------------------------------------------------------
Slicing
-------------------------------------------------------------------------

Slicing creates a new table with it's own copy of data.
But it retains the properties of the original object.

>>> new_table = table[:3]
>>> print(new_table)
+----------+------+--------+
|   name   | rank | gender |
+----------+------+--------+
|  Ethan   |  2   |  boy   |
+----------+------+--------+
| Isabella |  1   |  girl  |
+----------+------+--------+
|  Jacob   |  1   |  boy   |
+----------+------+--------+

You can do much more with TablePrinter but this much should give you a
good start. Those of you who are interested to have more control can
read the API Documentation.
