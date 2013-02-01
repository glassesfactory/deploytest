bind = 'unix:/home/gunicorn/gunicorn.sock'

preload_app = True
backlog = 2048
workers = 1
pidfile = '/home/gunicorn/gunicorn.pid'

logfile = '/var/log/gunicorn/gunicorn_dev.log'
loglevel = 'debug'
logconfig = None
