bind = 'unix:/tmp/gunicorn/gunicorn.sock'

preload_app = True
backlog = 2048
workers = 1
worker_class = 'egg:meinheld#gunicorn_worker'
pidfile = '/tmp/gunicorn/gunicorn.pid'

logfile = '/var/log/gunicorn/gunicorn_dev.log'
loglevel = 'debug'
logconfig = None
