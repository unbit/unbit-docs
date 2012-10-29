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
        self.start_response('404 Not Found', [('Content-Type','text/html')])
        header = self.get_html_template('header.html')
        footer = self.get_html_template('footer.html')
        sha = self.git_index[item][8]
        body = self.apply_vars(self.repo.get_blob(sha).as_raw_string()) 
        return [header, body, footer]
        pass

    def render_rst(self, item):
        self.start_response('200 OK', [('Content-Type','text/html')])
        sha = self.git_index[item][8]
        blob = self.repo.get_blob(sha)
        header = self.get_html_template('header.html')
        footer = self.get_html_template('footer.html')
        body = str(publish_parts(self.apply_vars(blob.as_raw_string()), writer_name='html')['html_body'])
        return [header, body, footer]

    def __init__(self, path='.'):
        self.repo = Repo(path)
        self.allowed_ext = {'html':self.render_html, 'rst':self.render_rst}
        self.git_index = self.repo.open_index()

    def __call__(self, environ, start_response):
        self.start_response = start_response
        self.env = environ
        self.page = self.env['PATH_INFO'][1:]
        if self.page == '':
            self.page = 'README'
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
        header = self.get_html_template('header.html')
        footer = self.get_html_template('footer.html')
        body = self.get_html_template('notfound.html')
        if body == '':
            body = '<h1>Not Found</h1>'
        return [header, body, footer]
    
