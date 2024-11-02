import reflex as rx
from ..ui.base import base_page
from .. import navigation
from ..state import State
from ..ui.resumen import resumen

def fin_compra() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Compra finalizada con éxito"),
            resumen(),
            rx.button(
                "Volver al inicio",
                on_click=rx.redirect(navigation.routes.HOME_ROUTE)
            ),
            padding_top="6em"
        ),        
    )