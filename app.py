from flask import Flask, render_template, request, redirect, jsonify
import logging
import psycopg2
from sender import send_email
app = Flask(__name__)

logging.basicConfig(filename='app.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')

# connecting to Azure's postgres with psycopg2 library 
logging.info("connecting to postgresql: start")

connection = psycopg2.connect(
    host="localhost", \
    dbname="postgres", \
    user="postgres",\
    password="pw")

logging.info("connecting to postgresql: end")


@app.route('/')
def hello():
    return "Hello"

@app.route('/form/')
def form():
    return render_template("form.html")

@app.route('/data', methods=["GET", "POST"])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        email = request.form['Contact-Email']
        send_email(email)
        return render_template("data.html")
        return email









if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True) 