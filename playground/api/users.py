from flask import Blueprint, jsonify, abort
from playground.database import db_session, init_db
from playground.models.address import Address
from playground.models.user import User

users_api = Blueprint("users_api", __name__)


@users_api.route("/users")
def all_users():
    users = db_session.query(User).all()
    return jsonify({"users": users})


@users_api.route("/users/<user_id>")
def user_by_id(user_id):
    user = User.find_by_id(db_session, user_id)

    if user is None:
        abort(404)

    return jsonify(user)


@users_api.route("/mando")
def mando():
    mando = User.find_by_name_and_address(db_session, "The Mandalorian", "Home")
    return jsonify(mando)


@users_api.route("/users/<user_id>/addresses/<label>")
def address_by_label(user_id, label):
    address = Address.find_by_user_id_and_label(db_session, user_id, label)

    if address is None:
        abort(404)

    return jsonify({"address": address, "user_name": address.user.name,})
