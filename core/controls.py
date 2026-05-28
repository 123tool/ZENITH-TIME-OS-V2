import sys
from blessed import Terminal

def get_key(term, timeout=None):
    """Mengembalikan tombol yang ditekan, dengan timeout."""
    if timeout:
        return term.inkey(timeout=timeout)
    return term.inkey()

def is_exit(key):
    return key.lower() in ('q', 'esc') or key.name == 'KEY_ESCAPE'

def handle_sigint(term):
    """Clean exit on Ctrl+C"""
    print(term.clear + term.normal)
    sys.exit(0)
