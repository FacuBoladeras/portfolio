import reflex as rx
from Mi_portfolio.components.header import header
from Mi_portfolio.components.footer import footer
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.pages.projects import projects_page
from Mi_portfolio.pages.linkedin import linkedin_page

from Mi_portfolio.constants.styles import PADDING_SMALL, PADDING_MEDIUM, MARGIN_MEDIUM, MAX_WIDTH_MEDIUM


def index():
    return rx.vstack(
        header(),
        rx.text("Experiencia", size= '8', color= "indigo",weight="bold",high_contrast=True),
        projects_page(),
        rx.text("Proyectos", size= '8', color= "indigo",weight="bold",high_contrast=True),
        linkedin_page(),
        footer(),
        spacing="9",
        align_items="center",
        justify_content="center",
        padding=PADDING_SMALL
    )


app = rx.App()
app.add_page(index, route="/")