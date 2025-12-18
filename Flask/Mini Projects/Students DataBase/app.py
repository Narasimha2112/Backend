from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

#DB Connection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Admin@123",
    database = "flaskdb"
)

cursor = db.cursor(dictionary=True)

# HOME - SHOW LIST
@app.route("/")
def home():
    cursor.execute("SELECT * FROM STUDENTS")
    data = cursor.fetchall()
    return render_template("index.html", students = data)

#ADD STUDENTS
@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        marks = request.form["marks"]
        
        sql = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, age, marks))
        db.commit()
        
        return redirect("/")
    
    return render_template("add.html")

#Update Student - Details
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        marks = request.form["marks"]
        
        sql = "UPDATE students SET name=%s, age=%s, marks=%s WHERE id=%s"
        cursor.execute(sql, (name, age, marks, id))
        db.commit()
        
        return redirect("/")
    
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    
    return render_template("edit.html", student=student)

#Delete Student
@app.route("/delete/<int:id>")
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)