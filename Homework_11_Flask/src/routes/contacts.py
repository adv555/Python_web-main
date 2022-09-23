from flask import render_template, Blueprint

contact_bp = Blueprint('contacts', __name__, url_prefix='/contacts')


@contact_bp.route('/', methods=('GET', 'POST'))
def base():
    return render_template('base.html')