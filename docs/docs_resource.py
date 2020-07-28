from models import Docs
from flask_restful import abort, Resource, reqparse
from flask import jsonify
from flask_login import current_user
from mongoengine.errors import ValidationError


def abort_if_doc_not_found(doc_id):
    try:
        doc = Docs.objects(id=doc_id).first()
        if not doc:
            abort(404, message=f"doc {doc_id} not found")
    except ValidationError:
        abort(404, message=f"doc {doc_id} not found")


class DocsResource(Resource):
    @staticmethod
    def parse():
        parser = reqparse.RequestParser()
        parser.add_argument('text', required=False)
        parser.add_argument('name', required=False)
        return parser

    @staticmethod
    def get(doc_id):
        abort_if_doc_not_found(doc_id)
        doc = Docs.objects(id=doc_id).first().text
        return jsonify({'doc': doc})

    @staticmethod
    def post():
        args = DocsResource.parse().parse_args()
        if args['name'] is not None:
            name = args['name']
        else:
            name = 'Новый документ'
        if args['text'] is not None:
            text = args['text']
        else:
            text = ''
        doc_id = Docs.get_doc_id(name, text)
        return jsonify({'success': 'OK', 'id': str(doc_id), 'text': text, 'name': name})

    @staticmethod
    def delete(doc_id):
        abort_if_doc_not_found(doc_id)
        doc = Docs.objects(id=doc_id)
        doc.delete()
        return jsonify({'success': 'OK'})

    @staticmethod
    def put(doc_id):
        args = DocsResource.parse().parse_args()
        abort_if_doc_not_found(doc_id)
        if args['name'] is not None:
            Docs.objects(id=doc_id).update(name=args['name'])
        if args['text'] is not None:
            Docs.objects(id=doc_id).update(text=args['text'])
        return jsonify({'success': 'OK'})


class DocsListResource(Resource):
    @staticmethod
    def get():
        doc = Docs.objects(author=current_user.id)
        return jsonify({'docs': [item.to_dict() for item in doc]})


