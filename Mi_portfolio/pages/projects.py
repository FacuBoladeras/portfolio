import reflex as rx
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.constants.styles import SPACING_MEDIUM, PADDING_MEDIUM

projects = [
    {
        "text": "Pizza Margarita\n\nIngredientes:\n- Harina\n- Tomate\n- Mozzarella\n- Albahaca fresca\n- Aceite de oliva",
        "color": "#FF5733"
    },
    {
        "text": "Pasta al Pesto\n\nIngredientes:\n- Pasta\n- Albahaca\n- Piñones\n- Ajo\n- Aceite de oliva\n- Queso parmesano",
        "color": "#33FF57"
    },
    {
        "text": "Ensalada César\n\nIngredientes:\n- Lechuga romana\n- Crutones\n- Pollo\n- Salsa César\n- Parmesano",
        "color": "#5733FF"
    },
    {
        "text": "Tacos de Pollo\n\nIngredientes:\n- Tortillas\n- Pollo\n- Aguacate\n- Cebolla\n- Limón\n- Cilantro fresco",
        "color": "#FFC300"
    },
    {
        "text": "Batido de Frutas\n\nIngredientes:\n- Banana\n- Fresas\n- Yogur natural\n- Miel\n- Leche de almendras",
        "color": "#DAF7A6"
    },
    {
        "text": "Brownies de Chocolate\n\nIngredientes:\n- Chocolate\n- Mantequilla\n- Huevos\n- Harina\n- Azúcar\n- Nueces picadas",
        "color": "#C70039"
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
                    *[project_card(p["text"], p["color"]) for p in projects],
                    spacing=SPACING_MEDIUM,
                    align_items="center",
                    justify_content="flex-start",
                ),
                type="always",  # ✅ Barra horizontal siempre visible
                # overflow_x="scroll",
                width=visible_width,
                style={
                    "paddingBottom": "24px",
                    "scrollbarWidth": "thin",
                    "scrollbarColor": "#999 #f0f0f0",
                },
            ),
            padding_bottom=SPACING_MEDIUM,
        ),
        padding=PADDING_MEDIUM,
        align_items="center",
        justify_content="center",
        width="100%",
    )

