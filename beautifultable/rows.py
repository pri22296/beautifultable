from __future__ import unicode_literals
from .utils import get_output_str, termwidth, textwrap
from .base import BaseRow
from .enums import WidthExceedPolicy
from .compat import basestring, to_unicode, zip_longest


class RowData(BaseRow):
    def _get_row_within_width(self, row):
        """Process a row so that it is clamped by column_width.

        Parameters
        ----------
        row : array_like
             A single row.

        Returns
        -------
        list of list:
            List representation of the `row` after it has been processed
            according to width exceed policy.
        """
        table = self._table
        lpw, rpw = table.left_padding_widths, table.right_padding_widths
        wep = table.width_exceed_policy

        list_of_rows = []

        if (wep is WidthExceedPolicy.WEP_STRIP or
                wep is WidthExceedPolicy.WEP_ELLIPSIS):

            # Let's strip the row
            delimiter = '' if wep is WidthExceedPolicy.WEP_STRIP else '...'
            row_item_list = []
            for index, row_item in enumerate(row):
                left_pad = table._column_pad * lpw[index]
                right_pad = table._column_pad * rpw[index]
                clmp_str = (left_pad
                            + self._clamp_string(row_item, index, delimiter)
                            + right_pad)
                row_item_list.append(clmp_str)
            list_of_rows.append(row_item_list)
        elif wep is WidthExceedPolicy.WEP_WRAP:

            # Let's wrap the row
            string_partition = []

            for index, row_item in enumerate(row):
                width = table.column_widths[index] - lpw[index] - rpw[index]
                string_partition.append(textwrap(row_item, width))

            for row_items in zip_longest(*string_partition, fillvalue=''):
                row_item_list = []
                for index, row_item in enumerate(row_items):
                    left_pad = table._column_pad * lpw[index]
                    right_pad = table._column_pad * rpw[index]
                    row_item_list.append(left_pad + row_item + right_pad)
                list_of_rows.append(row_item_list)

        if len(list_of_rows) == 0:
            return [[''] * table.column_count]
        else:
            return list_of_rows

    def _clamp_string(self, row_item, column_index, delimiter=''):
        """Clamp `row_item` to fit in column referred by column_index.

        This method considers padding and appends the delimiter if `row_item`
        needs to be truncated.

        Parameters
        ----------
        row_item: str
            String which should be clamped.

        column_index: int
            Index of the column `row_item` belongs to.

        delimiter: str
            String which is to be appended to the clamped string.

        Returns
        -------
        str
            The modified string which fits in it's column.
        """
        width = (self._table.column_widths[column_index]
                 - self._table.left_padding_widths[column_index]
                 - self._table.right_padding_widths[column_index])

        if termwidth(row_item) <= width:
            return row_item
        else:
            if width - len(delimiter) >= 0:
                clamped_string = (textwrap(row_item, width-len(delimiter))[0]
                                  + delimiter)
            else:
                clamped_string = delimiter[:width]
            return clamped_string

    def __str__(self):
        """Return a string representation of a row."""
        rows = []
        table = self._table
        width = table.column_widths
        align = table.column_alignments
        sign = table.sign_mode
        lpw = table.left_padding_widths
        rpw = table.right_padding_widths
        string = []
        for i, item in enumerate(self._row):
            if isinstance(item, type(table)):
                # temporarily change the max width of the table
                curr_max_width = item.max_table_width
                item.max_table_width = width[i] - lpw[i] - rpw[i]
                rows.append(to_unicode(item).split('\n'))
                item.max_table_width = curr_max_width
            else:
                rows.append(to_unicode(item).split('\n'))
        for row in map(list, zip_longest(*rows, fillvalue='')):
            for i in range(len(row)):
                row[i] = get_output_str(row[i], table.detect_numerics,
                                        table.numeric_precision, sign.value)
            list_of_rows = self._get_row_within_width(row)
            for row_ in list_of_rows:
                for i in range(table.column_count):
                    # str.format method doesn't work for multibyte strings
                    # hence, we need to manually align the texts instead
                    # of using the align property of the str.format method
                    pad_len = width[i] - termwidth(row_[i])
                    if align[i].value == '<':
                        right_pad = ' ' * pad_len
                        row_[i] = to_unicode(row_[i]) + right_pad
                    elif align[i].value == '>':
                        left_pad = ' ' * pad_len
                        row_[i] = left_pad + to_unicode(row_[i])
                    else:
                        left_pad = ' ' * (pad_len//2)
                        right_pad = ' ' * (pad_len - pad_len//2)
                        row_[i] = left_pad + to_unicode(row_[i]) + right_pad
                content = table.column_separator_char.join(row_)
                content = table.left_border_char + content
                content += table.right_border_char
                string.append(content)
        return '\n'.join(string)


class HeaderData(RowData):
    def __init__(self, table, row):
        for i in row:
            self.validate(i)
        RowData.__init__(self, table, row)

    def __getitem__(self, key):
        return self._row[key]

    def __setitem__(self, key, value):
        self.validate(value)
        if not isinstance(key, int):
            raise TypeError(("header indices must be integers, "
                             "not {}").format(type(key).__name__))
        self._row[key] = value

    def validate(self, value):
        if not isinstance(value, basestring):
            raise TypeError(("header must be of type 'str', "
                             "got {}").format(type(value).__name__))
