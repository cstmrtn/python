import flet as ft
from openai import OpenAI
import time
import threading


def main_style() -> dict[str, any]:
    return {
        "width": 400,
        "height": 300, 
        "bgcolor": "#141518",
        "border_radius": 10,
        "padding": 15,
    }

def promp_style() -> dict[str, any]:
    return {
        "width": 420,
        "height": 40, 
        "border_color": "white",
        "content_padding": 10,
        "cursor_color": "white",
    }

class CreateMessage(ft.Column):
    def __init__(self, name: str, message: str) -> None: 
        self.name: str = name
        self.message: str = message
        self.text = ft.Text(self.message) 
        super().__init__(spacing=4)
        self.controls = [ft.Text(self.name, opacity=0.6), self.text]

class MainContentArea(ft.Container):
    def __init__(self) -> None:
        super().__init__(**main_style())
        self.chat = ft.ListView(
            expand=True,
            height=200,
            spacing=15,
            auto_scroll=True
        )
        self.content = self.chat

class Prompt(ft.TextField):
    def __init__(self, chat: ft.ListView) -> None:
        super().__init__(**promp_style(), on_submit=self.run_prompt)
        self.chat = chat

    def animate_text_output(self, name: str, prompt: str) -> None:
        word_list: list = []
        msg = CreateMessage(name, "")
        self.chat.controls.append(msg)

        for word in list(prompt):
            word_list.append(word)
            msg.text.value = "".join(word_list)
            self.chat.update()
            time.sleep(0.008)
            

    def user_output(self, prompt) -> None:
        self.animate_text_output(name="Te", prompt=prompt)
        
    def gpt_output(self, prompt):
        try:
            response = client.embeddings.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            client = OpenAI(api_key="sk-proj-hjRe0SbKKosGUGIiVSrPT3BlbkFJTJirgjefTwlDsH27t4MS")
            completion = client.chat.completions.create
            response_text = response.choices[0].message.content.strip()
            self.animate_text_output(name="ChatGPT", prompt=response_text)
        except Exception as e:
            self.animate_text_output(name="ChatGPT", prompt=f"Error: {str(e)}")

    def run_prompt(self, event) -> None:
        text = event.control.value
        
        self.value = ""
        self.update()

        self.user_output(prompt=text)

        
        threading.Thread(target=self.gpt_output, args=(text,)).start()

def main(page: ft.Page) -> None:
    page.window_width = 400
    page.window_height = 600
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "dark"
    
    main_content = MainContentArea()
    prompt = Prompt(chat=main_content.chat)

    page.add(
        ft.Text("ChatGPT", size=30, weight="w800"),
        main_content,
        ft.Divider(height=6, color="transparent"),
        prompt,
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
