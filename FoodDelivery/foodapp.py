from flask import *
import sqlite3

app = Flask(__name__)
app.config['SECRET_key'] = "foo"

@app.route("/")
def index():
    return render_template("food.html");

@app.route("/savedetails", methods=["POST","GET"])
def savedetails():
    msg = "msg"
    if request.method == "POST":
        try:
            email = request.form["email"]
            password = request.form["password"]
            with sqlite3.connect("foodapp.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Customer (email,password) values(?,?)",(email,password))
                con.commit()
                msg = "Successfully added!!"
        except:
            con.rollback()
            msg = "We can not add you"
        finally:
            return render_template("food.html", msg=msg)
            con.close()



@app.route("/about")
def about():
    return render_template('about.html')     

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')    

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/recipe")
def recipe():
    return render_template('tag-template.html')

@app.route("/anda")
def anda():
    return render_template('Anda.html')

@app.route("/soup")
def soup():
    return render_template('soup.html')

@app.route("/poha")
def poha():
    return render_template('poha.html')

@app.route("/pancake")
def pancake():
    return render_template('banana.html')



if __name__ == "__main__":
    app.run(debug = True)





