class haxe_macro_Error(haxe_Exception):
    _hx_class_name = "haxe.macro.Error"
    __slots__ = ("pos",)
    _hx_fields = ["pos"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,pos,previous = None):
        self.pos = None
        super().__init__(message,previous)
        self.pos = pos
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pos = None
haxe_macro_Error._hx_class = haxe_macro_Error
_hx_classes["haxe.macro.Error"] = haxe_macro_Error

