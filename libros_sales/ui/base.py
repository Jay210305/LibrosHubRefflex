import reflex as rx

from .navbar import navbar

def base_page(child: rx.Component) -> rx.Component:
    return rx.vstack(
        navbar(),
        child,
        rx.color_mode.button(position="bottom-right"),
        rx.logo(),
        padding="2em",
        justify="center",
        align="center",
    )