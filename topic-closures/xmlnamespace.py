#
class XMLNamespaces:  # 9 LOC
    """
    Handling of XML namespaces

    >>> ns = XMLNamespaces(html="http://www.w3.org/1999/xhtml")
    >>> ns("/{html}html")
    '/{http://www.w3.org/1999/xhtml}html'
    """
    def __init__(self, **namespaces):
        self.nsmap = {}
        for name, uri in namespaces.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.nsmap.setdefault(name, "{%s}" % uri)

    def __call__(self, path: str):
        return path.format_map(self.nsmap)


def xmlnamespace(**namespaces):  # 11 LOC
    """
    Handling of XML namespaces

    >>> ns = xmlnamespace(html="http://www.w3.org/1999/xhtml")
    >>> ns("/{html}html")
    '/{http://www.w3.org/1999/xhtml}html'
    """
    nsmap = {}

    def register(name, url):
        """
        Register a name with a URL.
        """
        nonlocal nsmap
        nsmap.setdefault(name, "{%s}" % url)

    def wrapper(path):
        return path.format_map(nsmap)

    for name, url in namespaces.items():
        register(name, url)

    wrapper.register = register
    # wrapper.nsmap = nsmap
    return wrapper


if __name__ == "__main__":
    ns = xmlnamespace(html="http://www.w3.org/1999/xhtml",
                      db="http://docbook.org/ns/docbook",
                      xlink="http://www.w3.org/1999/xlink")
    print(ns("/{db}book/{db}chapter/@{xlink}href"))
    print(dir(ns))
    ns.register("xi", "http://www.w3.org/2001/XInclude")
    print(ns("/{xi}include/@href"))
    print(ns)
    print("varnames:", ns.__code__.co_varnames)
    print("freevars:", ns.__code__.co_freevars)
