import timeit
from logs import WriteLog
SETUP_CODE = '''from Salary_Calculation import Salary'''


class Benchmark:
    def benchmark(self):


        TEST_CODE = '''
salary = Salary(10000, 10, 5)
salary.calculatePF()
salary.calculatePension()
salary.calculateInhandSalary()'''


        repetitions = timeit.repeat(setup=SETUP_CODE,
                                    stmt=TEST_CODE,
                                    repeat=1,
                                    number=1)

        print("In-Hand salary calculation time is: " + format(min(repetitions)))
        WriteLog.logger.info("In-Hand salary calculation time is: " + format(min(repetitions)))