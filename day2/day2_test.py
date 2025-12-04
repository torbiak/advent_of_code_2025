import unittest
import day2

class Tests(unittest.TestCase):
    def test_current_or_next_double_number(self):
        tests = [
            [0, 11],
            [1, 11],
            [2, 11],
            [11, 11],
            [13, 22],
            [21, 22],
            [23, 33],
            [99, 99],
            [100, 1010],
        ]
        for n, want in tests:
            with self.subTest(n=n, want=want):
                got = day2.current_or_next_double_number(n)
                self.assertEqual(got, want)

    def test_find_double_numbers(self):
        tests = [
            [(11, 22), [11, 22]],
            [(95, 115), [99]],
            [(998, 1012), [1010]],
            [(1188511880, 1188511890), [1188511885]],
            [(222220, 222224), [222222]],
            [(1698522, 1698528), []],
            [(446443, 446449), [446446]],
            [(38593856, 38593862), [38593859]],
            [(565653, 565659), []],
            [(824824821, 824824827), []],
            [(2121212118, 2121212124), []],
        ]
        for (start, stop), want in tests:
            with self.subTest(start=start, stop=stop):
                got = list(day2.find_double_numbers(start, stop))
                self.assertListEqual(got, want)

    def test_find_multi_numbers(self):
        tests = [
            [(11, 22), [11, 22]],
            [(95, 115), [99, 111]],
            [(998, 1012), [999, 1010]],
            [(1188511880, 1188511890), [1188511885]],
            [(222220, 222224), [222222]],
            [(1698522, 1698528), []],
            [(446443, 446449), [446446]],
            [(38593856, 38593862), [38593859]],
            [(565653, 565659), [565656]],
            [(824824821, 824824827), [824824824]],
            [(2121212118, 2121212124), [2121212121]],
        ]
        for (start, stop), want in tests:
            with self.subTest(start=start, stop=stop):
                got = list(day2.find_multi_numbers(start, stop))
                self.assertListEqual(got, want)
