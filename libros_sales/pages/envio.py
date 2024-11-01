import reflex as rx
from ..ui.base import base_page
from .. import navigation
from ..state import State
from ..ui.resumen import resumen

def envio():
    return base_page(
        rx.vstack(
            rx.link("Volver al Checkout", href=navigation.routes.CHECKOUT),
            rx.heading("Método de Envío"),
            rx.hstack(
                rx.vstack(                    
                    rx.text("Dirección: "),
                    rx.vstack(
                        rx.badge("Método elegido "+State.text),
                        rx.radio(
                            ["UPS Ground - $5.00", "UPS 2nd Day Air - $12.50", "UPS Next Day Air - $20.00"],
                            on_change=State.set_text,
                            direction="column"
                        ),
                    ),
                ),
                rx.vstack(
                    resumen(),
                    rx.button(
                        "Continuar a Método de Pago",
                        on_click=rx.redirect(navigation.routes.METODO_PAGO),
                    ),
                ),                
            ),
            padding_top="6em"
        )
    )