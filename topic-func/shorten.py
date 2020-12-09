def shorten(text, length=25, indicator="..."):
    """
    Returns text or a truncated copy with the indicator added.

    :param text: your string
    :param length: is the maximum length of the return string
        (including any indicator)
    :param indicator: is the string added at the end to indicate
        that the text has been shortend
    :return: the shortend string

    >>> shorten("Python is cool")
    'Python is cool'
    >>> shorten("Voices from the Street", 17)
    'Voices from th...'
    >>> shorten("Tux, Wilber, Gimp", 12, "*")
    'Tux, Wilber*'
    """
    if len(text) > length:
        text = text[:length - len(indicator)] + indicator
    return text


if __name__ == "__main__":
    print(shorten("The quick brown fox jumps over the lazy dog", ))
