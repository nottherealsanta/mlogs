import flet as ft
from rich import print
from flet import colors, Container, GestureDetector, TextField, Stack


# class collision(ft.UserControl):
#     def __init__(self, width=400, height=200):
#         super().__init__()
#         self.width = width
#         self.height = height
#         self.top = 100
#         self.left = 100
#         self.container_a = Container(
#             bgcolor=colors.BLUE,
#             border_radius=10,
#         )
#         self.container_b = Container(
#             bgcolor=colors.BLUE_GREY_50,
#             border_radius=10,
#             margin=ft.margin.all(10),
#             content=TextField(
#                 label="[1]",
#                 value="import pandas as pd",
#                 multiline=True,
#                 border_color=colors.CYAN,
#             ),
#         )

#         self.stack_a = Stack(
#             [self.container_a],
#         )
#         self.stack_b = Stack(
#             [self.container_b], width=width - 20, height=height - 20, top=10, left=10
#         )

#         self.gd = GestureDetector(
#             mouse_cursor=ft.MouseCursor.GRAB,
#             on_pan_update=self.on_pan_update,
#             content=self.stack_a,
#             left=0,
#             top=0,
#             width=width,
#             height=height,
#         )

#         self.stack_c = Stack(
#             [self.gd, self.stack_b],
#             top=0,
#             left=0,
#             width=width,
#             height=height,
#             expand=True,
#         )

#     def on_pan_update(self, e: ft.DragUpdateEvent):

#         self.top = max(0, self.top + e.delta_y)
#         self.left = max(0, self.left + e.delta_x)
#         self.update()

#     def build(self):
#         return self.stack_c


# def main(page: ft.Page):
#     page.title = "Collision"
#     # page.add(collision())

#     main_stack = Stack([collision()], width=1000, height=1000, expand=True)
#     page.add(main_stack)


# ft.app(target=main)


class Outer(ft.UserControl):

    def __init__(self, width=700, height=700):
        super().__init__()
        self.width = width
        self.height = height
        self.top = 100
        self.left = 100

        self.container_a = Container(
            bgcolor=colors.BLUE_100,
            border_radius=10,
        )

        self.stack_a = Stack(
            [self.container_a],
            width=width,
            height=height,
            top=0,
            left=0,
        )
    
    def build(self):
        return self.stack_a

class Inner(ft.UserControl):

    def __init__(self, outer: Outer, width=400, height=200):
        super().__init__()
        self.width = width
        self.height = height
        self.top = 100
        self.left = 100

        self.outer = outer

        self.container_a = Container(
            bgcolor=colors.BLUE,
            border_radius=10,
        )
        self.container_b = Container(
            bgcolor=colors.BLUE_GREY_50,
            border_radius=10,
            margin=ft.margin.all(10),
            content=TextField(
                label="[1]",
                value="import pandas as pd",
                multiline=True,
                border_color=colors.CYAN,
            ),
        )

        self.stack_a = Stack(
            [self.container_a],
        )
        self.stack_b = Stack(
            [self.container_b], width=width - 20, height=height - 20, top=10, left=10
        )

        self.gd = GestureDetector(
            mouse_cursor=ft.MouseCursor.GRAB,
            on_pan_update=self.on_pan_update,
            content=self.stack_a,
            left=0,
            top=0,
            width=width,
            height=height,
        )

        self.stack_c = Stack(
            [self.gd, self.stack_b],
            top=0,
            left=0,
            width=width,
            height=height,
            expand=True,
        )

    def on_pan_update(self, e: ft.DragUpdateEvent): 

        self.top = min(self.top, self.outer.height - self.height + self.outer.top)
        self.left = min(self.left, self.outer.width - self.width + self.outer.left)

        self.top = max(self.top + e.delta_y, self.outer.top)
        self.left = max(self.left + e.delta_x, self.outer.left)

        self.update()
    
    def build(self):
        return self.stack_c

def main(page: ft.Page):
    page.title = "Collision"

    outer = Outer()
    inner = Inner(outer)

    main_stack = Stack([outer, inner], width=1000, height=1000, expand=True)

    page.add(main_stack)
        
ft.app(target=main)