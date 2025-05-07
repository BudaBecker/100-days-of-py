from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        text = function()
        return f"<b>{text}</b>"
    return wrapper
def make_italic(function):
    def wrapper():
        text = function()
        return f"<i>{text}</i>"
    return wrapper

@app.route("/")
def route():
    return f'<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2UzN2V6ZGJ6cmRrZWh6bWZndGgzY3hxNjJ2aHUyaHptNGN2dXNkeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MUHNdrm3vk7MoyUsCO/giphy.gif" width=400>'

@app.route("/bold")
@make_bold
@make_italic
def teste():
    return "bold?"

if __name__ == "__main__":
    app.run()