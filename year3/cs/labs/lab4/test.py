import unittest
from DES_permutation import *

class TestDESRoundKeyGeneration(unittest.TestCase):

    def test_apply_permutation(self):
        input_bits = [0, 1, 1, 0, 1, 0, 0, 1]
        permutation = [3, 2, 0, 1, 6, 5, 7, 4]
        expected_output = [0, 1, 0, 1, 0, 0, 1, 1]
        self.assertEqual(apply_permutation(input_bits, permutation), expected_output)

    def test_left_shift(self):
        bits = [0, 1, 1, 0, 1, 0, 0, 1]
        expected_output_1_shift = [1, 1, 0, 1, 0, 0, 1, 0]
        expected_output_3_shift = [0, 1, 0, 0, 1, 0, 1, 1]
        self.assertEqual(left_shift(bits, 1), expected_output_1_shift)
        self.assertEqual(left_shift(bits, 3), expected_output_3_shift)

    def test_generate_round_keys(self):
        PC1_dummy = [7, 6, 5, 4, 3, 2, 1, 0]
        SHIFT_dummy = [1, 2, 1, 2]
        PC2_dummy = [1, 0, 3, 2, 5, 4]
        dummy_key = 0b11011000
        round_keys = generate_round_keys(dummy_key, PC1_dummy, SHIFT_dummy, PC2_dummy)
        expected_keys = [
            [0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 1]
        ]
        self.assertEqual(round_keys, expected_keys)


if __name__ == "__main__":
    unittest.main()
