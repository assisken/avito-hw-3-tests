from collections import namedtuple
from unittest import TestCase

from lib.one_hot_encoder import fit_transform

Case = namedtuple('Case', 'given expect')


class TestIssue03(TestCase):
    def test_fit_transform(self):
        cases = [
            Case(
                ['red', 'red', 'green'],
                [
                    ('red', [0, 1]),
                    ('red', [0, 1]),
                    ('green', [1, 0]),
                ]
            ),
            Case(
                ['Moscow', 'New York', 'Moscow', 'London'],
                [
                    ('Moscow', [0, 0, 1]),
                    ('New York', [0, 1, 0]),
                    ('Moscow', [0, 0, 1]),
                    ('London', [1, 0, 0]),
                ]
            ),
            Case(
                ['foo'],
                [('foo', [1])]
            ),
            Case(
                [''],
                [('', [1])]
            )
        ]

        for c in cases:
            with self.subTest(c.given):
                self.assertEqual(fit_transform(*c.given), c.expect)
                for transformed in fit_transform(*c.given):
                    self.assertIn(transformed, c.expect)

    def test_fit_transform_exception(self):
        self.assertRaises(TypeError, fit_transform)
