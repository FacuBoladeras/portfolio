import reflex as rx

def header():
    return rx.hstack(
        rx.link("Inicio", href="/"),
        rx.link("Sobre mí", href="/about"),
        rx.link("Proyectos", href="/projects"),
        rx.link("Contacto", href="/contact"),
        spacing=3,  # ✅ Número entero entre 0 y 9
        padding="1em",
        justify_content="center",
        border_bottom="1px solid #eaeaea"
    )