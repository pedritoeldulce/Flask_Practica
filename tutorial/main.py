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


@app.route("/usuario/<string:last_name>/<string:user_name>/<int:age>")
def usuario(last_name, user_name, age):
    try:
        return "Hola {1} {0}, con {2} años".format(last_name, user_name, age)
    except E:
        return "valor de edad no es entero"


if __name__ == "__main__":
    app.run(debug= True, port=9000)