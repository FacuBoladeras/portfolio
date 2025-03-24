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
                width="40%",
                height="auto",
                object_fit="contain",
                border_top_radius="0px",
                margin="0 auto",
                padding_top=PADDING_SMALL,
                padding_bottom=PADDING_SMALL
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

                
            ),
        ),
        border=f"2px solid {color}",
        border_radius="0px",
        box_shadow="md",
        width="300px",
        padding=PADDING_EXTRA_LARGE,
        height="300px",
        flex_shrink=0,
        overflow="hidden",
    )