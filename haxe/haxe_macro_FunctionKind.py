class haxe_macro_FunctionKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FunctionKind"
    _hx_constructs = ["FAnonymous", "FNamed", "FArrow"]

    @staticmethod
    def FNamed(name,inlined = None):
        return haxe_macro_FunctionKind("FNamed", 1, (name,inlined))
haxe_macro_FunctionKind.FAnonymous = haxe_macro_FunctionKind("FAnonymous", 0, ())
haxe_macro_FunctionKind.FArrow = haxe_macro_FunctionKind("FArrow", 2, ())
haxe_macro_FunctionKind._hx_class = haxe_macro_FunctionKind
_hx_classes["haxe.macro.FunctionKind"] = haxe_macro_FunctionKind

