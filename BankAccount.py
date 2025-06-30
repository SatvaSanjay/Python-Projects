class BankAccount:
    def __init__(self, hname, cbalance):
        self.hname = hname
        self.cbalance = cbalance
        print(f"Account holder name : {self.hname}")
        print(f"Current Balance : {self.cbalance}")
    
    def deposit(self, dm):
        print(f"Total balance after deposit : {self.cbalance + dm}")
        self.cbalance = self.cbalance + dm

    def withdraw(self, wm):
        if wm> self.cbalance:
            print("Insufficient Balance !!")
        else:
            print(f"{wm} Has been withdrawn.\nNow the current balance is : {self.cbalance-wm}.")
 



a = BankAccount('vidhi', 2000)
a.deposit(500)
a.withdraw(300)