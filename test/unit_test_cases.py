import Salary_Calculation
import unittest

class UnitTest_Salary(unittest.TestCase):

    def run_test(self):
        salaryCalc = Salary_Calculation.Salary(10000, 10, 5)

        self.assertNotEqual(salaryCalc.calculatePF(), 500, "PASS")
        self.assertTrue(salaryCalc.calculateInhandSalary(), 500, "PASS")
        self.assertFalse(salaryCalc.calculatePF(), 500, "PASS")
        self.assertGreater(salaryCalc.calculatePF(), 500, "PASS")
        self.assertLess(salaryCalc.calculatePF(), 500, "PASS")