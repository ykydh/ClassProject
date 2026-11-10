"""
SHARED CONTRACT — owned by the whole team.
Agree on these names in the first 5 minutes, then DON'T change them without
telling everyone (other files import them).

Source: "Revised Final State Model" diagram (10/29 doc).
"""
from enum import Enum


class SessionState(Enum):
    """UI/navigation states from the top of the diagram (owner: Aiden, session.py)."""
    SIGNED_OUT = "Signed Out"            # initial / final pseudo-state
    SIGNED_IN = "Signed In"
    APPT_MANAGER_OPENED = "Appointment Manager Opened"
    VIEWER_OPENED = "Viewer Opened"      # calendar view


class AppointmentStatus(Enum):
    """Appointment lifecycle states (owner: Anika, appointment.py)."""
    SCHEDULED = "Appointment Scheduled"
    CANCELLED = "Appointment Cancelled"
    NO_SHOW = "No Show"
    CHECKED_IN = "Checked In"
    SERVICES_PROVIDED = "Services Provided"
    CHECKED_OUT = "Checked Out"
    # TODO(team): diagram has "User Notified" as a state. Decide: is it a real
    # appointment status, or just the result of Notifications.send*()?


class BillStatus(Enum):
    """Billing branch of the diagram (owner: Yutaro, billing.py)."""
    ISSUED = "Bill Issued"
    PAYMENT_RECEIVED = "Payment Received"
    BILLING_REVIEWED = "Billing Reviewed"


class InvalidTransition(Exception):
    """Raise this when an event isn't allowed from the current state,
    or a guard condition fails. Everyone uses the same exception."""
