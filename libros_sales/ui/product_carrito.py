import reflex as rx
from ..state import State

def product_carrito():
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.image(
                    src="/logo.jpg",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                ),
                rx.heading("Nombre del Libro"),
            ),            
            rx.hstack(
                rx.text("$Price"),
                rx.separator(),
                rx.cond(
                    State.count_product >= 1,
                    rx.button(
                        "Decrement",
                        on_click=State.decrement_product,
                    ),
                    rx.button(
                        "Decrement",
                        on_click=State.decrement_product,
                        disabled=True,
                    )
                ),
                rx.text(State.count_product),
                rx.button(
                    "Increment",
                    on_click=State.increment_product,
                ),
            )
        )        
    )