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
                border="2px solid #000000",
                border_radius="10px",
                
            ),
            # Descripción
            rx.text(
                description or "LinkedIn Project",
                text_align="center",
                color="black",
                font_family=font_family,
                font_size="1.2em",
                font_weight="bold",
                margin_top="8px",
            ),
            align_items="stretch",
            justify_content="flex-start",
            spacing="4"  # Espaciado uniforme entre elementos
        ),
        border="3px solid #000000",
        border_radius="10px",
        box_shadow="0px 6px 8px rgba(0, 0, 0, 0.2)",
        padding="16px",
        width="300px",
        height="360px",
        margin="12px",
        background="#FCF5E5",
        display="flex",
        flex_direction="column",
        justify_content="flex-start",  # Asegura que los hijos queden al principio
        align_items="stretch",
        on_click=lambda: rx.redirect(link),
        cursor="pointer",
        _hover={
            "box_shadow": "0px 6px 12px rgba(0, 0, 0, 0.3)",
            "transform": "translateY(-5px)",
            "transition": "transform 0.3s ease-in-out"
        }
    )


