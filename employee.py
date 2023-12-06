"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Contract:
    def __init__(self, number, rate):
        self.number = number
        self.rate = rate
    def get_pay(self):
        return self.number * self.rate
    def __str__(self):
        return f'contract of {self.number} hours at {self.rate}/hour'

class CommissionContract(Contract):
    def __init__(self, number, rate):
        super().__init__(number, rate)
    def __str__(self):
        return f'receives a commission for {self.number} contract(s) at {self.rate}/contract'

class Salary:
    def __init__(self, salary):
        self.salary = salary
    def get_pay(self):
        return self.salary
    def __str__(self):
        return f'monthly salary of {self.salary}'

class BonusCommission(Salary):
    def __init__(self, amount):
        super().__init__(amount)
    def __str__(self):
        return f'receives a bonus commission of {self.salary}'

class Employee:
    def __init__(self, name, ContractOrSalary, BonusCommissionOrCommissionContract=None):
        self.name = name
        self.ContractOrSalary = ContractOrSalary
        self.BonusCommissionOrCommissionContract = BonusCommissionOrCommissionContract

    def get_pay(self):
        if self.BonusCommissionOrCommissionContract:
            return self.ContractOrSalary.get_pay() + self.BonusCommissionOrCommissionContract.get_pay()
        else:
            return self.ContractOrSalary.get_pay()

    def __str__(self):
        if self.BonusCommissionOrCommissionContract:
            return f'{self.name} works on a {self.ContractOrSalary} and {self.BonusCommissionOrCommissionContract}.  Their total pay is {self.get_pay()}.'
        else:
            return f'{self.name} works on a {self.ContractOrSalary}.  Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Salary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Salary(3000), CommissionContract(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract(150, 25), CommissionContract(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Salary(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract(120, 30), BonusCommission(600))

print(str(jan))