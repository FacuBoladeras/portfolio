import reflex as rx
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.constants.styles import SPACING_MEDIUM, PADDING_MEDIUM,PADDING_SMALL
CARD_WIDTH = 400
CARD_SPACING = 16

def projects_page(font_family):
    return rx.container(
        rx.flex(
            *[
                project_card(p["color"], p["image"], p["items"], font_family=font_family)
                for p in projects
            ],
            direction={"base": "column", "md": "row"},
            wrap="wrap",
            spacing=SPACING_MEDIUM,
            align="center",
            justify="center",
            width="100%",
        ),
        center_content=True,
        padding=PADDING_MEDIUM,
    )


projects = [
    {
        "color": "#6ea7cf",
        "image": "/ceregeo.png",
        "items": [
            "+4 years",
            "Research",
            "Python/GIS",
        ]
    },
    {
        "color": "#6ea7cf",
        "image": "/conicet_logo.jpg",
        "items": [
            "+2 years",
            "Research",
            "Python/GIS",            
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
            "Developing",
            "Python/GIS",
        ]
    },
]

VISIBLE_CARDS = 3
CARD_WIDTH = 400
CARD_SPACING = 16

def projects_page(font_family):
    return rx.container(
        rx.flex(
            *[
                project_card(p["color"], p["image"], p["items"], font_family=font_family)
                for p in projects
            ],
            direction={"base": "column", "md": "row"},
            wrap="wrap",
            spacing="2",
            align="center",
            justify="start",  # 👈 Cambiado aquí
            width="100%",
        ),
        center_content=True,
        padding="0px",
        max_width="100%",  # 👈 asegura que aproveche toda la pantalla
    )


