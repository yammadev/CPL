# Get base path
import sys
sys.path.append('../')

# Import
from flask import Flask

# Init
app = Flask(__name__)

# Importing controllers
import controllers.main
import controllers.api

# Main
if __name__ == "__main__":
    app.run()
