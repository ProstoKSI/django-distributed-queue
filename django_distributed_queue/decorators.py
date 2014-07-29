from pymisc.modules import get_class_by_name

from .utils import LazyModel


def resolve_self(model_class_name):
    _cached = {}
    def wrapper(func):
        def wrapped_func(*args, **kwargs):
            if 'model_class' not in _cached:
                _cached['model_class'] = model_class = get_class_by_name(model_class_name)
            else:
                model_class = _cached['model_class']
            # Resolve self argument from instance id into lazy model instance.
            pk = kwargs.pop('self__pk', None)
            if isinstance(pk, int):
                args = [LazyModel(model_class, pk=pk)] + list(args)
            return func(*args, **kwargs)
        return wrapped_func
    return wrapper
