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
                width="150px",
                height="100px",
                object_fit="cover",
                border_radius="10px",
                border="4px solid black",
                box_shadow="0px 4px 6px rgba(0, 0, 0, 0.2)",
                margin="0",
                padding="0",
            ),
            # Lista
            rx.hstack(
                rx.list(
                    *[
                        rx.hstack(
                            rx.image(src="check-mark2.png", width="40px", height="40px"),
                            rx.text(item, font_family=font_family, class_name="content", weight="bold"),
                        )
                        for item in items
                    ]
                ),
            ),
            spacing="3",
            align_items="center",  # Alinea al centro dentro del vstack
            justify_content="center",  # Centra verticalmente
        ),
        border_radius="0px",
        width="250px",
        padding=PADDING_SMALL,
        height="280px",
        flex_shrink=0,
        overflow="hidden",
    )



