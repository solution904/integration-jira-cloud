import collections

def flatten(d, parent_key='', sep='.'):
    '''
    Flattens a nested dict.  Shamelessly ripped from
    `this <https://stackoverflow.com/a/6027615>`_ Stackoverflow answer.
    '''
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.abc.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)