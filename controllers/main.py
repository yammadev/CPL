# Get base path
import sys
sys.path.append('../')

# Import
from application import app as main
from flask import render_template

# Index route...
# [GET]
# @return response
@main.route('/')
def index():
	return render_template('index.html')
