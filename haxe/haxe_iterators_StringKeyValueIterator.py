class haxe_iterators_StringKeyValueIterator:
    _hx_class_name = "haxe.iterators.StringKeyValueIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        tmp = self.offset
        s = self.s
        index = self.offset
        self.offset = (self.offset + 1)
        return _hx_AnonObject({'key': tmp, 'value': (-1 if ((index >= len(s))) else ord(s[index]))})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringKeyValueIterator._hx_class = haxe_iterators_StringKeyValueIterator
_hx_classes["haxe.iterators.StringKeyValueIterator"] = haxe_iterators_StringKeyValueIterator

