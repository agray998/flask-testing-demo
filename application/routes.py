from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Demo
from application.forms import Add

@app.route('/')
def index():
    return render_template('index.html', results=map(str, Demo.query.all()))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = Add()
    if request.method == 'POST' and form.validate():
        new_item = Demo(field1=form.add.data)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)