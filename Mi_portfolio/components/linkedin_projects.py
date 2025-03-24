import reflex as rx


def linkedin_project_box(link, image_url, description=None):
    return rx.box(
        rx.vstack(
            # Imagen en la parte superior
            rx.image(
                src=image_url,
                width="100%",
                height="150px",
                object_fit="cover",
                border_top_radius="0px",
            ),
            # Descripción centrada en el espacio disponible
            rx.text(
                description or "LinkedIn Project", 
                margin_top="8px", 
                text_align="center"
            ),
            # Botón con el icono de LinkedIn
            rx.button(
                rx.icon("linkedin", margin_right="8px"),
                rx.text("View Post"),
                on_click=lambda: rx.redirect(link),  # Redirige al link
                bg="#0A66C2",  # Color de fondo tipo LinkedIn
                color="white",
                _hover={"bg": "#005582"},  # Cambio de color al pasar el mouse
                border_radius="0px",
                width="100%",
                margin_top="auto",  # Empuja el botón hacia abajo
            ),
            align_items="stretch",
            justify_content="space-between",  # Espacio entre elementos
            height="100%",  # Asegura que el vstack ocupe toda la altura
        ),
        border="2px solid #0A66C2",  # Color de LinkedIn
        border_radius="0px",
        padding="0px",
        width="300px",
        height="300px",
        box_shadow="md",
        margin="12px",
        display="flex",
        flex_direction="column",  # Asegura que los hijos se apilen verticalmente
    )
