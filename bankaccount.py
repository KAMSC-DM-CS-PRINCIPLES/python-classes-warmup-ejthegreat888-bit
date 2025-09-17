# TODO create class BankAccount

class BankAccount:

    balance = 0

    def __init__(self, balance):
        self.balance = balance

    def deposite(self, n):
        if self.balance < 0:
            return self.balance
        self.balance += n
        return self.balance

    def withdrawl(self, n):
        if n > self.balance:
            return "Insufficient Funds"
        elif n < 0:
            return self.balance
        return self.balance - n

    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    # create BankAccount below this
    pass