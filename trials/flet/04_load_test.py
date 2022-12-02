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

    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.ALWAYS

    def on_pan_update(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    def create_gd(left, top, width=1000, height=10000):
        textfield_a = TextField(
            label="[1]",
            value="import pandas as pd",
            multiline=True,
            border_color=colors.CYAN,
        )
        container_a = Container(
            bgcolor=colors.BLUE,
            border=ft.border.all(1, colors.WHITE70),
            padding=ft.padding.all(10),
            content=textfield_a,
            border_radius=10,
        )
        stack_a = Stack(
            [
                container_a,
            ]
        )

        gd = GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE,
            on_pan_update=on_pan_update,
            left=left,
            top=top,
            width=width,
            height=height,
            content=stack_a,
        )
        return gd
    

    main_stack = []
    for i in range(2):
        gd = create_gd(100, 100 * i)
        main_stack.append(gd)
    
    page.add(Stack(main_stack, expand=True))
    # main_container = Container(
    #     content=Stack(main_stack, expand=True),
    #     width=10000,
    #     height=10000,
    # )
    # page.add(main_container)
    

ft.app(target=main)

