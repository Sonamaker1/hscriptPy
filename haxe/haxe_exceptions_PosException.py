class haxe_exceptions_PosException(haxe_Exception):
    _hx_class_name = "haxe.exceptions.PosException"
    __slots__ = ("posInfos",)
    _hx_fields = ["posInfos"]
    _hx_methods = ["toString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,previous = None,pos = None):
        self.posInfos = None
        super().__init__(message,previous)
        if (pos is None):
            self.posInfos = _hx_AnonObject({'fileName': "(unknown)", 'lineNumber': 0, 'className': "(unknown)", 'methodName': "(unknown)"})
        else:
            self.posInfos = pos
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def toString(self):
        return ((((((((("" + HxOverrides.stringOrNull(super().toString())) + " in ") + HxOverrides.stringOrNull(self.posInfos.className)) + ".") + HxOverrides.stringOrNull(self.posInfos.methodName)) + " at ") + HxOverrides.stringOrNull(self.posInfos.fileName)) + ":") + Std.string(self.posInfos.lineNumber))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.posInfos = None
haxe_exceptions_PosException._hx_class = haxe_exceptions_PosException
_hx_classes["haxe.exceptions.PosException"] = haxe_exceptions_PosException


