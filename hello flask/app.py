from flask import Flask, render_template

app = Flask(__name__)


@app.route(
    "/"
)  # if website domain is www.abc.com, https://www.abc.com/ will trigger this function
@app.route('/hello/')
@app.route(
    "/hello/<name>"
)  # if the route contains /hello/<name>, it will trigger the function below
def hello(name=None):
    if name:
        # return f'<h1>Hello, {name}!</h1><p style="color:red">I am excited to learn Flask.</p>'
        return render_template("index.html", username=name)
    return "Hello, World!"


# Create another route like '/square/<number>', so the web app will display the square of the integer
@app.route('/square/')
@app.route('/square/<number>')
# @app.route('/square/<int:number>')
def square(number=None):
    if number:
        return str(float(number) ** 2)
    return "You need to provide a number."


if __name__ == "__main__":
    app.run(debug=True)