class Dad:
    def __init__(self, amount):
        self.amount = amount
 
    def dadWallet(self):
        print(f"Wallet amount of Dad: {self.amount}")
 
    def emptyPocket(self):
        self.amount = 0
        print("Dad's pocket is now empty.")
 
class Son(Dad):
    def __init__(self, sonWallet, amount):
        super().__init__(amount)  
        self.sonWallet = sonWallet
 
    def theft(self):
        self.sonWallet += self.amount
        print(f"Son wallet after theft: {self.sonWallet}")
 
    def theftAmount(self):
        print(f"The Amount Stolen: {self.sonWallet}")
dada = Dad(10000)
dada.dadWallet()
s1 = Son(0, 10000)
s1.theft()
dada.emptyPocket()
dada.dadWallet()

#SAME USING __STR__()METHOD 
class Book:
    def __init__(self,title):
        self.title=title
    def __str__(self):
        return f"Your Book is {self.title}"
book1=Book("the great gatsby")
print(book1)


#OUTPUT
#Wallet amount of Dad: 10000
#Son wallet after theft: 10000
#Dad's pocket is now empty.
#Wallet amount of Dad: 0
#Your Book is the great gatsby
