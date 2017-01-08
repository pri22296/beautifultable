"""The printer module contains Classes intended for printing Tabular data to terminals.

Example
-------
>>> from printer_tools import BeautifulTable
>>> table = BeautifulTable()
>>> table.set_column_headers(['1st column', '2nd column'])
>>> for i in range(5):
...    table.append_row([i, i*i])
...
>>> print(table)
+------------+------------+
| 1st column | 2nd column |
+------------+------------+
|     0      |     0      |
+------------+------------+
|     1      |     1      |
+------------+------------+
|     2      |     4      |
+------------+------------+
|     3      |     9      |
+------------+------------+
|     4      |     16     |
+------------+------------+
"""

import enum
import itertools
import copy
import operator
import collections

__all__ = ['BeautifulTable']

class WidthExceedPolicy(enum.Enum):
    WEP_WRAP = 1
    WEP_STRIP = 2
    WEP_ELLIPSIS = 3

class SignMode(str, enum.Enum):
    SM_PLUS = '+'
    SM_MINUS = '-'
    SM_SPACE = ' '

class Alignment(str, enum.Enum):
    ALIGN_LEFT = '<'
    ALIGN_CENTER = '^'
    ALIGN_RIGHT = '>'

    def __repr__(self):
        return self.name


class BeautifulTable:
    """Utility Class to print data in tabular format to terminal.

    The instance attributes can be used to customize the look of the
    table. To disable a behaviour, just set its corresponding attribute
    to an empty string. For example, if Top border should not be drawn,
    set `top_border_char` to ''.

    Attributes
    ----------
    default_alignment : enum
        Initial Alignment for new columns.
        
        It can be one of the following:
        
        * BeautifulTable.ALIGN_LEFT
        * BeautifulTable.ALIGN_CENTER
        * BeautifulTable.ALIGN_RIGHT
        
    default_padding : int
        Initial value for Left and Right padding widths for new columns.

    sign_mode : enum
        Attribute to control how signs are displayed for numerical data.
        
        It can be one of the following:

        ========================  =================================================================================
         Option                    Meaning                                                                
        ========================  =================================================================================
         BeautifulTable.SM_PLUS    A sign should be used for both +ve and -ve numbers.                              
         BeautifulTable.SM_MINUS   A sign should only be used for -ve numbers.                                      
         BeautifulTable.SM_SPACE   A leading space should be used for +ve numbers and a minus sign for -ve numbers. 
        ========================  =================================================================================

    width_exceed_policy : enum
        Attribute to control the behaviour of table when items exceed the column width.
        
        It can be one of the following:

        ============================  ===========================================================================
         Option                        Meaning                                                                      
        ============================  ===========================================================================
         BeautifulTable.WEP_WRAP       An item is wrapped so every line fits within it's column width.              
         BeautifulTable.WEP_STRIP      An item is stripped to fit in it's column.                                   
         BeautifulTable.WEP_ELLIPSIS   An item is stripped to fit in it's column and appended with ...(Ellipsis).   
        ============================  ===========================================================================
        
    left_border_char : str
        Character used to draw the left border.
        
    right_border_char : str
        Character used to draw the right border.
        
    top_border_char : str
        Character used to draw the top border.
        
    bottom_border_char : str
        Character used to draw the bottom border.
        
    header_seperator_char : str
        Character used to draw the line seperating Header from data.
        
    row_seperator_char : str
        Character used to draw the line seperating two rows.
        
    column_seperator_char : str
        Character used to draw the line seperating two columns.
        
    intersection_char : str
        Character used to draw intersection of a vertical and horizontal
        line.
        disabling it just draws the horizontal line char in it's place.

    Parameters
    ----------
    max_width: int, optional
        maximum width of the table in number of characters.
        
    default_alignment : int, optional
        Default alignment for new columns.

    default_padding : int, optional
        Default width of the left and right padding for new columns.
    """
    
    WEP_WRAP = WidthExceedPolicy.WEP_WRAP
    WEP_STRIP = WidthExceedPolicy.WEP_STRIP
    WEP_ELLIPSIS = WidthExceedPolicy.WEP_ELLIPSIS
    SM_PLUS = SignMode.SM_PLUS
    SM_MINUS = SignMode.SM_MINUS
    SM_SPACE = SignMode.SM_SPACE
    ALIGN_LEFT = Alignment.ALIGN_LEFT
    ALIGN_CENTER = Alignment.ALIGN_CENTER
    ALIGN_RIGHT = Alignment.ALIGN_RIGHT

    def __init__(self, max_width=80, default_alignment=ALIGN_CENTER, default_padding=1):
        self.default_alignment = default_alignment
        self.default_padding = default_padding
        
        self.left_border_char = '|'
        self.right_border_char = '|'
        self.top_border_char = '-'
        self.bottom_border_char = '-'
        self.header_seperator_char = '-'
        self.column_seperator_char = '|'
        self.row_seperator_char = '-'
        self.intersection_char = '+'
        
        self._sign_mode = BeautifulTable.SM_MINUS
        self._width_exceed_policy = BeautifulTable.WEP_WRAP
        self._column_pad = " "
        self._max_table_width = max_width

        self._initialize_table(0)
        self._table = []

    def __setattr__(self, name, value):
        if name in ('left_border_char', 'right_border_char', 'top_border_char',
                    'bottom_border_char', 'header_seperator_char',
                    'column_seperator_char', 'row_seperator_char',
                    'intersection_char') and not isinstance(value, str):
            raise TypeError("Expected {attr} to be of type 'str', got {attr_type}".format(attr=name, attr_type=type(value).__name__))
        super().__setattr__(name, value)

            
    @property
    def sign_mode(self):
        return self._sign_mode

    @sign_mode.setter
    def sign_mode(self, value):
        if not isinstance(value, SignMode):
            error_msg = ("allowed values for sign_mode are: "
                         + ', '.join("{}.{}".format(type(self).__name__, i.name) for i in SignMode))
            raise ValueError(error_msg)
        self._sign_mode = value

    @property
    def width_exceed_policy(self):
        """Attribute to control the behaviour of table when items exceed the column width.
        
        It can be one of the following:

        ============================  ===========================================================================
         Option                        Meaning                                                                      
        ============================  ===========================================================================
         BeautifulTable.WEP_WRAP       An item is wrapped so every line fits within it's column width.           
         BeautifulTable.WEP_STRIP      An item is stripped to fit in it's column.                                
         BeautifulTable.WEP_ELLIPSIS   An item is stripped to fit in it's column and appended with ...(Ellipsis).   
        ============================  ===========================================================================
        """
        return self._width_exceed_policy

    @width_exceed_policy.setter
    def width_exceed_policy(self, value):
        if not isinstance(value, WidthExceedPolicy):
            error_msg = ("allowed values for width_exceed_policy are: "
                         + ', '.join("{}.{}".format(type(self).__name__, i.name) for i in WidthExceedPolicy))
            raise ValueError(error_msg)
        self._width_exceed_policy = value

    def _initialize_table(self, column_count):
        """Sets the column count of the table.

        This method is called to set the number of columns for the first time.
        It should only be called when `self._column_count` is 0.

        Parameters
        ----------
        column_count : int
            number of columns in the table
        """
        self._column_count = column_count
        self._column_headers = [''] * self._column_count
        self._column_alignments = [self.default_alignment] * column_count
        self._column_widths = [0] * column_count
        self._left_padding_widths = [self.default_padding] * column_count
        self._right_padding_widths = [self.default_padding] * column_count

    """def begin(self):
        Performs initial tasks prior to printing table.

        It is recommended to perform all customization to the BeautifulTable
        instance before calling this method. This method is necessary to call
        for printing table.
        
        pass

    def end(self):
        Performs clean up tasks after printing table.

        This method should always be called after printing all rows of the
        table to ensure that all rows have been flushed. It also closes the
        table visually.
        
        pass"""

    def _validate_row(self, row):
        if not isinstance(row, collections.Iterable):
            raise TypeError("parameter must be an iterable")
        
        row = list(row)
        if self._column_count == 0:
            self._initialize_table(len(row))
            
        if len(row) != self._column_count:
            raise ValueError("'Expected iterable of length {}, got {}".format(self._column_count, len(row)))
        return row

    def set_column_headers(self, header):
        """Set titles for the columns of the table.

        `header` can be any iterable having all memebers an instance of `str`.

        Parameters
        ----------
        header : array_like
            titles for the columns.
        """
        header = self._validate_row(header)
        """if self._column_count == 0:
            self._initialize_table(len(header))

        assert self._column_count == len(header)"""
        for i in header:
            if not isinstance(i, str):
                raise TypeError("Headers should be of type 'str'")
        self._column_headers = header

    def set_column_alignments(self, alignment):
        """Set titles for the columns of the table.

        Parameters
        ----------
        alignment : array_like
            alignment for the columns. It follows the default alignment
            rules of the format method.

            * BeautifulTable.ALIGN_LEFT - left alignment
            * BeautifulTable.ALIGN_CENTER - center alignment
            * BeautifulTable.ALIGN_RIGHT - right alignment

        """
        """alignment = list(alignment)
        if self._column_count == 0:
            self._initialize_table(len(alignment))

        assert self._column_count == len(alignment)"""
        alignment = self._validate_row(alignment)
        
        self._column_alignments = alignment

    def auto_calculate_width(self):
        """Calculate width of column automatically based on data."""
        table_width = self.get_table_width()
        offset = table_width - sum(self._column_widths)
        widths= [(self._left_padding_widths[index] + self._right_padding_widths[index]) for index in range(self._column_count)]
        for index, column in enumerate(zip(*self._table)):
            max_length = (max(len(str(i)) for i in column))
            max_length = max(max_length, len(str(self._column_headers[index])))
            #max_length += self._left_padding_widths[index] + self._right_padding_widths[index]
            widths[index] += max_length
        widths_copy = widths.copy()
        sum_ = sum(widths)
        """while sum_ > self._max_table_width - offset:
            for i in range(self._column_count):
                if widths[i] > sum_/self._column_count:
                    widths[i] = round(widths[i] / 1.2)
            sum_temp = sum(widths)
            if sum_ == sum_temp:
                break
            sum_ = sum_temp"""
        desired_sum = self._max_table_width - offset
        self._column_widths = [round(width * desired_sum / sum_) if width > round(desired_sum/self._column_count) else width for i, width in enumerate(widths)]
        #self._column_widths = [round(width * (self._max_table_width - offset) / sum_) if width < widths_copy[i] else width for i, width in enumerate(widths)]
        

    def set_column_widths(self, width):
        """Set width for the columns of the table.

        Width of the column specifies the max number of characters
        a column can contain. Larger characters are handled according to
        the WIDTH_EXCEED_POLICY.

        Parameters
        ----------
        width
            width for the columns.
        
        """
        """width = list(width)
        if self._column_count == 0:
            self._initialize_table(len(width))

        assert self._column_count == len(width)"""
        width = self._validate_row(width)
        self._column_widths = width

    def set_left_padding_widths(self, pad_width):
        """Set width for left padding of the columns of the table.

        Left Width of the padding specifies the number of characters
        on the left of a column reserved for padding. By Default It is 1.

        Parameters
        ----------
        pad_width : array_like
            left pad widths for the columns.

        """
        """pad_width = list(pad_width)
        if self._column_count == 0:
            self._initialize_table(len(pad_width))
            
        assert self._column_count == len(pad_width)"""
        pad_width = self._validate_row(pad_width)
        self._left_padding_widths = pad_width

    def set_right_padding_widths(self, pad_width):
        """Set width for right padding of the columns of the table.

        Right Width of the padding specifies the number of characters
        on the rigth of a column reserved for padding. By default It is 1.

        Parameters
        ----------
        pad_width : array_like
            rigth pad widths for the columns.

        """
        """pad_width = list(pad_width)
        if self._column_count == 0:
            self._initialize_table(len(pad_width))
            
        assert self._column_count == len(pad_width)"""
        pad_width = self._validate_row(pad_width)
        self._right_padding_widths = pad_width

    def set_padding_widths(self, pad_width):
        """Set width for left and rigth padding of the columns of the table.

        Parameters
        ----------
        pad_width : array_like
            pad widths for the columns.
        """
        self.set_left_padding_widths(pad_width)
        self.set_right_padding_widths(pad_width)

    def _clamp_string(self, row_item: str, column_index: int, delimiter='')-> str:
        """Clamp `row_item` to fit in column referred by column_index.

        This method considers padding and appends the delimiter if `row_item`
        needs to be truncated.

        Parameters
        ----------
        row_item
            String which should be clamped.

        column_index
            Index of the column `row_item` belongs to.

        delimiter
            String which is to be appended to the clamped string.

        Returns
        -------
        str
            The modified string which fits in it's column.
        """
        width = (self._column_widths[column_index]
                 - self._left_padding_widths[column_index]
                 - self._right_padding_widths[column_index])
        if len(row_item) <= width:
            return row_item
        else:
            assert width-len(delimiter) >= 0
            clamped_string = (row_item[:width-len(delimiter)]
                              + delimiter)
            assert len(clamped_string) == width
            return clamped_string

    def _get_row_within_width(self, row):
        """Process a row so that it is clamped by column_width.

        Parameters
        ----------
        row : array_like
             A single row.

        Returns
        -------
        list of list:
            List representation of the `row` after it has been processed according
            to width exceed policy.
        """
        list_of_rows = []
        if (self._width_exceed_policy is BeautifulTable.WEP_STRIP or
                self._width_exceed_policy is BeautifulTable.WEP_ELLIPSIS):
            delimiter = '' if self._width_exceed_policy is BeautifulTable.WEP_STRIP else '...'
            row_item_list = []
            for index, row_item in enumerate(row):
                left_pad = self._column_pad * self._left_padding_widths[index]
                right_pad = self._column_pad * self._right_padding_widths[index]
                clmp_str = left_pad + self._clamp_string(row_item, index, delimiter) + right_pad
                row_item_list.append(clmp_str)
            list_of_rows.append(row_item_list)
        elif self._width_exceed_policy is BeautifulTable.WEP_WRAP:
            row_item_list = []
            for i in itertools.count():
                line_empty = True
                for index, row_item in enumerate(row):
                    width = self._column_widths[index] - self._left_padding_widths[index] - self._right_padding_widths[index]
                    left_pad = self._column_pad * self._left_padding_widths[index]
                    right_pad = self._column_pad * self._right_padding_widths[index]
                    clmp_str = row_item[i*width:(i+1)*width]
                    if len(clmp_str) != 0:
                        line_empty = False
                    row_item_list.append(left_pad + clmp_str + right_pad)
                if line_empty:
                    break
                else:
                    list_of_rows.append(row_item_list)
                    row_item_list = []
        if len(list_of_rows) == 0:
            return [['']*self._column_count]
        else:
            return list_of_rows

    def _clean_item(self, item):
        """Helper method to convert a string to float or int if possible."""
        try:
            r = float(item)
            if r.is_integer():
                r = int(r)
            return r
        except (ValueError, TypeError):
            return item
                

    def _get_row_as_str(self, row):
        """Return a string representation of a row."""
        row = [self._clean_item(item) for item in row]
        width = self._column_widths
        align = self._column_alignments
        sign = self._sign_mode
        for i in range(self._column_count):
            try:
                row[i] = '{:{sign}}'.format(str(row[i]), sign=sign)
            except ValueError:
                row[i] = str(row[i])
        string = []
        list_of_rows = self._get_row_within_width(row)
        for row_ in list_of_rows:
            for i in range(self._column_count):
                row_[i] = '{:{align}{width}}'.format(
                    str(row_[i]), align=align[i], width=width[i])
            content = self.column_seperator_char.join(row_)
            content = self.left_border_char + content
            content += self.right_border_char
            string.append(content)
        return '\n'.join(string)

    def __getitem__(self, key):
        """Get a row, or a column, or a new table by slicing.

        Parameters
        ----------
        key : int, slice, str
            If key is an `int`, returns a row.
            If key is an `str`, returns iterator to a column with heading `key`.
            If key is a slice object, returns a new table sliced according to rows.

        Raises
        ------
        TypeError
            If key is not of type int, slice or str.
        IndexError
            If `int` key is out of range.
        KeyError
            If `str` key is not found in headers.
        """
        if isinstance(key, slice):
            new_table = copy.copy(self)
            new_table._table = self._table[key]
            return new_table
        elif isinstance(key, int):
            return self._table[key]
        elif isinstance(key, str):
            return self.get_column(key)
        else:
            raise TypeError("table indices must be integers or slices, not {}".format(type(key).__name__))

    def __delitem__(self, key):
        """Delete a row, or a column, or multiple rows by slicing.

        Parameters
        ----------
        key : int, slice, str
            If key is an `int`, deletes a row.
            If key is a slice object, deletes multiple rows.
            If key is an `str`, delete the first column with heading `key`

        Raises
        ------
        TypeError
            If key is not of type int, slice or str.
        IndexError
            If `int` key is out of range.
        KeyError
            If `str` key is not found in headers.
        """
        if isinstance(key, int) or isinstance(key, slice):
            del self._table[key]
        elif isinstance(key, str):
            return self.pop_column(key)
        else:
            raise TypeError("table indices must be integers or slices, not {}".format(type(key).__name__))

    def __setitem__(self, key, value):
        """Update a row, or a column, or multiple rows by slicing.

        Parameters
        ----------
        key : int, slice, str
            If key is an `int`, updates a row.
            If key is an `str`, appends `column` to the list with header as `key`.
            If key is a slice object, updates multiple rows according to slice rules.

        Raises
        ------
        TypeError
            If key is not of type int, slice or str.
        IndexError
            If `int` key is out of range.
        """
        if isinstance(key, int) or isinstance(key, slice):
            self._table[key] = value
        elif isinstance(key, str):
            self.update_column(key, value)
        else:
            raise TypeError("table indices must be integers or slices, not {}".format(type(key).__name__))

    def __len__(self):
        return len(self._table)

    def __contains__(self, key):
        if isinstance(key, str):
            return key in self._column_headers
        elif isinstance(key, collections.Iterable):
            return list(key) in self._table
        else:
            raise TypeError("'key' must be str or Iterable, not {}".format(type(key).__name__))

    def __iter__(self):
        return iter(self._table)

    def __next__(self):
        return next(self._table)

    def __repr__(self):
        return repr(self._table)

    def __str__(self):
        return self.get_string()

    def sort(self, key):
        """Stable sort of the table *IN-PLACE* with respect to a column.

        Parameters
        ----------
        index:
            index of the column. Normal list rules apply.
        """
        if isinstance(key, int):
            index = key
        elif isinstance(key, str):
            index = self.get_column_index(key)
        else:
            raise TypeError("'key' must either be 'int' or 'str'")
        self._table.sort(key=operator.itemgetter(index))

    def copy(self):
        """Return a deepcopy of the table.

        Returns
        -------
        BeautifulTable:
            deepcopy of the BeautifulTable instance.
        """
        new_table = copy.deepcopy(self)
        return new_table

    def get_column_header(self, index):
        """Get header of a column from it's index.

        Parameters
        ----------
        index: int
            Normal list rules apply.
        """
        return self._column_headers[index]

    def get_column_index(self, header):
        """Get index of a column from it's header.

        Parameters
        ----------
        header: str
            header of the column.

        Raises
        ------
        ValueError:
            If no column could be found corresponding to `header`.
        """
        try:
            index = self._column_headers.index(header)
            return index
        except ValueError:
            raise KeyError("'{}' is not a header for any column".format(header)) from None

    def get_column(self, key):
        """Return an iterator to a column.

        Parameters
        ----------
        key : int, str
            index of the column, or the header of the column.
            If index is specified, then normal list rules apply.

        Raises
        ------
        TypeError:
            If key is not of type `int`, or `str`.

        Returns
        -------
        iter:
            Iterator to the specified column.
        """
        if isinstance(key, int):
            index = key
        elif isinstance(key, str):
            index = self.get_column_index(key)
        else:
            raise TypeError("key must be an int or str, not {}".format(type(key).__name__))
        return iter(map(operator.itemgetter(index), self._table))

    def reverse(self):
        """Reverse the table row-wise *IN PLACE*."""
        self._table.reverse()

    def pop_row(self, index=-1):
        """Remove and return row at index (default last).

        Parameters
        ----------
        index : int
            index of the row. Normal list rules apply.
        """
        row = self._table.pop(index)

    def pop_column(self, index=-1):
        """Remove and return row at index (default last).

        Parameters
        ----------
        index : int, str
            index of the column, or the header of the column.
            If index is specified, then normal list rules apply.

        Raises
        ------
        TypeError:
            If index is not an instance of `int`, or `str`.

        IndexError:
            If Table is empty.
        """
        if isinstance(index, int):
            pass
        elif isinstance(index, str):
            index = self.get_column_index(index)
        else:
            raise TypeError("column indices must be integers or slices, not {}".format(type(key).__name__))
        #assert self._column_count > 0
        if self._column_count == 0:
            raise IndexError("pop from empty table")
        if self._column_count == 1:
            # This is the last column. So we should clear the table to avoid empty rows
            self.clear(clear_column_properties=True)
        else:
            # Not the last column. safe to pop from row
            self._column_count -= 1
            self._column_alignments.pop(index)
            self._column_widths.pop(index)
            self._left_padding_widths.pop(index)
            self._right_padding_widths.pop(index)
            self._column_headers.pop(index)
            for row in self._table:
                row.pop(index)

    def insert_row(self, index, row):
        """Insert a row before index in the table.

        Parameters
        ----------
        index : int
            List index rules apply
            
        row : iterable
            Any iterable of appropriate length.

        Raises
        ------
        TypeError:
            If `row` is not an iterable.

        ValueError:
            If size of `row` is inconsistent with the current number
            of columns.
        
        """
        """row = list(row)
        if self._column_count == 0:
            self._initialize_table(len(row))

        if len(row) != self._column_count:
            raise ValueError("expected 'row' to be of length {}, got {}".format(self._column_count, len(row)))"""
        row = self._validate_row(row)
        self._table.insert(index, row)

    def append_row(self, row):
        """Append a row to end of the table.

        Parameters
        ----------
        row : iterable
            Any iterable of appropriate length.
        
        """
        self.insert_row(len(self._table), row)

    def update_column(self, header, column):
        index = self.get_column_index(header)
        if not isinstance(header, str):
            raise ValueError("header must be of type str")
        for i, (row, new_item) in enumerate(zip(self._table, column)):
            row[index] = new_item

    def insert_column(self, index, header, column):
        """Insert a column before `index` in the table.

        If length of column is bigger than number of rows, lets say
        `k`, only the first `k` values of `column` is considered.
        If column is shorter than 'k', ValueError is raised.
        
        Note that Table remains in consistent state even if column
        is too short. Any changes made by this method is rolled back
        before raising the exception.

        Parameters
        ----------
        index : int
            List index rules apply.
            
        header : str
            Title of the column.

        column : iterable
            Any iterable of appropriate length.

        Raises
        ------
        ValueError:
            If `header` is not of type `str`.

            If length of `column` is shorter than number of rows.
        """
        if self._column_count == 0:
            self.set_column_headers([header])
            self._table = [[i] for i in column]
        else:
            if not isinstance(header, str):
                raise ValueError("header must be of type str")
            for i, (row, new_item) in enumerate(zip(self._table, column)):
                row.insert(index, new_item)
            if i == len(self._table) - 1:
                self._column_count += 1
                self._column_headers.insert(index, header)
                self._column_alignments.insert(index, self.default_alignment)
                self._column_widths.insert(index, 0)
                self._left_padding_widths.insert(index, self.default_padding)
                self._right_padding_widths.insert(index, self.default_padding)
            else:
                # Roll back changes so that table remains in consistent state
                for j in range(i, -1, -1):
                    self._table[j].pop(index)
                    #row.pop(index)
                raise ValueError("length of 'column' should be atleast {}, got {}".format(len(self._table), i+1))

    def append_column(self, header, column):
        """Append a column to end of the table.

        Parameters
        ----------
        header : str
            Title of the column

        column : iterable
            Any iterable of appropriate length.
        """
        self.insert_column(self._column_count, header, column)

    def clear(self, clear_column_properties=False):
        """Clear the contents of the table.

        Clear all rows of the table, and if specified clears all column specific data.

        Parameters
        ----------
        clear_column_properties : bool, optional
            If it is true(default False), all metadata of columns such as their alignment,
            padding, width, etc. are also cleared and number of columns is set to 0.
        """
        self._table.clear()
        if clear_column_properties:
            self._initialize_table(0)

    def _get_horizontal_line(self, char):
        """Get a horizontal line for the table.

        Internal method used to actually get all horizontal lines in the table.
        Column width should be set prior to calling this method. This method
        detects intersection and handles it according to the value of
        `intersection_char`.

        Parameters
        ----------
        char : str
            Character used to draw the line.

        Returns
        -------
        str
            String which will be printed as the Top border of the table.
        """
        table_width = self.get_table_width()
        intersection = self.intersection_char
        try:
            line = list(char * (int(table_width/len(char)) + 1))[:table_width]
        except ZeroDivisionError:
            line = [' '] * table_width
        # Only if Special Intersection is enabled and horizontal line is visible
        if self.intersection_char and not char.isspace():
            # If left border is enabled and it is visible
            if self.left_border_char and not self.left_border_char.isspace():
                length = min(len(self.left_border_char), len(self.intersection_char))
                for i in range(length):
                    line[i] = intersection[i]
            # If right border is enabled and it is visible
            if self.right_border_char and not self.right_border_char.isspace():
                length = min(len(self.right_border_char), len(self.intersection_char))
                for i in range(length):
                    line[-i-1] = intersection[-i-1]
            # If column seperator is enabled and it is visible
            if self.column_seperator_char and not self.column_seperator_char.isspace():
                index = len(self.left_border_char)
                for i in range(self._column_count-1):
                    index += (self._column_widths[i])
                    length = min(len(self.column_seperator_char), len(self.intersection_char))
                    for i in range(length):
                        line[index+i] = intersection[i]
                    index += len(self.column_seperator_char)
                    
        return ''.join(line)

    def get_top_border(self):
        """Get the Top border of table.

        Column width should be set prior to calling this method.

        Returns
        -------
        str
            String which will be printed as the Top border of the table.
        """
        return self._get_horizontal_line(self.top_border_char)

    def get_header_seperator(self):
        """Get the Header seperator of table.

        Column width should be set prior to calling this method.

        Returns
        -------
        str
            String which will be printed as Header seperator of the table.
        """
        return self._get_horizontal_line(self.header_seperator_char)

    def get_row_seperator(self):
        """Get the Row seperator of table.

        Column width should be set prior to calling this method.

        Returns
        -------
        str
            String which will be printed as Row seperator of the table.
        """
        return self._get_horizontal_line(self.row_seperator_char)

    def get_bottom_border(self):
        """Get the Bottom border of table.

        Column width should be set prior to calling this method.

        Returns
        -------
        str
            String which will be printed as the Bottom border of the table.
        """
        return self._get_horizontal_line(self.bottom_border_char)

    def get_table_width(self):
        """Get the width of the table as number of characters.

        Column width should be set prior to calling this method.

        Returns
        -------
        int
            Width of the table as number of characters.
        """
        width = sum(self._column_widths)
        
        width += ((self._column_count - 1)
                    * len(self.column_seperator_char))
        width += len(self.left_border_char)
        width += len(self.right_border_char)
        return width

    def get_number_of_columns(self):
        """Get the current number of columns.

        Returns
        -------
        int:
            Current number of columns in the Table.
        """
        return self._column_count

    def get_string(self, recalculate_width=True):
        """Get the table as a String.

        Parameters
        ----------
        recalculate_width : bool, optional
            If width for each column should be recalculated(default True).
            Note that width is always calculated if it wasn't set
            explicitly when this method is called for the first time ,
            regardless of the value of `recalculate_width`.

        Returns
        -------
        str:
            Table as a string.
        """

        if recalculate_width or sum(self._column_widths) == 0:
            self.auto_calculate_width()

        string_ = []

        if self.top_border_char:
            string_.append(
                self.get_top_border())

        headers = self._get_row_as_str(self._column_headers)
        string_.append(headers)

        if self.header_seperator_char:
            string_.append(
                self.get_header_seperator())

        first_row_encountered = False
        for i, row in enumerate(self._table):
            if first_row_encountered and self.row_seperator_char:
                string_.append(
                    self.get_row_seperator())
            first_row_encountered = True
            content = self._get_row_as_str(row)
            string_.append(content)

        if self.bottom_border_char:
            string_.append(
                self.get_bottom_border())

        return '\n'.join(string_)


