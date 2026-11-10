"""
OWNER: Aiden (integration) — fill in during the last ~15 minutes.
Run:  python main.py

Each scenario = one path through the Revised Final State Model.
Uncomment / write them as the modules they depend on are finished.
"""
# from hospital.users import Patient, Administrator
# from hospital.staff import Doctor, Nurse, DeskAssistant
# from hospital.appointment import Appointment
# from hospital.session import Session
# from hospital.notifications import Notifications
# from hospital.billing import Bill
# from hospital.states import InvalidTransition


def scenario_happy_path():
    # TODO: Patient signs in -> opens appointments -> opens calendar ->
    #       chooses free day (SCHEDULED, confirmation sent) ->
    #       desk checks in -> doctor documents visit (SERVICES_PROVIDED) ->
    #       bill issued -> payment approved -> billing reviewed (receipt sent)
    pass


def scenario_day_not_free():
    # TODO: choose a day that's taken -> stays in VIEWER_OPENED, "show other days"
    pass


def scenario_cancel():
    # TODO: SCHEDULED -> cancel -> CANCELLED, cancellation notification sent
    pass


def scenario_no_show():
    # TODO: SCHEDULED, time passes, not checked in -> NO_SHOW
    pass


def scenario_payment_declined():
    # TODO: bill ISSUED -> declined (stays ISSUED, patient notified) -> approved
    pass


def scenario_invalid_transitions():
    # TODO: try things the diagram forbids and confirm InvalidTransition is raised:
    #   - cancel a CHECKED_OUT appointment
    #   - patient (not staff) tries to check someone out  [UserIsStaff]
    #   - check in a CANCELLED appointment                [ApptScheduled]
    pass


if __name__ == "__main__":
    for s in (scenario_happy_path, scenario_day_not_free, scenario_cancel,
              scenario_no_show, scenario_payment_declined,
              scenario_invalid_transitions):
        print(f"--- {s.__name__} ---")
        s()
