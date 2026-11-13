from nicegui import ui


@ui.page("/")
def main_page():
    ui.page_title("Personal Data Manager")
    ui.label("Personal Data Manager")
    name = ui.input(label="Your name")
    greeting = ui.label("Type a name and press the button.").props('role="status" aria-live="polite"')

    def greet():
        if name.value.strip():
            greeting.set_text(f"Hello, {name.value.strip()}!")
        else:
            greeting.set_text("Please enter a name.")

    ui.button("Greet", on_click=greet)


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Personal Data Manager", reload=False, show=False, port=8099)
