import reflex as rx


def linkedin_project_box(link, image_url, description=None, font_family="Tektur"):
    return rx.box(
        rx.vstack(
            # Imagen en la parte superior con margen negativo y borde interno
            rx.image(
                src=image_url,
                width="100%",
                height="150px",
                object_fit="cover",
                weight="bold",
                border="2px solid #000000",  # Borde interno blanco
                margin_top="5px",         # Margen negativo para que sobresalga
                border_radius="10px"        # Redondear los bordes de la imagen
            ),
            # Descripción centrada en el espacio disponible
            rx.text(
                description or "LinkedIn Project",
                margin_top="8px",
                text_align="center",
                color="black",
                font_family=font_family,
                font_size="1.2em",  # Ajusta este valor según el tamaño deseado
                font_weight="bold",
                padding_top="2px",
            ),
            align_items="stretch",
            justify_content="space-between",
            height="100%",
        ),
        border="3px solid #000000",  
        border_radius="10px",# Bordes negros para la tarjeta
        box_shadow="0px 6px 8px rgba(0, 0, 0, 0.2)",  # Sombra para realce                            # Bordes redondeados para la tarjeta
        padding="16px",                         # Espaciado interno del box
        width="300px",
        height="340px",                         # Aumenta la altura si es necesario
        margin="12px",
        display="flex",
        justify_content="center",
        flex_direction="column",
        background="#ffffff",                   # Fondo blanco para la tarjeta
        on_click=lambda: rx.redirect(link),     # Hace que todo el box sea clickeable
        cursor="pointer",
                _hover={
            "box_shadow": "0px 6px 12px rgba(0, 0, 0, 0.3)",
            "transform": "translateY(-5px)",  # Mueve el box 5px hacia arriba
            "transition": "transform 0.3s ease-in-out"  # Añade una transición suave
        },  # Efecto hover
    )


