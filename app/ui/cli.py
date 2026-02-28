from app.controllers.app_controller import AppController


class CLI:
    def __init__(self, controller: AppController):
        self.controller = controller
