import reflex as rx

from ..ui.sidebar import sidebar_bottom_profile
from ..ui.base import base_page
from rxconfig import config
from ..state import State

def landing_page() -> rx.Component:
    return base_page(
        rx.hstack(
            rx.cond(
                State.show,
                sidebar_bottom_profile(),
            ),
            
            rx.vstack(
                rx.heading("Welcome to Reflex!", size="9"),
                rx.text(
                    "Get started by editing ",
                    rx.code(f"{config.app_name}/{config.app_name}.py"),
                    size="5",
                ),
                rx.link(
                    rx.button("Check out our docs!"),
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    is_external=True,
                ),      
                spacing="5",
                # justify="center",
                min_height="85vh",
                padding_top="6em",
            ),
        ),
    )