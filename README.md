# sqlc-python-demo

This project aims to use as much raw SQL as possible:

- Migrations using raw SQL 🥩.
- ORM _generated_ 🧙 from raw SQL 🥩 queries (thanks to [sqlc-gen-python](https://github.com/sqlc-dev/sqlc-gen-python).

## Quickstart 🚀

```bash
# install deps in an activated virtual environment
make install

# start up postgres container
make dbup

# apply migrations
make migrateup

# (define queries to be consumed by sqlc in sqlc/queries.sql)

# generate sqlalchemy ORM, using pydantic models
make sqlcgen

# (see the generated code in src/demo/db/users/queries.py)

# run demo program (src/demo/main.py)
make run
```

## The setup

### Alembic

First, I set up Alembic:

```bash
alembic init migrations
```

I edited `alembic.ini` to specify the postgres database connection string and the filename template. Then I created the first migration:

```bash
alembic revision -m "create users table"
```

I then made the migrations load side-car `.sql` files and executes those rather than SQLAlchemy ORM queries.

### Sqlc

Using [sqlc](https://github.com/kyleconroy/sqlc), I initiated a default config file:

```bash
sqlc init
```

I then had to replace basically all of it with the example yaml at [https://github.com/sqlc-dev/sqlc-gen-python](https://github.com/sqlc-dev/sqlc-gen-python). I tweaked the paths and filenames somewhat, as well as the Python package name.

I added in a few queries into the `sqlc/queries.sql` file, and finally I ran `make sqlcgen` to generate the ORM code in `src/demo/db`.
