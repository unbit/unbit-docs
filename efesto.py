from pygments.formatters import HtmlFormatter
INLINESTYLES = True

from pygments.formatters import HtmlFormatter
DEFAULT = HtmlFormatter(noclasses=INLINESTYLES)

VARIANTS = {
    'linenos': HtmlFormatter(noclasses=INLINESTYLES, linenos=True),
}


from docutils import nodes
from docutils.parsers.rst import directives

from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer

from docutils.core import publish_parts
from dulwich.repo import Repo

def pygments_directive(name, arguments, options, content, lineno,
                       content_offset, block_text, state, state_machine):
    try:
        lexer = get_lexer_by_name(arguments[0])
    except ValueError:
        lexer = TextLexer()
    formatter = options and VARIANTS[options.keys()[0]] or DEFAULT
    parsed = highlight(u'\n'.join(content), lexer, formatter)
    parsed = '<div class="highlight">%s</div>' % parsed
    return [nodes.raw('', parsed, format='html')]

pygments_directive.arguments = (1, 0, 1)
pygments_directive.content = 1
pygments_directive.options = dict([(key, directives.flag) for key in VARIANTS])

directives.register_directive('code-block', pygments_directive)

class Efesto:

    def render_html(self, item):
        self.start_response('200 OK', [('Content-Type','text/html')])
        header = self.get_html_template(self.header)
        footer = self.get_html_template(self.footer)
        sha = self.git_index[item][8]
        body = self.apply_vars(self.repo.get_blob(sha).as_raw_string()) 
        return [header, body, footer]

    def render_rst(self, item):
        self.start_response('200 OK', [('Content-Type','text/html')])
        sha = self.git_index[item][8]
        blob = self.repo.get_blob(sha)
        header = self.get_html_template(self.header)
        footer = self.get_html_template(self.footer)
        body = unicode(publish_parts(self.apply_vars(blob.as_raw_string()), writer_name='html')['html_body']).encode('utf8')
        return [header, self.prefix, body, self.suffix, footer]

    def __init__(self, path='.',prefix='',suffix='',header='header.html',footer='footer.html', notfound='notfound.html'):
        self.repo = Repo(path)
        self.prefix = prefix
        self.suffix = suffix
        self.header = header
        self.footer = footer
        self.notfound = notfound
        self.allowed_ext = {'html':self.render_html, 'rst':self.render_rst}

    def __call__(self, environ, start_response):
        self.start_response = start_response
        self.env = environ
        self.git_index = self.repo.open_index()
        requested_item = environ['PATH_INFO'][1:].rstrip('/')
        if requested_item == '': requested_item = 'index'
        self.page = requested_item
        return self.render_page()

    def render_page(self):
        for ext in self.allowed_ext.keys():
            if "%s.%s" % (self.page, ext) in self.git_index:
                return self.allowed_ext[ext]("%s.%s" % (self.page, ext))
        return self.notfound()

    def apply_vars(self, body):
        for env in self.env.keys():
            body = body.replace("|%s|" % env, str(self.env[env]))
        return body

    def get_html_template(self, html):
        path = self.page
        while True:
            current_path = path
            path = '/'.join(path.split('/')[:-1])
            if current_path == path: break
            item = ("%s/%s" % (path, html))[1:]
            if item in self.git_index:
                sha = self.git_index[item][8]
                return self.apply_vars(self.repo.get_blob(sha).as_raw_string())
        return ''

    def notfound(self):
        self.start_response('404 Not Found', [('Content-Type','text/html')])
        header = self.get_html_template(self.header)
        footer = self.get_html_template(self.footer)
        body = self.get_html_template(self.notfound)
        if body == '':
            body = '<h1>Not Found</h1>'
        return [header, body, footer]
    
