from flask import Flask, render_template, request

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
    return "Hola {1} {0}, con {2} años".format(last_name, user_name, age)


@app.route("/datos")
def datos():
    nombre = request.args.get('nombre') #Diccionario
    curso = request.args.get('curso')
    return "Listado de datos: " + nombre + curso


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=9000)