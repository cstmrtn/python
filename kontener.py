import flet as ft

def main(page: ft.Page):
    page.title = "Négyen egy sorban?"

    page.window_width = 400
    page.window_height = 400
    page.add( 
        ft.Row([
        ft.Container(bgcolor=ft.colors.BLUE, width= 450 , height=100 , padding=40, content=ft.Text("1. konténer"), alignment = ft.alignment.top_center, ), 
    ft.Container(bgcolor=ft.colors.BLUE, width= 500 , height=100 , padding=40, content=ft.Text("2. konténer"),alignment = ft.alignment.top_center,),
    ft.Container(bgcolor=ft.colors.BLUE, width= 550 , height=100 , padding=40, content=ft.Text("3. konténer"),alignment = ft.alignment.top_center,),
    ft.Container(bgcolor=ft.colors.BLUE, width= 600 , height=100 , padding=40, content=ft.Text("4. konténer"),alignment = ft.alignment.top_center,)
    ],
    wrap=True))
    page.update()

if __name__ == '__main__':
    ft.app(target=main)