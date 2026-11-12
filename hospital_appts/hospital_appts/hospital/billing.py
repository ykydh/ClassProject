from hospital.states import BillStatus, AppointmentStatus
import appointment
import notifications

class Bill:
    status = None
    BillAmount = None
    Balance = None
    def __init__(self, appointment: object, amount: float):
        #appointment has to be type hospital.AppointmentStatus
        if appointment.getStatus() == AppointmentStatus.SERVICES_PROVIDED:
            self.status = BillStatus.ISSUED
            self.BillAmount = amount
            self.Balance = self.BillAmount
        else:
            raise ValueError("Service has not provided yet")
        

    def pay(self, payment: object, notifier) -> None:
        if payment.PaymentAmount >= self.BillAmount:
            self.Balance = payment.PaymentAmount - self.BillAmount 
            self.status = BillStatus.PAYMENT_RECEIVED
            if self.Balance > 0:
                print(f"Refunded Amount:{self.Balance}")
        else:
            notifier.sendPaymentDeclined(self)

    def review(self, notifier: object) -> None:
        print(f"Bill Status: {self.status}")
        print(f"Bill Amount: {self.BillAmount}")
        print(f"Balance: {self.Balance}")
        self.status = BillStatus.BILLING_REVIEWED
        notifier.sendReceipt(self)
        

    def getStatus(self) -> BillStatus:
        print(f"Bill Status: {self.status}")
        return self.status

class Payment:
    PaymentAmount = None
    def __init__(self,appointment,ammount):
        if appointment.getStatus() == AppointmentStatus.SERVICES_PROVIDED:
            self.PaymentAmount = ammount
        