from flask import Flask
from dotenv import load_dotenv
import controllers.indexController as idxCtrl
import os

load_dotenv()

app = Flask(__name__,static_folder="static",static_url_path="")
app.secret_key = os.getenv("KEY")

@app.route("/", methods=["GET"])
def index():
    return idxCtrl.index()

@app.route("/login", methods=["GET"])
def login():
    return idxCtrl.login()

@app.route("/register", methods=["GET"])
def register():
    return idxCtrl.register()

if __name__ == "__main__":
    app.run(host= os.getenv("HOST"), port= os.getenv("PORT"))