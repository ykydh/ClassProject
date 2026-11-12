def get_users():
    return {
        "jsmith": {"password": "pass", "role": "patient", "name": "John Smith"},
        "mjones": {"password": "pass", "role": "patient", "name": "Mary Jones"},
        "drlee": {"password": "pass", "role": "staff", "name": "Dr. Sarah Lee"},
        "admin": {"password": "pass", "role": "admin", "name": "System Admin"},
    }


def get_appointments():
    return [
        {"id": 101, "date": "2026-11-18 09:00", "patient": "jsmith", "provider": "drlee",
         "type": "Annual Checkup", "department": "Primary Care", "status": "SCHEDULED"},
        {"id": 102, "date": "2026-11-25 14:30", "patient": "jsmith", "provider": "drlee",
         "type": "Follow-up", "department": "Primary Care", "status": "CONFIRMED"},
        {"id": 103, "date": "2026-11-18 10:00", "patient": "mjones", "provider": "drlee",
         "type": "Consultation", "department": "Primary Care", "status": "SCHEDULED"},
    ]


def get_roles():
    return [
        {"name": "patient", "permissions": ["view_own_appointments", "view_own_profile"]},
        {"name": "staff", "permissions": ["view_own_schedule", "view_appointment_details"]},
        {"name": "admin", "permissions": ["view_roles", "manage_users", "view_reports"]},
    ]
