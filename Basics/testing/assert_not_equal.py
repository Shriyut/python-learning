import unittest

def copy_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return copy

class TEstInequality(unittest.TestCase):

    def test_inequality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual(True, False)

    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_add_element(values, 4)

        self.assertEqual(result, [1,2,3,4])
        self.assertNotEqual(
            values,
            [1, 2, 3, 4, 5],
            "COpy and add element function is mutating the input"
        )

if __name__ == "__main__":
    unittest.main()