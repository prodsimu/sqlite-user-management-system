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
    def logout_message() -> str:
        return "Exiting session...\n"

    @staticmethod
    def successfully_logged_in() -> str:
        return "Logged in successfully\n"

    @staticmethod
    def startup_message() -> str:
        return "The system was started\n"

    @staticmethod
    def password_do_not_match_message() -> str:
        return "Passwords do not match\n"

    @staticmethod
    def password_updated_message() -> str:
        return "Password updated successfully\n"

    @staticmethod
    def user_successfully_created_message() -> str:
        return "New user successfully created\n"

    @staticmethod
    def user_successfully_deleted_message() -> str:
        return "User successfully deleted\n"

    def show_all_users(user_list: list) -> str:
        formated_list = []

        for user in user_list:
            formated_user = "".join(
                f"ID ------- {user.id}\n"
                f"Name ----- {user.name}\n"
                f"Username - {user.username}\n"
                f"Role ----- {user.role}\n"
            )
            formated_list.append(formated_user)

        return "\n".join(formated_list)
