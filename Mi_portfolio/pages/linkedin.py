import reflex as rx
from Mi_portfolio.components.linkedin_projects import linkedin_project_box

def linkedin_page():
    linkedin_links = [
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_m%C3%A9todo-kde-para-estimar-densidades-generar-activity-7301384179869507584-Oz6k?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/heatmap.jpg",
            "description": "Heatmap"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_estimacion-de-bosques-implantados-mediante-activity-7265337631884910592-P3r3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/deep L.jpg",
            "description": "Deep learning"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_mofuss-python-globalecosystemsdynamicinvestigation-activity-7224546612184850434-HLmc?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/biomass.jpg",
            "description": "Biomass estimate"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_python-aws-lambda-activity-7168324246182604800-54qb?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/lass.jpg",
            "description": "Moffus"
        },
    ]



    return rx.vstack(
        # Primera fila (dos boxes)
        rx.hstack(
            linkedin_project_box(linkedin_links[0]["link"], linkedin_links[0]["image_url"], linkedin_links[0]["description"]),
            linkedin_project_box(linkedin_links[1]["link"], linkedin_links[1]["image_url"], linkedin_links[1]["description"]),
            spacing="2",
        ),
        # Segunda fila (otros dos boxes)
        rx.hstack(
            linkedin_project_box(linkedin_links[2]["link"], linkedin_links[2]["image_url"], linkedin_links[2]["description"]),
            linkedin_project_box(linkedin_links[3]["link"], linkedin_links[3]["image_url"], linkedin_links[3]["description"]),
            spacing="2",
        ),
        spacing="2",  # Espacio entre las filas
        align_items="center",
        justify_content="center",
        padding="24px",
    )
    
    
    
def linkedin_page_freelance():
    linkedin_links = [
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_m%C3%A9todo-kde-para-estimar-densidades-generar-activity-7301384179869507584-Oz6k?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/heatmap.jpg",
            "description": "Heatmap"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_estimacion-de-bosques-implantados-mediante-activity-7265337631884910592-P3r3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/deep L.jpg",
            "description": "Deep learning"
        }
    ]

    return rx.vstack(
        # Una única fila (dos boxes)
        rx.hstack(
            linkedin_project_box(linkedin_links[0]["link"], linkedin_links[0]["image_url"], linkedin_links[0]["description"]),
            linkedin_project_box(linkedin_links[1]["link"], linkedin_links[1]["image_url"], linkedin_links[1]["description"]),
            spacing="2",
        ),
        spacing="2",
        align_items="center",
        justify_content="center",
        padding="24px",
    )
