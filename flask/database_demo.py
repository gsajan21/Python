from flask import Flask, render_template, jsonify, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "enter@123"
app.config["MYSQL_DB"] = "library"

mysql = MySQL(app)

@app.route("/")
def index():
    return("MySql Test")

@app.route("/register", methods =["GET", "POST"])
def register():
    if request.method == "POST":
        formdata = request.form
        formStudentId = formdata["studentID"] 
        formStudentFname = formdata["studentFname"]
        formStudentLname = formdata["studentLname"]
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO student values(%s, %s, %s)", (formStudentId, formStudentFname, formStudentLname))
        mysql.connection.commit()
        cursor.close()
        return "Successfully Inserted!"

    return render_template("register.html")


if __name__ == "__main__":
    app.run(port=5002, debug=True)
    
