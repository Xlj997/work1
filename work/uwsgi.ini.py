[uwsgi]
socket=0.0.0.0:8080
# http=0.0.0.0:12000
chdir=/root/home/work/work1/work
wsgi-file=work/wsgi.py
processes=4
threads=2
master=True
pidfile=uwsgi.pid
daemonize=uwsgi.log
