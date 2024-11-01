import reflex as rx

from .pages.landing import landing_page
from . import navigation, pages

def index() -> rx.Component:
    return landing_page(),

app = rx.App()
app.add_page(index)
app.add_page(pages.login_page, route=navigation.routes.LOGIN)
app.add_page(pages.signup, route=navigation.routes.SIGN_UP)
