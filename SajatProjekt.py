import flet as ft
from flet import Text, Row, Column, TextField,ElevatedButton



class ControlEvent:
    def __init__(self, source):
        self.source = source


def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 600
    page.title = 'Bejelentkezés'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    

    tb1: TextField = TextField(label="Username", width=350, border_color="red", cursor_color="red",)
    tb2: TextField = TextField(label="Password", width=350, password=True,
    border_color="red", can_reveal_password=True, cursor_color="red")
    button: ElevatedButton = ElevatedButton(text="OK", color="red", disabled=True)
    button2: ElevatedButton = ElevatedButton(text="TOVÁBB", color="red")

    img = ft.Image(
        src=f"/Users/csataimartin/Documents/mobile_application/projektek/icons/emmanuel-jdz.gif",
        width=500,
        height=500,
        fit=ft.ImageFit.CONTAIN,
        )
    images = ft.Row(expand=1, wrap=False, scroll="always")
    
    def submit2(e:ControlEvent) ->None:
        page.clean()

        page.add(
            img,images
        )
        



    def validate(e:ControlEvent) ->None:
        if all ([tb1.value, tb2.value]):
            button.disabled = False
        else:
            button.disabled = True
        
        page.update()

    def submit(e: ControlEvent) ->None:
    
        page.clean()

        page.add(
            Row(
                controls = [Text(value=f'Üdvozollek: {tb1.value} \n A jelszavad: {tb2.value}', size=20)],
                alignment= ft.MainAxisAlignment.CENTER 
            ), button2
        )
    
    tb1.on_change = validate
    tb2.on_change = validate
    button.on_click = submit
    button2.on_click = submit2

    page.add(
        Row(
            controls=[
                Column(
                    [tb1,
                    tb2,
                    button]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER 
        )
    )
if __name__ == '__main__':
    ft.app(target=main)
