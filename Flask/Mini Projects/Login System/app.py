from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response

app = Flask(__name__)
app.secret_key = "abc123"

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["user"]
        
        if username == "":
            flash("Username required!", "error")
            return redirect(url_for("login"))
        
        #save session
        session["user"] = username
        
        #save cookie
        resp = make_response(redirect(url_for("dashboard")))
        resp.set_cookie("username", username)
        
        flash("Login Successful", "success")
        return resp
    
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        flash("please login first!", "error")
        return redirect(url_for("login"))
    
    username = request.cookies.get("username")
    return render_template("dashboard.html", name = username)

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out!", "success")
    return render_template("logout.html")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)