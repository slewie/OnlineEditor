from flask import redirect, render_template, Blueprint, jsonify, url_for
from flask_login import login_required, current_user
from .docs_forms import DocForm
docs = Blueprint('docs', __name__, template_folder='templates', static_folder='static')
from models import Docs


@login_required
@docs.route('/all_pages')
def all_pages():
    pages = Docs.objects(author=current_user.id).all()
    return render_template('docs/pages.html', pages=pages)


@login_required
@docs.route('/create_docs')
def create():
    return redirect(f'/doc/{Docs.get_doc_id()}')


@login_required
@docs.route('/doc/<doc_id>', methods=['GET', 'POST'])
def doc(doc_id):
    form = DocForm()
    document = Docs.objects(id=doc_id).first()
    if len(document.text) != 0 and form.text_area.data is None:
        form.text_area.data = document.text
    if form.is_submitted():
        document.update(text=form.text_area.data)
    return render_template('docs/docs.html', form=form)


@login_required
@docs.route('/doc/delete/<doc_id>')
def delete_docs(doc_id):
    Docs.objects(id=doc_id).delete()
    return redirect('/all_pages')


