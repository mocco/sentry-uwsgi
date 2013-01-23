# Sentry deployment with uWSGI

    git clone git@github.com:mocco/sentry-uwsgi.git
    mv sentry-uwsgi sentry
    cd sentry/
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Add DB settings to `settings/local.py`


## uWSGI config

    [uwsgi]
    socket = 127.0.0.1:9001
    virtualenv = /<path_to_sentry_parent_dir>/sentry/venv
    chdir = /<path_to_sentry_parent_dir>/sentry
    wsgi-file = /<path_to_sentry_parent_dir>/sentry/wsgi.py
    procname-prefix = sentry
    daemonize=/var/log/uwsgi/sentry.log

    master = true
    processes = 1
