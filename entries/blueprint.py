#!/usr/bin/env python3

from app import db
from flask import Blueprint, redirect, render_template, request, url_for
from helpers import object_list
from models import Entry
from entries.forms import EntryForm

entries = Blueprint('entries', __name__, template_folder='templates')

@entries.route('/')
def index():
	entries = Entry.query.order_by(Entry.created_timestamp.desc())
	return entry_list('entries/index.html', entries)

@entries.route('/create/', methods=['GET', 'POST'])
def create():
	if request.method == 'POST':
		form = EntryForm(request.form)
		if form.validate():
			entry = form.save_entry(Entry())
			db.session.add(entry)
			db.session.commit()
			return redirect(url_for('entries.detail', slug=entry. slug))
	else:
			form = EntryForm() 
		
	return render_template('entries/create.html', form=form)

@entries.route('/<slug>/edit/', methods=['GET', 'POST'])
def edit(slug):
	entry = Entry.query.filter(Entry.slug == slug).first_or_404()
	if request.method == 'POST':
		form = EntryForm(request.form, obj=entry)
		if form.validate():
			entry = form.save_entry(entry) 
			db.session.add(entry)
			db.session.commit()
			return redirect(url_for('entries.detail', slug=entry.slug))
	else:
		form = EntryForm(obj=entry)
	return render_template('entries/edit.html', entry=entry, form=form)


@entries.route('/<slug>/delete/', methods=['GET', 'POST'])
def delete(slug):
	entry = Entry.query.filter(Entry.slug == slug).first_or_404()
	if request.method == 'POST':
		db.session.delete(entry)
		db.session.commit()
		return redirect(url_for('entries.index'))
		
	return render_template('entries/delete.html', entry=entry)


@entries.route('/<slug>/')
def detail(slug):
	entry = Entry.query.filter(Entry.slug == slug).first_or_404()
	return render_template('entries/detail.html', entry=entry)


def entry_list(template, query, **context):
	search = request.args.get('q')
	if search:
		query = query.filter( (Entry.body.contains(search)) | (Entry.title.contains(search)))
	
	return object_list(template, query, **context)
