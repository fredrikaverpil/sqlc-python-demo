import sqlalchemy

from demo.db.users.models import User
from demo.db.users.queries import Querier


def main() -> None:
    db_url = "postgresql://root:secret@0.0.0.0/test"
    engine = sqlalchemy.create_engine(db_url)

    with engine.connect() as conn:
        store = Querier(conn=conn)

        created_user: User = store.create_user(name="foo", email="foo@bar.baz")
        print(f"Created user: {created_user}")

        refetched_user: User = store.get_user(id=created_user.id)
        print(f"Refetched user: {refetched_user}")


if __name__ == "__main__":
    main()
