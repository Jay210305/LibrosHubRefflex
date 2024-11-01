import reflex as rx

class State(rx.State):
    show : bool = False
    login_s_h : bool = True
    def handle_navbar_show_onclick(self):
        self.show = not(self.show)

    def login_nav_search_hide(self):
        self.login_s_h = not(self.show)
