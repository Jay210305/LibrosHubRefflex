import reflex as rx

def resumen() -> rx.Component:
    return rx.box(
        rx.heading("Resumen", size="5"),
        rx.separator(),
        rx.text("Subtotal: "),
        rx.text("Envío: "),
        rx.text("Imp. Est.: "),
        rx.text("Total: ", align="right", as_="div"),
        direction="column",
        width="100%",
        align="center",
        justify="center"                               
    ),