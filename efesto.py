from docutils.core import publish_parts
from dulwich.repo import Repo

class Efesto:

    def render_html(self, page, start_response):
        pass

    def render_rst(self, page, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        sha = self.git_index[page][8]
        blob = self.repo.get_blob(sha)
        return [self.get_header(page), str(publish_parts(blob.as_raw_string(), writer_name='html')['html_body']), self.get_footer(page)]

    def __init__(self, path='.'):
        self.repo = Repo(path)
        self.allowed_ext = {'html':self.render_html, 'rst':self.render_rst}
        self.git_index = self.repo.open_index()

    def __call__(self, environ, start_response):
        requested_item = environ['PATH_INFO'][1:]
        if requested_item == '': requested_item = 'index'
        print requested_item
        return self.render_page(requested_item, start_response)

    def render_page(self, page, start_response):
        for ext in self.allowed_ext.keys():
            if "%s.%s" % (page, ext) in self.git_index:
                return self.allowed_ext[ext]("%s.%s" % (page, ext), start_response)
        return self.render_notfound(page, start_response)

    def get_header(self, page):
        if 'header.html' in self.git_index:
            sha = self.git_index['header.html'][8]
            return self.repo.get_blob(sha).as_raw_string() 
        return ''

    def get_footer(self, page):
        if 'footer.html' in self.git_index:
            sha = self.git_index['footer.html'][8]
            return self.repo.get_blob(sha).as_raw_string() 
        return ''

    def render_notfound(self, filename, start_response):
        start_response('404 Not Found', [('Content-Type','text/html')])
        return 'Not Found'
    
