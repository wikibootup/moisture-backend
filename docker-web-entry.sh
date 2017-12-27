python moisture/manage.py makemigrations
python moisture/manage.py migrate
gunicorn moisture.wsgi:application -b 0.0.0.0:8000 --chdir moisture/
