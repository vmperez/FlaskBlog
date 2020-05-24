#!/usr/bin/env python3

from app import app, db
import os
import models
import views

from entries.blueprint import entries
app.register_blueprint(entries, url_prefix='/entries')

def check_db():
	if not os.path.exists('./blog.db'):
		os.mknod('./blog.db')
		
		
	# SQLite database file header is 100 bytes
	if os.path.getsize('./blog.db') < 100:
		db.create_all()
	else:
		print("No need to create new DB")

if __name__ == '__main__':
	check_db()
	app.run()
