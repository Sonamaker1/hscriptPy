class haxe_macro_FieldType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FieldType"
    _hx_constructs = ["FVar", "FFun", "FProp"]

    @staticmethod
    def FVar(t,e = None):
        return haxe_macro_FieldType("FVar", 0, (t,e))

    @staticmethod
    def FFun(f):
        return haxe_macro_FieldType("FFun", 1, (f,))

    @staticmethod
    def FProp(get,set,t = None,e= None):
        return haxe_macro_FieldType("FProp", 2, (get,set,t,e))
haxe_macro_FieldType._hx_class = haxe_macro_FieldType
_hx_classes["haxe.macro.FieldType"] = haxe_macro_FieldType

