class Customer:
    def __init__(self, custID, fName, age, city):
        self.custID = custID
        self.fName = fName
        self.age = age
        self.city = city
        self.c_account = None
        self.s_account = None

    def getCustID(self):
        return self.custID

    def getFirstName(self):
        return self.fName

    def getAge(self):
        return self.age

    def getcity(self):
        return self.city
    
    def getCAccount(self):
        return self.c_account

    def setCAccount(self, c_account):
        self.c_account = c_account

    def getSAccount(self):
        return self.c_account

    def setSAccount(self, s_account):
        self.s_account = s_account

    def __str__(self):
        return f"Customer ID: {self.custID}\nName: {self.fName}\nage: {self.age}\ncity: {str(self.city)}"
