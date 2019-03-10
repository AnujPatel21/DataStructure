import collections

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

a1 = {'a': {'b': {'c': {'d': {'e': 'f'}}}}, 'g': {'h': {'i': {'j': {'k': 'l'}}}}  }
print(flatten(a1))
