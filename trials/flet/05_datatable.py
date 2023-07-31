import flet as ft
from rich import print
from flet import colors, Container, GestureDetector, TextField, Stack


def main(page: ft.Page):

    page.scroll = ft.ScrollMode.ALWAYS

    rows = []

    for i in range(100):
        rows.append(
            ft.DataRow(
                [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text(f"{i}"))],
                selected=True,
                on_select_changed=lambda e: print(f"row select changed: {e.__dict__}"),
            )
        )

    datatable = ft.DataTable(
        width=700,
        bgcolor="yellow",
        border=ft.border.all(2, "red"),
        border_radius=20,
        vertical_lines=ft.border.BorderSide(3, "blue"),
        horizontal_lines=ft.border.BorderSide(1, "green"),
        sort_column_index=0,
        sort_ascending=True,
        heading_row_color=ft.colors.BLACK12,
        heading_row_height=100,
        data_row_color={"hovered": "0x30FF0000"},
        # show_checkbox_column=True,
        divider_thickness=0,
        column_spacing=200,
        columns=[
            ft.DataColumn(
                ft.Text("Column 1"),
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
            ft.DataColumn(
                ft.Text("Column 2"),
                tooltip="This is a second column",
                numeric=True,
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
        ],
        rows=rows,
    )
    page.add(datatable)


ft.app(target=main)
