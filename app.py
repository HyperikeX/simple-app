from flask import Flask, render_template, request
# test

app = Flask(__name__)


def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]


@app.route("/user/<variable>")
def greet(variable):
    return f"<p>Hello, {variable}</p>"


@app.route("/")
def homeInfo():
    name = "Anthony"
    content = ['This is my site', 'Hellow']
    content = readDetails('static/content.txt')
    return render_template("base.html", name=name, aboutMe=content)


@app.route("/form", methods= ['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name = request.form('name')

    return render_template('form.html', name=name)


app.run(debug=False)
