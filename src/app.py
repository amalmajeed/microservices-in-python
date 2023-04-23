import os
import requests
import socket
from flask import Flask,jsonify,request,render_template


app = Flask(__name__)

def hostinfo():
    hostname = socket.gethostname()
    print("HOST NAME IS: ",hostname)
    ip = socket.gethostbyname(hostname)
    return(hostname,ip)

@app.route("/abc")
def abc():
    filename = "/Users/amalmajeed/Desktop/Python projects/microservices-in-python/src/templates/abc"
    file = open(filename, "r")
    file_contents = file.read()
    file.close()
    print("Hello World")
    return(file_contents)

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/")
def hello():
    return("<h1> HELLO WORLD </h1>")

@app.route("/details",methods=["GET","POST"])
def details():
    if request.method == "GET":
        h_name,i_addr = hostinfo()
        return render_template("index.html",hostname=h_name,ip=i_addr)

app.run(debug=True)