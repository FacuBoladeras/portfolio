import reflex as rx
from Mi_portfolio.constants.styles import PADDING_MEDIUM,PADDING_LARGE,PADDING_EXTRA_LARGE,PADDING_SMALL

CARD_WIDTH = "300px"
CARD_HEIGHT = "300px"
IMAGE_HEIGHT = "120px"  # ✅ Altura fija para la imagen

def project_card(color, image_url, items):
    return rx.box(
        rx.vstack(
            # Imagen
            rx.image(
                src=image_url,
                width="150px",         # Ancho fijo
                height="100px",        # Altura fija
                object_fit="cover",    # Asegúrate de que la imagen llena el área definida
                border_radius="10px 50px",
                border="5px solid #555",
                margin="0 auto",
                padding_top=PADDING_SMALL,
                padding_bottom=PADDING_SMALL,
            ),
            # Hstack con listas
            rx.hstack(
                rx.list(
                    *[
                        rx.hstack(
                            rx.icon("circle_check_big", color="green"),
                            rx.text(item),
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
