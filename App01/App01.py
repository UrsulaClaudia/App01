import reflex as rx
from App01 import style
from App01.state import TutorialState

def index() -> rx.Component:
    return rx.container(chat(),action_bar(),align="center")

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question,style=style.question_style),text_align="right"
        ),
        rx.box(
            rx.text(answer,style=style.answer_style),text_align="left",
        ),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            TutorialState.chat_history,
            lambda messages: qa(messages[0],messages[1])
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=TutorialState.question,
            placeholder="Ask a question",
            style=style.input_style,
            on_change=TutorialState.set_question(""),
        ),
        rx.button(
            "Ask",
            style=style.button_style,
            on_click=TutorialState.answer,
        ),
    )

app = rx.App()
app.add_page(index)