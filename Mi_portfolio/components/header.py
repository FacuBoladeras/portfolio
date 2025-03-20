import reflex as rx

def header():
    return rx.vstack(
        rx.text(
            "Mi Portfolio - Encabezado",
            font_size="1.5em",
            font_weight="bold",
            text_align="center"
        ),
        rx.box(
            border_top="1px solid #eaeaea",  # ✅ Línea arriba
            border_bottom="1px solid #eaeaea",  # ✅ Línea abajo
            margin="1em 0",  # ✅ Espaciado arriba y abajo de la línea
            width="100%"
        )
    )