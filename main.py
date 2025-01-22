from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/timeweb")
def timeweb():
    return "Это страница /timeweb"

@app.route("/blog")
def blog():
    return "Это страница /blog"

@app.route("/cloud")
def cloud():
    return "Это страница /cloud"

@app.route("/get_example")
def get_example():
    framework = request.args.get('framework')
    language = request.args.get('language')
    version = request.args.get('version')

    return "language: {}; framework: {}; version: {}".format(language, framework, version)

@app.route("/authorization", methods=["POST", "GET"])
def authorization():
    if request.method == "POST":
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        if Login == "admin" and Password == "admin":
            return "Correct"
        else:
            return "Incorrect"

    return """
    <form method="POST">
         <div><label>Login: <input type="text" name="Login"></label></div>
         <div><label>Password: <input type="text" name="Password"></label></div>
         <input type="submit" value="Enter">
    </form>
    """


if __name__ == "__main__":
    app.run()