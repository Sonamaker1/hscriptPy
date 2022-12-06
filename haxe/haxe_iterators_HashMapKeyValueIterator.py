class haxe_iterators_HashMapKeyValueIterator:
    _hx_class_name = "haxe.iterators.HashMapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys.iterator()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        _this = self.map.values
        key1 = key.hashCode()
        return _hx_AnonObject({'value': _this.h.get(key1,None), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_HashMapKeyValueIterator._hx_class = haxe_iterators_HashMapKeyValueIterator
_hx_classes["haxe.iterators.HashMapKeyValueIterator"] = haxe_iterators_HashMapKeyValueIterator


