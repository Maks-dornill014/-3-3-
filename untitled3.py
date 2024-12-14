class BankAccount:
    def __init__(self, owner, account_number, balance=0.0):
        
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        
        if amount <= 0:
            print("Сума для поповнення повинна бути більше 0.")
            return
        self.balance += amount
        print(f"Поповнено {amount:.2f}. Новий баланс: {self.balance:.2f}.")

    def withdraw(self, amount):
       
        if amount > self.balance:
            print("Недостатньо коштів на рахунку.")
            return
        if amount <= 0:
            print("Сума для зняття повинна бути більше 0.")
            return
        self.balance -= amount
        print(f"Знято {amount:.2f}. Новий баланс: {self.balance:.2f}.")

    def __str__(self):
       
        return f"Власник: {self.owner}, Номер рахунку: {self.account_number}, Баланс: {self.balance:.2f}"


class Bank:
    def __init__(self):
        
        self.accounts = {}

    def create_account(self, owner, account_number, initial_balance=0.0):
        
        if account_number in self.accounts:
            print("Рахунок з таким номером вже існує.")
            return
        self.accounts[account_number] = BankAccount(owner, account_number, initial_balance)
        print(f"Рахунок для {owner} створено з номером {account_number}.")

    def get_account(self, account_number):
       
        return self.accounts.get(account_number, None)

    def transfer(self, from_account_number, to_account_number, amount):
        
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if not from_account:
            print(f"Рахунок відправника {from_account_number} не знайдено.")
            return
        if not to_account:
            print(f"Рахунок отримувача {to_account_number} не знайдено.")
            return
        if from_account.balance < amount:
            print("Недостатньо коштів для переказу.")
            return
        if amount <= 0:
            print("Сума переказу повинна бути більше 0.")
            return

        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Переказано {amount:.2f} з рахунку {from_account_number} на рахунок {to_account_number}.")

    def show_accounts(self):
        
        if not self.accounts:
            print("У банку немає рахунків.")
        else:
            print("Рахунки у банку:")
            for account in self.accounts.values():
                print(account)



if __name__ == "__main__":
    bank = Bank()

   
    bank.create_account("Олег", "12345", 5000)
    bank.create_account("Анна", "67890", 3000)

    
    bank.show_accounts()

    
    account = bank.get_account("12345")
    if account:
        account.deposit(2000)

   
    if account:
        account.withdraw(1000)

   
    bank.transfer("12345", "67890", 1500)

  
    bank.show_accounts()
