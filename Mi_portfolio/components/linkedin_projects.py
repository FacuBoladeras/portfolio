import reflex as rx

def linkedin_project_box(link, image_url, description=None):
    return rx.box(
        rx.vstack(
            # Imagen más cerca del borde
            rx.image(
                src=image_url,
                width="100%",
                height="150px",
                object_fit="cover",
                border_top_radius="8px",
                margin="0",  # Sin margen adicional
                padding="0",  # O con un pequeño padding si deseas un mínimo espacio
            ),
            # Texto con mayor margen
            rx.text(
                description or "LinkedIn Project",
                margin_top="16px",  # Más espacio arriba del texto
                margin_bottom="8px",
            ),
            rx.link(
                "View Post",
                href=link,
                target="_blank",
                color="blue",
                text_decoration="underline",
                margin_top="8px",  # Espaciado solo para el enlace
            ),
        ),
        border="2px solid #0A66C2",  # Color de LinkedIn
        border_radius="8px",
        padding="16px",  # Padding general del box
        width="300px",
        height="300px",
        box_shadow="md",
        margin="12px",
    )
