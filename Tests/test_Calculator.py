import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    # default test
    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_subtraction(self):
        test_data = CsvReader("Tests/Data/UnitTestSubtraction.csv").data
        for row in test_data:
            result_float = float(row['Result'])
            self.assertEqual(self.calculator.subtract(float(row['Value 1']), float(row['Value 2'])), result_float)
            result_int = int(row['Result'])
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), result_int)

    def test_addition(self):
        test_data = CsvReader("Tests/Data/UnitTestAddition.csv").data
        for row in test_data:
            result_float = float(row['Result'])
            self.assertEqual(self.calculator.add(float(row['Value 1']), float(row['Value 2'])), result_float)
            result_int = int(row['Result'])
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), result_int)

    def test_multiplication(self):
        test_data = CsvReader("Tests/Data/UnitTestMultiplication.csv").data
        for row in test_data:
            result_float = float(row['Result'])
            self.assertEqual(self.calculator.multiply(float(row['Value 1']), float(row['Value 2'])), result_float)
            result_int = int(row['Result'])
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), result_int)

    def test_division(self):
        test_data = CsvReader("Tests/Data/UnitTestDivision.csv").data
        for row in test_data:
            result_float = float(row['Result'])
            self.assertEqual(self.calculator.divide(float(row['Value 1']), float(row['Value 2'])), result_float)
            result_int = float(row['Result'])
            self.assertEqual(self.calculator.divide(int(row['Value 1']), int(row['Value 2'])), result_int)

    def test_square(self):
        test_data = CsvReader("Tests/Data/UnitTestSquare.csv").data
        for row in test_data:
            result_float = float(row['Result'])
            self.assertEqual(self.calculator.squared(float(row['Value 1'])), result_float)
            result_int = int(row['Result'])
            self.assertEqual(self.calculator.squared(int(row['Value 1'])), result_int)

    def test_square_root(self):
        test_data = CsvReader("Tests/Data/UnitTestSquare Root.csv").data
        for row in test_data:
            result_float = float(row['Result'])
            self.assertEqual(round(self.calculator.square_root(float(row['Value 1'])) , 8), result_float)
            result_int = float(row['Result'])
            self.assertEqual(round(self.calculator.square_root(int(row['Value 1'])) , 8), result_int)


if __name__ == '__main__':
    unittest.main()