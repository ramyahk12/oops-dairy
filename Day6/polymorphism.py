class Payment:
    def pay(self):
        print("Making a payment")


class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay")


class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")

class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")


p = Payment()
gpay = GooglePay()
phonepe = PhonePe()
card = CreditCard()

p.pay()
gpay.pay()
phonepe.pay()
card.pay()