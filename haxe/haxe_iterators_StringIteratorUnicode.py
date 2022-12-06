class haxe_iterators_StringIteratorUnicode:
    _hx_class_name = "haxe.iterators.StringIteratorUnicode"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]
    _hx_statics = ["unicodeIterator"]

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
    def unicodeIterator(s):
        return haxe_iterators_StringIteratorUnicode(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIteratorUnicode._hx_class = haxe_iterators_StringIteratorUnicode
_hx_classes["haxe.iterators.StringIteratorUnicode"] = haxe_iterators_StringIteratorUnicode


