release: python manage.py collectstatic --noinput
web: gunicorn habiba_blog.wsgi --bind 0.0.0.0:$PORT --log-file -
