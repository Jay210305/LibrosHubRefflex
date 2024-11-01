import reflex as rx

class State(rx.State):
    show : bool = False
    def handle_navbar_show_onclick(self):
        self.show = not(self.show)