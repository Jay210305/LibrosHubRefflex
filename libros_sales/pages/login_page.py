import reflex as rx
from ..ui.base import base_page
from .. import navigation

def login_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.card(
                rx.vstack(
                    rx.center(
                        rx.image(
                            src="/logo.jpg",
                            width="2.5em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading(
                            "Sign in to your account",
                            size="6",
                            as_="h2",
                            text_align="center",
                            width="100%",
                        ),
                        direction="column",
                        spacing="5",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Email address",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="user@reflex.dev",
                            type="email",
                            size="3",
                            width="100%",
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Password",
                                size="3",
                                weight="medium",
                            ),
                            rx.link(
                                "Forgot password?",
                                href="#",
                                size="3",
                            ),
                            justify="between",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Enter your password",
                            type="password",
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.button("Sign in", size="3", width="100%"),
                    rx.center(
                        rx.text("New here?", size="3"),
                        rx.link("Sign up", href=navigation.routes.SIGN_UP, size="3"),
                        opacity="0.8",
                        spacing="2",
                        direction="row",
                    ),
                    spacing="6",
                    width="100%",
                ),
                size="5",
                max_width="28em",
                width="100%",
                justify="center",
                align="center"
            ),
            padding_top="6em",
            justify="center",
            align="center"
        )
    )