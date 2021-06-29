import Salary_Calculation
import unittest

class UnitTest_Salary(unittest.TestCase):

    def test_run(self):
        salaryCalc = Salary_Calculation.Salary(10000, 10, 5)

        self.assertEqual(salaryCalc.calculatePF(), 1000, "PASS")
        self.assertNotEqual(salaryCalc.calculatePF(), 500, "PASS")
        self.assertTrue(salaryCalc.calculatePension() == 500, "PASS")
        self.assertFalse(salaryCalc.calculatePension() == 1000, "PASS")
        self.assertGreater(salaryCalc.calculateInhandSalary(), 5000, "PASS")
        self.assertLess(salaryCalc.calculateInhandSalary(), 10000, "PASS")

if __name__ == '__main__':
    unittest.main()