import reflex as rx


def linkedin_project_box(link, image_url, description=None, font_family="Tektur"):
    return rx.box(
        rx.vstack(
            # Imagen en la parte superior
            rx.image(
                src=image_url,
                width="100%",
                height="150px",
                object_fit="cover",
                weight= "bold",
                border_top_radius="0px",
            ),
            # Descripción centrada en el espacio disponible
            rx.text(
                description or "LinkedIn Project",
                margin_top="8px",
                text_align="center",
                color="black",
                font_family=font_family,
            ),
            align_items="stretch",
            justify_content="space-between",
            height="100%",
        ),
        border="3px solid #000000",
        box_shadow="0px 4px 6px rgba(0, 0, 0, 0.2)",
        border_radius="0px",
        padding="0px",
        width="300px",
        height="200px",
        margin="12px",
        display="flex",
        flex_direction="column",
        on_click=lambda: rx.redirect(link),  # Hace que todo el box sea clickeable
        cursor="pointer",  # Cambia el cursor para indicar que es un link
        _hover={"box_shadow": "lg"},  # Efecto al pasar el mouse
    )

