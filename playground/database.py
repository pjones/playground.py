from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///test.db", convert_unicode=True)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import playground.models.user
    import playground.models.address

    Base.metadata.create_all(bind=engine)


# Find a user with the given user_name, and with an address with the
# given label.
def find_user_with_address(db, user_name, address_label):
    from playground.models.user import User
    from playground.models.address import Address

    return (
        db.query(User)
        .filter(User.name == user_name)
        .join(Address)
        .filter(Address.label == address_label)
        .first()
    )
