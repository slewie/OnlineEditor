from authorize.authorize import authorize
from docs.docs import docs
from app import app, api
from docs import docs_resource
import view

app.register_blueprint(authorize)
app.register_blueprint(docs)
api.add_resource(docs_resource.DocsResource, '/api/docs')
api.add_resource(docs_resource.DocsListResource, '/api/list/docs')

if __name__ == '__main__':
    app.run()
