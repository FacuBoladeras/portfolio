import reflex as rx

def footer():
    return rx.vstack(
        rx.text("Facundo Boladeras."),
        rx.text("Email: facuboladeras@gmail.com"),
        rx.text("GitHub: https://github.com/facundo"),
        spacing="2",  # Separación entre líneas internas
        padding="1em",
        align_items="center",
        margin="2em 0 0 0",  # Separación entre footer y contenido anterior
        border_top="1px solid #eaeaea"
    )