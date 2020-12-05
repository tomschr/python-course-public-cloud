# Source: Fluent Python, Luciano Ramalho, page 153


def clip(text: str, max_len: int = 80):
    """
    Return text clipped at the last space before or after max_len.

    :param text: the text to clip
    :param max_len: the maximum length
    :return: the clipped text

    >>> text="The quick brown fox jumps over the lazy dog"
    >>> clip(text)
    'The quick brown fox jumps over the lazy dog'
    >>> clip(text, 10)
    'The quick'
    >>> clip(text, 20)
    'The quick brown fox'
    >>> clip("Text_without_space")
    'Text_without_space'
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(" ", 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(" ", max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()
