from flask_smorest import Blueprint

bp = Blueprint("sales_receipts", __name__, description="Routes for Sales_Receipts")

from . import routes