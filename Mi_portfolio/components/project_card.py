import reflex as rx
from Mi_portfolio.constants.styles import PADDING_MEDIUM,PADDING_LARGE,PADDING_EXTRA_LARGE,PADDING_SMALL

CARD_WIDTH = "300px"
CARD_HEIGHT = "300px"
IMAGE_HEIGHT = "120px"  # ✅ Altura fija para la imagen

def project_card(color, image_url, items, font_family=None):
    return rx.box(
        rx.vstack(
            # Imagen
            rx.image(
                src=image_url,
                width="150px",         # Fija un ancho uniforme
                height="100px",        # Fija una altura uniforme
                object_fit="cover",    # Hace que la imagen se recorte o escale para llenar el espacio asignado
                border_radius="0px",   # Sin bordes redondeados (opcional)
                border="4px solid black", # Bordes negros
                box_shadow="0px 4px 6px rgba(0, 0, 0, 0.2)", # Sombra
                margin="0",            # Sin márgenes
                padding="0"            # Sin padding
            ),
            # Hstack con listas
            rx.hstack(
                rx.list(
                    *[
                        rx.hstack(
                            rx.icon("circle_check_big", color="green"),
                            rx.text(item, font_family=font_family, class_name="content", weight="bold"),  # Añade la clase aquí
                        )
                        for item in items
                    ]
                ),
                align="center",  # Cambiado a "align"
            ),
        ),
        # border=f"2px solid {color}",
        border_radius="0px",
        box_shadow="md",
        width="250px",
        padding=PADDING_LARGE,
        height="250px",
        flex_shrink=0,
        overflow="hidden",
        align="center",  # Cambiado a "align"
    )


