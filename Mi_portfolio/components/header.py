import reflex as rx

def header():
    return rx.vstack(
        # Encabezado principal
        rx.text(
            "Mi Portfolio - Encabezado",
            font_size="1.5em",
            font_weight="bold",
            text_align="center",
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
            rx.text(
                "Este es mi portfolio personal donde comparto mis proyectos y experiencias.",
                font_size="1em",
                flex="1",
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
                align_items="center",  # Centra el avatar y los botones en su contenedor
                spacing="1",  # Espaciado entre elementos del vstack
            ),
            spacing="1",  # Espaciado entre el texto y el contenedor del avatar
        )
    )
