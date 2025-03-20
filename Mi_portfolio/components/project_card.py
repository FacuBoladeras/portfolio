import reflex as rx
from Mi_portfolio.constants.styles import PADDING_MEDIUM

CARD_WIDTH = "300px"
CARD_HEIGHT = "200px"

def project_card(text, color):
    return rx.box(
        rx.scroll_area(
            rx.text(
                text,
                font_size="1em",
                font_weight="bold",
                white_space="normal",  
            ),
            height="100%",
            overflow_x="hidden", 
            overflow_y="auto",   
            type="auto",         
            padding=PADDING_MEDIUM,     
        ),
        border=f"2px solid {color}",
        border_radius="8px",
        box_shadow="md",
        width=CARD_WIDTH,
        height=CARD_HEIGHT,
        flex_shrink=0,
        overflow="hidden",
    )
