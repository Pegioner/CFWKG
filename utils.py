import flet as ft


class KeyCard(ft.Card):
    NORMAL_ELEVATION = 3
    HOVERED_ELEVATION = 7

    def __init__(self, key_id: int, key_info: str = "License Key", key_lic: str = ""):
        super(KeyCard, self).__init__(elevation=self.NORMAL_ELEVATION)
        self.key_id = str(key_id)
        self.key_txt = key_info
        self.key_lic = key_lic
        self.col = {"sm": 8, "md": 6}

    def _build(self):
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        f"Key #{self.key_id}",
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        self.key_txt,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Row(
                        [
                            ft.TextButton(
                                on_click=self.copy_key,
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.COPY),
                                        ft.Text("Copy Key", weight=ft.FontWeight.BOLD)
                                    ],
                                )
                            ),
                            ft.TextButton(
                                on_click=self.delete_key_card,
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.DELETE, color=ft.colors.ERROR),
                                        ft.Text("Delete", color=ft.colors.ERROR)
                                    ],
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            width=400,
            padding=10,
            on_hover=self.hover_elevation,
            border_radius=18,
        )

    def copy_key(self, e):
        self.page.set_clipboard(self.key_lic)
        self.page.show_snack_bar(
            ft.SnackBar(
                ft.Text(f"Copied License Key to Clipboard!"),
                open=True
            )
        )

    def delete_key_card(self, e):
        self.page.keys_row.controls.remove(self)
        self.update()
        self.page.update()
        self.page.show_snack_bar(
            ft.SnackBar(
                ft.Text(f"License Key was successfully deleted!"),
                open=True
            )
        )

    def hover_elevation(self, e):
        self.elevation = self.HOVERED_ELEVATION if self.elevation == self.NORMAL_ELEVATION else self.NORMAL_ELEVATION
        self.update()

