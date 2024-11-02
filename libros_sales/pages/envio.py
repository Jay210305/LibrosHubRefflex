import reflex as rx
from ..ui.base import base_page
from .. import navigation
from ..state import State
from ..ui.resumen import resumen

def envio():
    return base_page(
        rx.box(
            rx.vstack(
                rx.link("Volver al Checkout", href=navigation.routes.CHECKOUT, margin_bottom="1rem"),
                rx.hstack(
                    rx.box(
                        rx.vstack(
                            rx.heading("Método de Envío", size="8", text_align="center"),
                            rx.text("Dirección:", margin_bottom="1rem"),
                            rx.vstack(
                                rx.badge("Método elegido " + State.text),
                                rx.radio(
                                    ["UPS Ground - $5.00", "UPS 2nd Day Air - $12.50", "UPS Next Day Air - $20.00"],
                                    on_change=State.set_text,
                                    direction="column"
                                ),
                            ),
                        ),
                        padding="2rem",
                        background_color="var(--light-color)",
                        border="1px solid var(--accent-color)",
                        border_radius="10px",
                        box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
                        max_width="400px",
                        text_align="center",
                    ),
                    rx.box(
                        rx.vstack(
                            resumen(),
                            rx.button(
                                "Continuar a Método de Pago",
                                on_click=rx.redirect(navigation.routes.METODO_PAGO),
                            ),
                        ),
                        padding="2rem",
                        background_color="var(--light-color)",
                        border="1px solid var(--accent-color)",
                        border_radius="10px",
                        box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
                        max_width="400px",
                        text_align="center",
                    ),
                    spacing="2rem",
                    align="center",
                    justify="center",
                ),
                padding_top="2rem",
                spacing="2rem",
                align="center",
                justify="center",
            ),
            display="flex",
            align_items="center",
            justify_content="center",
            width="100vw",
            height="100vh",
        )
    )