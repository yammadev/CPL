# Import
from flask import Flask

# Init
app = Flask(__name__)

# Importing controllers
import controllers.main

# Main
if __name__ == "__main__":
    app.run()
