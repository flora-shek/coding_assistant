from flask import Flask,render_template
from code_languages import CODE_LANGUAGES
app = Flask(__name__)

@app.route("/")
@app.route("/<language>")
def index(language="Python(Default)"):

  return render_template("index.html",languages =CODE_LANGUAGES,language=language,login=None)
@app.route("/login")
def login():
    return render_template('signin.html')
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4530, debug=True)