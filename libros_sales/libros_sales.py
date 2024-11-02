import reflex as rx

from .pages.landing import landing_page
from . import navigation, pages

def index() -> rx.Component:
    return landing_page(),

app = rx.App()
app.add_page(index)
app.add_page(pages.login_page, route=navigation.routes.LOGIN)
app.add_page(pages.signup, route=navigation.routes.SIGN_UP)
app.add_page(pages.carrito, route=navigation.routes.CARRITO)
app.add_page(pages.checkout, route=navigation.routes.CHECKOUT)
app.add_page(pages.envio, route=navigation.routes.ENVIO)
app.add_page(pages.metodo_pago, route=navigation.routes.METODO_PAGO)
app.add_page(pages.fin_compra, route=navigation.routes.FIN_COMPRA)
