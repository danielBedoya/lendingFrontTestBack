from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

api_bp = Blueprint('api', __name__)

@api_bp.route('/apply', methods=['POST'])
def loan_application():
    data = request.get_json()
    tax_id = data.get('tax_id')
    business_name = data.get('business_name')
    try:
        requested_amount = int(data.get('requested_amount'))
    except Exception as e:
        return jsonify({'error': 'requested_amount must be int'}), 400
        
    decision = ''

    if requested_amount > 50000:
        decision = 'Declined'
    elif requested_amount == 50000:
        decision = 'Undecided'
    elif requested_amount < 50000:
        decision = 'Approved'
    
    response = jsonify({'decision': decision})
    
    return response
