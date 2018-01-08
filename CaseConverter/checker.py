import re
from functools import wraps

has_upper_re = re.compile('.*[A-Z].*')
has_lower_re = re.compile('.*[a-z].*')
has_underscore_re = re.compile('.*_.*')
has_hyphen_re = re.compile('.*-.*')


def no_hyphens(func):
    @wraps(func)
    def wrapper(val):
        if has_hyphen_re.match(val):
            raise ValueError('Error: Cannot have hyphens')
        return func(val)
    return wrapper


def no_underscores(func):
    @wraps(func)
    def wrapper(val):
        if has_underscore_re.match(val):
            raise ValueError('Error: Cannot have underscores')
        return func(val)
    return wrapper


def no_mixed_case(func):
    @wraps(func)
    def wrapper(val):
        if has_upper_re.match(val) and has_lower_re.match(val):
            raise ValueError('Error: Cannot have mixed case')
        return func(val)
    return wrapper


def no_spaces(func):
    @wraps(func)
    def wrapper(variable_name):
        if variable_name.find(' ') != -1:
            raise ValueError('Error: Spaces are forbidden')
        return func(variable_name)
    return wrapper