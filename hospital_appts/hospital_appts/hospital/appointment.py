"""
OWNER: Anika
Class: Appointment  — the heart of the state model.
UML: -ApptID: int, +Date: int, +Status: string, +Type: string

Transitions to implement (from Revised Final State Model):
  (created)              --Choose Day [DayIsFree]-->            SCHEDULED      / Notification Sent
  SCHEDULED              --Reschedule-->                        (back to Viewer, new date) / notice
  SCHEDULED              --Cancel-->                            CANCELLED      / Cancellation Notification Sent
  SCHEDULED              --Appt Time Passed [NotCheckedIn]-->   NO_SHOW
  SCHEDULED              --Opens Appointment [ApptScheduled]--> CHECKED_IN
  CHECKED_IN             --Provider Completes Visit-->          SERVICES_PROVIDED
  SERVICES_PROVIDED      --[UserIsStaff]-->                     Bill Issued (billing.py, Yutaro)
  SERVICES_PROVIDED      --Check Person Out [UserIsStaff]-->    CHECKED_OUT

Any event not listed from the current state -> raise InvalidTransition.
"""
from hospital.states import AppointmentStatus, InvalidTransition


class Appointment:
    def __init__(self, appt_id: int, date, appt_type: str, patient=None):
        # TODO: -ApptID (private), Date, Type, Status = SCHEDULED
        # NOTE: UML says Date: int — consider datetime; flag as a model revision.
        # TODO: who is notified? keep a reference to the Patient.
        pass

    # ---- class-model operations ----
    def updateAppt(self, appt_id: int) -> None:
        """UML: +updateAppt(int ApptID)
        TODO: what does 'update' change that reschedule doesn't? Decide."""
        raise NotImplementedError

    def cancelAppt(self, appt_id: int) -> None:
        """UML: +cancelAppt(int ApptID)
        State: SCHEDULED --Cancel--> CANCELLED / Cancellation Notification Sent"""
        raise NotImplementedError

    def rescheduleAppt(self, new_date) -> None:
        """UML: +rescheduleAppt(DateTime newDate): void
        State: SCHEDULED --Reschedule--> SCHEDULED (new date) / reschedule notice"""
        raise NotImplementedError

    def checkIn(self) -> None:
        """UML: +checkIn(): void
        State: SCHEDULED --[ApptScheduled]--> CHECKED_IN"""
        raise NotImplementedError

    # ---- operations the STATE model needs but the CLASS model lacks ----
    # (good material for the "model gaps" discussion)
    def markNoShow(self, now) -> None:
        """SCHEDULED --Appointment Time Passed [NotCheckedIn]--> NO_SHOW"""
        raise NotImplementedError

    def completeVisit(self) -> None:
        """CHECKED_IN --Provider Completes Visit--> SERVICES_PROVIDED
        (Doctor.documentVisit should call this — Jacob)"""
        raise NotImplementedError

    def checkOut(self, user) -> None:
        """SERVICES_PROVIDED --Check Person Out [UserIsStaff]--> CHECKED_OUT"""
        raise NotImplementedError

    def getStatus(self) -> AppointmentStatus:
        raise NotImplementedError


if __name__ == "__main__":
    # TODO(Anika): walk one appointment through happy path + one invalid
    # transition (e.g. cancel after CHECKED_OUT) and confirm it raises.
    pass