class _BufferedPrinter:
    """Utility Class to print to terminal with a fixed buffer size.

    Parameters
    ----------

    max_buffer_size
        maximum size of the internal buffer after which buffer is
        emptied by flushing it's content. Larger buffer size usually leads
        to efficient printing.
    """
    def __init__(self, max_buffer_size: int):
        self._max_buffer_size = max_buffer_size
        self._buffer = []

    def set_max_buffer_size(self, max_buffer_size: int):
        """Set max buffer size.

        Parameters
        ----------

        max_buffer_size
            new size for the internal buffer.
        """
        self._max_buffer_size = max_buffer_size

    def flush(self):
        """flush the buffer to a stream, or to sys.stdout by default.

        Note
        ----
        It is recommended to always call this method before exiting otherwise
        you could lose important information.
        """
        print(''.join(self._buffer), end='', flush=True)
        self._buffer = []

    def print(self, *args, sep=' ', end='\n'):
        """Prints the values to the internal buffer.

        Parameters
        ----------

        *args
            values to be printed

        sep : str, optional
            string inserted between values, default a space.

        end : str, optional
            string appended after the last value, default a newline.
        """
        self._buffer.append(sep.join(args) + end)
        if len(self._buffer) == self._max_buffer_size:
            self.flush()


def _demo_table_printer():
    """Basic Demo for the BeautifulTable class."""
    print("Following is a Demo for BeautifulTable\n")
    table_printer = BeautifulTable()
    table_printer.set_column_headers(["I"*40, "SQUARE OF I", "CUBE OF I"])
    table_printer.set_column_alignments(['<', '^', '>'])

    for i in range(1000):
        table_printer.append_row([i, i**2, i**3])
    table_printer.append_row(['a'*50, 'b'*100, 'c'*233])
    print(table_printer)


def main():
    pass
    _demo_table_printer()

if __name__ == '__main__':
    main()
