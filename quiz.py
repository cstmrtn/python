import flet as ft
import time
import random

def main(page: ft.Page):
    page.title = "Kvíz Alkalmazás"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False

    JoValasz = 0
    jelenlegi_valasz = -1

    def check_answer(e):
        nonlocal JoValasz
        if e.control.data == "correct":
            e.control.bgcolor = ft.colors.GREEN_200
            JoValasz += 1
        else:
            e.control.bgcolor = ft.colors.RED_200
        e.control.update()
        page.update()
        time.sleep(0.10)
        show_next_question()

    def show_next_question():
        nonlocal jelenlegi_valasz
        jelenlegi_valasz += 1
        if jelenlegi_valasz < len(questions):
            question_view.controls[0].value = questions[jelenlegi_valasz]["question"]
            answers = questions[jelenlegi_valasz]["answers"]
            random.shuffle(answers)  # Shuffle the answers
            answers_view.controls.clear()
            for answer in answers:
                answers_view.controls.append(
                    ft.ElevatedButton(
                        content=ft.Text(answer["text"]),
                        data=answer["correct"],
                        on_click=check_answer,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10))
                        ),
                        width=170,
                        height=60,
                    )
                )
            page.update()
        else:
            question_view.controls[0].value = f"A kvíznek vége van! {JoValasz} kérdésre válaszoltál helyesen a {len(questions)} kérdésből."
            answers_view.controls.clear()
            page.update()

    questions = [
        {
            "question": "Mi Magyarország fővárosa?",
            "answers": [
                {"text": "Budapest", "correct": "correct"},
                {"text": "Debrecen", "correct": "incorrect"},
                {"text": "Szeged", "correct": "incorrect"},
                {"text": "Pécs", "correct": "incorrect"},
            ],
        },
        {
            "question": "Ki írta a Himnuszt?",
            "answers": [
                {"text": "Kölcsey Ferenc", "correct": "correct"},
                {"text": "Petőfi Sándor", "correct": "incorrect"},
                {"text": "Arany János", "correct": "incorrect"},
                {"text": "Vörösmarty Mihály", "correct": "incorrect"},
            ],
        },
        {
            "question": "Melyik híres magyar találmány?",
            "answers": [
                {"text": "Rubik kocka", "correct": "correct"},
                {"text": "Telefon", "correct": "incorrect"},
                {"text": "Repülőgép", "correct": "incorrect"},
                {"text": "Számítógép", "correct": "incorrect"},
            ],
        },
        {
            "question": "Melyik folyó folyik keresztül Budapesten?",
            "answers": [
                {"text": "Duna", "correct": "correct"},
                {"text": "Tisza", "correct": "incorrect"},
                {"text": "Dráva", "correct": "incorrect"},
                {"text": "Rába", "correct": "incorrect"},
            ],
        },
        {
            "question": "Mikor ünnepeljük Magyarországon az államalapítás ünnepét?",
            "answers": [
                {"text": "Augusztus 20.", "correct": "correct"},
                {"text": "Március 15.", "correct": "incorrect"},
                {"text": "Október 23.", "correct": "incorrect"},
                {"text": "November 1.", "correct": "incorrect"},
            ],
        },
        {
            "question": "Ki volt az első magyar király?",
            "answers": [
                {"text": "Szent István", "correct": "correct"},
                {"text": "IV. Béla", "correct": "incorrect"},
                {"text": "Mátyás király", "correct": "incorrect"},
                {"text": "I. Ferenc József", "correct": "incorrect"},
            ],
        },
        {
            "question": "Melyik város híres a termálfürdőiről?",
            "answers": [
                {"text": "Budapest", "correct": "incorrect"},
                {"text": "Szarvas", "correct": "correct"},
                {"text": "Szeged", "correct": "incorrect"},
                {"text": "Győr", "correct": "incorrect"},
            ],
        },
        {
            "question": "Melyik magyar író alkotta meg a Lúdas Matyi meséjét?",
            "answers": [
                {"text": "Fazekas Mihály", "correct": "correct"},
                {"text": "Mikszáth Kálmán", "correct": "incorrect"},
                {"text": "Móricz Zsigmond", "correct": "incorrect"},
                {"text": "Jókai Mór", "correct": "incorrect"},
            ],
        },
        {
            "question": "Melyik városban található a Széchenyi fürdő?",
            "answers": [
                {"text": "Budapest", "correct": "correct"},
                {"text": "Debrecen", "correct": "incorrect"},
                {"text": "Pécs", "correct": "incorrect"},
                {"text": "Miskolc", "correct": "incorrect"},
            ],
        },
    ]

    def start_quiz(e):
        landing_view.visible = False
        quiz_view.visible = True
        show_next_question()
        page.update()

    landing_view = ft.Column(
        controls=[
            ft.Text("Üdvözöllek a Kvíz alkalmazásomban!", size=30, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Mennyire vagy jó Töriből? Most megtudhatod...",
                size=16,
                text_align=ft.TextAlign.JUSTIFY,
            ),
            ft.ElevatedButton("INDÍT", on_click=start_quiz),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    question_view = ft.Column(
        controls=[
            ft.Text(
                "",
                size=20,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    answers_view = ft.Row(
        wrap=True,
        spacing=10,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    quiz_view = ft.Column(
        visible=False,
        controls=[
            question_view,
            answers_view,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )

    page.add(
        ft.Column(
            controls=[
                landing_view,
                quiz_view,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

ft.app(target=main)
