class IntIterator:
    _hx_class_name = "IntIterator"
    __slots__ = ("min", "max")
    _hx_fields = ["min", "max"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_min,_hx_max):
        self.min = _hx_min
        self.max = _hx_max

    def hasNext(self):
        return (self.min < self.max)

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.min
                _hx_local_0.min = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_local_2()
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.min = None
        _hx_o.max = None
IntIterator._hx_class = IntIterator
_hx_classes["IntIterator"] = IntIterator


