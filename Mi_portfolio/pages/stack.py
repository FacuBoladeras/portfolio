import reflex as rx

def stack():
    # Lista de logos con sus respectivas rutas
    logos = [
        "/icons8-python-96.png",
        "/icons8-aws-96.png",
        "/icons8-mysql-96.png",
        "/icons8-git-96.png",
        "/icons8-google-earth-96.png"
    ]

    # Crear un rx.hstack donde cada imagen está dentro de un rx.box
    return rx.hstack(
        *[
            rx.box(
                rx.image(
                    src=logo,
                    width="60px",
                    height="auto",
                    alt="Logo",
                ),
                background="#ffffff",  # Fondo blanco para el box
                border="2px solid #000000",  # Borde negro
                box_shadow="0px 4px 6px rgba(0, 0, 0, 0.3)",  # Sombra alrededor
                border_radius="10px",  # Bordes ligeramente redondeados
                padding="10px",  # Espaciado interno del box
                align_items="center",
                justify_content="center",
                margin="10px"  # Margen alrededor del box
            )
            for logo in logos
        ],
        spacing="1",  # Espacio entre los boxes
        align_items="center",
        justify_content="center",
    )
