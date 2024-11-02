import reflex as rx
from ..ui.base import base_page
from .. import navigation
from ..state import State

def envio():
    return base_page(
        rx.vstack(
            rx.link("Volver al Checkout", href=navigation.routes.CHECKOUT),
            rx.heading("Método de Envío"),
            rx.text("Dirección: "),
            rx.badge(State.text, color_scheme="green"),
            rx.radio(
                ["1", "2", "3", "4"],
                on_change=State.set_text,
            ),
            padding_top="6em"
        )
    )