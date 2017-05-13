import unittest
from beautifultable import BeautifulTable

class TableOperationsTestCase(unittest.TestCase):
    def setUp(self):
        table = BeautifulTable()
        table.column_headers = ["name", "rank", "gender"]
        table.append_row(["Jacob", 1, "boy"])
        table.append_row(["Isabella", 1, "girl"])
        table.append_row(["Ethan", 2, "boy"])
        table.append_row(["Sophia", 2, "girl"])
        table.append_row(["Michael", 3, "boy"])
        self.table = table

    def compare_iterable(self, iterable1, iterable2):
        for item1, item2 in zip(iterable1, iterable2):
            self.assertEqual(item1, item2)

    # Tests for column operations

    def test_column_count(self):
        self.assertEqual(self.table.column_count, 3)

    def test_access_column_by_header(self):
        column = ['Jacob', 'Isabella', 'Ethan', 'Sophia', 'Michael']
        self.compare_iterable(column, self.table['name'])
        with self.assertRaises(KeyError):
            self.table['name1']

    def test_get_column_index(self):
        self.assertEqual(self.table.get_column_index('gender'), 2)
        with self.assertRaises(KeyError):
            self.table.get_column_index('rank1')

    def test_get_column_header(self):
        self.assertEqual(self.table.get_column_header(2), 'gender')
        with self.assertRaises(IndexError):
            self.table.get_column_header(self.table.column_count)

    def test_append_column(self):
        column = ['2010', '2012', '2008', '2010', '2011']
        title = 'year'
        self.table.append_column(title, column)
        self.assertEqual(self.table.column_count, 4)
        self.compare_iterable(column,
                              self.table.get_column(self.table.column_count - 1))

    def test_insert_column(self):
        column = ['2010', '2012', '2008', '2010', '2011']
        title = 'year'
        position = 2
        self.table.insert_column(position, title, column)
        self.assertEqual(self.table.column_count, 4)
        self.compare_iterable(column, self.table.get_column(position))

    def test_pop_column_by_position(self):
        position = 2
        header = self.table.get_column_header(position)
        self.table.pop_column(position)
        self.assertEqual(self.table.column_count, 2)
        with self.assertRaises(KeyError):
            self.table.get_column(header)

    def test_pop_column_by_header(self):
        header = 'gender'
        self.table.pop_column(header)
        self.assertEqual(self.table.column_count, 2)
        with self.assertRaises(KeyError):
            self.table.get_column(header)

    def test_update_column(self):
        header = 'rank'
        column = [3,2,1,2,4]
        self.table.update_column(header, column)
        self.assertEqual(self.table.column_count, 3)
        self.compare_iterable(column, self.table.get_column(header))

    # Tests for row operations

    def test_row_count(self):
        self.assertEqual(len(self.table), 5)

    def test_access_row_by_index(self):
        row = ["Sophia", 2, "girl"]
        self.compare_iterable(row, self.table[3])
        with self.assertRaises(IndexError):
            self.table[len(self.table)]

    def test_append_row(self):
        row = ['Gary', 2, 'boy']
        self.table.append_row(row)
        self.assertEqual(len(self.table), 6)
        self.compare_iterable(self.table[5], row)

    def test_insert_row(self):
        row = ['Gary', 2, 'boy']
        position = 2
        self.table.insert_row(position, row)
        self.assertEqual(len(self.table), 6)
        self.compare_iterable(self.table[position], row)

    def test_pop_row(self):
        position = 2
        self.table.pop_row(position)
        self.assertEqual(len(self.table), 4)

    def test_update_row(self):
        row = ['Sophie', 5, 'girl']
        position = 3
        self.table.update_row(position, row)
        self.compare_iterable(self.table[position], row)

    def test_update_row_slice(self):
        rows = [['Sophie', 5, 'girl'], ['Mike', 4, 'boy']]
        self.table.update_row(slice(3, 5, 1), rows)
        self.assertEqual(len(self.table), 5)
        self.compare_iterable(self.table[3], rows[0])
        self.compare_iterable(self.table[4], rows[1])

    # Tests for special methods

    def test_getitem_slice(self):
        new_table = self.table[:3]
        self.assertEqual(len(new_table), 3)
        self.assertEqual(self.table.column_count, 3)

    def test_delitem_int(self):
        del self.table[1]
        self.assertEqual(len(self.table), 4)

    def test_delitem_slice(self):
        del self.table[2:]
        self.assertEqual(len(self.table), 2)

    def test_delitem_str(self):
        del self.table['rank']
        self.assertEqual(self.table.column_count, 2)
        with self.assertRaises(KeyError):
            self.table.get_column('rank')

    def test_setitem_int(self):
        position = 3
        row = ['Sophie', 5, 'girl']
        self.table[position] = row
        self.compare_iterable(self.table[position], row)

    def test_setitem_slice(self):
        rows = [['Sophie', 5, 'girl'], ['Mike', 4, 'boy']]
        self.table[3:] = rows
        self.assertEqual(len(self.table), 5)
        self.compare_iterable(self.table[3], rows[0])
        self.compare_iterable(self.table[4], rows[1])

    def test_setitem_str(self):
        header = 'rank'
        column = [3,2,1,2,4]
        self.table[header] = column
        self.assertEqual(self.table.column_count, 3)
        self.compare_iterable(column, self.table.get_column(header))

    def test_contains(self):
        self.assertTrue('rank' in self.table)
        self.assertFalse('rankk' in self.table)
        self.assertTrue(["Isabella", 1, "girl"] in self.table)
        self.assertFalse(['Ethan', 3, 'boy'] in self.table)

    # Test for printing operations

    def test_get_string(self):
        string = """+----------+------+--------+
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
+----------+------+--------+"""
        self.assertEqual(string, self.table.get_string())


if __name__ == '__main__':
    unittest.main()
