import unittest
from oop.lotto3 import Lotto


class TestLotto(unittest.TestCase):
    def test_lotto_initialization(self):
        # Valid initialization
        lotto = Lotto([1, 2, 3, 4, 5, 6])
        self.assertEqual(lotto.numbers, [1, 2, 3, 4, 5, 6])

        # Invalid number of elements
        with self.assertRaises(ValueError) as cm:
            Lotto([1, 2, 3, 4, 5])
        self.assertEqual(str(cm.exception), '6개의 숫자를 입력해주세요.')

        # Duplicate numbers
        with self.assertRaises(ValueError) as cm:
            Lotto([1, 2, 3, 4, 5, 5])
        self.assertEqual(str(cm.exception), '중복된 숫자가 있습니다.')

        # Numbers out of range
        with self.assertRaises(ValueError) as cm:
            Lotto([0, 2, 3, 4, 5, 6])
        self.assertEqual(str(cm.exception), '숫자는 1~45 사이여야 합니다')

        with self.assertRaises(ValueError) as cm:
            Lotto([1, 2, 3, 4, 5, 46])
        self.assertEqual(str(cm.exception), '숫자는 1~45 사이여야 합니다')

if __name__ == '__main__':
    unittest.main()
