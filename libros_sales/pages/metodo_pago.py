import reflex as rx
from ..ui.base import base_page
from .. import navigation
from ..state import State
from ..ui.resumen import resumen

def metodo_pago() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.link("Volver al Checkout", href=navigation.routes.CHECKOUT),
            rx.heading("Método de Pago"),
            rx.hstack(
                rx.vstack(
                    rx.text("Dirección de Envío: 123 Calle Principal, Ciudad"),
                    rx.text("Método de Envío: UPS Ground - $5.99"),
                    rx.text("Método de Pago"),
                    rx.hstack(
                        rx.input(
                            placeholder="Número de tarjeta"
                        ),
                        rx.input(
                            placeholder="MM/YY"
                        ),
                        rx.input(
                            placeholder="CVC"
                        )
                    ),
                    rx.text("Dirección de Facturación"),
                    rx.radio(
                            ["La misma que la dirección de envío", "Usar una dirección diferente"],
                            direction="column"
                    ),
                ),
                rx.vstack(
                    resumen(),
                    rx.button(
                        "Finalizar compra",
                        on_click=rx.redirect(navigation.routes.FIN_COMPRA),
                    ),
                ),
            ),            
            padding_top="6em"
        )
    )