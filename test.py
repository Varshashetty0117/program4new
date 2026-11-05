import unittest


class TestApplication(unittest.TestCase):

    def test_application(self):
        name = "VVCE"
        self.assertEqual(name, "cse")


if __name__ == "__main__":
    unittest.main()
