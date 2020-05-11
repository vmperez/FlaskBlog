#!/usr/bin/env python3

from flask import render_template, request
from app import app

@app.route('/')
def homepage():
	return render_template('homepage.html')
