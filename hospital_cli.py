from auth import login
from menus import appointments_menu, admin_menu


def main():
    try:
        while True:
            print("\n=== Hospital Outpatient System ===")
            print("1) Login as Patient")
            print("2) Login as Staff")
            print("3) Login as Admin")
            print("0) Exit")
            choice = input("> ").strip()
            if choice == "1":
                username = login("patient")
                if username:
                    appointments_menu(username, "patient", "Patient Menu")
            elif choice == "2":
                username = login("staff")
                if username:
                    appointments_menu(username, "staff", "Staff Menu")
            elif choice == "3":
                username = login("admin")
                if username:
                    admin_menu(username)
            elif choice == "0":
                print("Goodbye.")
                return
            else:
                print("Invalid option.")
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye.")


if __name__ == "__main__":
    main()
