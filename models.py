#!/usr/bin/env python3

import datetime, re

from app import db

def slugify(s):
	return re.sub('[^\w]+', '-', s).lower()
	

class Entry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	slug = db.Column(db.String(100), unique=True)
	body = db.Column(db.Text)
	created_timestamp = db.Column(db.DateTime, default = datetime.datetime.now)
	modified_timestamp = db.Column(db.DateTime, default = datetime.datetime.now, onupdate = datetime.datetime.now)
	
	def __init__(self, *args, **kwargs):
		super(Entry, self).__init__(*args, **kwargs) # Parent constructor call
		self.generate_slug()
		
	def generate_slug(self):
		self.slug = ''
		if self.title:
			self.slug = slugify(self.title)
			
	def __repr__(self):
		return f'<Entry: {self.title}>'
		

		
