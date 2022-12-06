class haxe_iterators_MapKeyValueIterator:
    _hx_class_name = "haxe.iterators.MapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        return _hx_AnonObject({'value': self.map.get(key), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_MapKeyValueIterator._hx_class = haxe_iterators_MapKeyValueIterator
_hx_classes["haxe.iterators.MapKeyValueIterator"] = haxe_iterators_MapKeyValueIterator


