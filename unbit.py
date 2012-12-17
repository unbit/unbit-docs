from efesto import Efesto
from gitwhoosh import GitWhoosh
from uwsgidecorators import cron
import uwsgi

gw = GitWhoosh('.','indexes')
ef = Efesto(prefix='<div class="container">', suffix='</div>')

class StartResponseWrapper:
    def __init__(self, original_sr):
        self.status = 500
        self.original_start_response = original_sr

    def __call__(self, status, headers, exc=None):
        try:
            self.status = int(status[0:3])
        except:
            self.status = 500
        return self.original_start_response(status, headers, exc)

def application(environ, start_response):
    sr = StartResponseWrapper(start_response);
    if environ['PATH_INFO'].startswith('/search'):
        return gw(environ, sr)
    page = ef(environ, sr)
    if sr.status == 200:
        uwsgi.cache_update(environ['PATH_INFO'], ''.join(page))
    return page

@cron(-5, -1, -1, -1, -1)
def reindex(signum):
    gw.index('\.(rst|html)$')
