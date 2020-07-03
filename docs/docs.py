from flask import redirect, render_template, Blueprint
from flask_login import login_required

docs = Blueprint('docs', __name__, template_folder='templates', static_folder='static')
from models import Docs


@login_required
@docs.route('/all_pages')
def pages():
    return render_template('docs/pages.html')


@login_required
@docs.route('/create_docs')
def create():
    return redirect(f'/doc/{Docs.get_doc_id()}')


@login_required
@docs.route('/doc/<doc_id>')
def doc(doc_id):
    return 'ab'