"""This module runs the Flask app"""

# libraries that this app needs
from flask import Flask

# initialize app
# __name__ helps determine root path
app = Flask(__name__)

# load app settings
app.config.from_pyfile('settings.py')

# routes
from routes import *

# only start web server if app.py is called directly;
# when file is called directly, __name__  is "__main__"
if __name__ == "__main__":
    # start server
    app.run()
