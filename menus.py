from views import view_appointments, view_roles


def run_menu(title, option_label, action):
    while True:
        print(f"\n--- {title} ---")
        print(f"1) {option_label}")
        print("2) Sign out")
        choice = input("> ").strip()
        if choice == "1":
            action()
        elif choice == "2":
            print("Signed out.")
            return
        else:
            print("Invalid option.")


def appointments_menu(username, role, title):
    run_menu(title, "View my appointments", lambda: view_appointments(username, role))


def admin_menu(username):
    run_menu("Admin Menu", "View roles", view_roles)
