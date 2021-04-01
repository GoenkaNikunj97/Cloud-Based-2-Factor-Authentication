from flask import *

SAVED_USERNAME = "admin"
SAVED_PASSWORD = "admin"
app = Flask(__name__)


@app.route('/')
def showLoginPage():
   return render_template("index.html")

@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':

      print(request.form['userName'])
      user = request.form['userName']
      password = request.form['password']
      #print(user + "  -->  "+ password)
      if (user == SAVED_USERNAME and password == SAVED_PASSWORD):
         return redirect(url_for('success',name = user))
      else:
         return render_template("index.html", message = "INVALID USERNAME OR PASSWORD")
   else:
      print("not POST METHOD")

@app.route('/success/<name>')
def success(name):
   return render_template('welcome.html', name1 = name)

if __name__ == '__main__':
    app.run(debug=True)
