class Menu:

    @staticmethod
    def admin_seed_menu() -> None:
        print("=== SYSTEM FIRST STARTUP ===")
        print("Admin created automatically:")
        print("Username: admin")
        print("Password: admin123")
        print("Logging in...\n")

    @staticmethod
    def public_menu() -> None:
        print("=== PUBLIC MENU ===")
        print("1 - Login")
        print("0 - Shutdown")

    @staticmethod
    def admin_menu() -> None:
        print("=== ADMIN MENU ===")
        print("1 - Create user")
        print("2 - List users")
        print("3 - Update user")
        print("4 - Delete user")
        print("0 - Logout")

    @staticmethod
    def user_menu() -> None:
        print("=== USER MENU ===")
        print("1 - Change password")
        print("0 - Logout")

    @staticmethod
    def show_error(message: str) -> None:
        print(message)