import flet as ft
import time

checked = []
name = {'vezeteknev': '', 'keresztnev': ''}
alkalmazas = False 

def ContainerStyling(header):
    return {
        "height": 130,
        "width": 800,
        "border_radius": 10,
        "border": ft.border.only(top=ft.border.BorderSide(6, "#ffffff")) if header == "header" else ft.border.only(left=ft.border.BorderSide(6, "#ffffff")),
        "bgcolor": "#b0b0b0",
        "margin": 15,
        "padding" : 15
    }



def getChanges(e):
    global Name
    Name = False
    allowed_chars = "qwertzuiopőúüóöasdfghjkléáűmnbvcxyí "
    if all(char.lower() in allowed_chars for char in e.control.value):
        e.control.error_text = ""
    else:
        e.control.error_text = "Csak betűk írhatók be!"
    e.control.update()
    if e.control.label == "Vezetékneved:":
        name['vezeteknev'] = e.control.value
    elif e.control.label == "Keresztneved:":
        name['keresztnev'] = e.control.value
    if(len(name['vezeteknev']) > 0 and len(name['keresztnev']) > 0):
        Name = True
    else:
        Name = False
    checkSubmitAvailability()
    erdekeltseg.update()

def checkBoxChange(e):
    global checked
    global alkalmazas

    
    if e.control.value:
        checked.append(e.control.label)
    else:
        checked = [label for label in checked if label != e.control.label]
    
    if(len(checked) > 0):
        alkalmazas = True
    else:
        alkalmazas = False
    
    checkSubmitAvailability()
    erdekeltseg.update()

def checkSubmitAvailability():
    global alkalmazas, Name
    if not (alkalmazas and Name and radio.value and (erdekeltseg.value is not None and len(erdekeltseg.value) > 0)):
        button.disabled = True
    else:
        button.disabled = False
    button.update()



def main(page: ft.Page):
    page.title = "Form"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#1f1e1e"
    page.scroll = "auto"

    header_content = ft.Row(
        [
            ft.Column([
                ft.Text(
                    value="Form",
                    size=60,
                    color="#1f1e1e",
                    weight="bold",
                ),
            ]),
        ],
        alignment="center"
    )

    header = ft.Container(**ContainerStyling("header"), content=header_content)

    contentTexts = ["Írd  be a nevedet:", "Egy 1-10-ig terjedő skálán mennyire szereted a pythont?", "Milyen alkalmazásaid vannak a gépeden?", "Melyik igaz rád leginkább?"]

    first_content = ft.Column(
        [
            ft.Text(
                value=contentTexts[0],
                size=20,
                color="#1f1e1e",
                weight="bold",
            ),
            ft.Row(
                [
                    ft.TextField(
                        label="Vezetékneved:",
                        width=300,
                        hint_text="pl: Suhanyecz",
                        on_change=lambda e: getChanges(e),
                        height=100
                    ),
                    ft.TextField(
                        label="Keresztneved:",
                        width=300,
                        hint_text="pl: László",
                        on_change=lambda e: getChanges(e),
                        height=100
                    )
                ],
                alignment="center"
            )
        ],
        alignment="center"
    )

    elsoKerdes = ft.Container(**ContainerStyling("questions"), content=first_content)

    global radio
    radio = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="1", label="1"),
                ft.Radio(value="2", label="2"),
                ft.Radio(value="3", label="3"),
                ft.Radio(value="4", label="4"),
                ft.Radio(value="5", label="5"),
                ft.Radio(value="6", label="6"),
                ft.Radio(value="7", label="7"),
                ft.Radio(value="8", label="8"),
                ft.Radio(value="9", label="9"),
                ft.Radio(value="10", label="10"),
            ],
            alignment="center"
        )
    )
    second_content = ft.Column(
        [
            ft.Text(
                value=contentTexts[1],
                size=20,
                color="#1f1e1e",
                weight="bold",
            ),
            radio
        ],
        alignment="center"
    )

    masodikKerdes = ft.Container(**ContainerStyling("questions"), content=second_content)

    third_content = ft.Column(
        [
            ft.Text(
                value=contentTexts[2],
                size=20,
                color="#1f1e1e",
                weight="bold",
            ),
            ft.Row(
                [
                    ft.Checkbox(label="VLC Media Player", on_change=lambda e: checkBoxChange(e)),
                    ft.Checkbox(label="Google Chrome", on_change=lambda e: checkBoxChange(e)),
                    ft.Checkbox(label="Adobe Photoshop", on_change=lambda e: checkBoxChange(e)),
                    ft.Checkbox(label="CodeBlocks", on_change=lambda e: checkBoxChange(e)),
                    ft.Checkbox(label="Visual Studio Code", on_change=lambda e: checkBoxChange(e)),
                ],
                alignment="center"
            )
        ],
        alignment="center"
    )

    harmadikKerdes = ft.Container(**ContainerStyling("questions"), content=third_content)

    global erdekeltseg
    erdekeltseg = ft.Dropdown(
        label="erdekeltseg",
        on_change=lambda e: checkSubmitAvailability(),
        options=[
            ft.dropdown.Option("Backend fejlesztő - Adatbázisok és szerveroldali logika."),
            ft.dropdown.Option("Frontend fejlesztő - Felhasználóbarát weboldalak és alkalmazások."),
            ft.dropdown.Option("Adat tudós - Adatbányászat és gépi tanulás."),
            ft.dropdown.Option("DevOps mérnök - Automatizálás és CI/CD folyamatok."),
            ft.dropdown.Option("Kiberbiztonsági szakértő - Rendszer- és adatvédelem."),
        ]
    )

    fourth_content = ft.Column(
        [
            ft.Text(
                value=contentTexts[3],
                size=20,
                color="#1f1e1e",
                weight="bold",
            ),
            ft.Row(
                [
                    erdekeltseg
                ],
                alignment="center"
            )

        ],
        alignment="center"
    )

    negyedikKerdes = ft.Container(**ContainerStyling("questions"), content=fourth_content)

    global button
    button = ft.ElevatedButton(
        text="Küldés",
        on_click=lambda e: submit(e),
        width=100,
        height=30,
        disabled=True 
    )

    global result_text
    result_text = ft.Text(
        value="",
        size=20,
        weight = "bold"
    )

    page.add(header, elsoKerdes, masodikKerdes, harmadikKerdes, negyedikKerdes, button, result_text)

    def submit(e):
        result_text.value = ""
        appendres = ""
        for i in checked:
            appendres += i + " "
        typed_text = f"Neved: {name['vezeteknev']} {name['keresztnev']}\n"
        typed_text += f"Ennyire szereted a pythont: {radio.value}\n"
        typed_text += f"Ezek az alkalmazások vannak meg a gépeden: {appendres} \n"
        typed_text += f"Leginkább ez igaz rád: {erdekeltseg.value}\n"
        print(typed_text)
        typing = 0.05

        for char in typed_text:
            result_text.value += char
            page.update()
            time.sleep(typing)

    page.update()

ft.app(target=main)