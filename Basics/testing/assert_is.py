import unittest

class IdentityTests(unittest.TestCase):
    def test_identity(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]

        self.assertEqual(a, b)
        self.assertNotEqual(a, c, "A nad C are equal")

        self.assertIs(a, b)
        self.assertIsNot(a, c)
        self.assertIsNot(b, c)

if __name__ == "__main__":
    unittest.main()