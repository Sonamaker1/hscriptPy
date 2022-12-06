class python_HaxeIterable:
    _hx_class_name = "python.HaxeIterable"
    __slots__ = ("x",)
    _hx_fields = ["x"]
    _hx_methods = ["iterator"]

    def __init__(self,x):
        self.x = x

    def iterator(self):
        return python_HaxeIterator(self.x.__iter__())

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.x = None
python_HaxeIterable._hx_class = python_HaxeIterable
_hx_classes["python.HaxeIterable"] = python_HaxeIterable


