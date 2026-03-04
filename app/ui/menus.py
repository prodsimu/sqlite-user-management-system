class Menu:

    @staticmethod
    def admin_seed_menu() -> str:
        return (
            "=== SYSTEM FIRST STARTUP ===\n"
            "Admin created automatically:\n"
            "Username: admin\n"
            "Password: admin123\n"
            "Logging in...\n"
        )

    @staticmethod
    def public_menu() -> str:
        return "=== PUBLIC MENU ===\n" "1 - Login\n" "0 - Shutdown\n"

    @staticmethod
    def admin_menu() -> str:
        return (
            "=== ADMIN MENU ===\n"
            "1 - Create user\n"
            "2 - List users\n"
            "3 - Update user\n"
            "4 - Delete user\n"
            "0 - Logout\n"
        )

    @staticmethod
    def user_menu() -> str:
        return "=== USER MENU ===\n" "1 - Change password\n" "0 - Logout\n"

    @staticmethod
    def show_error(message: str) -> str:
        return f"{message}\n"

    @staticmethod
    def shutdown_message() -> str:
        return "Shutting down system...\n"

    @staticmethod
    def successfully_logged_in() -> str:
        return "logged in successfully"
