import reflex as rx
from App01 import style
from App01.state import State

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
            State.chat_history,
            lambda messages: qa(messages[0],messages[1])
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            style=style.input_style,
            on_change=State.setquestion,
        ),
        rx.button(
            "Ask",
            style=style.button_style,
            on_clic=State.answer,
        ),
    )

app = rx.App()
app.add_page(index)
