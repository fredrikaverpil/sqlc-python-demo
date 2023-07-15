install:
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -e .

dbup:
	docker run --rm --name postgres12 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=test -d postgres:12-alpine

dbdown:
	docker stop postgres12

psql:
	docker exec -it postgres12 psql -U root -d test

create-migration:
	alembic revision -m "create users table"

migrateup:
	alembic upgrade head

migrateup1:
	alembic upgrade +1

migratedown:
	alembic downgrade base

migratedown1:
	alembic downgrade -1

sqlcgen:
	sqlc generate
	touch src/demo/db/__init__.py
	touch src/demo/db/users/__init__.py

make run:
	python -c "from demo.main import main; main()"


.PHONY = install dbup dbdown psql create-migration migrateup migrateup1 migratedown migratedown1 sqlcgen run

