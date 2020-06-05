from application import app as main
from flask import Flask, render_template

# Index route...
# [GET]
# @return response
@main.route('/')
def index():
	return render_template('index.html')
