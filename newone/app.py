
from flask import Flask, request
from flask_migrate import Migrate
from models.base import db
# from views.category_route import user_auth_bp
from models.category import Category

app = Flask(__name__)
migrate = Migrate(app, db)
POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'divum',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)
# app.register_blueprint(user_auth_bp)


@app.route('/category/api')
def api_create():
    if request.method == 'POST':
        if request.is_json():
            data = request.get_json()
            value = Category(name=data['name'])
            value.save()
    return 'First Flask application!'


if __name__ == '__main__':
    app.run()
