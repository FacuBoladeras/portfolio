import reflex as rx
from Mi_portfolio.constants.styles import PADDING_MEDIUM, MARGIN_MEDIUM, MAX_WIDTH_MEDIUM

def project_card(text, color):
    return rx.box(
        rx.text(
            text,
            font_size="1.2em",
            font_weight="bold",
            overflow="hidden",
            text_overflow="ellipsis",
            white_space="normal"
        ),
        
        padding=PADDING_MEDIUM,      # ✅ Usa valor centralizado
        border=f"2px solid {color}",
        border_radius="8px",
        box_shadow="md",
        margin=MARGIN_MEDIUM,        # ✅ Usa valor centralizado
        width="100%",
        max_width=MAX_WIDTH_MEDIUM   # ✅ Usa valor centralizado
    )
