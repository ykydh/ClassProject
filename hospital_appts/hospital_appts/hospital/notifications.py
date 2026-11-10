"""
OWNER: Yutaro
Class: Notifications  — produces the "User Notified" state in the diagram.
For this activity, "sending" can just print and append to a log list
(so tests can check what was sent).
"""


class Notifications:
    def __init__(self):
        # TODO: a list to record sent messages
        pass

    def sendConfirmation(self, appointment) -> None:
        """UML: +sendConfirmation(a appointment): void
        State: Appointment Scheduled --Notification Sent--> User Notified"""
        raise NotImplementedError

    def sendReminder(self, appointment) -> None:
        """UML: +sendReminder(a appointment): void"""
        raise NotImplementedError

    def sendCancellation(self, appointment) -> None:
        """UML: +sendCancellation(a Appointment): void
        State: Appointment Cancelled --/ Cancellation Notification Sent--> User Notified"""
        raise NotImplementedError

    def sendRescheduleNotice(self, appointment) -> None:
        """UML: +sendRescheduleNotice(a Appointment): void"""
        raise NotImplementedError

    def sendPaymentDeclined(self, bill) -> None:
        """NOT in class model — state model has Bill Issued --[PaymentDeclined] / Notify Patient."""
        raise NotImplementedError

    def sendReceipt(self, bill) -> None:
        """NOT in class model — state model has Billing Reviewed --Receipt Sent--> User Notified."""
        raise NotImplementedError
