import reflex as rx
from Mi_portfolio.components.linkedin_projects import linkedin_project_box

def linkedin_page(font_family="Tektur"):
    linkedin_links = [
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_m%C3%A9todo-kde-para-estimar-densidades-generar-activity-7301384179869507584-Oz6k?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/heatmap.gif",
            "description": "Python scripting: Python techniques applied to geospatial data analysis"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_estimacion-de-bosques-implantados-mediante-activity-7265337631884910592-P3r3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/deep_L.png",
            "description": "Machine learning/Deep learning: training ML and DL models using Python"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_geemap-python-activity-7218685252397875201-5-B5?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/grafico-dispersion.png",
            "description": "Biomass estimate: generating biomass estimation models using Python and Google Earth Engine"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_mofuss-python-globalecosystemsdynamicinvestigation-activity-7224546612184850434-HLmc?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/time-serie.png",
            "description": "International: generating time series of AGB maps for international projects"
        },
    ]

    return rx.container(
        rx.flex(
            *[
                linkedin_project_box(link["link"], link["image_url"], link["description"], font_family=font_family)
                for link in linkedin_links
            ],
            direction={"base": "column", "md": "row"},
            wrap="wrap",
            spacing="1",
            justify="center",
            align="center",
        ),
        center_content=True,
        padding="10px",
    )


def linkedin_page_freelance(font_family="Tektur"):
    linkedin_links = [
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_python-aws-streamlit-activity-7181350825821147136-46Uq?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/code.png",
            "description": "Web Apps: Development of commercial web apps using Streamlit"
        },
        {
            "link": "https://www.linkedin.com/posts/facundo-boladeras-382043292_python-aws-lambda-activity-7168324246182604800-54qb?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbXOlIBq6apVMLzAn9FUv1dX_UA7q3sNSA",
            "image_url": "/lidar.jpg",
            "description": "Web Apps: Development of GIS web apps using Streamlit and geospatial libraries"
        }
    ]

    return rx.container(
        rx.flex(
            *[
                linkedin_project_box(link["link"], link["image_url"], link["description"], font_family=font_family)
                for link in linkedin_links
            ],
            direction={"base": "column", "md": "row"},
            wrap="wrap",
            spacing="8",
            justify="center",
            align="center",
        ),
        center_content=True,
        padding="10px",
    )