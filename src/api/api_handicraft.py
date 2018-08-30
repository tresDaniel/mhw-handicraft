from flask import Blueprint, request, url_for, session, jsonify
from werkzeug.utils import redirect

# from common.utils import Utils
from models.weapon_type import WeaponType

handicraft_blueprint = Blueprint('handicraft', __name__)


# @handicraft_blueprint.route('/weapon_type/<name>', methods=['GET'])
# def payment():
#
#         buyer_name = request.form['buyer_name']
#         buyer_email = Utils.validate_email(request.form['buyer_email'])
#         buyer_cpf = Utils.validate_cpf(request.form['buyer_cpf'])
#
#         try:
#             temp_buyer = Buyer(buyer_name, buyer_email, buyer_cpf)
#             buyer = Buyer.check_buyers(temp_buyer)
#         except Errors.Error as e:
#             return e.message
#
#         payment_amount = request.form['payment_amount']
#         payment_type = request.form['payment_type']
#
#         if payment_type == 'Boleto':
#             return redirect(url_for(".boleto_payment"))
#         elif payment_type == 'Card':
#             card_holder_name = request.form['card_holder_name']
#             card_number = Utils.validate_card(request.form['card_number'])
#             card_expiration_date = request.form['card_expiration_date']
#             card_cvv = request.form['card_cvv']
#
#             try:
#                 temp_card = Card(card_holder_name, card_number, card_expiration_date, card_cvv)
#                 card = Card.check_cards(temp_card)
#             except Errors.Error as e:
#                 return e.message
#
#             payment = Payment(client_id, payment_type, payment_amount, buyer, card)
#             payment_status = Payment.register(payment)
#
#             return redirect(url_for(".card_payment", status=payment_status))

@handicraft_blueprint.route('/weapon_type/<name>', methods=['GET'])
def get_weapon_type(name):
        weapon_type = WeaponType.find_by_name(name)
        return jsonify(weapon_type.json())


@handicraft_blueprint.route('/weapon_type', methods=['GET'])
def get_all_weapon_type():
        weapon_types = WeaponType.find_all()
        return jsonify(weapon_types.json())


@handicraft_blueprint.route('/weapon_type', methods=['POST'])
def set_weapon_type():
        weapon_type_name = request.form['weapon_type_name']
        weapon_type_multiplier = request.form['weapon_type_multiplier']
        weapon_type_id = request.form['weapon_type_id']

        weapon_type = WeaponType(weapon_type_name, weapon_type_multiplier, weapon_type_id)
        WeaponType.register(weapon_type)

        return weapon_type.name