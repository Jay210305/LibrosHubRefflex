import reflex as rx

from ..state import State
from .. import navigation

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.link(
                        rx.heading(
                            "LibrosHub", size="6", weight="bold",
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    align_items="center",
                ),
                rx.input(
                        rx.input.slot(rx.icon("search")),
                        placeholder="Search...",
                        type="search",
                        width="500px",
                        justify="end",
                    ),
                rx.hstack(
                        rx.button(
                            "Sign Up",
                            on_click=rx.redirect(navigation.routes.SIGN_UP),
                            size="3",
                            variant="outline",
                        ),
                        rx.button(                        
                            "Sign in",
                            on_click=rx.redirect(navigation.routes.LOGIN),
                            size="3"
                        ),                        
                        rx.button(
                            "Carrito",
                            on_click=State.handle_navbar_show_onclick,
                            size="3",
                        ),
                        spacing="4",
                        justify="end",
                    ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.link(
                        rx.heading(
                            "LibrosHub", size="6", weight="bold",
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    align_items="center",
                ),
                rx.input(
                        rx.input.slot(rx.icon("search")),
                        placeholder="Search...",
                        type="search",
                        size="2",
                        justify="end",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Carrito", on_click=State.handle_navbar_show_onclick,),
                        rx.menu.separator(),
                        rx.menu.item("Log in", on_click=rx.redirect(navigation.routes.LOGIN)),
                        rx.menu.item("Sign up", on_click=rx.redirect(navigation.routes.SIGN_UP)),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        top="0px",
        z_index="5",
        width="100%",
    )