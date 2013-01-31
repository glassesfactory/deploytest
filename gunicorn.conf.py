bind = 'unix:/tmp/gunicorn/gunicorn.sock'

preload_app = True
backlog = 2048
workers = 1
pidfile = '/tmp/gunicorn/gunicorn.pid'

logfile = '/var/log/gunicorn/gunicorn_dev.log'
loglevel = 'debug'
logconfig = None
