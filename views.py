from data import get_users, get_appointments, get_roles

ROW = "{:<4} {:<18} {:<15} {:<15} {:<14} {}"


def view_appointments(username, role):
    users = get_users()
    mine, other = ("patient", "provider") if role == "patient" else ("provider", "patient")
    appts = [a for a in get_appointments() if a[mine] == username]
    print("\nMy Appointments")
    if not appts:
        print("No appointments found.")
        return
    print(ROW.format("ID", "Date/Time", "With", "Type", "Department", "Status"))
    for a in appts:
        print(ROW.format(a["id"], a["date"], users[a[other]]["name"],
                         a["type"], a["department"], a["status"]))


def view_roles():
    users = get_users()
    print("\nRoles")
    for role in get_roles():
        members = [u for u, info in users.items() if info["role"] == role["name"]]
        print(f"- {role['name']}: {', '.join(role['permissions'])} (users: {', '.join(members)})")
