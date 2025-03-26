import reflex as rx
from Mi_portfolio.components.header import header
from Mi_portfolio.components.footer import footer
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.pages.projects import projects_page
from Mi_portfolio.pages.linkedin import linkedin_page,linkedin_page_freelance
from Mi_portfolio.pages.stack import stack
from Mi_portfolio.constants.tipografia import PIXEL_FONT_SMALL,PIXEL_FONT_MEDIUM, PIXEL_FONT_LARGE
from Mi_portfolio.constants.styles import PADDING_SMALL, PADDING_MEDIUM, MARGIN_MEDIUM, MAX_WIDTH_MEDIUM


def index():
    return rx.vstack(
        header(title_font_family="Pixelify Sans", title_class_name="title-primary", content_font_family="Tektur", content_class_name="content_header"),
        rx.text("Experiencia", size='9',  weight="bold",   high_contrast=True,   font_family="Pixelify Sans",    class_name="title-secondary" ),        
        projects_page(font_family="Doto"),
        rx.text("Stack tecnológico", size='9', weight="bold", high_contrast=True,font_family="Pixelify Sans", class_name="title-secondary"),
        stack(),
        rx.text("Proyectos GIS", size='9', weight="bold", high_contrast=True,font_family="Pixelify Sans", class_name="title-secondary"),
        linkedin_page(font_family="Pixelify Sans"),
        rx.text("Proyectos Freelance", size='9', weight="bold", high_contrast=True,font_family="Pixelify Sans", class_name="title-secondary"),
        linkedin_page_freelance(font_family="Pixelify Sans"),
        footer(),
        spacing="9",
        align_items="center",
        justify_content="center",
        padding=PADDING_SMALL,
        style={
            "background": "linear-gradient(#240046, #d86aff, #FFFFFF)",  # Degradado de color
            "width": "100%",  # Asegurarse de que el gradiente cubra todo el ancho
            "height": "100%",  # Asegurarse de que el gradiente cubra toda la altura
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