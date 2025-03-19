import reflex as rx

def project_card(title, description, image_url, link_url):
    return rx.box(
        rx.image(src=image_url, border_radius="8px"),
        rx.vstack(
            rx.text(title, font_size="1.2em", font_weight="bold"),
            rx.text(description),
            rx.link("Ver más →", href=link_url, color="#3182ce"),
            spacing=3,
            padding="1em",
        ),
        border="1px solid #eaeaea",
        border_radius="8px",
        overflow="hidden",
        box_shadow="sm",
    )