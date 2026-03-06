from app.controllers.app_controller import AppController
from app.domain.user import User
from app.ui.menus import Menu
from app.ui.prompts import Prompt
from app.utils.terminal import clear_screen


class CLI:
    def __init__(self, controller: AppController):
        self.controller = controller
        self.running: bool = True
        self.flash_message: str | None = None

    def start_app(self) -> None:
        self.controller.bootstrap()
        self.main_loop()

    def shutdown_system(self) -> None:
        self.running = False
        clear_screen()
        print(Menu.shutdown_message(), end="")

    # MAIN LOOP

    def main_loop(self) -> None:

        if self.controller.was_admin_seeded():
            self.flash_message = Menu.admin_seed_menu()

        while self.running:

            if not self.controller.has_active_session():
                menu = Menu.public_menu()
            elif self.controller.is_admin():
                menu = Menu.admin_menu()
            else:
                menu = Menu.user_menu()

            clear_screen()

            if self.flash_message:
                print(self.flash_message, end="")
                self.flash_message = None

            print(menu, end="")

            if not self.controller.has_active_session():
                self.handle_public_flow()

            elif self.controller.is_admin():
                self.handle_admin_flow()

            else:
                self.handle_user_flow()

    # FLOWS

    def handle_public_flow(self) -> None:
        choice = Prompt.get_choice([0, 1])

        match choice:

            case 0:
                self.shutdown_system()

            case 1:
                self._handle_login()

    def handle_admin_flow(self) -> None:
        choice = Prompt.get_choice([0, 1, 2, 3, 4])

        match choice:

            case 0:
                self._handle_logout()
            case 1:
                self._handle_user_creation()
            case 2:
                self._handle_list_users()
            case 3:
                pass
            case 4:
                self._handle_delete_user()

    def handle_user_flow(self) -> None:
        choice = Prompt.get_choice([0, 1])

        match choice:

            case 0:
                self._handle_logout()

            case 1:
                self.change_own_password(self.controller.current_user)

    # USER ACTIONS

    def change_own_password(self, current_user: User) -> None:
        new_password, confirm_new_password = Prompt.ask_new_password()

        if new_password != confirm_new_password:
            self.flash_message = Menu.password_dont_match_message()
            return

        try:
            self.controller.update_password(current_user.id, new_password)
            self.flash_message = Menu.password_updated_message()
        except Exception as e:
            self.flash_message = Menu.show_error(str(e))

    def _handle_login(self) -> None:
        username = Prompt.ask_username()
        password = Prompt.ask_password()

        try:
            self.controller.login(username, password)
            self.flash_message = Menu.successfully_logged_in()
        except Exception as e:
            self.flash_message = Menu.show_error(str(e))

    def _handle_logout(self) -> None:
        self.flash_message = Menu.logout_message()
        self.controller.logout()

    # ADMIN ACTIONS

    def _handle_user_creation(self) -> None:
        name, username, password = Prompt.ask_user_data_to_creation()

        try:
            self.controller.create_user(name, username, password)
            self.flash_message = Menu.user_successfully_created_message()
        except Exception as e:
            self.flash_message = Menu.show_error(str(e))

    def _handle_list_users(self) -> None:
        user_list = self.controller.list_all_users()
        self.flash_message = Menu.show_all_users(user_list)

    def _handle_delete_user(self) -> None:
        user_id = Prompt.ask_user_id()

        try:
            self.controller.delete_user(user_id)
            self.flash_message = Menu.user_successfully_deleted_message()
        except Exception as e:
            self.flash_message = Menu.show_error(str(e))
