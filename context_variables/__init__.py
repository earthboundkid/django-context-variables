class context_variable(object):

    def __init__(self, func):
        self.func = func
        self.__doc__ = func.__doc__

    def __get__(self, obj, objtype=None):
        # Handle case of being called from class instead of an instance
        if obj is None:
            return self
        # If we got a plain value, return that
        if not callable(self.func):
            return self.func
        # Evaluate the property
        value = self.func(obj)
        # Save value into the instance, replacing the descriptor
        object.__setattr__(obj, self.func.__name__, value)
        return value


def get_context_variables(obj):
    context = {}

    for attr in dir(obj.__class__):
        # Don't bother to check _private/__special attributes
        if attr.startswith('_'):
            continue

        # Get attributes off the class, in case they've already been
        # cached as their final values in the instance dictionary and to
        # avoid general descriptor weirdness
        raw_attr = getattr(obj.__class__, attr)
        if isinstance(raw_attr, context_variable):
            # Force evaluation of obj.`attr`
            context[attr] = getattr(obj, attr)

    return context

