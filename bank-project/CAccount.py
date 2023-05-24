class CAccount:
    bsbNo = 1246

    def __init__(self, accNo, accType, bal, minAmt=50.00):
        self.accNo = accNo
        self.accType = accType
        self.bal = bal
        self.minAmt = minAmt

    def getAccNo(self):
        return self.accNo

    def getAccType(self):
        return self.accType
    
    def getBal(self):
        return self.bal
    
    def getMinAmt(self):
        return self.minAmt

    # 1. Start
    def deposit(self, amount):
        ## 2. Store deposit amount (input) // done in main program to make use of the parameter

        if (amount < self.minAmt):              ## 3. If the deposit amount is less than the minimum amount
            print("==================================")
            print("Deposit Error: The amount deposited must be the same, or greater then the minimum deposit amount.") # 3.4 Display error message (output)
            print("Account: %s" % self.accNo)   # 3.1 Display account number (output)
            print("Deposit: $%s" % amount)      # 3.2 Display deposit amount (output)
            print("Balance: $%s" % self.minAmt) # 3.3 Display minimum amount (output)
            pass                                # 3.5 Go to step 5

        else:                                   # 4. Else
            self.bal += amount                  # 4.1 Add the deposit amount to the balance (input)

            print("==================================")
            print("$%s Has sucessfully been deposited into the account:%s!" % (amount, self.accNo)) # 4.5 Display successful deposit transaction message (output)
            print("Account: %s" % self.accNo)   # 4.2 Display account number (output)
            print("Deposit: $%s" % amount)      # 4.3 Display deposit amount (output)
            print("Balance: $%s" % self.bal)    # 4.4 Display minimum amount (output)
            pass                                # 4.6 Go to step 5
        pass                                    ## 5. End
    
    
    # 1. Start
    def withdraw(self, amount):
        # 2. Store withdrawal amount (input) // done in main program to make use of the parameter

        if (amount > self.bal):                 # 3. If the withdrawal amount is greater than the balance
            print("==================================")
            print("WithdrawlError: Cannot withdraw more money then in balance.") # 3.4. Display error message (output)
            print("Account: %s" % self.accNo)   # 3.1 Display account number (output)
            print("Withdrawn: %s" % amount) # 3.2 Display withdrawal amount (output)
            print("Balance: $%s" % self.bal)    # 3.3 Display the current balance (output)
            pass                                # 3.5 Go to step 5
        
        else: # 4. Else    
            self.bal -= amount                  # 4.1 Subtract withdrawal amount from the balance (input)
            print("==================================")
            print("$%s Has sucessfully been withdrawn into the account:%s!" % (amount, self.accNo)) # 4.5 Display successful withdrawal transaction message (output)
            print("Account: %s" % self.accNo)   # 4.2 Display account number (output)
            print("Withdraw: %s" % amount) # 4.3 Display withdrawal amount (output)
            print("Balance: $%s" % self.bal)    # 4.4 Display the closing balance (output)
            pass                                # 4.6 Go to step 5

        pass # 5. End

    def __str__(self):
        return f"accNo: {self.accNo}, accType: {self.accType}, bal: {self.bal}, minAmt: {self.minAmt}, branchNo: {CAccount.bsbNo}"