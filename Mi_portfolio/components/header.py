import reflex as rx

def header(title_font_family="Tektur", title_class_name="title-primary", content_font_family="Roboto", content_class_name="content"):
    return rx.vstack(
        # Encabezado principal
        rx.text(
            "Mi Portfolio GIS",            
            font_weight="bold",
            text_align="center",
            font_family=title_font_family,
            class_name=title_class_name,
        ),
        # Línea divisoria
        rx.box(
            border_top="1px solid #eaeaea",
            border_bottom="1px solid #eaeaea",
            margin="1em 0",
            width="100%",
        ),
        # Contenido principal del header
        rx.hstack(
            # Texto a la izquierda
            rx.box(
                rx.text(
                    "Hello 👋 my name is Facundo Boladeras, I'm a Biology graduate from the Universidad Autónoma de Entre Ríos, "
                    "currently pursuing a PhD through a CONICET scholarship.\n\n"
                    "I specialize in Geographic Information Systems (GIS) with strong experience in technologies "
                    "like Python and Google Earth Engine, combining skills in data science and geoprocessing.",
                    font_family=content_font_family,
                    class_name=content_class_name
                ),
                max_width="800px",
                padding="20px",
            ),
            # Avatar y enlaces a la derecha
            rx.vstack(
                # Avatar arriba
                rx.avatar(
                    name="Facundo M",
                    src="/avatar.jpg",
                    size="9",
                    margin_bottom="8px",
                    radius="full",
                    border="4px solid white"
                ),
                # Iconos de redes sociales con links
                rx.hstack(
                    # LinkedIn icon linked
                    rx.link(
                        rx.icon("linkedin", size=25, color="#ffffff"),
                        href="https://www.linkedin.com/in/facundo-boladeras-382043292/",
                        target="_blank",
                        _hover={"color": "gray"},
                        margin_right="8px",
                    ),
                    # GitHub icon linked
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
            ),
            spacing="1",
        ),
        # Agrega padding superior aquí
        padding_top="80px",  # Ajusta este valor según lo que necesites
    )
