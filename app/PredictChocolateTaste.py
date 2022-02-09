from flask import Flask
from flask import request, render_template
app = Flask(__name__)
import joblib

@app.route("/", methods = ["GET","POST"])
def index ():
    if request.method == "POST":
        sugar = request.form.get("sugar")
        milk = request.form.get("milk")
        print("TEST")
        model = joblib.load("CTaste")
        print("TEST@")
        pred = model.predict([[sugar,milk]])
        print(pred)
        s = "The predicted taste is: " + str(pred[0])
        print(sugar, milk)
        return (render_template("index.html", taste = s))
    else:
        return (render_template("index.html", taste = "Predict Taste2"))

app.run()
