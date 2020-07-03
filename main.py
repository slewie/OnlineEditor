from authorize.authorize import authorize
from docs.docs import docs
from app import app
import view

app.register_blueprint(authorize)
app.register_blueprint(docs)


if __name__ == '__main__':
    app.run()
