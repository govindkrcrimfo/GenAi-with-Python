# Parent class
class Payment:
    def pay(self):
        print("Payment successful")


# -----------------------------
# 1. Single Inheritance
# -----------------------------
class CreditCard(Payment):
    def card_payment(self):
        print("Paid using Credit Card")


# -----------------------------
# 2. Multilevel Inheritance
# -----------------------------
class UPI(Payment):
    def upi_payment(self):
        print("Paid using UPI")


class Razorpay(UPI):
    def razorpay_payment(self):
        print("Paid using Razorpay")


# -----------------------------
# 3. Multiple Inheritance
# -----------------------------
class OnlinePayment:
    def online(self):
        print("Online payment")


class RazorpayUPI(UPI, OnlinePayment):
    def payment(self):
        print("Razorpay UPI payment")


# -----------------------------
# Testing
# -----------------------------

# Single Inheritance
credit_card = CreditCard()
credit_card.pay()
credit_card.card_payment()


# Multilevel Inheritance
razorpay = Razorpay()
razorpay.pay()
razorpay.upi_payment()
razorpay.razorpay_payment()


# Multiple Inheritance
razorpay_upi = RazorpayUPI()
razorpay_upi.pay()
razorpay_upi.upi_payment()
razorpay_upi.online()
razorpay_upi.payment()