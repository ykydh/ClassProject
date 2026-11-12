from data import get_users


def login(expected_role):
    users = get_users()
    for _ in range(3):
        username = input("Username: ").strip()
        password = input("Password: ")
        user = users.get(username)
        if user and user["password"] == password and user["role"] == expected_role:
            print(f"Welcome, {user['name']}!")
            return username
        print("Invalid login.")
    return None
