import reflex as rx
from ..ui.base import base_page

def login_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Log-in"),
            padding_top="6em",
        )
    )