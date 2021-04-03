from flask import *

SAVED_USERNAME = "admin"
SAVED_PASSWORD = "admin"
app = Flask(__name__)
app.secret_key = "SecretKey"

@app.route('/')
def showLoginPage():
   if "username" in session:
      username = session['username']
      return redirect(url_for('success',name = username))
   return render_template("index.html")

@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      print(request.form['userName'])
      user = request.form['userName']
      password = request.form['password']
      if (user == SAVED_USERNAME and password == SAVED_PASSWORD):
         session['username'] = request.form["userName"]
         return redirect(url_for('success',name = user))
      else:
         return render_template("index.html", message = "INVALID USERNAME OR PASSWORD")
   else:
      print("not POST METHOD")

@app.route('/success/<name>')
def success(name):
   if "username" in session:
      return render_template('single.html', name1 = name)
   else:
      render_template("index.html", message = "user is not set")



if __name__ == '__main__':
    app.run(debug=True)
