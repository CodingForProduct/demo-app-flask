"""This module runs the Flask app"""

# libraries that this app needs
from flask import Flask

# initialize app
# __name__ helps determine root path
app = Flask(__name__)

# turn on debug to automatically restart app when changes are made
app.debug = True

@app.route("/")
def home():
    """display root route"""
    return "hi"

# only start web server if app.py is called directly;
# when file is called directly, __name__  is "__main__"
if __name__ == "__main__":
    # start server
    app.run()
