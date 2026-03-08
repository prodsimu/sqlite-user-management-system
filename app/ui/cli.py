from app.controllers.app_controller import AppController
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
            self.flash_message = Menu.admin_seed_message()

        while self.running:

            clear_screen()
            self._show_flash()

            print(self._get_current_menu(), end="")
            self._handle_current_flow()

    # FLOWS

    def _handle_public_flow(self) -> None:
        choice = Prompt.get_choice([0, 1])

        match choice:

            case 0:
                self.shutdown_system()

            case 1:
                self._handle_login()

    def _handle_admin_flow(self) -> None:
        choice = Prompt.get_choice([0, 1, 2, 3, 4])

        match choice:

            case 0:
                self._handle_logout()
            case 1:
                self._handle_user_creation()
            case 2:
                self._handle_list_users()
            case 3:
                self._handle_update_flow()
            case 4:
                self._handle_delete_user()

    def _handle_user_flow(self) -> None:
        choice = Prompt.get_choice([0, 1])

        match choice:

            case 0:
                self._handle_logout()

            case 1:
                self._handle_update_password()

    # MAIN LOOP ACTIONS

    def _get_current_menu(self) -> str:
        if not self.controller.has_active_session():
            return Menu.public_menu()
        if self.controller.is_admin():
            return Menu.admin_menu()
        return Menu.user_menu()

    def _handle_current_flow(self) -> None:
        if not self.controller.has_active_session():
            self._handle_public_flow()
        elif self.controller.is_admin():
            self._handle_admin_flow()
        else:
            self._handle_user_flow()

    def _show_flash(self) -> None:
        if self.flash_message:
            print(self.flash_message, end="")
            self.flash_message = None

    # AUTH

    def _handle_login(self) -> None:
        username = Prompt.ask_username()
        password = Prompt.ask_password()

        def action():
            self.controller.login(username, password)
            self.flash_message = Menu.logged_in_message()

        self._execute(action)

    def _handle_logout(self) -> None:
        self.flash_message = Menu.logout_message()
        self.controller.logout()

    # CREATE

    def _handle_user_creation(self) -> None:
        name, username, password = Prompt.ask_user_data_to_creation()

        def action():
            self.controller.create_user(name, username, password)
            self.flash_message = Menu.user_created_message()

        self._execute(action)

    # READ

    def _handle_list_users(self) -> None:
        user_list = self.controller.list_all_users()
        self.flash_message = Menu.show_all_users(user_list)

    # UPDATE

    def _handle_update_name(self) -> None:

        def action():
            user_id = Prompt.ask_user_id()
            self.controller.user_exists(user_id)

            new_name = Prompt.ask_new_name()

            self.controller.update_name(user_id, new_name)
            self.flash_message = Menu.name_updated_message()

        self._execute(action)

    def _handle_update_username(self) -> None:

        def action():
            user_id = Prompt.ask_user_id()
            self.controller.user_exists(user_id)

            new_username = Prompt.ask_new_username()

            self.controller.update_username(user_id, new_username)
            self.flash_message = Menu.username_updated_message()

        self._execute(action)

    def _handle_update_password(self) -> None:

        new_password, confirm_new_password = Prompt.ask_new_password()

        if not self._verify_new_passwords_match(new_password, confirm_new_password):
            self.flash_message = Menu.password_do_not_match_message()
            return

        if self._is_new_password_same_as_current(new_password):
            self.flash_message = Menu.is_new_password_same_as_current_message()
            return

        def action():
            self.controller.update_password(
                self.controller.current_user.id, new_password
            )
            self.flash_message = Menu.password_updated_message()

        self._execute(action)

    def _handle_update_role(self) -> None:
        def action():
            user_id = Prompt.ask_user_id()
            self.controller.user_exists(user_id)

            new_role = Prompt.ask_new_role()

            self.controller.update_role(user_id, new_role)
            self.flash_message = Menu.role_updated_message()

        self._execute(action)

    def _handle_update_flow(self) -> None:
        print(Menu.update_user_menu())

        choice = Prompt.get_choice([0, 1, 2, 3, 4])

        match choice:
            case 0:
                pass
            case 1:
                self._handle_update_name()
            case 2:
                self._handle_update_username()
            case 3:
                self._handle_update_password()
            case 4:
                self._handle_update_role()

    # DELETE

    def _handle_delete_user(self) -> None:
        user_id = Prompt.ask_user_id()

        def action():
            self.controller.delete_user(user_id)
            self.flash_message = Menu.user_deleted_message()

        self._execute(action)

    # HELPER

    def _execute(self, action):
        try:
            action()
        except Exception as e:
            self.flash_message = Menu.show_error(str(e))

    # PASSWORD VERIFICATION

    def _is_new_password_same_as_current(self, new_password: str) -> bool:
        return self.controller.is_new_password_same_as_current(new_password)

    def _verify_new_passwords_match(
        self, new_password: str, confirm_new_password: str
    ) -> bool:
        if new_password != confirm_new_password:
            return False

        return True
