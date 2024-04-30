from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")  # You can use this if you need the password
        return render_template("success.html", username=username, email=email)
    return render_template("register.html")


if __name__ == "__main__":
    # choose a random port
    random_port = random.randint(2000, 9000)
    app.run(debug=True, port=random_port)
