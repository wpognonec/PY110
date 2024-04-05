def b(text: str):
    """returns string in blue"""
    return f"\x1b[0;34;1m{text}\x1b[0m"

def r(text: str):
    """returns string in red"""
    return f"\x1b[0;31;1m{text}\x1b[0m"

def g(text: str):
    """returns string in green"""
    return f"\x1b[0;32;1m{text}\x1b[0m"