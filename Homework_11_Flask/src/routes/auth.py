from flask import render_template, Blueprint


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/', methods=('GET', 'POST'))
def base():
    return render_template('base.html')


@auth_bp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template('auth/register.html')


@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('auth/login.html')
