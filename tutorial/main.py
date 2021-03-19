from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    name = "paolo"
    course = "Python Web"
    return render_template("index.html", username=name, course_name=course)


if __name__ == "__main__":
    app.run(debug= True, port=9000)