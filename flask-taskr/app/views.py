#flask-taskr
#views.py

from flask import Flask,render_template, request, session,\
flash,redirect,url_for,g
import sqlite3
from functools import wraps

app=Flask(__name__)
app.config.from_object('config')


def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/',methods=['GET','POST'])
def login():
	error=None
	if request.method == 'POST':
		if request.form['username']!= app.config['USERNAME']\
			or request.form['password']!=app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again!'
		else:
			session['logged_in']=True
			return redirect(url_for('tasks'))
	return render_template('login.html',error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash('You are now logged out. See you again:)')
	return redirect(url_for('login'))


def login_required(test):
	@wraps(test)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return test(*args,**kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap
	
@app.route('/tasks')
@login_required
def tasks():
	g.db=connect_db()
	cur=g.db.execute('select name, due_date, priority, taskid from ftasks where status=1')
	open_tasks=[dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
	cur=g.db.execute('select name, due_date, priority, taskid from ftasks where status=0')
	closed_tasks=[dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
	g.db.close()
	return render_template('tasks.html',open_tasks=open_tasks, closed_tasks=closed_tasks)
	
#Add new tasks
@app.route('/add',methods=['POST'])
@login_required
def new_task():
	g.db=connect_db()
	name=request.form['name']
	date=request.form['due_date']
	priority=request.form['priority']
	if not name or not date or not priority:
		flash("All fields are required. Please try again!")
		return redirect(url_for('tasks'))
	else:
		g.db.execute('insert into ftasks(name,due_date,priority, status) values(?,?,?,1)',[name,date,priority])
		g.db.commit()
		g.db.close()
		flash('New entry was successfully posted')
		return redirect(url_for('tasks'))

#Mark tasks as complete
@app.route('/complete/<int:task_id>')
@login_required
def complete(task_id):
	g.db=connect_db()
	cur=g.db.execute('update ftasks set status =0\
	where taskid='+str(task_id))
	g.db.commit()
	g.db.close()
	flash('The task was marked as complete')
	return redirect(url_for('tasks'))

#Delete tasks
@app.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
	g.db=connect_db()
	cur=g.db.execute('delete from ftasks where taskid='+str(task_id))
	g.db.commit()
	g.db.close()
	flash('The task was deleted')
	return redirect(url_for('tasks'))
	
	
