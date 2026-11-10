"""
OWNER: Aiden
The navigation part of the state diagram (top half):

  [init] --Signs In--> Signed In
  Signed In --Open Appointments--> Appointment Manager Opened
  Appointment Manager Opened --Opens Calendar--> Viewer Opened
  Appointment Manager Opened --Opens Appointment [ApptScheduled]--> (appointment.checkIn)
  Viewer Opened --Choose Day [DayNotFree] / Show Other Days--> Viewer Opened
  Viewer Opened --Choose Day [DayIsFree]--> (Appointment Scheduled)
  Viewer Opened --Cancel Existing Appointment--> (Appointment Cancelled)

Not a class in the class model — it's the controller that drives the state
diagram. Note that as a design decision in your write-up.
"""
from hospital.states import SessionState, InvalidTransition


class Session:
    def __init__(self, user):
        # TODO: hold the User; start in SessionState.SIGNED_OUT
        pass

    def signIn(self, password: str) -> None:
        """SIGNED_OUT -> SIGNED_IN (delegate password check to User.signIn)"""
        raise NotImplementedError

    def openAppointments(self) -> None:
        """SIGNED_IN -> APPT_MANAGER_OPENED"""
        raise NotImplementedError

    def openCalendar(self) -> None:
        """APPT_MANAGER_OPENED -> VIEWER_OPENED"""
        raise NotImplementedError

    def chooseDay(self, date, schedule) -> object:
        """VIEWER_OPENED, guard [DayIsFree]  -> create Appointment (SCHEDULED)
           VIEWER_OPENED, guard [DayNotFree] -> stay, 'Show Other Days'
        TODO: what is `schedule`? A list of existing Appointments works fine."""
        raise NotImplementedError

    def cancelExistingAppointment(self, appointment) -> None:
        """VIEWER_OPENED -> calls appointment.cancelAppt(...)"""
        raise NotImplementedError

    def signOut(self) -> None:
        """any signed-in state -> SIGNED_OUT"""
        raise NotImplementedError
