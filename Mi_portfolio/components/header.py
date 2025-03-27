import reflex as rx
from Mi_portfolio.constants.styles import PADDING_SMALL, PADDING_MEDIUM, MARGIN_MEDIUM, MAX_WIDTH_MEDIUM


from Mi_portfolio.constants.styles import PADDING_SMALL, PADDING_MEDIUM
import reflex as rx

def header(
    title_font_family="Tektur",
    title_class_name="title-primary",
    content_font_family="Roboto",
    content_class_name="content"
):
    return rx.container(
        rx.vstack(
            # Encabezado principal
            rx.text(
                "My GIS Portfolio",
                font_weight="bold",
                text_align="center",
                font_family=title_font_family,
                class_name=title_class_name,
                font_size={"base": "2xl", "md": "4xl"},
            ),

            # Línea divisoria
            rx.box(
                border_top="1px solid #eaeaea",
                border_bottom="1px solid #eaeaea",
                margin="1em 0",
                width="100%",
            ),

            # Contenido principal
            rx.flex(
                # Texto a la izquierda
                rx.box(
                    rx.text(
                        "Hello my name is Facundo Boladeras, I'm a Biology graduate from the Universidad Autónoma de Entre Ríos, "
                        "currently pursuing a PhD through a CONICET scholarship.\n\n"
                        "I specialize in Geographic Information Systems (GIS) with strong experience in technologies "
                        "like Python and Google Earth Engine, combining skills in data science and geoprocessing.",
                        font_family=content_font_family,
                        class_name=content_class_name,
                        font_size={"base": "sm", "md": "lg"},
                        text_align="justify",
                    ),
                    width="100%",
                    padding={"base": PADDING_SMALL, "md": PADDING_MEDIUM},
                ),

                # Avatar y redes sociales a la derecha
                rx.vstack(
                    rx.avatar(
                        name="Facundo M",
                        src="/avatar.jpg",
                        size="9",
                        margin_bottom="8px",
                        radius="full",
                        border="4px solid white"
                    ),
                    rx.hstack(
                        rx.link(
                            rx.icon("linkedin", size=25, color="#ffffff"),
                            href="https://www.linkedin.com/in/facundo-boladeras-382043292/",
                            target="_blank",
                            _hover={"color": "gray"},
                            margin_right="8px",
                        ),
                        rx.link(
                            rx.icon("github", size=25, color="#ffffff"),
                            href="https://github.com/FacuBoladeras",
                            target="_blank",
                            _hover={"color": "gray"},
                        ),
                        spacing="1",
                    ),
                    align_items="center",
                    spacing="1",
                    padding_top="12px",
                ),

                direction={"base": "column", "md": "row"},
                spacing="6",
                justify="center",
                align="center",
                width="100%",
            ),

            padding_top="100px",
            padding_bottom="80px",
            spacing="4",
            width="100%",
        ),
        max_width="1000px",  # <-- ajusta el ancho máximo que ocupará el contenido
        center_content=True,  # <-- centra horizontalmente todo el contenido
    )
