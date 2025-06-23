class BankAccount:
    def __init__(self, acc_no, holder_name, balance):
        self.__acc_no = acc_no
        self.__holder_name = holder_name
        self.__balance = balance

    def get_account_info(self):
        return self.__acc_no, self.__holder_name, self.__balance

    def set_account_info(self, acc_no=None, holder_name=None, balance=None):
        if acc_no: self.__acc_no = acc_no
        if holder_name: self.__holder_name = holder_name
        if balance is not None: self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

# Demonstration
account = BankAccount("123456", "John Doe", 1000)
account.deposit(500)
account.withdraw(300)
print("Account Info:", account.get_account_info())
