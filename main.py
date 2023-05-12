from flask import Flask, render_template

app = Flask(__name__)

#criarpaginas
#route + função
@app.route("/")
def home():
    return render_template("home.html")

#sitenoar
if __name__ == "__main__":
    app.run(debug=True)
