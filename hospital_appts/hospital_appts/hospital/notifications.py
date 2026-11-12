
class Notifications:
    messagesent = None
    def __init__(self):
        self.message = []

    def sendConfirmation(self, appointment: object) -> None:
        print(f"Appoint Confirmation: {appointment.Date}\nStatus: {appointment.Status}")
        self.message.append("Confirmation")

    def sendReminder(self, appointment) -> None:
        print(f"Appoint Reminder: {appointment.Date}\nStatus: {appointment.Status}")
        self.message.append("Reminder")

    def sendCancellation(self, appointment) -> None:
        print(f"Appoint Cancellation: {appointment.Date}")
        self.message.append("Cancellation")

    def sendRescheduleNotice(self, appointment) -> None:
        print(f"Reschedule Note: {appointment.Date}\nStatus: {appointment.Status}")
        self.message.append("Reschedule")

    def sendPaymentDeclined(self, bill) -> None:
        print(f"Payment got declined check the billed amount.\nBill Amount: {bill.BillAmount}")
        self.message.append("Payment Declined")

    def sendReceipt(self, bill) -> None:
        print(f"Receipt has sent\n Bill Amount: {bill.BillAmount}")
        self.message.append("Receipt Sent")
