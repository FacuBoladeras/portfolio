import reflex as rx

def footer(font_family="Tektur", class_name="content"):
    return rx.vstack(
        rx.text("Email: facuboladeras@gmail.com", font_family="Tektur", class_name="content"),
        rx.text("GitHub: https://github.com/facundo",font_family="Tektur", class_name="content"),
        spacing="2",  # Separación entre líneas internas
        padding="1em",
        align_items="center",
        margin="2em 0 0 0",  # Separación entre footer y contenido anterior
        border_top="4px solid #000000"
    )