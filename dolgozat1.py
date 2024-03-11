import flet as ft

def main(page: ft.Page):
    page.title = "Dolgozat"
    page.scroll = ft.ScrollMode.AUTO
    page.add(
        ft.Row(controls=
        [
            ft.Container(ft.Text("Hello"), alignment = ft.alignment.center_left, expand=True),
            ft.Container(ft.Text("world"), alignment = ft.alignment.center_right, expand=True),
            ]),
            ft.Row(wrap=True [ft.Container(bgcolor=ft.colors.YELLOW, width= 200 , height=200 ,alignment = ft.alignment.top_center),
            ft.Container(bgcolor=ft.colors.BLUE, width= 200 , height=200 ,alignment = ft.alignment.top_center),
            ft.Container(bgcolor=ft.colors.GREEN, width= 200 , height=200 ,alignment = ft.alignment.top_center),
            ft.Container(bgcolor=ft.colors.BLACK, width= 200 , height=200 ,alignment = ft.alignment.top_center),
            ft.Container(bgcolor=ft.colors.RED, width= 200 , height=200 ,alignment = ft.alignment.top_center)
            ]))
            
    
    page.update(
    )        


if __name__ == '__main__':
    ft.app(target=main)
