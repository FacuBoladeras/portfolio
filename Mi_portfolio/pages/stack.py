import reflex as rx

def grid_page_with_icons_vhstack():
    # Lista de logos con sus respectivas rutas
    logos = [
        "/icons8-python-96.png",
        "/icons8-aws-96.png",
        "/icons8-mysql-96.png",
        "/icons8-git-96.png",
        "/icons8-google-earth-96.png"
    ]

    # Crear filas (hstack) de iconos
    rows = []
    for i in range(3):  # Queremos 3 filas
        row_items = [
            rx.box(
                rx.image(
                    src=logos[j % len(logos)],  # Reutiliza logos si hay más celdas que imágenes
                    width="60px",
                    height="60px",  # Aseguramos que todas las imágenes tengan el mismo tamaño
                    border_radius="10px",
                    alt=f"Logo {j + 1}",
                ),
                width="100px",
                height="100px",
                border="1px dotted #e0e0e0",
                background="#FCF5E5",
                display="flex",
                align_items="center",
                justify_content="center",
            )
            for j in range(5)  # Cada fila tiene 5 celdas
        ]
        rows.append(rx.hstack(*row_items, spacing="0"))

    # Agrupar todas las filas en un vstack
    return rx.vstack(
        *rows,
        spacing="0",
        align_items="center",
        justify_content="center",
        padding="10px",
        border="2px solid #000",
        border_radius="10px",
        box_shadow="0px 4px 6px rgba(0, 0, 0, 0.3)",
        background="#ffffff"
    )
