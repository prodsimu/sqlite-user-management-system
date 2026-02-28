from app.controllers.app_controller import AppController
from app.domain.user_role import UserRole


class CLI:
    def __init__(self, controller: AppController):
        self.controller = controller
        self.running: bool = True

    def start_app(self) -> None:
        self.controller.bootstrap()
        self.main_loop()

    def shutdown_system(self) -> None:
        self.running = False

    def main_loop(self) -> None:
        while self.running:
            if not self.controller.current_session:
                pass

            elif self.controller.current_user.role == UserRole.ADMIN.value:
                pass

            else:
                pass
