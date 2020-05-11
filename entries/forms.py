#!/usr/bin/env python3

import wtforms

from models import Entry

class EntryForm(wtforms.Form):
	title = wtforms.StringField('Title')
	body = wtforms.TextAreaField('Body')
	
	def save_entry(self, entry):
		self.populate_obj(entry)
		entry.generate_slug()
		return entry
