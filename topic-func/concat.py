
def concat(*args, sep="/"):
    """
    Concatenate arbitrary arguments seperated by sep.

    Args:
        sep (str, optional): The separator. Defaults to "/".

    Returns:
        str: the concatenated string
    """
    return sep.join(args)
