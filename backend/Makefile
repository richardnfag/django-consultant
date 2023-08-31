.PHONY: run dotenv test coverage create_migrations migrate example

run:
	python manage.py runserver 0.0.0.0:8000
test:
	pytest -v

coverage:
	pytest --cov

create_migrations:
	python manage.py makemigrations

dotenv:
	cp .env.sample .env

migrate:
	python manage.py migrate

example:
	python manage.py migrate
	python manage.py loaddata example.json
	DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --noinput --username admin --email admin@admin.com
