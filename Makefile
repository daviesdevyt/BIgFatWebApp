up:
	gunicorn bigfat.wsgi --daemon

down:
	pkill gunicorn

restart:
	pkill gunicorn
	gunicorn bigfat.wsgi --daemon
