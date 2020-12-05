# Source: Programming in Python 3, Mark Summerfield, page 204f


def is_balanced(text, brackets="()[]{}<>"):
    """
    Checks if a text has balanced brackets.

    :param text: The text to check for balanced brackets
    :return: True if the text contains balanced brackets, False otherwise.
    """
    counts = {}
    left_for_right = {}
    # Prepare helper dictionaries
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "The bracket characters must differ"
        counts[left] = 0
        left_for_right[right] = left

    #
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            left = left_for_right[c]
            if counts[left] == 0:
                return False
            counts[left] -= 1

    return not any(counts.values())
