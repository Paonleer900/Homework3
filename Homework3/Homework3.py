class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Enter the amount to be added: "))
        self._balance += amount
        print(f"New balance: {self._balance}")

    def _kill(self):
        self._balance = 0
        print("Balance is zeroed out")

    def __jackpot(self):
        self._balance *= 10
        print(f"Jackpot! New balance: {self._balance}")

    def transfer_balance(self, other):
        self._balance += other._balance
        print(f"Your new balance: {self._balance}")

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return Calculator(self.value / other.value)
        else:
            return "Error: Division by zero!!"

    def __str__(self):
        return str(self.value)

client1 = Bank("Bekbolot", 3000)
client2 = Bank("Rustan", 1000)

client1.moneyX()
client1._kill()
client1._Bank__jackpot()
client1.transfer_balance(client2)

calc1 = Calculator(10)
calc2 = Calculator(20)

result_add = calc1 + calc2
result_sub = calc1 - calc2
result_mul = calc1 * calc2
result_div = calc1 / calc2

print(result_add)  # 30
print(result_sub)  # -10
print(result_mul)  # 200
print(result_div)  # 0.5
