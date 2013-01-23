from sentry.conf.server import *

try:
    from settings.local import *
except ImportError:
    raise ImportError("Couldn't load local settings")