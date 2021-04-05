from flask import *

import loginLogic
import registrationLogic

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

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
         return render_template("index.html", error = "INVALID USERNAME OR PASSWORD")
   else:
      print("not POST METHOD")

@app.route("/register", methods=["POST"] )
def registerUser():
    if request.method == 'POST':
        data = dict()
        data['accountNumber'] = request.form['accountNumber']
        data['userName'] = request.form['userName']
        data['password']= request.form['password']
        data['email'] = request.form['email']
        data['phNumber'] = request.form['phNumber']

        if (registrationLogic.registerUser(data)):
            return render_template("index.html", message = "User Created")
        else:
            return render_template("index.html", error="USER NOT CREATED")

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
    return redirect(url_for('success', name="Nikunj"))

if __name__ == '__main__':
    app.run(debug=True)
