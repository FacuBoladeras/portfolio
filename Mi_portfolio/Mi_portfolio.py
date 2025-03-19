import reflex as rx
from Mi_portfolio.components.header import header
from Mi_portfolio.components.footer import footer

def index():
    return rx.vstack(
        header(),
        rx.box(
            rx.text("¡Hola! Soy [Tu Nombre]", font_size="2em", font_weight="bold"),
            rx.text("Desarrollador Front-end | Python Developer"),
            padding="2em",
            text_align="center"
        ),
        footer(),
        spacing=3,
        align_items="center",
        justify_content="center",
    )

app = rx.App()
app.add_page(index, route="/")