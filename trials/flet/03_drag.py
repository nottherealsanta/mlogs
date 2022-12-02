import flet as ft
from rich import print
from flet import (
    colors,
    Container,
    GestureDetector,
    TextField,
    Stack
)

def main(page: ft.Page):

    page.scroll = ft.ScrollMode.ALWAYS
    def on_pan_update(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()


    textfield_a = TextField(
        label="[1]",
        value="import pandas as pd",
        multiline=True,
        border_color=colors.CYAN,
    )
    container_a = Container(
        bgcolor=colors.TRANSPARENT,
        border=ft.border.all(1, colors.WHITE70),
        padding=ft.padding.all(10),
        content=textfield_a,
    )
    stack_a = Stack(
        [
            container_a,
        ]
    )

    gd = GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        on_pan_update=on_pan_update,
        left=100,
        top=100,
        width=1000,
        height=10000,
        content=stack_a,
    )

    page.add(Stack([gd], expand=True))


ft.app(target=main)
