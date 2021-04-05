from flask import *
import os
import requests
import configparser
import json

import loginLogic

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.secret_key = os.urandom(16)


@app.route('/')
def showLoginPage():
   if "username" in session:
      username = session['username']
      return redirect(url_for('success',name = username))
   return render_template("index.html")

@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      userId = request.form['userName']
      password = request.form['password']

      if(loginLogic.isUserValid(userId, password)):
          session['username'] = request.form["userName"]
          return redirect(url_for('success', name=userId))
      else:
         return render_template("index.html", message = "INVALID USERNAME OR PASSWORD")
   else:
      print("not POST METHOD")



@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        requestBody = {"account_number":int(request.form['account_number']),"emailid":request.form['emailid'],
                       "mobile":int(request.form['mobile']),"password":request.form['password'],"username":request.form['username']}
        registrationUrl = readConfig('AwsServiceUrl', 'aws.registration')
        print(request.form.to_dict())
        print(json.dumps(requestBody))
        response = requests.post(registrationUrl,json.dumps(requestBody))
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
   if "username" in session:
      return render_template('single.html', name1 = name)
   else:
      return redirect(url_for('showLoginPage'))


@app.route("/logout", methods=["GET"])
def logout():
  session.clear()
  return redirect(url_for('showLoginPage'))

@app.route("/submitLoanApplication",methods=["POST"])
def submitLoanApplication():
    print("-----------------------")
    print(request.form['phoneNumber'])
    print(request.files['loanFile'])
    return redirect(url_for('success', name="Nikunj"))

@app.route("/register", methods=["POST"] )
def registerUser():
    pass


def readConfig(section,key):

    configParser = configparser.RawConfigParser()
    configParser.read('configFile.properties')

    return configParser.get(section, key);


if __name__ == '__main__':
    app.run(debug=True)
