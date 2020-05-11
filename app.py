#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import configuration
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
