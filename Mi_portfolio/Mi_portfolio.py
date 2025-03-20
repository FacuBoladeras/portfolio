import reflex as rx
from Mi_portfolio.components.header import header
from Mi_portfolio.components.footer import footer
from Mi_portfolio.components.project_card import project_card
from Mi_portfolio.pages.projects import projects_page

def index():
    return rx.vstack(
        header(),
        projects_page(),
        footer(),
        spacing="2",
        align_items="center",
        justify_content="center",
        padding="2em"
    )


app = rx.App()
app.add_page(index, route="/")