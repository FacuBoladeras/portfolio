import reflex as rx

def grid_page_with_icons_vhstack():
    # Definir una grilla explícita: cada fila es una lista de nombres de archivo PNG (o None si está vacía)
    grid = [
        ["/icons8-python-96.png", "/sklearn.png", "/tensorflow.png", "/FastAPI.png", "/Streamlit.png"],
        ["/satelite.png", "/qgis.png", "/icons8-google-earth-96.png", "/geopandas.png", None],
        ["/informatica.png", "/icons8-aws-96.png", "/icons8-mysql-96.png", "/icons8-git-96.png", "/docker.png"],
    ]

    # Crear las filas (hstack) de la grilla
    rows = []
    for row_index, row in enumerate(grid):
        row_items = [
            rx.box(
                rx.image(
                    src=logo,
                    width="60px",
                    height="60px",
                    border_radius="10px",
                    alt="Logo" if logo else "",
                ) if logo else rx.box(),  # Si no hay logo, renderiza un box vacío
                width="100px",
                height="100px",
                display="flex",
                align_items="center",
                justify_content="center",
                border="1px dotted #e0e0e0",
                background="#FCF5E5" if col_index > 0 else "#f2e5d7",  # Fondo más oscuro para la primera columna
            )
            for col_index, logo in enumerate(row)
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

