import reflex as rx
from ..ui.base import base_page

def checkout():
    return base_page(
        rx.hstack(
            rx.vstack(
                rx.heading("Información de Envío", size="8"),
                rx.text("Email"),
                rx.input(
                    type="email",
                ),
                rx.hstack(
                    rx.vstack(
                        rx.text("Nombre"),
                        rx.input(
                        ),
                        align="center",
                    ),
                    rx.vstack(
                        rx.text("Apellido"),
                        rx.input(
                        ),
                        align="center",
                    ),
                    spacing="2",
                    justify="center",
                    align="center",
                ),
                rx.text("Dirección"),
                rx.input(
                ),
                rx.hstack(
                    rx.vstack(
                        rx.text("Ciudad"),
                        rx.input(
                        ),
                        align="center",
                    ),
                    rx.vstack(
                        rx.text("Región/Estado"),
                        rx.input(
                        ),
                        align="center",
                    ),                    
                    spacing="2",
                    justify="center",
                    align="center",                    
                ),
                rx.text("Código postal"),
                rx.input(),
                rx.button(
                    "Continuar a Método de Envío"
                ),
                width="60%",
            ),
            rx.vstack(
                rx.heading("Resumen"),
                rx.text("Total a pagar: "),
                justify="center",
                align="center",
            ),
            padding_top="6em",
            width="100%",
            margin_x="2em"
        )
    )