import flet as ft
from utils import KeyCard
from key import return_key



def main(page: ft.Page):
    page.title = "CFWKG"
    page.keys_id_counter = 0
    page.theme = ft.theme.Theme(color_scheme_seed="deeppurple")
    page.dark_theme = ft.theme.Theme(color_scheme_seed="deeppurple")
    # page.theme_mode = "dark"
    page.splash = ft.ProgressBar(visible=False)

    def close_dlg(e):
        page.dialog.open = False
        page.update()

    def open_dlg(e):
        page.dialog.open = True
        page.update()

    def close_banner(e):
        page.banner.open = False
        page.update()

    def open_banner(e):
        page.banner.open = True
        page.update()

    def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        theme_icon_button.selected = not theme_icon_button.selected
        page.update()

    def generate(e):
        close_banner(None)
        page.splash.visible = True
        key_gen_btn.disabled = True
        page.update()

        if (fetched_key := return_key()) is not None:
            page.keys_id_counter += 1
            page.keys_row.controls.append(KeyCard(key_id=page.keys_id_counter, key_info=fetched_key[0], key_lic=fetched_key[1]))
        else:
            open_banner(None)

        page.splash.visible = False
        key_gen_btn.disabled = False
        page.update()

    page.dialog = ft.AlertDialog(
        modal=False,
        title=ft.Text("CFWKG v0.1", weight=ft.FontWeight.BOLD),
        content=ft.Text("Key generator for CloudFlare WARP\n\nMade with ❤ by Pegioner", text_align=ft.TextAlign.CENTER),
        actions=[
            ft.Row(
                [
                    ft.FilledTonalButton(
                        on_click=lambda e: page.launch_url(
                        "https://github.com/Pegioner/CFWKG"),
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.CODE_ROUNDED),
                                ft.Text("GitHub", weight=ft.FontWeight.BOLD)
                            ],
                        )
                    ),
                    ft.TextButton(
                        on_click=close_dlg,
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.CLOSE_ROUNDED),
                                ft.Text("Close", weight=ft.FontWeight.BOLD)
                            ],
                        )
                    ),
                ]
            ),    
            
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "Oops, there were some errors while trying to fetch the License Key. Please make sure you are connected "
            "to the internet or try again later"
        ),
        actions=[
            ft.TextButton("Retry", on_click=generate),
            ft.TextButton("Ignore", on_click=close_banner),
        ],
    )

    theme_icon_button = ft.IconButton(
        icon=ft.icons.DARK_MODE_ROUNDED,
        selected_icon=ft.icons.LIGHT_MODE_ROUNDED,
        selected=True if page.theme_mode == "dark" else False,
        icon_size=32,
        tooltip="Change Theme",
        on_click=change_theme,
    )

    page.appbar = ft.AppBar(
        title=ft.Text("CFWKG", weight=ft.FontWeight.BOLD),
        center_title=True,
        bgcolor=ft.colors.PRIMARY_CONTAINER,
        actions=[theme_icon_button],
        leading=ft.IconButton(
            icon=ft.icons.INFO_ROUNDED,
            icon_color=ft.colors.ON_SURFACE_VARIANT,
            icon_size=32,
            tooltip="About",
            on_click=open_dlg,
        )
    )

    page.keys_row = ft.ResponsiveRow([],)

    page.add(
        ft.Row(
            controls=[
                key_gen_btn := ft.ElevatedButton(
                    on_click=generate,
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.RESTART_ALT),
                            ft.Text("Generate a Key!", weight=ft.FontWeight.BOLD)
                        ]
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Column(
            [page.keys_row],
            scroll=ft.ScrollMode.HIDDEN,
            expand=True
        ),
    )

    page.update()


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
