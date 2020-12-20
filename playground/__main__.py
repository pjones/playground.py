from playground.database import db_session, init_db, find_user_with_address
from playground.fake_data import maybe_create_fake_data
from flask import jsonify, Flask

app = Flask(__name__)


@app.route("/users")
def users():
    from playground.models.user import User

    users = db_session.query(User).all()
    return jsonify({"users": users})


@app.route("/mando")
def mando():
    mando = find_user_with_address(db_session, "The Mandalorian", "Home")
    return jsonify(mando)


def main():
    init_db()
    maybe_create_fake_data(db_session)
    app.run()


if __name__ == "__main__":
    main()
