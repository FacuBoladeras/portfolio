import reflex as rx
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.constants.styles import SPACING_MEDIUM, PADDING_MEDIUM

projects = [
    {"text": "Proyecto A", "color": "#FF5733"},
    {"text": "Proyecto B", "color": "#33FF57"},
    {"text": "Proyecto C", "color": "#5733FF"},
]

def projects_page():
    return rx.hstack(
        *[project_card(p["text"], p["color"]) for p in projects],
        spacing=SPACING_MEDIUM,      # ✅ Espaciado centralizado
        padding=PADDING_MEDIUM,      # ✅ Padding centralizado
        align_items="center"
    )
