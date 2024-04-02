from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from app.models.car_model import CarModel
from app.resources.sale_receipt import bp as sale_receipt_bp
from app.resources.car import bp as car_bp

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(sale_receipt_bp)
app.register_blueprint(car_bp)
