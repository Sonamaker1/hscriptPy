class haxe_iterators_StringIterator:
    _hx_class_name = "haxe.iterators.StringIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        index = self.offset
        self.offset = (self.offset + 1)
        return ord(self.s[index])

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIterator._hx_class = haxe_iterators_StringIterator
_hx_classes["haxe.iterators.StringIterator"] = haxe_iterators_StringIterator


