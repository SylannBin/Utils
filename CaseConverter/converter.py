import re
from checker import no_hyphens, no_underscores, no_mixed_case, no_spaces

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
inner_cap_re = re.compile('([a-z0-9])([A-Z])')
inner_underscore_re = re.compile('(?!^)_([a-zA-Z])')
inner_hyphen_re = re.compile('(?!^)-([a-zA-Z])')


def camel_to_cobol(text):
    raise NotImplementedError("TODO")


@no_spaces
@no_hyphens
@no_underscores
def camel_to_kebab(text):
    s1 = first_cap_re.sub(r'\1-\2', text)
    return inner_cap_re.sub(r'\1-\2', s1).lower()


def camel_to_pascal(text):
    raise NotImplementedError("TODO")


@no_spaces
@no_hyphens
@no_underscores
def camel_to_snake(text):
    s1 = first_cap_re.sub(r'\1_\2', text)
    return inner_cap_re.sub(r'\1_\2', s1).lower()


def camel_to_train(text):
    raise NotImplementedError("TODO")


def cobol_to_camel(text):
    raise NotImplementedError("TODO")


def cobol_to_kebab(text):
    raise NotImplementedError("TODO")


def cobol_to_pascal(text):
    raise NotImplementedError("TODO")


def cobol_to_snake(text):
    raise NotImplementedError("TODO")


def cobol_to_train(text):
    raise NotImplementedError("TODO")


@no_spaces
@no_mixed_case
@no_underscores
def kebab_to_camel(text):
    # inner_hyphen_re.sub(r'', text)
    return re.sub(r'(?!^)-([a-zA-Z])', lambda m: m.group(1).upper(), text)


def kebab_to_cobol(text):
    raise NotImplementedError("TODO")


@no_spaces
@no_mixed_case
@no_underscores
def kebab_to_pascal(text):
    return ''.join(x.capitalize() or '-' for x in text.split('_'))


def kebab_to_snake(text):
    raise NotImplementedError("TODO")


def kebab_to_train(text):
    raise NotImplementedError("TODO")


def pascal_to_camel(text):
    raise NotImplementedError("TODO")


def pascal_to_cobol(text):
    raise NotImplementedError("TODO")


def pascal_to_kebab(text):
    raise NotImplementedError("TODO")


def pascal_to_snake(text):
    raise NotImplementedError("TODO")


def pascal_to_train(text):
    raise NotImplementedError("TODO")


@no_spaces
@no_mixed_case
@no_hyphens
def snake_to_camel(text):
    # inner_underscore_re.sub(r'', text)
    return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), text)


def snake_to_cobol(text):
    raise NotImplementedError("TODO")


def snake_to_kebab(text):
    raise NotImplementedError("TODO")


@no_spaces
@no_mixed_case
@no_hyphens
def snake_to_pascal(text):
    return ''.join(x.capitalize() or '_' for x in text.split('_'))


def snake_to_train(text):
    raise NotImplementedError("TODO")


def train_to_camel(text):
    raise NotImplementedError("TODO")


def train_to_cobol(text):
    raise NotImplementedError("TODO")


def train_to_kebab(text):
    raise NotImplementedError("TODO")


def train_to_pascal(text):
    raise NotImplementedError("TODO")


def train_to_snake(text):
    raise NotImplementedError("TODO")
