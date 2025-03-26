import reflex as rx
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.constants.styles import SPACING_MEDIUM, PADDING_MEDIUM


projects = [
    {
        "color": "#6ea7cf",
        "image": "/ceregeo.png",
        "items": [
            "+4 years",
            "Research",
            "GIS/Python",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/conicet_logo.jpg",
        "items": [
            "+2 years",
            "Research",
            "GIS/Science",            
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/logo-ee.jpg",
        "items": [
            "+3 months",
            "Teaching",
            "Python/GIS",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/deorigen_la_logo.jpg",
        "items": [
            "+1 year",
            "Developed",
            "Python/GIS",
        ]
    },
]

VISIBLE_CARDS = 3
CARD_WIDTH = 400
CARD_SPACING = 16

def projects_page(font_family):
    return rx.vstack(
        rx.hstack(
            # ✅ Iteración directa sobre la lista de diccionarios
            *[
                project_card(p["color"], p["image"], p["items"], font_family=font_family)
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



