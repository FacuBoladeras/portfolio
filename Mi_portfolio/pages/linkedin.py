import reflex as rx
from Mi_portfolio.components.linkedin_projects import linkedin_project_box

def linkedin_page():
    linkedin_links = [
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_m%C3%A9todo-kde-para-estimar-densidades-generar-activity-7301384179869507584-Oz6k?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "https://media.licdn.com/dms/image/v2/D4D22AQHCfWAPdahEgQ/feedshare-shrink_800/B4DZVO6NU.HIAg-/0/1740785640128?e=1745452800&v=beta&t=uNWYfRBJN--DIm2_vsADLxEz8PUHimGtfejOEW-kfNs",
            "description": "Heatmap"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_estimacion-de-bosques-implantados-mediante-activity-7265337631884910592-P3r3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "https://media.licdn.com/dms/image/v2/D4D22AQEPfzq0f2B6Bw/feedshare-shrink_800/feedshare-shrink_800/0/1732191473078?e=1745452800&v=beta&t=Un_IlSsKPr03SVJgbXT6QBiQ4C_GJkET1uHrj9IRhdk",
            "description": "Deep learning"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_geemap-python-activity-7218685252397875201-5-B5?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "https://media.licdn.com/dms/image/v2/D4D22AQEUw3gSw6UJaw/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1721068679666?e=1745452800&v=beta&t=CSkKfzp1eTcc-_RvXvqIQSFfVWiQJtu2x9oLwtCWiUM",
            "description": "Biomass estimate"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_mofuss-python-globalecosystemsdynamicinvestigation-activity-7224546612184850434-HLmc?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "https://media.licdn.com/dms/image/v2/D4D22AQHoSjClh0ay6w/feedshare-shrink_800/feedshare-shrink_800/0/1722466137150?e=1745452800&v=beta&t=jBsmvsJ755LUjmsAIjmONMRdfQAgxrmFYaJe91JuJFM",
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