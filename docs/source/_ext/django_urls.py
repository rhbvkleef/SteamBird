from django.urls.resolvers import get_resolver, URLPattern, URLResolver
from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class DjangoUrlsNode(nodes.Admonition, nodes.Element):
    tagname = 'django-urls'


def list_of_string(argument: str):
    return argument.split(',')


class DjangoUrlsDirective(SphinxDirective):
    """
    A directive that can be used to list out relevant django URLs.

    Options:

    * Namespaces: A comma-separated list of namespaces that should be included
    * Extra_urls: A comma-separated list of urls that should be included
    * Application_packages: A comma-separated list of base-packages that should
      be included.
    """

    option_spec = {
        'namespaces': list_of_string,
        'extra_urls': list_of_string,
        'application_packages': list_of_string,
    }

    def run(self):
        url_resolver = get_resolver()

        self.options.setdefault('namespaces', [])
        self.options.setdefault('extra_urls', [])
        self.options.setdefault('application_packages', [])

        all_urls = []

        def populate_level(urls, parents=None, namespace=None):
            if parents is None:
                parents = []

            for url in urls.url_patterns:
                if isinstance(url, URLResolver):
                    populate_level(url, parents + [url.pattern], namespace=(url.namespace or namespace))
                elif isinstance(url, URLPattern):
                    path = ' '.join(map(str, parents + [url.pattern]))
                    cls = None
                    if hasattr(url.callback, 'view_class'):
                        cls = url.callback.view_class.__module__ + "." + url.callback.view_class.__name__
                    # pending_xref()
                    all_urls.append([
                        nodes.Text(path),
                        nodes.Text(namespace or '-'),
                        nodes.Text(str(url.name)),
                        nodes.Text(cls),
                    ])

        populate_level(url_resolver)

        all_urls = filter(lambda url:
                          url[1] in self.options['namespaces'] or
                          url[0] in self.options['extra_urls'] or
                          any(filter(lambda pkg: str.startswith(url[3], pkg), self.options['application_packages'])),
                          all_urls)

        return [self.build_table_from_list(all_urls, ['Pattern', 'Namespace', 'Name', 'Class'])]

    @staticmethod
    def build_table_from_list(data, headers=None):
        col_widths = [100 // len(headers)] * len(headers)
        table = nodes.table()
        tgroup = nodes.tgroup(cols=len(col_widths))
        table += tgroup
        for col_width in col_widths:
            colspec = nodes.colspec(colwidth=col_width)
            tgroup += colspec

        if headers:
            head_row = nodes.row()
            for cell in headers:
                entry = nodes.entry()
                entry += nodes.Text(cell)
                head_row += entry
            thead = nodes.thead()
            thead.append(head_row)
            tgroup.append(thead)

        rows = []
        for row in data:
            row_node = nodes.row()
            for cell in row:
                entry = nodes.entry()
                entry += nodes.Text(cell)
                row_node += entry
            rows.append(row_node)
        tbody = nodes.tbody()
        tbody.extend(rows)
        tgroup.append(tbody)

        return table


def setup(app):
    # app.add_node(DjangoUrlsNode)

    app.add_directive('django-urls', DjangoUrlsDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
