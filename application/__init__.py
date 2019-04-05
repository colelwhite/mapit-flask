import flask
app = flask.Flask(__name__)
conn_string = 'postgresql://postgres:EloiSwamp@144.217.4.173:5432/geos'
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string
app.config['SECRET_KEY'] = "SECRET_KEY"
app.config['DEBUG'] = True
import application.views
