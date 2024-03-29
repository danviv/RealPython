#flask-taskr-SQLAlchemy
#views.py
#/app/tasks/views.py

from app import db
from flask import Blueprint, Flask,render_template, request, session,flash,redirect,url_for,g
from app.views import login_required, flash_errors
from app.models import FTasks
from app.tasks.forms import AddTask


mod = Blueprint('tasks', __name__, url_prefix='/tasks', template_folder='templates', static_folder='static')


	
@mod.route('/tasks',methods=['GET','POST'])
#@login_required
def tasks():
#use SQLAlchemy wrapper
	
	
	open_tasks=db.session.query(FTasks).filter_by(status='1').order_by(FTasks.due_date.asc())
	closed_tasks=db.session.query(FTasks).filter_by(status='0').order_by(FTasks.due_date.asc())
	
	return render_template('tasks/tasks.html',form=AddTask(request.form),open_tasks=open_tasks, closed_tasks=closed_tasks)
	
#Add new tasks
@mod.route('/add',methods=['GET','POST'])
#@login_required
def new_task():
	form=AddTask(request.form,csrf_enabled=False)
	if form.validate_on_submit():
		new_task=FTasks(
					form.name.data,
					form.due_date.data,
					form.priority.data,
					form.posted_date.data,
					'1',
					session['user_id']
					)
		db.session.add(new_task)
		db.session.commit()
		flash('New entry was successfully posted')
	else:
		flash_errors(form)
	
	return redirect(url_for('.tasks'))

#Mark tasks as complete
@mod.route('/complete/<int:task_id>')
@login_required
def complete(task_id):
	new_id=task_id
	db.session.query(FTasks).filter_by(task_id=new_id).update({"status":"0"})
	db.session.commit()
	flash('The task was marked as complete')
	return redirect(url_for('.tasks'))

#Delete tasks
@mod.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
	
	new_id=task_id
	db.session.query(FTasks).filter_by(task_id=new_id).delete()
	db.session.commit()
	flash('The task was deleted')
	return redirect(url_for('.tasks'))
