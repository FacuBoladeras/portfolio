from Mi_portfolio.constants.styles import PADDING_SMALL
import reflex as rx

def project_card(color, image_url, items, font_family=None):
    return rx.container(
        rx.box(
            rx.vstack(
                rx.image(
                    src=image_url,
                    width="150px",
                    height="100px",
                    object_fit="cover",
                    border_radius="10px",
                    border="4px solid black",
                    box_shadow="0px 4px 6px rgba(0, 0, 0, 0.2)",
                    margin="0",
                    padding="0",
                ),
                rx.vstack(
                    *[
                        rx.hstack(
                            rx.image(src="check-mark2.png", width="30px", height="30px"),
                            rx.text(
                                item,
                                font_family=font_family,
                                class_name="content",
                                font_weight="bold",
                                font_size={"base": "sm", "md": "md"}
                            ),
                            spacing="2",
                            align_items="center"
                        )
                        for item in items
                    ],
                    spacing="2",
                    align_items="flex-start",
                    width="100%",
                ),
                spacing="3",
                align_items="center",
                justify_content="center",
                width="100%",
            ),
            border_radius="0px",
            padding="4px 4px",  # 👈 vertical mayor que horizontal
            margin="0px",
            height="auto",
            min_height="280px",
            overflow="hidden",
            width="195px",
        ),
        center_content=True,
        padding="0px",
    )

