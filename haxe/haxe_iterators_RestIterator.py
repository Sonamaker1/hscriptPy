class haxe_iterators_RestIterator:
    _hx_class_name = "haxe.iterators.RestIterator"
    __slots__ = ("args", "current")
    _hx_fields = ["args", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,args):
        self.current = 0
        self.args = args

    def hasNext(self):
        return (self.current < len(self.args))

    def next(self):
        index = self.current
        self.current = (self.current + 1)
        return python_internal_ArrayImpl._get(self.args, index)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.args = None
        _hx_o.current = None
haxe_iterators_RestIterator._hx_class = haxe_iterators_RestIterator
_hx_classes["haxe.iterators.RestIterator"] = haxe_iterators_RestIterator


