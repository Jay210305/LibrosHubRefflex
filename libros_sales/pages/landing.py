import reflex as rx
from ..ui.sidebar import sidebar_bottom_profile
from ..ui.base import base_page
from rxconfig import config
from ..state import State

books = [
    {"title": "Libro 1", "image": "/images/libro1.jpg", "price": "$10.00"},
    {"title": "Libro 2", "image": "/images/libro2.jpg", "price": "$15.00"},
    {"title": "Libro 3", "image": "/images/libro3.jpg", "price": "$12.00"},
    {"title": "Libro 4", "image": "/images/libro4.jpg", "price": "$20.00"},
    {"title": "Libro 5", "image": "/images/libro5.jpg", "price": "$8.00"},
    {"title": "Libro 6", "image": "/images/libro6.jpg", "price": "$18.00"},
]

def landing_page() -> rx.Component:
    return base_page(
        rx.hstack(
            rx.cond(
                State.show,
                sidebar_bottom_profile(),
            ),
            rx.vstack(
                rx.heading("Bienvenido a LibroHub!", size="9"),
                rx.text("Tienda Virtual de Libros", size="5"),
                rx.grid(
                    rx.foreach(
                        books,
                        lambda book: rx.card(
                            rx.vstack(
                                rx.image(src=book["image"], height="200px"),
                                rx.text(book["title"], font_size="lg"),
                                rx.text(book["price"], font_size="md"),
                                rx.button("Agregar al Carrito", 
                                          on_click=lambda: State.add_to_cart(book["title"])),
                            ),
                            width="100%",
                            padding="4",
                        ),
                    ),
                    columns="3",
                    spacing="4",
                    width="100%",
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                padding_top="6em",
            ),
        ),
    )