import reflex as rx
from ..ui.base import base_page
from .. import navigation

def item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )

def checkout():
    return base_page(
        rx.hstack(
            rx.vstack(
                rx.heading("Información de Envío", size="8"),
                rx.separator(),
                rx.hstack(
                    rx.link("volver a Carrito", href=navigation.routes.CARRITO),
                ),
                rx.text("Email"),
                rx.input(
                    type="email",
                    required=True,
                ),
                rx.hstack(
                    rx.vstack(
                        rx.text("Nombre"),
                        rx.input(
                            required=True,
                        ),
                        align="center",
                    ),
                    rx.vstack(
                        rx.text("Apellido"),
                        rx.input(
                            required=True,
                        ),
                        align="center",
                    ),
                    spacing="2",
                    justify="center",
                    align="center",
                ),
                rx.text("Dirección"),
                rx.input(
                    required=True,
                ),
                rx.hstack(
                    rx.vstack(
                        rx.text("Ciudad"),
                        rx.input(
                            required=True,
                        ),
                    ),
                    rx.vstack(
                        rx.text("Región/Estado"),
                        rx.input(
                            required=True,
                        ),
                    ),                    
                    spacing="2",
                    justify="center",
                    align="center",                    
                ),
                rx.text("Código postal"),
                rx.input(
                    required=True,
                ),
                rx.button(
                    "Continuar a Método de Envío",
                    on_click=rx.redirect(navigation.routes.ENVIO),                   
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