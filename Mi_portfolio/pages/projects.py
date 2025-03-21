import reflex as rx
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.constants.styles import SPACING_MEDIUM, PADDING_MEDIUM


projects = [
    {
        "color": "#6ea7cf",
        "image": "/uader.png",
        "items": [
            "Harina",
            "Tomate",
            "Mozzarella",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/uader.png",
        "items": [
            "Pasta",
            "Albahaca",
            "Piñones",
            "Ajo",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/uader.png",
        "items": [
            "Lechuga",
            "Pollo",
            "Parmesano",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/uader.png",
        "items": [
            "Tortilla",
            "Pollo",
            "Aguacate",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/uader.png",
        "items": [
            "Banana",
            "Yogur",
            "Miel",
        ]
    },
]

VISIBLE_CARDS = 3
CARD_WIDTH = 300
CARD_SPACING = 16

def projects_page():
    visible_width = f"{(CARD_WIDTH + CARD_SPACING) * VISIBLE_CARDS - CARD_SPACING}px"

    return rx.vstack(
        rx.box(
            rx.scroll_area(
                rx.hstack(
                    # ✅ Iteración correcta sobre la lista de diccionarios
                    *[
                        project_card(p["color"], p["image"], p["items"])
                        for p in projects
                    ],
                    spacing=SPACING_MEDIUM,
                    align_items="center",
                    justify_content="flex-start",
                ),
                type="always",
                # overflow_x="scroll",
                width=visible_width,
                style={
                    "paddingBottom": "24px",
                    "scrollbarWidth": "thin",
                    "scrollbarColor": "#999 #f0f0f0",
                },
            ),
            padding_bottom=SPACING_MEDIUM,
            border="1px solid black",
            border_radius="16px"

        ),
        padding=PADDING_MEDIUM,
        align_items="center",
        justify_content="center",
        width="100%",
    )
