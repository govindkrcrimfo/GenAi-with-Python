from abc import ABC ,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    #concrete method in abstract class
    def paymentSuccess(self):
        print("Payment done successfully !!")

class CreditCard(Payment):
    def pay(self):
        print("Payment logic using CreditCard !!")

class UPI(Payment):
    def pay(self):
        print("Payment logic using UPI !!")


creditCart=CreditCard()
creditCart.pay()
creditCart.paymentSuccess()

upi=UPI()
upi.pay()
upi.paymentSuccess()
