# -*- coding: utf-8 -*-


import unittest
import os

from beautifultable import BeautifulTable


class TableOperationsTestCase(unittest.TestCase):
    def setUp(self):
        self.create_table()

    def create_table(self, max_width=80):
        table = BeautifulTable(max_width)
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

    # Test for table operations

    def test_filter(self):
        new_table = self.table.filter(lambda x: x["rank"] > 1)
        self.assertEqual(len(self.table), 5)
        rows = [
            ["Ethan", 2, "boy"],
            ["Sophia", 2, "girl"],
            ["Michael", 3, "boy"],
        ]
        for row_t, row in zip(new_table, rows):
            self.compare_iterable(row_t, row)

    def test_sort_by_index(self):
        self.table.sort(0)
        rows = [
            ["Ethan", 2, "boy"],
            ["Isabella", 1, "girl"],
            ["Jacob", 1, "boy"],
            ["Michael", 3, "boy"],
            ["Sophia", 2, "girl"],
        ]
        for row_t, row in zip(self.table, rows):
            self.compare_iterable(row_t, row)

    def test_sort_by_index_reversed(self):
        self.table.sort(0, reverse=True)
        rows = [
            ["Ethan", 2, "boy"],
            ["Isabella", 1, "girl"],
            ["Jacob", 1, "boy"],
            ["Michael", 3, "boy"],
            ["Sophia", 2, "girl"],
        ]
        for row_t, row in zip(self.table, reversed(rows)):
            self.compare_iterable(row_t, row)

    def test_sort_by_header(self):
        self.table.sort("name")
        rows = [
            ["Ethan", 2, "boy"],
            ["Isabella", 1, "girl"],
            ["Jacob", 1, "boy"],
            ["Michael", 3, "boy"],
            ["Sophia", 2, "girl"],
        ]
        for row_t, row in zip(self.table, rows):
            self.compare_iterable(row_t, row)

    def test_sort_by_callable(self):
        self.table.sort(lambda x: (x[1], x[0]))
        rows = [
            ["Isabella", 1, "girl"],
            ["Jacob", 1, "boy"],
            ["Ethan", 2, "boy"],
            ["Sophia", 2, "girl"],
            ["Michael", 3, "boy"],
        ]
        for row_t, row in zip(self.table, rows):
            self.compare_iterable(row_t, row)

    def test_sort_raises_exception(self):
        with self.assertRaises(TypeError):
            self.table.sort(None)

    # Tests for column operations

    def test_column_count(self):
        self.assertEqual(self.table.column_count, 3)

    def test_access_column_by_header(self):
        column = ["Jacob", "Isabella", "Ethan", "Sophia", "Michael"]
        self.compare_iterable(column, self.table["name"])
        with self.assertRaises(KeyError):
            self.table["name1"]

    def test_get_column_index(self):
        self.assertEqual(self.table.get_column_index("gender"), 2)
        with self.assertRaises(KeyError):
            self.table.get_column_index("rank1")

    def test_get_column_header(self):
        self.assertEqual(self.table.get_column_header(2), "gender")
        with self.assertRaises(IndexError):
            self.table.get_column_header(self.table.column_count)

    def test_append_column(self):
        title = "year"
        column = ["2010", "2012", "2008", "2010", "2011"]
        self.table.append_column(title, column)
        self.assertEqual(self.table.column_count, 4)
        last_column = self.table.get_column(self.table.column_count - 1)
        self.compare_iterable(column, last_column)

    def test_insert_column(self):
        column = ["2010", "2012", "2008", "2010", "2011"]
        title = "year"
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
        header = "gender"
        self.table.pop_column(header)
        self.assertEqual(self.table.column_count, 2)
        with self.assertRaises(KeyError):
            self.table.get_column(header)

    def test_update_column(self):
        header = "rank"
        column = [3, 2, 1, 2, 4]
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

    def test_access_row_element_by_index(self):
        self.assertEqual(self.table[2][0], "Ethan")

    def test_access_row_element_by_header(self):
        self.assertEqual(self.table[2]["name"], "Ethan")

    def test_append_row(self):
        row = ["Gary", 2, "boy"]
        self.table.append_row(row)
        self.assertEqual(len(self.table), 6)
        self.compare_iterable(self.table[5], row)

    def test_insert_row(self):
        row = ["Gary", 2, "boy"]
        position = 2
        self.table.insert_row(position, row)
        self.assertEqual(len(self.table), 6)
        self.compare_iterable(self.table[position], row)

    def test_pop_row(self):
        position = 2
        self.table.pop_row(position)
        self.assertEqual(len(self.table), 4)

    def test_update_row(self):
        row = ["Sophie", 5, "girl"]
        position = 3
        self.table.update_row(position, row)
        self.compare_iterable(self.table[position], row)

    def test_update_row_slice(self):
        rows = [["Sophie", 5, "girl"], ["Mike", 4, "boy"]]
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
        del self.table["rank"]
        self.assertEqual(self.table.column_count, 2)
        with self.assertRaises(KeyError):
            self.table.get_column("rank")

    def test_setitem_int(self):
        position = 3
        row = ["Sophie", 5, "girl"]
        self.table[position] = row
        self.compare_iterable(self.table[position], row)

    def test_setitem_slice(self):
        rows = [["Sophie", 5, "girl"], ["Mike", 4, "boy"]]
        self.table[3:] = rows
        self.assertEqual(len(self.table), 5)
        self.compare_iterable(self.table[3], rows[0])
        self.compare_iterable(self.table[4], rows[1])

    def test_setitem_str(self):
        header = "rank"
        column = [3, 2, 1, 2, 4]
        self.table[header] = column
        self.assertEqual(self.table.column_count, 3)
        self.compare_iterable(column, self.table.get_column(header))

    def test_contains(self):
        self.assertTrue("rank" in self.table)
        self.assertFalse("rankk" in self.table)
        self.assertTrue(["Isabella", 1, "girl"] in self.table)
        self.assertFalse(["Ethan", 3, "boy"] in self.table)

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

    def test_left_align(self):
        self.table.column_alignments[0] = self.table.ALIGN_LEFT
        string = """+----------+------+--------+
| name     | rank | gender |
+----------+------+--------+
| Jacob    |  1   |  boy   |
+----------+------+--------+
| Isabella |  1   |  girl  |
+----------+------+--------+
| Ethan    |  2   |  boy   |
+----------+------+--------+
| Sophia   |  2   |  girl  |
+----------+------+--------+
| Michael  |  3   |  boy   |
+----------+------+--------+"""
        self.assertEqual(string, self.table.get_string())

    def test_right_align(self):
        self.table.column_alignments[0] = self.table.ALIGN_RIGHT
        string = """+----------+------+--------+
|     name | rank | gender |
+----------+------+--------+
|    Jacob |  1   |  boy   |
+----------+------+--------+
| Isabella |  1   |  girl  |
+----------+------+--------+
|    Ethan |  2   |  boy   |
+----------+------+--------+
|   Sophia |  2   |  girl  |
+----------+------+--------+
|  Michael |  3   |  boy   |
+----------+------+--------+"""
        self.assertEqual(string, self.table.get_string())

    def test_mixed_align(self):
        self.table.column_alignments = [
            self.table.ALIGN_LEFT,
            self.table.ALIGN_CENTER,
            self.table.ALIGN_RIGHT,
        ]
        string = """+----------+------+--------+
| name     | rank | gender |
+----------+------+--------+
| Jacob    |  1   |    boy |
+----------+------+--------+
| Isabella |  1   |   girl |
+----------+------+--------+
| Ethan    |  2   |    boy |
+----------+------+--------+
| Sophia   |  2   |   girl |
+----------+------+--------+
| Michael  |  3   |    boy |
+----------+------+--------+"""
        self.assertEqual(string, self.table.get_string())

    def test_align_all(self):
        self.table.column_alignments = self.table.ALIGN_LEFT
        string = """+----------+------+--------+
| name     | rank | gender |
+----------+------+--------+
| Jacob    | 1    | boy    |
+----------+------+--------+
| Isabella | 1    | girl   |
+----------+------+--------+
| Ethan    | 2    | boy    |
+----------+------+--------+
| Sophia   | 2    | girl   |
+----------+------+--------+
| Michael  | 3    | boy    |
+----------+------+--------+"""
        self.assertEqual(string, self.table.get_string())

    def test_signmode_plus(self):
        self.table.sign_mode = self.table.SM_PLUS
        string = """+----------+------+--------+
|   name   | rank | gender |
+----------+------+--------+
|  Jacob   |  +1  |  boy   |
+----------+------+--------+
| Isabella |  +1  |  girl  |
+----------+------+--------+
|  Ethan   |  +2  |  boy   |
+----------+------+--------+
|  Sophia  |  +2  |  girl  |
+----------+------+--------+
| Michael  |  +3  |  boy   |
+----------+------+--------+"""
        self.assertEqual(string, self.table.get_string())

    def test_wep_wrap(self):
        self.create_table(20)
        self.table.width_exceed_policy = self.table.WEP_WRAP
        string = """+-------+----+-----+
| name  | ra | gen |
|       | nk | der |
+-------+----+-----+
| Jacob | 1  | boy |
+-------+----+-----+
| Isabe | 1  | gir |
|  lla  |    |  l  |
+-------+----+-----+
| Ethan | 2  | boy |
+-------+----+-----+
| Sophi | 2  | gir |
|   a   |    |  l  |
+-------+----+-----+
| Micha | 3  | boy |
|  el   |    |     |
+-------+----+-----+"""
        self.assertEqual(string, self.table.get_string())

    def test_wep_strip(self):
        self.create_table(20)
        self.table.width_exceed_policy = self.table.WEP_STRIP
        string = """+-------+----+-----+
| name  | ra | gen |
+-------+----+-----+
| Jacob | 1  | boy |
+-------+----+-----+
| Isabe | 1  | gir |
+-------+----+-----+
| Ethan | 2  | boy |
+-------+----+-----+
| Sophi | 2  | gir |
+-------+----+-----+
| Micha | 3  | boy |
+-------+----+-----+"""
        self.assertEqual(string, self.table.get_string())

    def test_wep_ellipsis(self):
        self.create_table(20)
        self.table.width_exceed_policy = self.table.WEP_ELLIPSIS
        string = """+-------+----+-----+
| name  | .. | ... |
+-------+----+-----+
| Jacob | 1  | boy |
+-------+----+-----+
| Is... | 1  | ... |
+-------+----+-----+
| Ethan | 2  | boy |
+-------+----+-----+
| So... | 2  | ... |
+-------+----+-----+
| Mi... | 3  | boy |
+-------+----+-----+"""
        self.assertEqual(string, self.table.get_string())

    def test_empty_header(self):
        self.table.column_headers = ["", " ", "  "]
        string = """+----------+---+------+
|  Jacob   | 1 | boy  |
+----------+---+------+
| Isabella | 1 | girl |
+----------+---+------+
|  Ethan   | 2 | boy  |
+----------+---+------+
|  Sophia  | 2 | girl |
+----------+---+------+
| Michael  | 3 | boy  |
+----------+---+------+"""
        self.assertEqual(string, self.table.get_string())

    def test_serialno(self):
        self.table.serialno = True
        string = """+----+----------+------+--------+
| SN |   name   | rank | gender |
+----+----------+------+--------+
| 1  |  Jacob   |  1   |  boy   |
+----+----------+------+--------+
| 2  | Isabella |  1   |  girl  |
+----+----------+------+--------+
| 3  |  Ethan   |  2   |  boy   |
+----+----------+------+--------+
| 4  |  Sophia  |  2   |  girl  |
+----+----------+------+--------+
| 5  | Michael  |  3   |  boy   |
+----+----------+------+--------+"""
        self.assertEqual(string, self.table.get_string())

    def test_eastasian_characters(self):
        string = u"""+------------+------+--------+
|    name    | rank | gender |
+------------+------+--------+
|   Jacob    |  1   |  boy   |
+------------+------+--------+
|  Isabella  |  1   |  girl  |
+------------+------+--------+
|   Ethan    |  2   |  boy   |
+------------+------+--------+
|   Sophia   |  2   |  girl  |
+------------+------+--------+
|  Michael   |  3   |  boy   |
+------------+------+--------+
| こんにちは |  2   |  boy   |
+------------+------+--------+"""
        self.table.append_row([u"こんにちは", 2, "boy"])
        self.assertEqual(string, self.table.get_string())

    def test_newline(self):
        string = """+---+---+
| 0 | a |
|   | b |
+---+---+"""
        table = BeautifulTable()
        table.append_row(["0", "a\nb"])
        self.assertEqual(string, table.get_string())

    def test_newline_multiple_columns(self):
        string = """+---+---+
| a | p |
| b | q |
| c |   |
+---+---+"""
        table = BeautifulTable()
        table.append_row(["a\nb\nc", "p\nq"])
        self.assertEqual(string, table.get_string())

    # Test for ANSI sequences

    def test_ansi_sequences(self):
        table = BeautifulTable()
        string = """+------+---+-----+
| \x1b[31mAdam\x1b[0m | 2 | boy |
+------+---+-----+"""
        table.append_row(["\x1b[31mAdam\x1b[0m", 2, "boy"])
        self.assertEqual(string, table.get_string())

    def test_ansi_wrap(self):
        table = BeautifulTable(max_width=30)
        string = """+-----------------+---+------+
| \x1b[31mThis is a very \x1b[0m | 2 | girl |
|    \x1b[32mlong name\x1b[0m    |   |      |
+-----------------+---+------+"""
        long_string = "\x1b[31mThis is a very \x1b[0m\x1b[32mlong name\x1b[0m"
        table.append_row([long_string, 2, "girl"])
        self.assertEqual(string, table.get_string())

    def test_ansi_wrap_mb(self):
        table = BeautifulTable(max_width=30)
        string = u"""+-----------------+---+------+
| \x1b[31mこれは非常に長\x1b[0m  | 2 | girl |
|   \x1b[31mい\x1b[0m\x1b[32m名前です\x1b[0m    |   |      |
+-----------------+---+------+"""
        long_string = u"\x1b[31mこれは非常に長い\x1b[0m\x1b[32m名前です\x1b[0m"
        table.append_row([long_string, 2, "girl"])
        self.assertEqual(string, table.get_string())

    def test_ansi_ellipsis(self):
        table = BeautifulTable(max_width=30)
        table.width_exceed_policy = table.WEP_ELLIPSIS
        string = """+-----------------+---+------+
| \x1b[31mThis is a ve\x1b[0m... | 2 | girl |
+-----------------+---+------+"""
        long_string = "\x1b[31mThis is a very \x1b[0m\x1b[32mlong name\x1b[0m"
        table.append_row([long_string, 2, "girl"])
        self.assertEqual(string, table.get_string())

    def test_ansi_ellipsis_mb(self):
        table = BeautifulTable(max_width=30)
        table.width_exceed_policy = table.WEP_ELLIPSIS
        string = u"""+-----------------+---+------+
| \x1b[31mこれは非常に\x1b[0m... | 2 | girl |
+-----------------+---+------+"""
        long_string = u"\x1b[31mこれは非常に長い\x1b[0m\x1b[32m名前です\x1b[0m"
        table.append_row([long_string, 2, "girl"])
        self.assertEqual(string, table.get_string())

    def test_ansi_strip(self):
        table = BeautifulTable(max_width=30)
        table.width_exceed_policy = table.WEP_STRIP
        string = """+-----------------+---+------+
| \x1b[31mThis is a very \x1b[0m | 2 | girl |
+-----------------+---+------+"""
        long_string = "\x1b[31mThis is a very \x1b[0m\x1b[32mlong name\x1b[0m"
        table.append_row([long_string, 2, "girl"])
        self.assertEqual(string, table.get_string())

    def test_ansi_strip_mb(self):
        table = BeautifulTable(max_width=30)
        table.width_exceed_policy = table.WEP_STRIP
        string = u"""+-----------------+---+------+
| \x1b[31mこれは非常に長\x1b[0m  | 2 | girl |
+-----------------+---+------+"""
        long_string = u"\x1b[31mこれは非常に長い\x1b[0m\x1b[32m名前です\x1b[0m"
        table.append_row([long_string, 2, "girl"])
        self.assertEqual(string, table.get_string())

    # Test on empty table

    def test_empty_table_by_column(self):
        self.create_table(20)
        for i in range(3):
            self.table.pop_column()
        self.assertEqual(self.table.get_string(), "")

    def test_empty_table_by_row(self):
        self.create_table(20)
        for i in range(5):
            self.table.pop_row()
        self.assertEqual(self.table.get_string(), "")

    def test_table_width_zero(self):
        self.create_table(20)
        self.table.clear(True)
        width = self.table.get_table_width()
        self.assertEqual(width, 0)

    def test_table_auto_width(self):
        row_list = ["abcdefghijklmopqrstuvwxyz", 1234, "none"]

        self.create_table(200)
        self.table.append_row(row_list)
        len_for_max_width_200 = len(str(self.table))

        self.create_table(80)
        self.table.append_row(row_list)
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

        self.assertEqual(len(self.table), len(test_table))
        self.assertEqual(self.table.column_headers, test_table.column_headers)

        # for index in range(len(self.table)):
        #     self.assertEqual(self.table[index], test_table[index])

        test_table = BeautifulTable()
        test_table.from_csv("beautiful_table.csv", header_exists=False)
        self.assertEqual(len(self.table), len(test_table) - 1)

        # Teardown step.
        os.remove("beautiful_table.csv")


if __name__ == "__main__":
    unittest.main()
