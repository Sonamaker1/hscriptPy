class haxe_macro_Constant(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Constant"
    _hx_constructs = ["CInt", "CFloat", "CString", "CIdent", "CRegexp"]

    @staticmethod
    def CInt(v):
        return haxe_macro_Constant("CInt", 0, (v,))

    @staticmethod
    def CFloat(f):
        return haxe_macro_Constant("CFloat", 1, (f,))

    @staticmethod
    def CString(s,kind = None):
        return haxe_macro_Constant("CString", 2, (s,kind))

    @staticmethod
    def CIdent(s):
        return haxe_macro_Constant("CIdent", 3, (s,))

    @staticmethod
    def CRegexp(r,opt):
        return haxe_macro_Constant("CRegexp", 4, (r,opt))
haxe_macro_Constant._hx_class = haxe_macro_Constant
_hx_classes["haxe.macro.Constant"] = haxe_macro_Constant

