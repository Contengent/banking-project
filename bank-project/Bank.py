from CAccount import CAccount
from SAccount import SAccount
from Customer import Customer

class Bank:
    def __init__(self):
        self.c_accounts = []  # 1st list (array) to store objects of CAccount and SAccount classes
        self.s_accounts = []  # 1st list (array) to store objects of SAccount class
        self.customers = []   # 2nd list (array) to store objects of Customer class

    def read_data(self):
        # Read CAccounts.txt file
        with open("CAccounts.txt", "r") as file:
            for line in file:
                acc_data = line.strip().split(";")
                acc_no = int(acc_data[0])
                acc_type = acc_data[1]
                balance = float(acc_data[2])
                c_account = CAccount(acc_no, acc_type, balance)
                self.c_accounts.append(c_account)

        # Read SAccounts.txt file
        with open("SAccounts.txt", "r") as file:
            for line in file:
                acc_data = line.strip().split(";")
                acc_no = int(acc_data[0])
                acc_type = acc_data[1]
                balance = float(acc_data[2])
                max_amt = float(acc_data[3]) if len(acc_data) > 4 else 0.0
                s_account = SAccount(acc_no, acc_type, balance, max_amt)
                self.s_accounts.append(s_account)

        # Read Customers.txt file
        with open("Customers.txt", "r") as file:
            for line in file:
                cust_data = line.strip().split(";")
                cust_id = int(cust_data[0])
                fname = cust_data[1]
                age = cust_data[2]
                city = cust_data[3]
                customer = Customer(cust_id, fname, age, city)
                self.customers.append(customer)

                # Assign CAccount and SAccount to Customer
                if cust_id < len(self.c_accounts):
                    customer.set_c_account(self.c_accounts[cust_id])
                if cust_id < len(self.s_accounts):
                    customer.set_s_account(self.s_accounts[cust_id])




    def display_c_accounts(self):
        # Iteration to display objects of CAccount class
        for ca in self.c_accounts:
            print(ca)

    def display_s_accounts(self):
        # Iteration to display objects of SAccount class
        for sa in self.s_accounts:
            print(sa)

    def display_c_account_details(self, Customer):
        for customer in self.customers:
            c_account = customer.getCAccount()
            if c_account is not None:
                print(f"Customer ID: {customer.getCustID()}")
                print(f"Account Number: {c_account.getAccNo()}")
                print(f"Account Type: {c_account.getAccType()}")
                print(f"Balance: {c_account.getBal()}")
                print(f"Minimum Balance: {c_account.getMinAmt()}")
                print()

    def display_s_account_details(self, Customer):
        for customer in self.customers:
            s_account = customer.getSAccount()
            if s_account is not None:
                print(f"Customer ID: {customer.getCustID()}")
                print(f"Account Number: {s_account.getAccNo()}")
                print(f"Account Type: {s_account.getAccType()}")
                print(f"Balance: {s_account.getBal()}")
                print(f"Minimum Balance: {s_account.getMinAmt()}")
                print(f"Maximum Amount: {s_account.getMaxAmt()}")
                print()

    def perform_invalid_transactions(self):
        # Performing invalid transactions on CAccount objects
        for ca in self.c_accounts:
            ca.deposit(-100)  # Invalid deposit
            ca.withdraw(10000)  # Invalid withdrawal

        # Performing invalid transactions on SAccount objects
        for sa in self.s_accounts:
            sa.deposit(-100)  # Invalid deposit
            sa.withdraw(10000)  # Invalid withdrawal

    def perform_valid_transactions(self):
        # Performing valid transactions on CAccount objects
        for ca in self.c_accounts:
            ca.deposit(100)  # Valid deposit
            ca.withdraw(50)  # Valid withdrawal

        # Performing valid transactions on SAccount objects
        for sa in self.s_accounts:
            sa.deposit(100)  # Valid deposit
            sa.withdraw(50)  # Valid withdrawal

    def generate_banking_receipts(self):
        # Inserting details of CAccount objects into BankingReceipt.txt file
        with open('BankingReceipt.txt', 'w') as file:
            file.write("Checking Account Transactions:\n")
            for ca in self.c_accounts:
                file.write(str(ca) + "\n")

        # Inserting details of SAccount objects into BankingReceipt.txt file
        with open('BankingReceipt.txt', 'a') as file:
            file.write("Saving Account Transactions:\n")
            for sa in self.s_accounts:
                file.write(str(sa) + "\n")

    def run_bank_operations(self):
        self.read_data()
        self.display_c_accounts()
        self.display_s_accounts()

        # Display details of checking and saving accounts for a specific customer
        customer_index = 0  # Specify the index of the customer
        customer = self.customers[customer_index]
        self.display_c_account_details(customer)
        self.display_s_account_details(customer)

        self.perform_invalid_transactions()
        self.perform_valid_transactions()
        self.generate_banking_receipts()


def main():
    bank = Bank()  # Create an instance of the Bank class
    bank.run_bank_operations()  # Call the run_bank_operations() method


if __name__ == "__main__":
    main()

