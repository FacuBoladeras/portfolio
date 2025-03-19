import reflex as rx

def footer():
    return rx.box(
        rx.text("© 2025 [Tu Nombre]. Todos los derechos reservados.", font_size="0.9em"),
        rx.hstack(
            rx.link("GitHub", href="https://github.com/tu-usuario", is_external=True),
            rx.link("LinkedIn", href="https://www.linkedin.com/in/tu-usuario", is_external=True),
            spacing=3,
            justify_content="center"
        ),
        padding="1em",
        border_top="1px solid #eaeaea",
        text_align="center",
        margin_top="2em"
    )