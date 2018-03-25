from flask import Flask, render_template, redirect
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    today = datetime.datetime.now().strftime("%A %d %B %Y")  # Sunday 18 March 2018
    return render_template('home.jinja2', today=today)



if __name__ == "__main__":
    app.run()


