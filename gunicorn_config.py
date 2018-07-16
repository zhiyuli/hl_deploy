#gunicorn_config.py

bind = '127.0.0.1:49153'
timeout = 600
max_requests = 2000
name = "hydrolearn-gunicorn"
workers = 4
raw_env = [
          'HOME=/home/ubuntu'
          ]
log_level = 'debug'
accesslog = '/home/ubuntu/HL_deploy/access.log'
errorlog = '/home/ubuntu/HL_deploy/error.log'
capture_output = True
access_log_format = 'process%(p)s XFF%({X-Forwarded-For}i)s; %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
