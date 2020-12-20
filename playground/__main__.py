from flask import Flask
from playground.api.users import users_api
from playground.database import db_session, init_db
from playground.fake_data import maybe_create_fake_data

app = Flask(__name__)
app.register_blueprint(users_api)


def main():
    init_db()
    maybe_create_fake_data(db_session)
    app.run()


if __name__ == "__main__":
    main()
