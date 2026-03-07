class Menu:

    # MAIN MENUS

    @staticmethod
    def public_menu() -> str:
        return "=== PUBLIC MENU ===\n" "1 - Login\n" "0 - Shutdown\n\n"

    @staticmethod
    def user_menu() -> str:
        return "=== USER MENU ===\n" "1 - Change password\n" "0 - Logout\n\n"

    @staticmethod
    def admin_menu() -> str:
        return (
            "=== ADMIN MENU ===\n"
            "1 - Create user\n"
            "2 - List users\n"
            "3 - Update user\n"
            "4 - Delete user\n"
            "0 - Logout\n\n"
        )

    # SUBMENUS

    @staticmethod
    def update_user_menu() -> str:
        return (
            "=== UPDATE MENU ===\n"
            "1 - Update name\n"
            "2 - Update username\n"
            "3 - Update password\n"
            "4 - Update role\n"
            "0 - Cancel\n"
        )

    # SYSTEM MESSAGES

    @staticmethod
    def startup_message() -> str:
        return "The system was started.\n\n"

    @staticmethod
    def shutdown_message() -> str:
        return "Shutting down system...\n"

    @staticmethod
    def admin_seed_message() -> str:
        return (
            "=== SYSTEM FIRST STARTUP ===\n"
            "Admin created automatically:\n"
            "Username: admin\n"
            "Password: admin123\n"
            "Logging in...\n\n"
        )

    @staticmethod
    def logged_in_message() -> str:
        return "Logged in successfully.\n\n"

    @staticmethod
    def logout_message() -> str:
        return "Exiting session...\n\n"

    # ERROR MESSAGES

    @staticmethod
    def show_error(message: str) -> str:
        return f"{message}\n\n"

    @staticmethod
    def password_do_not_match_message() -> str:
        return "Passwords do not match.\n\n"

    @staticmethod
    def is_new_password_same_as_current_message() -> str:
        return "New password cannot be the same as the current password.\n\n"

    # SUCCESS MESSAGES

    @staticmethod
    def user_created_message() -> str:
        return "User successfully created.\n\n"

    @staticmethod
    def name_updated_message() -> str:
        return "Name successfully updated.\n\n"

    @staticmethod
    def password_updated_message() -> str:
        return "Password successfully updated.\n\n"

    @staticmethod
    def role_updated_message() -> str:
        return "Role successfully updated.\n\n"

    @staticmethod
    def user_deleted_message() -> str:
        return "User successfully deleted.\n\n"

    # DATA DISPLAY

    @staticmethod
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

        return "\n".join(formated_list) + "\n"
