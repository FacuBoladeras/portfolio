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
        header(),
        rx.text("Experiencia", size= '9', weight="bold", high_contrast=True, font_family=PIXEL_FONT_LARGE),
        projects_page(),
        rx.text("Stack tecnológico", size= '9', weight="bold", high_contrast=True, font_family=PIXEL_FONT_LARGE),
        stack(),
        rx.text("Proyectos GIS", size= '9', weight="bold", high_contrast=True, font_family=PIXEL_FONT_LARGE),
        linkedin_page(),
        rx.text("Proyectos Freelance", size= '9', weight="bold", high_contrast=True, font_family=PIXEL_FONT_LARGE),
        linkedin_page_freelance(),
        footer(),
        spacing="9",
        align_items="center",
        justify_content="center",
        padding=PADDING_SMALL,
        style={
            "background": "linear-gradient(#4b0081, #d86aff, #FFFFFF)",  # Degradado de color
            "width": "100%",  # Asegurarse de que el gradiente cubra todo el ancho
            "height": "100%",  # Asegurarse de que el gradiente cubra toda la altura
        },
    )


app = rx.App()
app.add_page(index, route="/")