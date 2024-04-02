from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import abort
from uuid import uuid4
from . import bp
from schemas import SaleReceiptsSchema
from db import cars, sale_receipts

@bp.route('/sale_receipt', methods=['POST', 'GET'])
class SaleReceiptList(MethodView):
    
    def post(self):
        sale_receipt_data = request.get_json()
        if sale_receipt_data['sale'] not in cars:
            return jsonify({"message": "user does not exist"}), 400
        sale_receipt_id = uuid4().hex
        sale_receipts[sale_receipt_id] = sale_receipt_data

        return jsonify({
            'message': "Sale_receipt created",
            'sale_receipt_id': sale_receipt_id
            }), 201

    def get(self):
        return jsonify(list(sale_receipts.values()))

@bp.route('/sale_receipt/<sale_receipt_id>', methods=['GET', 'PUT', 'DELETE'])
class SaleReceipt(MethodView):

    def get(self, sale_receipt_id):
        try: 
            return jsonify(sale_receipts[sale_receipt_id])
        except KeyError:
            return jsonify({'message':"invalid post"}), 400

    def put(self, sale_receipt_id):
        sale_receipt_data = request.get_json()
        if sale_receipt_id in sale_receipts:
            sale_receipts[sale_receipt_id] = {k:v for k,v in sale_receipt_data.items() if k != 'id'} 

            return jsonify({'message': f'sale_receipt: {sale_receipt_id} updated'}), 201
        
        return jsonify({'message': "invalid sale_receipt"}), 400

    def delete(self, sale_receipt_id):
        if sale_receipt_id not in sale_receipts:
            return jsonify({ 'message' : "Invalid sale_receipt"}), 400
        
        sale_receipts.pop(sale_receipt_id)
        return jsonify({'message': f'Sale_receipt: {sale_receipt_id} deleted'})
