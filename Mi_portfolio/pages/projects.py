import reflex as rx
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.constants.styles import SPACING_MEDIUM, PADDING_MEDIUM


projects = [
    {
        "color": "#6ea7cf",
        "image": "/ceregeo.png",
        "items": [
            "Estudios de territorio",
            "Tomate",
            "Mozzarella",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/conicet_logo.jpg",
        "items": [
            "Pasta",
            "Albahaca",
            "Piñones",
            "Ajo",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/logo-ee.jpg",
        "items": [
            "Tortilla",
            "Pollo",
            "Aguacate",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/deorigen_la_logo.jpg",
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
    return rx.vstack(
        rx.hstack(
            # ✅ Iteración directa sobre la lista de diccionarios
            *[
                project_card(p["color"], p["image"], p["items"])
                for p in projects
            ],
            spacing=SPACING_MEDIUM,
            align_items="center",
            justify_content="flex-start",
        ),
        padding=PADDING_MEDIUM,
        align_items="center",
        justify_content="center",
        width="100%",
    )


