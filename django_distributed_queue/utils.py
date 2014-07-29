class LazyModel(object):
    """
    It's a helper class that is used in case you have model_class and object
    primary key. You might need to use only object id.
    
    If you try to access other fields of the model class then we will query the
    database to get that object and provide you with any field and method
    transparently proxying them.
    """
    def __init__(self, model_class, pk):
        self._model_class = model_class
        self.pk = pk
        self._instance = None

    def __getattribute__(self, attr_name):
        # Hiding traces of decoration.
        if attr_name in ('__init__', '__getattribute__', '_model_class', 'pk',
                '_instance'):
            # Stopping recursion.
            return object.__getattribute__(self, attr_name)
        # All other attr_names, including auto-defined by system in self, are
        # searched in decorated self.instance, e.g.: __module__, __class__, etc.
        if self._instance is None:
            self._instance = self._model_class.objects.get(pk=self.pk)
        # Raises correct AttributeError if name is not found in decorated self.func.
        return getattr(self.instance, attr_name)
