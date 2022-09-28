class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self._transactions.append(amount)
        else:
            raise ValueError("please use int for amount")

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, idx):
        return self._transactions[idx]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, acc2):
        return self.balance > acc2.balance

    def __ge__(self, acc2):
        return self.balance >= acc2.balance

    def __lt__(self, acc2):
        return self.balance < acc2.balance

    def __le__(self, acc2):
        return self.balance >= acc2.balance

    def __eq__(self, acc2):
        return self.balance == acc2.balance

    def __ne__(self, acc2):
        return self.balance != acc2.balance

    def __add__(self, other):
        new_owner = self.owner + "&" + other.owner
        new_amount = self.amount + other.amount

        new_acc = Account(new_owner, new_amount)

        [new_acc.add_transaction(t) for t in self]
        [new_acc.add_transaction(t) for t in other]

        return new_acc

acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)




