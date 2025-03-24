import reflex as rx

def stack():
    # Lista de logos con sus respectivas rutas
    logos = [
        "/logos/python.png",
        "/logos/react.png",
        "/logos/docker.png",
        "/logos/github.png",
    ]

    # Usar rx.hstack para una fila horizontal
    return rx.hstack(
        # Generar un logo como rx.image para cada entrada
        *[
            rx.image(
                src=logo,
                width="50px",  # Ajustar el tamaño del logo
                height="auto",
                alt="Logo"
            )
            for logo in logos
        ],
        spacing="4",  # Espacio entre los logos
        align_items="center",
        justify_content="center",
        padding="16px"
    )
