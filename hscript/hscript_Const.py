class hscript_Const(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.Const"
    _hx_constructs = ["CInt", "CFloat", "CString"]

    @staticmethod
    def CInt(v):
        return hscript_Const("CInt", 0, (v,))

    @staticmethod
    def CFloat(f):
        return hscript_Const("CFloat", 1, (f,))

    @staticmethod
    def CString(s):
        return hscript_Const("CString", 2, (s,))
hscript_Const._hx_class = hscript_Const
_hx_classes["hscript.Const"] = hscript_Const

