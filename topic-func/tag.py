# Source: Fluent Python, Luciano Ramalho, page 150


def tag(name: str, *content: tuple, cls: str = None, **attrs: dict) -> str:
    """
    Creates HTML/XML tags.

    :param name: the name of the tag (without the brackets)
    :param content: the (text) content to wrap. If more than one
        positional argument is given, each content is wrapped as
        a tag with the tag name "name".
    :param cls: An optional "class" attribute. Defaults to None.
    :return: the representation of the tag as string with all attributes
             the attributes inside the start tag are sorted.

    >>> tag("br")
    '<br />'
    >>> tag("p", "Hello")
    '<p>Hello</p>'
    >>> tag("p", "hello", id=33)
    '<p id="33">hello</p>'
    >>> tag("p", "Hello", "World")
    '<p>Hello</p>\\n<p>World</p>'
    >>> tag("img", title="Sunset", src="sunset.jpg", cls="framed")
    '<img class="framed" src="sunset.jpg" title="Sunset" />'
    """
    if cls is not None:
        attrs["class"] = cls
    if attrs:
        attr_str = "".join(
            f' {attr}="{value}"' for attr, value in sorted(attrs.items())
        )
    else:
        attr_str = ""
    if content:
        element = f"<{name}{attr_str}>%s</{name}>"
        return "\n".join(element % c for c in content)
    else:
        return f"<{name}{attr_str} />"
