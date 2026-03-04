import os

from app.controllers.app_controller import AppController
from app.ui.menus import Menu
from app.ui.prompts import Prompt


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
        self._clear_screen()
        print(Menu.shutdown_message(), end="")

    # MAIN LOOP

    def main_loop(self) -> None:

        while self.running:

            if not self.controller.has_active_session():
                menu = Menu.public_menu()
            elif self.controller.is_admin():
                menu = Menu.admin_menu()
            else:
                menu = Menu.user_menu()

            self._clear_screen()

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
                pass
            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

    def handle_user_flow(self) -> None:
        choice = Prompt.get_choice([0, 1])

        match choice:

            case 0:
                self._handle_logout()

            case 1:
                pass

    # UTIL

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

    def _clear_screen(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
