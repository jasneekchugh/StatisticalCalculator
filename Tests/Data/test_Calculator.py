import unittest
from Calculator.Calculator import Calculator
from CSVReader.CSVReader import CSVReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = CSVReader('Tests/Data/UnitTestAddition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CSVReader('Tests/Data/UnitTestSubtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CSVReader('Tests/Data/UnitTestDivision.csv').data
        for row in test_data:
            x = float(row['Value 1'])
            y = float(row['Value 2'])
            z = float(row['Result'])
            self.assertEqual(self.calculator.divide(y, x), round(z, 7))

    def test_multiply_method_calculator(self):
        test_data = CSVReader('Tests/Data/UnitTestMultiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_square_method_calculator(self):
        test_data = CSVReader('Tests/Data/UnitTestSquare.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squared(row['Value 1']), int(row['Result']))

    def test_sqrt_method_calculator(self):
            test_data = CSVReader('Tests/Data/UnitTestSquare Root.csv').data
            for row in test_data:
                x = float(row['Value 1'])
                y = float(row['Result'])
                self.assertEqual(self.calculator.Squared_root(x), round(y, 8))

    if __name__ == '__main__':
        unittest.main()