import reflex as rx
from ..ui.base import base_page
from .. import navigation
from ..ui.resumen import resumen

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
        rx.center(
            rx.hstack(
                # Información de Envío
                rx.box(
                    rx.heading("Información de Envío", size="8"),
                    rx.separator(),
                    rx.hstack(
                        rx.link("Volver a Carrito", href=navigation.routes.CARRITO),
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
                        width="100%",
                        margin_top="1em",
                    ),
                    width="60%",
                    padding="2em",
                    bg=rx.color("gray", 1),
                    border_radius="md",
                ),
                # Resumen
                rx.box(
                    resumen(),
                    width="35%",
                    padding="2em",
                    bg=rx.color("black", 2),
                    border_radius="md",
                    margin_left="2em",
                ),
                spacing="2em",
            ),
            justify="center",
            padding_y="4em",
            width="80%",
        )
    )