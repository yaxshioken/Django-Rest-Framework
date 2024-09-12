mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
run:
	python3 manage.py runserver
sort:
	black .
	isort .
user:
	python3 manage.py createsuperuser --username a --email yaxshioken@gmail.com
