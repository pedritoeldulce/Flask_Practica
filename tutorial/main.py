from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    name = "paolo"
    course = "Python Web"
    is_premiun = True
    studens = ["paolo", "noa", "filomena", "pedro"]

    return render_template("index.html", username=name,
                                        course_name=course,
                                        is_premiun=is_premiun,
                                        list_students=studens)


if __name__ == "__main__":
    app.run(debug= True, port=9000)