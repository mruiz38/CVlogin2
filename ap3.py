from flask import Flask, g, redirect, render_template, request, session, url_for

class User:
  def __init__(self, id, username, password):
    self.id= id
    self.username = username
    self.password = password

  def __repr__(self):
    return f'<User: {self.username}>'

users=[]
users.append(User(id=1, username='Anthony', password='password' ))
users.append(User(id=2,username='Marco', password='marco' ))
#print(users)


app= Flask(__name__)
app.secret_key='algunsecreto'

@app.before_request
def before_request():
  g.user=None
  if 'user_id' in session:
     user = [x for x in users if x.id== session['user_id']][0]
     g.user = user


@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    session.pop('user_id', None)
    username = request.form['username']
    password = request.form['password']

    user = [ x for x in users if x.username == username][0]
    if user and user.password == password:
      session['user_id'] = user.id
      return render_template('registrarCV2.html')
  return render_template('login.html')

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    return render_template("registrarCV2.html")
    

@app.route("/regresando", methods=["POST"])
def regresando():
    if not g.user:
       return render_template('login.html')

    varNombres = request.form.get("varNombres")
    varApe1 = request.form.get("varApe1")
    varApe2 = request.form.get("varApe2")
    varFecNac = request.form.get("varFecNac")
    varEmail = request.form.get("varEmail")
    varNumCel= request.form.get("varNumCel")
    varDNI = request.form.get("varDNI")
    varDir = request.form.get("varDir")
    varCiu= request.form.get("varCiu")
    varResumen = request.form.get("varResumen")
    varExperiencia= request.form.get("varExperiencia")
    varEstudios =request.form.get("varEstudios")
    varLogros= request.form.get("varLogros")
    varHabilidades=request.form.get("varHabilidades")
    varintereses=request.form.get("varintereses")
    varreferencias=request.form.get("varreferencias") 
    return render_template("registrarCV2.html", 
    varNombres=varNombres,varApe1=varApe1, 
    varApe2=varApe2, varFecNac=varFecNac, varEmail=varEmail,
    varNumCel=varNumCel, varDNI=varDNI, varDir=varDir,
    varCiu=varCiu, varResumen=varResumen, varExperiencia=varExperiencia,
    varEstudios=varEstudios, varLogros=varLogros, varHabilidades=varHabilidades,
    varintereses=varintereses, varreferencias=varreferencias)
