"""
OWNER: Jacob
Classes: Staff (base, extends User), Doctor, Nurse, DeskAssistant
Source: Revised Final Class Model. Inheritance: User -> Staff -> {Doctor, Nurse, DeskAssistant}

These classes mostly CALL Appointment methods (Anika) — use her method names
from the stubs even before she's finished; they'll work once she is.
"""
from hospital.users import User


class Staff(User):
    """UML: Staff (no attributes)"""

    def updatePatientHistory(self, patient, history: object) -> None:
        """UML: +updatePatientHistory(object PatientHistory): void
        TODO: UML has no patient param — you need one. Note the fix."""
        raise NotImplementedError

    def updatePatientHealth(self, patient, health: object) -> None:
        """UML: +updatePatientHealth(object PatientHealth): void"""
        raise NotImplementedError

    def createAppt(self, appt_id: int) -> None:
        """UML: +createAppt(int ApptID): void"""
        raise NotImplementedError


class Doctor(Staff):
    """UML: Doctor (no attributes)"""

    def enterPatientVitals(self, patient, vitals: object) -> None:
        """UML: +enterPatientVitals(object vitals)"""
        raise NotImplementedError

    def viewAppts(self) -> None:
        """UML: +viewAppts(): void
        TODO: needs access to a list of appointments — where does it come from?"""
        raise NotImplementedError

    def documentVisit(self, appointment) -> None:
        """UML: +documentVisit(int ApptID): void
        State: CHECKED_IN --Provider Completes Visit--> SERVICES_PROVIDED
        -> should call appointment.completeVisit()"""
        raise NotImplementedError


class Nurse(Staff):
    """UML: Nurse (no attributes)"""

    def enterPatientVitals(self, patient, vitals: object) -> None:
        """UML: +enterPatientVitals(): void
        TODO: Doctor and Nurse both have this — move it up to Staff? Discuss."""
        raise NotImplementedError


class DeskAssistant(Staff):
    """UML: Desk Assistant (no attributes)"""

    def updatePatientPay(self, patient, payment: object) -> None:
        """UML: +updatePatientPay(object payment): void"""
        raise NotImplementedError

    def createAppt(self, appt_id: int) -> None:
        """UML: +createAppt(int ApptID): void (overrides Staff)"""
        raise NotImplementedError

    def rescheduleAppt(self, appointment, new_date) -> None:
        """UML: +rescheduleAppt(int ApptID) -> appointment.rescheduleAppt(...)"""
        raise NotImplementedError

    def checkInPatient(self, appointment) -> None:
        """UML: +checkInPatient(int apptID): void -> appointment.checkIn()"""
        raise NotImplementedError

    def checkOutPatient(self, appointment) -> None:
        """NOT in class model, but state model has 'Check Person Out [UserIsStaff]'.
        -> appointment.checkOut(self)"""
        raise NotImplementedError


if __name__ == "__main__":
    # TODO(Jacob): create a DeskAssistant + Doctor, check a patient in,
    # document the visit, check out.
    pass
