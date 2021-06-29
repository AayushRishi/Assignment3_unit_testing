from logs import WriteLog

class Salary:
    def __init__(self, total_salary, pf_deduct, pension_deduct):
        self.total_salary = total_salary
        self.pf_deduct = pf_deduct
        self.pension_deduct = pension_deduct
        self.pf = 0
        self.pension = 0
        self.inhand_salary = 0

    def calculatePF(self):
        if self.pf_deduct <= 0:
            WriteLog.logger.warning("PF deduction percentage must be greater than 0.")
        else:
            self.pf = self.total_salary * self.pf_deduct/100
            WriteLog.logger.info("Total PF deducted is: " + str(self.pf))
            print("Total PF deducted is: " + str(self.pf))
            return self.pf

    def calculatePension(self):
        if self.pension_deduct <= 0:
            WriteLog.logger.warning("Pension deduction percentage must be greater than 0.")
        else:
            self.pension = self.total_salary * self.pension_deduct/100
            WriteLog.logger.info("Total Pension deducted is: " + str(self.pension))
            print("Total Pension deducted is: " + str(self.pension))
            return self.pension

    def calculateInhandSalary(self):
        try:
            self.inhand_salary = self.total_salary - (self.pf + self.pension)
            WriteLog.logger.info("Total salary was: " + str(self.total_salary))
            print("Total salary was: " + str(self.total_salary))
            WriteLog.logger.info("In-Hand salary is: " + str(self.inhand_salary))
            print("In-Hand salary is: " + str(self.inhand_salary))
            return self.inhand_salary
        except:
            WriteLog.logger.error("Error in calculating In-Hand salary !!")