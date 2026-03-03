from app.controllers.app_controller import AppController
from app.domain.user_role import UserRole
from app.ui.menus import Menu
from app.ui.prompts import Prompt


class CLI:
    def __init__(self, controller: AppController):
        self.controller = controller
        self.running: bool = True

    def start_app(self) -> None:
        self.controller.bootstrap()
        self.main_loop()

    def shutdown_system(self) -> None:
        self.running = False

    # MAIN LOOP

    def main_loop(self) -> None:

        if self.controller.was_admin_seeded():
            Menu.admin_seed_menu()

        while self.running:

            if not self.controller.has_active_session():
                self.handle_public_flow()

            elif self.controller.is_admin():
                Menu.admin_menu()
                break

            else:
                Menu.user_menu()
                break

    # UTIL

    def _handle_login(self) -> None:
        username = Prompt.ask_username()
        password = Prompt.ask_password()

        try:
            self.controller.login(username, password)
        except Exception as e:
            Menu.show_error(e)
