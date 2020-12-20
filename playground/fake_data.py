from playground.models.address import Address
from playground.models.user import User


def maybe_create_fake_data(db):
    query = db.query(User)

    if query.count() == 0:
        print("Creating fake data")

        user_1 = User(name="The Mandalorian")
        user_1.addresses = [
            Address(label="Home", display_text="Mandalore"),
            Address(label="Work", display_text="Razor Crest"),
        ]

        user_2 = User(name="Cara Dune")
        user_2.addresses = [Address(label="Home", display_text="Alderaan")]

        db.add(user_1)
        db.add(user_2)

        db.commit()
