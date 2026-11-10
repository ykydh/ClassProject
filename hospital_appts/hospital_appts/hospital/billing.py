"""
OWNER: Yutaro
Billing branch of the state model:

  Services Provided --[UserIsStaff]-->                   ISSUED
  ISSUED --Patient Pays [PaymentDeclined] / Notify Patient--> ISSUED   (self-loop)
  ISSUED --Patient Pays [PaymentApproved]-->            PAYMENT_RECEIVED
  PAYMENT_RECEIVED -->                                  BILLING_REVIEWED
  BILLING_REVIEWED --Receipt Sent-->                    (User Notified / final)
  ISSUED --Notification Sent-->                         (User Notified)

!! MODEL GAP: there is no Bill class in your Revised Final Class Model, but the
state model has billing states. Either keep this class (and add it to the
class model) or move these methods onto Appointment/Patient. Write down which.
"""
from hospital.states import BillStatus, InvalidTransition


class Bill:
    def __init__(self, appointment, amount: float):
        # TODO: link to appointment; status = ISSUED
        # TODO: guard — only create if appointment is SERVICES_PROVIDED and
        #       issued by staff [UserIsStaff]
        pass

    def pay(self, payment: object, notifier) -> None:
        """Patient Pays.
        [PaymentDeclined] -> stay ISSUED, notifier.sendPaymentDeclined(self)
        [PaymentApproved] -> PAYMENT_RECEIVED
        TODO: decide what makes a payment approved (amount >= balance? a flag?)"""
        raise NotImplementedError

    def review(self, notifier) -> None:
        """PAYMENT_RECEIVED -> BILLING_REVIEWED, then notifier.sendReceipt(self)"""
        raise NotImplementedError

    def getStatus(self) -> BillStatus:
        raise NotImplementedError
