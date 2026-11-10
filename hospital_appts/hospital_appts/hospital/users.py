"""
OWNER: Aiden
Classes: User (base), Patient, Administrator
Source: Revised Final Class Model.  Staff subclasses live in staff.py (Jacob).

UML visibility -> Python convention:
  +public  -> name
  #protected -> _name
  -private -> __name
"""


class User:
    """UML: User  |  #ID: int, -Password: string"""

    def __init__(self, user_id: int, password: str):
        # TODO: store #ID and -Password (consider hashing — CS security!)
        # TODO: track signed-in status? (needed by session.py)
        pass

    def signIn(self, password: str) -> None:
        """UML: +signIn(string pass): void
        State model: [initial] --Signs In--> Signed In
        TODO: check password; raise InvalidTransition (or return False) if wrong."""
        raise NotImplementedError

    def signOut(self) -> None:
        """UML: +signOut(): void
        State model: Appointment Scheduled --Signs Out--> [final]"""
        raise NotImplementedError

    def changePassword(self, password: str) -> None:
        """UML: +changePassword(string pass): void"""
        raise NotImplementedError

    def isStaff(self) -> bool:
        """Needed for guard [UserIsStaff] in the state model.
        TODO: decide — isinstance check vs. role attribute. Not in class model;
        note it as an addition."""
        raise NotImplementedError


class Patient(User):
    """UML: Patient  |  #Payment, #History, #Health: object;
    #Phone, #Insurance, #EmergencyContact: string"""

    def __init__(self, user_id: int, password: str, phone: str = "",
                 insurance: str = "", emergency_contact: str = ""):
        super().__init__(user_id, password)
        # TODO: store all protected attributes (_payment, _history, _health, ...)
        pass

    def updatePay(self, payment: object) -> None:
        """UML: +updatePay(object payment): void"""
        raise NotImplementedError

    def createAppt(self, appt_id: int) -> None:
        """UML: +createAppt(int ApptID): void
        TODO: probably needs a date + type too; build an Appointment
        (from appointment.py) — coordinate with Anika."""
        raise NotImplementedError

    def updateContactInfo(self, phone: str) -> None:
        """UML: +updateContactInfo(string phone): void"""
        raise NotImplementedError

    def updateEmergencyContact(self, contact: str) -> None:
        """UML: +updateEmergencyContact(string contact): void"""
        raise NotImplementedError


class Administrator(User):
    """UML: Administrator (no attributes)"""

    def manageProviders(self) -> None:
        """UML: +manageProviders(): void"""
        raise NotImplementedError

    def manageDepartments(self) -> None:
        """UML: +manageDepartments(): void  (uses Department, Yutaro)"""
        raise NotImplementedError

    def manageUsers(self) -> None:
        """UML: +manageUsers(): void"""
        raise NotImplementedError

    def manageApptTypes(self) -> None:
        """UML: +mamangeApptTypes(): void   (typo fixed in code)"""
        raise NotImplementedError

    def viewReports(self) -> None:
        """UML: +viewReports(): void"""
        raise NotImplementedError


if __name__ == "__main__":
    # TODO(Aiden): quick self-test — create a Patient, sign in, sign out.
    pass
