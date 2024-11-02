import reflex as rx
from ..ui.base import base_page
from ..ui.resumen import resumen
from ..ui.product_carrito import product_carrito
from .. import navigation

def carrito() -> rx.Component:
    return base_page(
        rx.box(
            rx.vstack(
                rx.heading("Tu carrito", size='8', text_align="center", margin_bottom="1rem"),
                rx.hstack(
                    rx.vstack(
                        product_carrito(),
                        padding_top="6em",
                        justify="center",
                        align="center",
                    ),
                    rx.vstack(
                        resumen(),
                        rx.button("Checkout", on_click=rx.redirect(navigation.routes.CHECKOUT)),
                        rx.button("Cancelar", on_click=rx.redirect(navigation.routes.HOME_ROUTE)),
                    ),
                    spacing="2rem",
                    align="center",
                    justify="center",
                ),
                justify="center",
                align="center",
                spacing="2",
                padding_top="2rem"
            ),
            display="flex",
            align_items="center",
            justify_content="center",
            width="100vw",
            height="100vh",
        )
    )