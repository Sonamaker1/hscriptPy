class haxe_ValueException(haxe_Exception):
    _hx_class_name = "haxe.ValueException"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["unwrap"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,value,previous = None,native = None):
        self.value = None
        super().__init__(Std.string(value),previous,native)
        self.value = value
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def unwrap(self):
        return self.value

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.value = None
haxe_ValueException._hx_class = haxe_ValueException
_hx_classes["haxe.ValueException"] = haxe_ValueException


