from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from Config import Config
from models.car_models import CarModel
from resources.sale_receipt import bp as sale_receipt_bp
from resources.car import bp as car_bp

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(sale_receipt_bp)
app.register_blueprint(car_bp)
