from flask import Flask, redirect, url_for, request, render_template, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from database import db_session, init_db, prefill_db_if_necessary
from models.user import User
from sqlalchemy.orm.exc import NoResultFound


login_manager = LoginManager()
app = Flask(__name__)
app.secret_key = 'abcdef'
init_db()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.route('/')
@login_required
def show_list():
    _items = User.query.all()
    items = [item for item in _items]

    return render_template('list.html', items=items)


@app.route('/delete/<id>')
@login_required
def delete(id):
    User.query.filter_by(id=id).delete()
    db_session.commit()
    flash('Deleted')

    return redirect(url_for('show_list'))


@app.route('/new', methods=['POST'])
@login_required
def new():
    u = User(
        request.form['name'],
        request.form['password']
    )
    db_session.add(u)
    db_session.commit()
    flash('Added')

    return redirect(url_for('show_list'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    prefill_db_if_necessary()
    if request.method == 'POST':
        user = User.query.filter_by(name=request.form['name']).filter_by(password=request.form['password']).scalar()
        if user:
            login_user(user)
            flash('Logged in')
            return redirect(url_for('show_list'))
        else:
            flash('Bad credentials')

    return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('login')


@login_manager.unauthorized_handler
def unauthorized():
    return redirect('login')


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.filter_by(id=int(user_id)).one()
    except NoResultFound:
        return None


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.rollback()
    db_session.remove()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)