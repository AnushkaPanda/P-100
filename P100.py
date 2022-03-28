class atm (object):
    def __init__ (self, cashWithdrawl,balanceEnquiry,personName):
        self.cashWithdrawl = cashWithdrawl
        self.balanceEnquiry = balanceEnquiry
        self.personName = personName
        
    def cashwithdrawed (self):
        print("Thank you! cash withdrawed")

    def balanceEnquired(self):
        print("balance checked")

Anushka = atm(10000, 200000, "Anushka")
print(Anushka.cashwithdrawed())
print(Anushka.balanceEnquired())

