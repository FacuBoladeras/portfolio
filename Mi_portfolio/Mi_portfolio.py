import reflex as rx
from Mi_portfolio.components.header import header
from Mi_portfolio.components.footer import footer
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.pages.projects import projects_page
from Mi_portfolio.pages.linkedin import linkedin_page,linkedin_page_freelance
from Mi_portfolio.pages.stack import grid_page_with_icons_vhstack
from Mi_portfolio.constants.tipografia import PIXEL_FONT_SMALL,PIXEL_FONT_MEDIUM, PIXEL_FONT_LARGE
from Mi_portfolio.constants.styles import PADDING_SMALL, PADDING_MEDIUM, MARGIN_MEDIUM, MAX_WIDTH_MEDIUM


def index():
    return rx.container(
        rx.vstack(
            header(title_font_family="Pixelify Sans", title_class_name="title-primary", content_font_family="Tektur", content_class_name="content_header"),
            rx.text("Experience", size='9', weight="bold", high_contrast=True, font_family="Pixelify Sans", class_name="title-secondary", padding="0px"),        
            projects_page(font_family="Doto"),
            rx.text("Technology stack", size='9', weight="bold", high_contrast=True, font_family="Pixelify Sans", class_name="title-secondary"),
            grid_page_with_icons_vhstack(),
            rx.text("GIS projects and skills", size='9', weight="bold", high_contrast=True, font_family="Pixelify Sans", class_name="title-secondary"),
            linkedin_page(font_family="Pixelify Sans"),
            rx.text("Freelance Projects", size='9', weight="bold", high_contrast=True, font_family="Pixelify Sans", class_name="title-secondary"),
            linkedin_page_freelance(font_family="Pixelify Sans"),
            footer(font_family="Pixelify Sans", class_name="content"),
            spacing="9",
            align_items="center",
            justify_content="center",
            padding=PADDING_SMALL,
            width="100%",
        ),
        max_width="100%",
        padding="0",
        center_content=True,
        style={
            "background-image": "linear-gradient(to bottom, transparent 60%, black 100%), url('/background.png')",
            "background-size": "cover, 100%",  # 👈 primero para gradiente, segundo para imagen
            "background-position": "center, top center",
            "background-repeat": "no-repeat, no-repeat",
            "background-color": "black",  # fondo negro de respaldo
            "width": "100%",
            "min_height": "100vh",
        },
    )


app = rx.App(
    stylesheets=[
        'https://fonts.googleapis.com/css2?family=Tektur:wght@400..900&display=swap',
        'https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&display=swap',
        'https://fonts.googleapis.com/css2?family=Doto:wght@600&display=swap',
        "/styles.css",        
    ]
)

app.add_page(index, route="/")