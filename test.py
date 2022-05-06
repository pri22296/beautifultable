# -*- coding: utf-8 -*-


import os
import unittest
import itertools

from beautifultable import BeautifulTable

try:
    import pandas as pd
except ImportError:
    pd = None
    PANDAS_INSTALLED = False
else:
    PANDAS_INSTALLED = True

REQUIRED_PANDAS_MESSAGE = "requires 'pandas' to be installed"


class TableOperationsTestCase(unittest.TestCase):
    def setUp(self):
        self.create_table()

    def create_table(self, maxwidth=80):
        table = BeautifulTable(maxwidth=maxwidth)

        table.rows.append(["Jacob", 1, "boy"])
        table.rows.append(["Isabella", 1, "girl"])
        table.rows.append(["Ethan", 2, "boy"])
        table.rows.append(["Sophia", 2, "girl"])
        table.rows.append(["Michael", 3, "boy"])

        table.columns.header = ["name", "rank", "gender"]
        table.rows.header = ["S1", "S2", "S3", "S4", "S5"]

        self.table = table

    def create_dataframe(self):
        return self.table.to_df()

    def compare_iterable(self, iterable1, iterable2):
        for item1, item2 in itertools.zip_longest(iterable1, iterable2):
            self.assertEqual(item1, item2)

    # Test for table operations

    def test_filter(self):
        new_table = self.table.rows.filter(lambda x: x["rank"] > 1)
        self.assertEqual(len(self.table.rows), 5)
        rows = [
            ["Ethan", 2, "boy"],
            ["Sophia", 2, "girl"],
            ["Michael", 3, "boy"],
        ]
        for row_t, row in zip(new_table.rows, rows):
            self.compare_iterable(row_t, row)

    def test_sort_by_index(self):
        self.table.rows.sort(0)
        rows = [
            ["Ethan", 2, "boy"],
            ["Isabella", 1, "girl"],
            ["Jacob", 1, "boy"],
            ["Michael", 3, "boy"],
            ["Sophia", 2, "girl"],
        ]
        for row_t, row in zip(self.table.rows, rows):
            self.compare_iterable(row_t, row)

    def test_sort_by_index_reversed(self):
        self.table.rows.sort(0, reverse=True)
        rows = [
            ["Ethan", 2, "boy"],
            ["Isabella", 1, "girl"],
            ["Jacob", 1, "boy"],
            ["Michael", 3, "boy"],
            ["Sophia", 2, "girl"],
        ]
        for row_t, row in zip(self.table.rows, reversed(rows)):
            self.compare_iterable(row_t, row)

    def test_sort_by_header(self):
        self.table.rows.sort("name")
        rows = [
            ["Ethan", 2, "boy"],
            ["Isabella", 1, "girl"],
            ["Jacob", 1, "boy"],
            ["Michael", 3, "boy"],
            ["Sophia", 2, "girl"],
        ]
        for row_t, row in zip(self.table.rows, rows):
            self.compare_iterable(row_t, row)

    def test_sort_by_callable(self):
        self.table.rows.sort(lambda x: (x[1], x[0]))
        rows = [
            ["Isabella", 1, "girl"],
            ["Jacob", 1, "boy"],
            ["Ethan", 2, "boy"],
            ["Sophia", 2, "girl"],
            ["Michael", 3, "boy"],
        ]
        for row_t, row in zip(self.table.rows, rows):
            self.compare_iterable(row_t, row)

    def test_sort_raises_exception(self):
        with self.assertRaises(TypeError):
            self.table.rows.sort(None)

    # Tests for column operations

    def test_column_aslist(self):
        self.assertEqual(
            [column.aslist() for column in self.table.columns],
            [
                ["Jacob", "Isabella", "Ethan", "Sophia", "Michael"],
                [1, 1, 2, 2, 3],
                ["boy", "girl", "boy", "girl", "boy"],
            ],
        )

    def test_column_asdict(self):
        with self.assertRaises(NotImplementedError):
            header_colval_map = [column.asdict() for column in self.table.columns]

    def test_column_count(self):
        self.assertEqual(len(self.table.columns), 3)

    def test_access_column_by_header(self):
        column = ["Jacob", "Isabella", "Ethan", "Sophia", "Michael"]
        self.compare_iterable(column, self.table.columns["name"])
        with self.assertRaises(KeyError):
            self.table.columns["name1"]

    def test_access_column_element_by_index(self):
        self.assertEqual(self.table.columns[0][2], "Ethan")

    def test_access_column_element_by_header(self):
        self.assertEqual(self.table.columns["name"][2], "Ethan")

    def test_get_column_index(self):
        self.assertEqual(self.table.columns.header.index("gender"), 2)
        with self.assertRaises(KeyError):
            self.table.columns.header.index("rank1")

    def test_get_column_header(self):
        self.assertEqual(self.table.columns.header[2], "gender")
        with self.assertRaises(IndexError):
            self.table.columns.header[len(self.table.columns)]

    def test_append_column(self):
        title = "year"
        column = ["2010", "2012", "2008", "2010", "2011"]
        self.table.columns.append(column, title)
        self.assertEqual(len(self.table.columns), 4)
        last_column = self.table.columns[len(self.table.columns) - 1]
        self.compare_iterable(column, last_column)

    def test_append_column_empty_table(self):
        self.table = BeautifulTable()
        title = "year"
        column = ["2010", "2012", "2008", "2010", "2011"]
        self.table.columns.append(column, header=title)
        string = """+------+
| year |
+------+
| 2010 |
+------+
| 2012 |
+------+
| 2008 |
+------+
| 2010 |
+------+
| 2011 |
+------+"""
        self.assertEqual(string, str(self.table))

    def test_insert_column(self):
        column = ["2010", "2012", "2008", "2010", "2011"]
        title = "year"
        position = 2
        self.table.columns.insert(position, column, title)
        self.assertEqual(len(self.table.columns), 4)
        self.compare_iterable(column, self.table.columns[position])

    def test_pop_column_by_position(self):
        position = 2
        header = self.table.columns.header[position]
        self.table.columns.pop(position)
        self.assertEqual(len(self.table.columns), 2)
        with self.assertRaises(KeyError):
            self.table.columns[header]

    def test_pop_column_by_header(self):
        header = "gender"
        self.table.columns.pop(header)
        self.assertEqual(len(self.table.columns), 2)
        with self.assertRaises(KeyError):
            self.table.columns[header]

    def test_update_column_by_index(self):
        index = 1
        column = [3, 2, 1, 2, 4]
        self.table.columns.update(index, column)
        self.assertEqual(len(self.table.columns), 3)
        self.compare_iterable(column, self.table.columns[index])

    def test_update_column_by_header(self):
        header = "rank"
        column = [3, 2, 1, 2, 4]
        self.table.columns.update(header, column)
        self.assertEqual(len(self.table.columns), 3)
        self.compare_iterable(column, self.table.columns[header])

    def test_update_column_slice(self):
        columns = [
            [5, "girl"],
            [4, "boy"],
            [4, "boy"],
            [2, "girl"],
            [1, "boy"],
        ]
        self.table.columns.update(slice(1, 3, 1), columns)
        self.assertEqual(len(self.table.columns), 3)
        self.compare_iterable(self.table.columns[1], [c[0] for c in columns])
        self.compare_iterable(self.table.columns[2], [c[1] for c in columns])

    # Tests for row operations

    def test_row_asdict(self):
        self.assertEqual(
            [row.asdict() for row in self.table.rows],
            [
                {"name": "Jacob", "rank": 1, "gender": "boy"},
                {"name": "Isabella", "rank": 1, "gender": "girl"},
                {"name": "Ethan", "rank": 2, "gender": "boy"},
                {"name": "Sophia", "rank": 2, "gender": "girl"},
                {"name": "Michael", "rank": 3, "gender": "boy"},
            ],
        )

    def test_row_aslist(self):
        self.assertEqual(
            [row.aslist() for row in self.table.rows],
            [
                ["Jacob", 1, "boy"],
                ["Isabella", 1, "girl"],
                ["Ethan", 2, "boy"],
                ["Sophia", 2, "girl"],
                ["Michael", 3, "boy"],
            ],
        )

    def test_row_count(self):
        self.assertEqual(len(self.table.rows), 5)

    def test_access_row_by_index(self):
        row = ["Sophia", 2, "girl"]
        self.compare_iterable(row, self.table.rows[3])
        with self.assertRaises(IndexError):
            self.table.rows[len(self.table.rows)]

    def test_access_row_by_header(self):
        row = ["Sophia", 2, "girl"]
        self.compare_iterable(row, self.table.rows["S4"])
        with self.assertRaises(IndexError):
            self.table.rows[len(self.table.rows)]

    def test_access_row_element_by_index(self):
        self.assertEqual(self.table.rows[2][0], "Ethan")

    def test_access_row_element_by_header(self):
        self.assertEqual(self.table.rows[2]["name"], "Ethan")

    def test_append_row(self):
        row = ["Gary", 2, "boy"]
        self.table.rows.append(row, header="S6")
        self.assertEqual(len(self.table.rows), 6)
        self.compare_iterable(self.table.rows[5], row)

    def test_insert_row(self):
        row = ["Gary", 2, "boy"]
        position = 2
        self.table.rows.insert(position, row, header="S6")
        self.assertEqual(len(self.table.rows), 6)
        self.compare_iterable(self.table.rows[position], row)

    def test_pop_row_by_position(self):
        position = 2
        self.table.rows.pop(position)
        self.assertEqual(len(self.table.rows), 4)

    def test_pop_row_by_header(self):
        header = "S3"
        self.table.rows.pop(header)
        self.assertEqual(len(self.table.rows), 4)

    def test_update_row_by_index(self):
        row = ["Sophie", 5, "girl"]
        position = 3
        self.table.rows.update(position, row)
        self.compare_iterable(self.table.rows[position], row)

    def test_update_row_by_header(self):
        row = ["Sophie", 5, "girl"]
        header = "S4"
        self.table.rows.update(header, row)
        self.compare_iterable(self.table.rows[header], row)

    def test_update_row_slice(self):
        rows = [["Sophie", 5, "girl"], ["Mike", 4, "boy"]]
        self.table.rows.update(slice(3, 5, 1), rows)
        self.assertEqual(len(self.table.rows), 5)
        self.compare_iterable(self.table.rows[3], rows[0])
        self.compare_iterable(self.table.rows[4], rows[1])

    # Tests for special row methods

    def test_row_getitem_slice(self):
        new_table = self.table.rows[:3]
        self.assertEqual(len(new_table.rows), 3)
        self.assertEqual(len(self.table.rows), 5)

    def test_row_delitem_int(self):
        del self.table.rows[1]
        self.assertEqual(len(self.table.rows), 4)

    def test_row_delitem_slice(self):
        del self.table.rows[2:]
        self.assertEqual(len(self.table.rows), 2)

    def test_row_delitem_str(self):
        del self.table.rows["S2"]
        self.assertEqual(len(self.table.rows), 4)
        with self.assertRaises(KeyError):
            self.table.rows["S2"]

    def test_row_setitem_int(self):
        position = 3
        row = ["Sophie", 5, "girl"]
        self.table.rows[position] = row
        self.compare_iterable(self.table.rows[position], row)

    def test_row_setitem_slice(self):
        rows = [["Sophie", 5, "girl"], ["Mike", 4, "boy"]]
        self.table.rows[3:] = rows
        self.assertEqual(len(self.table.rows), 5)
        self.compare_iterable(self.table.rows[3], rows[0])
        self.compare_iterable(self.table.rows[4], rows[1])

    def test_row_setitem_str(self):
        header = "S2"
        row = ["Mike", 4, "Boy"]
        self.table.rows[header] = row
        self.assertEqual(len(self.table.rows), 5)
        self.compare_iterable(row, self.table.rows[header])

    def test_row_contains(self):
        self.assertTrue(["Isabella", 1, "girl"] in self.table.rows)
        self.assertFalse(["Ethan", 3, "boy"] in self.table.rows)

    def test_row_header_contains(self):
        self.assertTrue("S3" in self.table.rows.header)
        self.assertFalse("S6" in self.table.rows.header)

    # Test for special column methods

    def test_column_getitem_slice(self):
        new_table = self.table.columns[:2]
        self.assertEqual(len(self.table.columns), 3)
        self.assertEqual(len(new_table.columns), 2)

    def test_column_delitem_int(self):
        del self.table.columns[1]
        self.assertEqual(len(self.table.columns), 2)

    def test_column_delitem_slice(self):
        del self.table.columns[2:]
        self.assertEqual(len(self.table.columns), 2)

    def test_column_delitem_str(self):
        del self.table.columns["rank"]
        self.assertEqual(len(self.table.columns), 2)
        with self.assertRaises(KeyError):
            self.table.columns["rank"]

    def test_column_setitem_int(self):
        position = 2
        row = [3, 4, 5, 6, 7]
        self.table.columns[position] = row
        self.compare_iterable(self.table.columns[position], row)

    def test_column_setitem_slice(self):
        columns = [
            [5, "girl"],
            [4, "boy"],
            [4, "boy"],
            [2, "girl"],
            [1, "boy"],
        ]
        self.table.columns[1:] = columns
        self.assertEqual(len(self.table.columns), 3)
        self.compare_iterable(self.table.columns[1], [c[0] for c in columns])
        self.compare_iterable(self.table.columns[2], [c[1] for c in columns])

    def test_column_setitem_str(self):
        header = "rank"
        column = [3, 2, 1, 2, 4]
        self.table.columns[header] = column
        self.assertEqual(len(self.table.columns), 3)
        self.compare_iterable(column, self.table.columns[header])

    def test_column_header_contains(self):
        self.assertTrue("rank" in self.table.columns.header)
        self.assertFalse("score" in self.table.columns.header)

    def test_column_contains(self):
        self.assertTrue(["boy", "girl", "boy", "girl", "boy"] in self.table.columns)
        self.assertFalse(["boy", "girl", "girl", "girl", "boy"] in self.table.columns)

    # Test for printing operations

    def test_get_string(self):
        string = """+----+----------+------+--------+
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
+----+----------+------+--------+"""
        self.assertEqual(string, str(self.table))

    def test_stream(self):
        def generator():
            for i in range(1, 6):
                yield [i, i**2]

        table = BeautifulTable()
        table.columns.header = ["Number", "It's Square"]
        self.compare_iterable(
            table.stream(generator()),
            [
                "+--------+-------------+",
                "| Number | It's Square |",
                "+--------+-------------+",
                "|   1    |      1      |",
                "+--------+-------------+",
                "|   2    |      4      |",
                "+--------+-------------+",
                "|   3    |      9      |",
                "+--------+-------------+",
                "|   4    |     16      |",
                "+--------+-------------+",
                "|   5    |     25      |",
                "+--------+-------------+",
            ],
        )

    def test_left_align(self):
        self.table.columns.alignment[0] = self.table.ALIGN_LEFT
        string = """+----+----------+------+--------+
|    | name     | rank | gender |
+----+----------+------+--------+
| S1 | Jacob    |  1   |  boy   |
+----+----------+------+--------+
| S2 | Isabella |  1   |  girl  |
+----+----------+------+--------+
| S3 | Ethan    |  2   |  boy   |
+----+----------+------+--------+
| S4 | Sophia   |  2   |  girl  |
+----+----------+------+--------+
| S5 | Michael  |  3   |  boy   |
+----+----------+------+--------+"""
        self.assertEqual(string, str(self.table))

    def test_right_align(self):
        self.table.columns.alignment[0] = self.table.ALIGN_RIGHT
        string = """+----+----------+------+--------+
|    |     name | rank | gender |
+----+----------+------+--------+
| S1 |    Jacob |  1   |  boy   |
+----+----------+------+--------+
| S2 | Isabella |  1   |  girl  |
+----+----------+------+--------+
| S3 |    Ethan |  2   |  boy   |
+----+----------+------+--------+
| S4 |   Sophia |  2   |  girl  |
+----+----------+------+--------+
| S5 |  Michael |  3   |  boy   |
+----+----------+------+--------+"""
        self.assertEqual(string, str(self.table))

    def test_mixed_align(self):
        self.table.columns.alignment = [
            self.table.ALIGN_LEFT,
            self.table.ALIGN_CENTER,
            self.table.ALIGN_RIGHT,
        ]
        string = """+----+----------+------+--------+
|    | name     | rank | gender |
+----+----------+------+--------+
| S1 | Jacob    |  1   |    boy |
+----+----------+------+--------+
| S2 | Isabella |  1   |   girl |
+----+----------+------+--------+
| S3 | Ethan    |  2   |    boy |
+----+----------+------+--------+
| S4 | Sophia   |  2   |   girl |
+----+----------+------+--------+
| S5 | Michael  |  3   |    boy |
+----+----------+------+--------+"""
        self.assertEqual(string, str(self.table))

    def test_align_all(self):
        self.table.columns.alignment = self.table.ALIGN_LEFT
        string = """+----+----------+------+--------+
|    | name     | rank | gender |
+----+----------+------+--------+
| S1 | Jacob    | 1    | boy    |
+----+----------+------+--------+
| S2 | Isabella | 1    | girl   |
+----+----------+------+--------+
| S3 | Ethan    | 2    | boy    |
+----+----------+------+--------+
| S4 | Sophia   | 2    | girl   |
+----+----------+------+--------+
| S5 | Michael  | 3    | boy    |
+----+----------+------+--------+"""
        self.assertEqual(string, str(self.table))

    def test_sign_plus(self):
        self.table.sign = self.table.SM_PLUS
        string = """+----+----------+------+--------+
|    |   name   | rank | gender |
+----+----------+------+--------+
| S1 |  Jacob   |  +1  |  boy   |
+----+----------+------+--------+
| S2 | Isabella |  +1  |  girl  |
+----+----------+------+--------+
| S3 |  Ethan   |  +2  |  boy   |
+----+----------+------+--------+
| S4 |  Sophia  |  +2  |  girl  |
+----+----------+------+--------+
| S5 | Michael  |  +3  |  boy   |
+----+----------+------+--------+"""
        self.assertEqual(string, str(self.table))

    def test_wep_wrap(self):
        self.create_table(20)
        self.table.columns.width_exceed_policy = self.table.WEP_WRAP
        string = """+---+------+---+---+
|   | name | r | g |
|   |      | a | e |
|   |      | n | n |
|   |      | k | d |
|   |      |   | e |
|   |      |   | r |
+---+------+---+---+
| S | Jaco | 1 | b |
| 1 |  b   |   | o |
|   |      |   | y |
+---+------+---+---+
| S | Isab | 1 | g |
| 2 | ella |   | i |
|   |      |   | r |
|   |      |   | l |
+---+------+---+---+
| S | Etha | 2 | b |
| 3 |  n   |   | o |
|   |      |   | y |
+---+------+---+---+
| S | Soph | 2 | g |
| 4 |  ia  |   | i |
|   |      |   | r |
|   |      |   | l |
+---+------+---+---+
| S | Mich | 3 | b |
| 5 | ael  |   | o |
|   |      |   | y |
+---+------+---+---+"""
        self.assertEqual(string, str(self.table))

    def test_wep_strip(self):
        self.create_table(20)
        self.table.columns.width_exceed_policy = self.table.WEP_STRIP
        string = """+---+------+---+---+
|   | name | r | g |
+---+------+---+---+
| S | Jaco | 1 | b |
+---+------+---+---+
| S | Isab | 1 | g |
+---+------+---+---+
| S | Etha | 2 | b |
+---+------+---+---+
| S | Soph | 2 | g |
+---+------+---+---+
| S | Mich | 3 | b |
+---+------+---+---+"""
        self.assertEqual(string, str(self.table))

    def test_wep_ellipsis(self):
        self.create_table(20)
        self.table.columns.width_exceed_policy = self.table.WEP_ELLIPSIS
        string = """+---+------+---+---+
|   | name | . | . |
+---+------+---+---+
| . | J... | 1 | . |
+---+------+---+---+
| . | I... | 1 | . |
+---+------+---+---+
| . | E... | 2 | . |
+---+------+---+---+
| . | S... | 2 | . |
+---+------+---+---+
| . | M... | 3 | . |
+---+------+---+---+"""
        self.assertEqual(string, str(self.table))

    def test_empty_header(self):
        self.table.columns.header = ["", " ", "  "]
        string = """+----+----------+---+------+
| S1 |  Jacob   | 1 | boy  |
+----+----------+---+------+
| S2 | Isabella | 1 | girl |
+----+----------+---+------+
| S3 |  Ethan   | 2 | boy  |
+----+----------+---+------+
| S4 |  Sophia  | 2 | girl |
+----+----------+---+------+
| S5 | Michael  | 3 | boy  |
+----+----------+---+------+"""
        self.assertEqual(string, str(self.table))

    def test_eastasian_characters(self):
        string = """+----+------------+------+--------+
|    |    name    | rank | gender |
+----+------------+------+--------+
| S1 |   Jacob    |  1   |  boy   |
+----+------------+------+--------+
| S2 |  Isabella  |  1   |  girl  |
+----+------------+------+--------+
| S3 |   Ethan    |  2   |  boy   |
+----+------------+------+--------+
| S4 |   Sophia   |  2   |  girl  |
+----+------------+------+--------+
| S5 |  Michael   |  3   |  boy   |
+----+------------+------+--------+
| S6 | こんにちは |  2   |  boy   |
+----+------------+------+--------+"""
        self.table.rows.append(["こんにちは", 2, "boy"], header="S6")
        self.assertEqual(string, str(self.table))

    def test_newline(self):
        string = """+---+---+
| 0 | a |
|   | b |
+---+---+"""
        table = BeautifulTable()
        table.rows.append(["0", "a\nb"])
        self.assertEqual(string, str(table))

    def test_newline_multiple_columns(self):
        string = """+---+---+
| a | p |
| b | q |
| c |   |
+---+---+"""
        table = BeautifulTable()
        table.rows.append(["a\nb\nc", "p\nq"])
        self.assertEqual(string, str(table))

    # Test for ANSI sequences

    def test_ansi_sequences(self):
        table = BeautifulTable()
        string = """+------+---+-----+
| \x1b[31mAdam\x1b[0m | 2 | boy |
+------+---+-----+"""
        table.rows.append(["\x1b[31mAdam\x1b[0m", 2, "boy"])
        self.assertEqual(string, str(table))

    def test_ansi_wrap(self):
        table = BeautifulTable(maxwidth=30)
        string = """+-----------------+---+------+
| \x1b[31mThis is a very \x1b[0m | 2 | girl |
|    \x1b[32mlong name\x1b[0m    |   |      |
+-----------------+---+------+"""
        long_string = "\x1b[31mThis is a very \x1b[0m\x1b[32mlong name\x1b[0m"
        table.rows.append([long_string, 2, "girl"])
        self.assertEqual(string, str(table))

    def test_ansi_wrap_mb(self):
        table = BeautifulTable(maxwidth=30)
        string = """+-----------------+---+------+
| \x1b[31mこれは非常に長\x1b[0m  | 2 | girl |
|   \x1b[31mい\x1b[0m\x1b[32m名前です\x1b[0m    |   |      |
+-----------------+---+------+"""
        long_string = "\x1b[31mこれは非常に長い\x1b[0m\x1b[32m名前です\x1b[0m"
        table.rows.append([long_string, 2, "girl"])
        self.assertEqual(string, str(table))

    def test_ansi_ellipsis(self):
        table = BeautifulTable(maxwidth=30)
        table.columns.width_exceed_policy = table.WEP_ELLIPSIS
        string = """+-----------------+---+------+
| \x1b[31mThis is a ve\x1b[0m... | 2 | girl |
+-----------------+---+------+"""
        long_string = "\x1b[31mThis is a very \x1b[0m\x1b[32mlong name\x1b[0m"
        table.rows.append([long_string, 2, "girl"])
        self.assertEqual(string, str(table))

    def test_ansi_ellipsis_mb(self):
        table = BeautifulTable(maxwidth=30)
        table.columns.width_exceed_policy = table.WEP_ELLIPSIS
        string = """+-----------------+---+------+
| \x1b[31mこれは非常に\x1b[0m... | 2 | girl |
+-----------------+---+------+"""
        long_string = "\x1b[31mこれは非常に長い\x1b[0m\x1b[32m名前です\x1b[0m"
        table.rows.append([long_string, 2, "girl"])
        self.assertEqual(string, str(table))

    def test_ansi_strip(self):
        table = BeautifulTable(maxwidth=30)
        table.columns.width_exceed_policy = table.WEP_STRIP
        string = """+-----------------+---+------+
| \x1b[31mThis is a very \x1b[0m | 2 | girl |
+-----------------+---+------+"""
        long_string = "\x1b[31mThis is a very \x1b[0m\x1b[32mlong name\x1b[0m"
        table.rows.append([long_string, 2, "girl"])
        self.assertEqual(string, str(table))

    def test_ansi_strip_mb(self):
        table = BeautifulTable(maxwidth=30)
        table.columns.width_exceed_policy = table.WEP_STRIP
        string = """+-----------------+---+------+
| \x1b[31mこれは非常に長\x1b[0m  | 2 | girl |
+-----------------+---+------+"""
        long_string = "\x1b[31mこれは非常に長い\x1b[0m\x1b[32m名前です\x1b[0m"
        table.rows.append([long_string, 2, "girl"])
        self.assertEqual(string, str(table))

    # Test on empty table

    def test_empty_table_by_column(self):
        self.create_table(20)
        for i in range(3):
            self.table.columns.pop()
        self.assertEqual(str(self.table), "")

    def test_empty_table_by_row(self):
        self.create_table(20)
        for i in range(5):
            self.table.rows.pop()
        self.assertEqual(str(self.table), "")

    def test_table_width_zero(self):
        self.create_table(20)
        self.table.clear(True)
        self.assertEqual(self.table._width, 0)

    def test_table_auto_width(self):
        row_list = ["abcdefghijklmopqrstuvwxyz", 1234, "none"]

        self.create_table(200)
        self.table.rows.append(row_list)
        len_for_max_width_200 = len(str(self.table))

        self.create_table(80)
        self.table.rows.append(row_list)
        len_for_max_width_80 = len(str(self.table))

        self.assertEqual(len_for_max_width_80, len_for_max_width_200)

    def test_csv_export(self):
        # Create csv files in path.
        self.table.to_csv("beautiful_table.csv")
        self.table.to_csv("./docs/beautiful_table.csv")

        with self.assertRaises(ValueError):
            self.table.to_csv(1)

        # Check if csv files exist.
        self.assertTrue(os.path.exists("beautiful_table.csv"))
        self.assertTrue(os.path.exists("./docs/beautiful_table.csv"))

        # Teardown step.
        os.remove("beautiful_table.csv")
        os.remove("./docs/beautiful_table.csv")

    def test_csv_import(self):
        # Export table as CSV file and import it back.
        self.table.to_csv("beautiful_table.csv")

        test_table = BeautifulTable()
        test_table.from_csv("beautiful_table.csv")

        with self.assertRaises(ValueError):
            self.table.from_csv(1)

        self.assertEqual(len(self.table.rows), len(test_table.rows))
        self.assertEqual(self.table.columns.header, test_table.columns.header)

        test_table = BeautifulTable()
        test_table.from_csv("beautiful_table.csv", header=False)
        self.assertEqual(len(self.table.rows), len(test_table.rows) - 1)

        # Teardown step.
        os.remove("beautiful_table.csv")

    @unittest.skipUnless(PANDAS_INSTALLED, REQUIRED_PANDAS_MESSAGE)
    def test_df_export(self):
        df = self.table.to_df()
        self.assertEqual(self.table.rows.header, df.index)
        self.assertEqual(self.table.columns.header, list(df.columns))
        self.assertEqual(
            [list(row) for row in list(df.values)],
            [list(row) for row in list(self.table._data)],
        )

    @unittest.skipUnless(PANDAS_INSTALLED, REQUIRED_PANDAS_MESSAGE)
    def test_df_import(self):
        df = self.create_dataframe()
        table = BeautifulTable()
        table = table.from_df(df)
        self.assertEqual(table.rows.header, df.index)
        self.assertEqual(table.columns.header, list(df.columns))
        self.assertEqual(
            [list(row) for row in list(df.values)],
            [list(row) for row in list(table.rows)],
        )

    @unittest.skipUnless(PANDAS_INSTALLED, REQUIRED_PANDAS_MESSAGE)
    def test_df_export_scenario1(self):
        table = BeautifulTable()
        table.rows.append(["Jacob", 1, "boy"])
        table.rows.append(["Isabella", 2, "girl"])
        df = table.to_df()
        self.assertEqual(table.rows.header, [None, None])
        self.assertEqual(table.columns.header, [None, None, None])
        self.assertEqual(list(df.index), [0, 1])
        self.assertEqual(list(df.columns), [0, 1, 2])

    @unittest.skipUnless(PANDAS_INSTALLED, REQUIRED_PANDAS_MESSAGE)
    def test_df_export_scenario2(self):
        table = BeautifulTable()
        table.rows.append(["Jacob", 1, "boy"])
        table.rows.append(["Isabella", 2, "girl"])
        table.columns.header = [None, "rank", "gender"]
        df = table.to_df()
        self.assertEqual(table.rows.header, [None, None])
        self.assertEqual(table.columns.header, [None, "rank", "gender"])
        self.assertEqual(list(df.index), [0, 1])
        self.assertEqual(list(df.columns), [None, "rank", "gender"])


if __name__ == "__main__":
    unittest.main()
