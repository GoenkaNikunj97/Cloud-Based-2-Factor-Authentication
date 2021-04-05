from flask import *
import os
import requests
import configparser

SAVED_USERNAME = "admin"
SAVED_PASSWORD = "admin"
app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route('/')
def showLoginPage():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':

        print(request.form['email'])
        user = request.form['email']
        password = request.form['password']
        # print(user + "  -->  "+ password)
        if (user == SAVED_USERNAME and password == SAVED_PASSWORD):
            return redirect(url_for('success', name=user))
        else:
            return render_template("index.html", message="INVALID USERNAME OR PASSWORD")
    else:
        print("not POST METHOD")


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':

        registrationUrl = readConfig('AwsServiceUrl', 'aws.registration')
        response = requests.post(registrationUrl,request.form.to_dict())
        print(response.content)
        if response.content:
            flash("Successfully registered!", "success")
            return render_template("index.html")
        else:
            flash("Error Occurred!", "warning")
            return render_template("index.html", message="SOME ERROR OCCURRED")
    else:
        print("Method signature error")


@app.route('/success/<name>')
def success(name):
    return render_template('welcome.html', name1=name)


def readConfig(section,key):

    configParser = configparser.RawConfigParser()
    configParser.read('configFile.properties')

    return configParser.get(section, key);


if __name__ == '__main__':
    app.run(debug=True)
